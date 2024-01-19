# routers/formation_router.py
from fastapi import APIRouter, Depends, HTTPException
from ..controllers.formation_controller import read_excel, count_sexe_by_formation,count_by_formation, count_response, count_by_text_response
from ..controllers.formation_controller import read_excel, count_sexe_by_formation,count_by_formation, count_response, count_by_text_response

from collections import Counter

#from fonctionAnnexes import getFiliere
from fastapi.responses import JSONResponse
import pandas as pd
from wordcloud import WordCloud

import re
#from definitions import *


formation_router = APIRouter(
    tags=["formations"],
)

#@formation_router.get("/formations/")
#def get_formations(column: str = "formation"):
#    file_path = "formatted_data/2023.xlsx"
#    try:
#        formations = read_excel(file_path, column)
#        return {"formations": formations}
#    except HTTPException as e:
#        raise e


@formation_router.get("/count-response/")
def get_count(year: int, column: str = "formation"):
    file_path = f"formatted_data/{year}.xlsx"
    try:
        json_file_path = "training_and_graph_data/count_response" + str(year) + ".json"

        response = count_response(file_path, column, json_file_path)
        return response
    except HTTPException as e:
        raise e


@formation_router.get("/formations/")
def get_formations(year: int, column: str = "formation"):
    file_path = f"formatted_data/{year}.xlsx"
    try:
        formations = read_excel(file_path, column)
        return {"formations": formations}
    except HTTPException as e:
        raise e

@formation_router.get("/sexe/")
def get_sexe_graph(year: int):
    file_path = f"formatted_data/{year}.xlsx"
    try:
       column_name="genre"
       if year == 2018 or year == 2019:
           column_name="sexe"
       json_file_path = "training_and_graph_data/count_sexe_by_formation" + str(year) + ".json"

       sexe = count_sexe_by_formation(file_path,column_name, json_file_path)
       return {"sexe": sexe}
    except HTTPException as e:
        raise e
    
    
@formation_router.get("/satisfaction/")
def get_satisfaction_graph(year: int):
    file_path = f"formatted_data/{year}.xlsx"
    
    column_name="globalement,sur une echelle allant de 1 a 5, etes-vous satisfait(e) de votre formation a polytech montpellier ? "
    if year == 2023:
        column_name="globalement, sur une echelle allant de 1 a 5, etes-vous satisfait·e de votre formation a polytech montpellier ? "
    if year == 2020:
        column_name="globalement,sur une echelle allant de 1 ‡ 5, ites-vous satisfait(e) de votre formation ‡ polytech montpellier ? "
        
    json_file_path = "training_and_graph_data/satisfaction_graph" + str(year) + ".json"
        
    try:
       satisfaction = count_by_formation(file_path, column_name, json_file_path)
       return {"satisfaction": satisfaction}
    except HTTPException as e:
        raise e


@formation_router.get("/importance/")
def get_importance_graph(year: int):
    file_path = f"formatted_data/{year}.xlsx"
    
    column_name="les elements suivants vous semblent-ils avoir joue un role dans votre recrutement? [la formation]"
    if year == 2023:
        column_name="les elements suivants vous semblent-ils avoir joue un role dans votre recrutement sur ce 1er emploi ? - la formation"
    if year == 2022:
        column_name="les elements suivants vous semblent-ils avoir joue un role dans votre recrutement sur ce 1er emploi? - la formation"
    if year == 2020 :
        column_name="les elements suivants vous semblent-ils avoir joue un rule dans votre recrutement? - la formation"
        
    json_file_path = "training_and_graph_data/importance_graph" + str(year) + ".json"
    try:
       satisfaction = count_by_formation(file_path, column_name, json_file_path)
       return {"importance": satisfaction}
    except HTTPException as e:
        raise e


@formation_router.get("/reputation/")
def get_importance_graph(year: int):
    file_path = f"formatted_data/{year}.xlsx"
    
    column_name=""
    if year == 2023:
        column_name="les elements suivants vous semblent-ils avoir joue un role dans votre recrutement ? - la reputation de la filiere de formation"
    if year == 2022:
        column_name="les elements suivants vous semblent-ils avoir joue un role dans votre recrutement? - la reputation de la filiere de formation"
    if year == 2020:
        column_name="les elements suivants vous semblent-ils avoir joue un rule dans votre recrutement? - la reputation de la filiere de formation"
    if year == 2021 or year == 2019 :
        column_name="les elements suivants vous semblent-ils avoir joue un role dans votre recrutement? [la reputation de la filiere de formation]"
    if year == 2018 :
        column_name="les elements suivants vous semblent-ils avoir joue un role dans votre recrutement sur ce 1er emploi? [la reputation du departement]"
    
    json_file_path = "training_and_graph_data/reputation_graph" + str(year) + ".json"

    try:
       satisfaction = count_by_formation(file_path, column_name, json_file_path)
       return {"reputation": satisfaction}
    except HTTPException as e:
        raise e


@formation_router.get("/count/")
def get_count_by_text_response(year: int, question: str):
    file_path = f"formatted_data/{year}.xlsx"
    print(question)
    print(file_path)
    json_file_path = "training_and_graph_data/count_by_text"+ question + str(year) + ".json"
    try:
       count = count_by_text_response(file_path, question, json_file_path)
       return {"count": count}
    except HTTPException as e:
        raise e   
    


from fastapi.responses import JSONResponse
import pandas as pd
 
@formation_router.get("/sentiment/")
def plot_sentiment_for_year_route(year: int):
    # Lecture du fichier Excel
    print("coucou")
    file_path =  f"training_and_graph_data/resultats_sentiments.xlsx"
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



   
@formation_router.get("/wordcloud/{filiere}/{modele}")
def get_wordcloud(filiere: str, modele: int):
    
    # Lire les données à partir du fichier CSV
    if int(modele) == 1:
        file_path = f"training_and_graph_data/formation_quels_enseignements_vous_semblent_les_plus_utiles_pour_lexercice_de_votre_metier_et_votre_insertion_professionnelle.csv"
    else :
        file_path = f"training_and_graph_data/formation_parmi_les_enseignements_fournis_par_lecole_quels_sont_ceux_qui_meriteraient_detre_approfondis_ou_renforces.csv"
    
    
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
    filtered_text = ' '.join(word.lower() for word in text.split() if word.lower() not in stop_words and word.lower() != 'cour' and word.lower() != 'cours'and word.lower() != 'enseignements'and word.lower() != 'plus'and word.lower() != 'a')
    
    # Obtenir les fréquences des mots
    word_frequencies = WordCloud().process_text(filtered_text)

    # Sélectionner les 5 mots les plus fréquents
    top_5_words = dict(sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True)[:10])
    print(top_5_words)
    # Retourner les 5 mots les plus fréquents au format JSON
    return top_5_words






def getFiliere(filiere):
    if filiere == "MI":
        return "Mecanique et Interactions (MI)"
    elif filiere == "STE":
        return "Sciences et Technologies de l'Eau (STE)"
    elif filiere == "MAT":
        return "Materiaux (MAT)"
    elif filiere == "IG":
        return "Informatique et Gestion (IG)"
    elif filiere == "GBA":
        return "Genie Biologique et Agroalimentaires (GBA)"
    elif filiere == "MEA":
        return "Microelectronique Et Automatique (MEA)"
    else:
        return filiere








import nltk
from nltk.corpus import stopwords



# Télécharger les stopwords français depuis NLTK
nltk.download('stopwords')
stop_words = set(stopwords.words('french'))

# Définissez vos listes de termes et de représentations ici

# MI
mechanical_terms = ["methode mecanique", "mecanique", "mmc", "calculs scientifiques",
                   "calcul scientifique", "mecanique des milieux continus", "conception mecanique", "conception",
                   "milieux continus", "mecanique milieux", "methode element", "mecaniques milieux", "elements finis", "mef",
                   "dimensionnement", "dimensionnement_term"]
computer_terms = ["informatique", "python", "programmation", "algorithmique", "logiciels"]
materials_terms = ["polymeres","polymere", "plastique","beton","ceramique","ceramiques","materiaux", "rdm", "resistance des materiaux", "materiaux standards", "plasticite", "viscoelasticite"]

# MAT 
eco_terms = ["Eco conception", "eco", "durabilite","Eco-conception"]

# IG

web_terms = ["developpement web", "web", "awii", "application web", "web dev"]
logiciel_terms = ["developpement logiciel", "logiciel","se", "software engineering", "software engineer", "software", "java", "design pattern", "design", "pattern","modelisation"]
# Tous
project_management_terms = ["gestion de projet", "management projet","management de projet","management de projets", "gestion", "management", "projet"]
language_terms = ["l'anglais","langue", "anglais","allemand", "espagnole"]
professional_insertion_terms = ["insertion", "professionnel", "insertion professionnelle", "carriere", "stage", "experience professionnelle"]
maths_terms = ["mathematiques","mathematique", "maths", "math", "calcul", "statistiques", 'simulation numerique', "numerique", "simulation", "matlab"]
etc_terms = ["tous", "tout", "tous enseignements", "enseignement"]

# STE
hydro_terms = ["hydrologie", "hydraulique","Hydrologie", "hydrologie hydrologie"]
procedes_terms = ["genie des procedes", "procedes"]
chimie_terms = ["chimie de l'eau", "chimie","Hydrogéologie", "chimie des eaux", "chimie organique"]
quali_terms = ["qualite des eaux", "qualite de l'eau"]
fluide_terms = ["mecanique des fluides","fluide", "fluide", "mecanique des fluide","MF"]

# Choisir des mots représentatifs pour chaque liste
representative_mechanical_term = "mecanique"
representative_project_management_term = "management_projet"
representative_computer_term = "informatique"
representative_materials_term = "materiaux"
representative_language_term = "langue"
representative_maths_term = "mathematiques"
representative_professional_insertion_term = "insertion_professionnelle"
representative_etc_term = "tout"
representative_hydro_term = "hydrologie"
representative_procedes_term = "genie_des_procedes"
representative_chimie_term = "chimie_de_l'eau"
representative_quali_term = "qualite_des_eaux"
representative_fluide_term = "mecanique_des_fluides"
representative_eco_term = "eco_conception"
representative_web_term = "web"
representative_logiciel_term = "logiciel"


term_categories = {
    "mechanical": mechanical_terms,
    "project_management": project_management_terms,
    "computer": computer_terms,
    "materials": materials_terms,
    "language": language_terms,
    "maths": maths_terms,
    "professional_insertion": professional_insertion_terms,
    "etc": etc_terms,
    "hydro": hydro_terms,
    "procedes": procedes_terms,
    "chimie": chimie_terms,
    "quali": quali_terms,
    "fluide": fluide_terms,
    "eco" : eco_terms,
    "web" : web_terms,
    "software engineer" :logiciel_terms
}

representative_terms = {
    "mechanical": representative_mechanical_term,
    "project_management": representative_project_management_term,
    "computer": representative_computer_term,
    "materials": representative_materials_term,
    "language": representative_language_term,
    "maths": representative_maths_term,
    "professional_insertion": representative_professional_insertion_term,
    "etc": representative_etc_term,
    "hydro": representative_hydro_term,
    "procedes": representative_procedes_term,
    "chimie": representative_chimie_term,
    "quali": representative_quali_term,
    "fluide": representative_fluide_term,
    "eco" : representative_eco_term,
    "web" : representative_web_term,
    "software engineer" : representative_logiciel_term
}

