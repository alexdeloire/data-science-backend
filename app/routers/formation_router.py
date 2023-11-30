# routers/formation_router.py
from fastapi import APIRouter, Depends, HTTPException
from ..controllers.formation_controller import read_excel

formation_router = APIRouter(
    prefix="/api",
    tags=["formations"],
)

@formation_router.get("/formations/")
def get_formations(column: str = "Formation"):
    file_path = "data/2023.xls"
    try:
        formations = read_excel(file_path, column)
        return {"formations": formations}
    except HTTPException as e:
        raise e
