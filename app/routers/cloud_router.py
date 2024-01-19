
from collections import Counter

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fonctionAnnexes import getFiliere
from fastapi.responses import JSONResponse
import pandas as pd
from wordcloud import WordCloud

import re
from definitions import *

@app.get("/wordcloud/{filiere}/{modele}")
def get_wordcloud(filiere: str, modele: int):
    
    # Lire les données à partir du fichier CSV
    if int(modele) == 1:
        file_path = r"C:\Users\charm\Downloads\formation_quels_enseignements_vous_semblent_les_plus_utiles_pour_lexercice_de_votre_metier_et_votre_insertion_professionnelle.csv"
    else :
        file_path = r"C:\Users\charm\data_science_merde\data_science_backend\training_and_graph_data\formation_parmi_les_enseignements_fournis_par_lecole_quels_sont_ceux_qui_meriteraient_detre_approfondis_ou_renforces.csv"
    
    
    df = pd.read_csv(file_path)
    
    filiere = getFiliere(filiere)
    # Filtrer les données pour la filière spécifique
    filiere_data = df[df['formation'] == filiere]

    # Concaténer les enseignements de la filière en une seule chaîne de texte
    text = ' '.join(filiere_data[df.columns[1]].astype(str))

    # Utiliser une expression régulière pour identifier les termes liés à différentes catégories
    for category, terms in term_categories.items():
        for term in terms:
            pattern = re.compile(rf'\b{re.escape(term)}\b', flags=re.IGNORECASE)
            text = pattern.sub(representative_terms[category], text)

    # Enlever les stopwords et le mot 'cour'
    filtered_text = ' '.join(word.lower() for word in text.split() if word.lower() not in stop_words and word.lower() != 'cour' and word.lower() != 'cours'and word.lower() != 'enseignements'and word.lower() != 'plus')
    
    # Obtenir les fréquences des mots
    word_frequencies = WordCloud().process_text(filtered_text)

    # Sélectionner les 5 mots les plus fréquents
    top_5_words = dict(sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True)[:10])
    print(top_5_words)
    # Retourner les 5 mots les plus fréquents au format JSON
    return top_5_words





@app.get("/sentiment/{year}")
def plot_sentiment_for_year_route(year: int):
    # Lecture du fichier Excel
    file_path = r"C:\Users\charm\resultats_sentiments.xlsx"
    df = pd.read_excel(file_path)

    # Conversion des étoiles en nombres
    df['Sentiment'] = df['Sentiment'].str.extract('(\d+)').astype(float)

    # Filtrage des données pour l'année spécifiée
    df_year = df[df['Annee'] == int(year)] 

    # Calcul du nombre de chaque note par filière
    sentiment_counts_by_formation = df_year.groupby(['Formation', 'Sentiment']).size().unstack(fill_value=0)
    
    # Conversion en format JSON
    result_json = {
        "res": sentiment_counts_by_formation.to_dict(orient='index')
    }
    
    return JSONResponse(content=result_json)
