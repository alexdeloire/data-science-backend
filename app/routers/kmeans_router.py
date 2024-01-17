# routers/kmeans_router.py
from fastapi import APIRouter, Depends, HTTPException
from ..controllers.kmeans_controller import get_useful_lessons

kmeans_router = APIRouter(
    tags=["kmeans"],
)


@kmeans_router.get("/kmeans/useful-lessons")
def predict_sector_from_query(formation: str = None):
    try:
        if formation is None : 
            formation = "ALL"
        file = get_useful_lessons(formation)
        return file
    except HTTPException as e:
        raise e

