
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

