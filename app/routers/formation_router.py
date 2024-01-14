# routers/formation_router.py
from fastapi import APIRouter, Depends, HTTPException
from ..controllers.formation_controller import read_excel

formation_router = APIRouter(
    tags=["formations"],
)

@formation_router.get("/formations/")
def get_formations(column: str = "formation"):
    file_path = "formatted_data/2023.xlsx"
    try:
        formations = read_excel(file_path, column)
        return {"formations": formations}
    except HTTPException as e:
        raise e
