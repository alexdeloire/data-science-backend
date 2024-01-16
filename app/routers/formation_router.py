# routers/formation_router.py
from fastapi import APIRouter, Depends, HTTPException
from ..controllers.formation_controller import read_excel, count_sexe_by_formation,count_by_formation, count_response, count_by_text_response
from ..controllers.formation_controller import read_excel, count_sexe_by_formation,count_by_formation, count_response, count_by_text_response

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
        response = count_response(file_path, column)
        return {"count": response}
    except HTTPException as e:
        raise e

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
        response = count_response(file_path, column)
        return {"count": response}
    except HTTPException as e:
        raise e

@formation_router.get("/formations/")
def get_formations(year: int, column: str = "formation"):
    file_path = f"formatted_data/{year}.xlsx"
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
       sexe = count_sexe_by_formation(file_path,column_name)
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
        
    try:
       satisfaction = count_by_formation(file_path, column_name)
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
        
    try:
       satisfaction = count_by_formation(file_path, column_name)
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
        
    try:
       satisfaction = count_by_formation(file_path, column_name)
       return {"reputation": satisfaction}
    except HTTPException as e:
        raise e


@formation_router.get("/count/")
def get_count_by_text_response(year: int, question: str):
    file_path = f"formatted_data/{year}.xlsx"
    print(question)
    print(file_path)
    try:
       count = count_by_text_response(file_path, question)
       return {"count": count}
    except HTTPException as e:
        raise e   