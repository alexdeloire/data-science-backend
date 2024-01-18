""" fonctionAnnexes.py """
""" Fichier pour avoir les fonctions annexes séparées des routes """

import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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
    
    




def plot_sentiment_for_year(year):
    # Lecture du fichier Excel
    file_path = r"C:\Users\charm\resultats_sentiments.xlsx"
    df = pd.read_excel(file_path)

    # Conversion des étoiles en nombres
    df['Sentiment'] = df['Sentiment'].str.extract('(\d+)').astype(float)

    # Filtrage des données pour l'année spécifiée
    df_year = df[df['Annee'] == year]

    # Calcul du sentiment moyen par filière
    mean_sentiment_by_formation = df_year.groupby('Formation')['Sentiment'].mean()

    # Conversion en format JSON
    result_json = {
        'sentiment_moyen': mean_sentiment_by_formation.mean(),
        'formation': mean_sentiment_by_formation.to_dict()
    }

    return json.dumps(result_json, indent=2)





