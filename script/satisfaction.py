import pandas as pd
from transformers import pipeline

# Charger le modèle de sentiment pré-entraîné pour le français
classifier = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

dataset_path = "../training_and_graph_data/formation_annee_obtention_du_diplome_vos_remarques_et_commentaires_relatifs_a_votre_insertion_professionnelle.csv" # Assurez-vous de spécifier le bon chemin

with open(dataset_path, 'r', encoding='ISO-8859-1', errors='ignore') as file:
    df = pd.read_csv(file, sep=',')


resultats = []

for index, row in df.iterrows():
    # Récupérer les données nécessaires
    annee = row["annee obtention du diplome"]  # Extraire l'année depuis la colonne "Date"
    formation = row["formation"]
    commentaire = row["vos remarques et commentaires relatifs a votre insertion professionnelle"]
    
    # Analyser le sentiment du commentaire
    resultat_sentiment = classifier(commentaire)
    sentiment = resultat_sentiment[0]['label']
    
    resultats.append({
        "Annee": annee,
        "Formation": formation,
        "Commentaire": commentaire,
        "Sentiment": sentiment
    })

# Créer un DataFrame à partir de la liste de résultats
df_resultats = pd.DataFrame(resultats)

df_resultats.to_excel("resultats_sentiments.xlsx", index=False)
