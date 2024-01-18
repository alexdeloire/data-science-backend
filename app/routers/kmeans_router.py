# routers/kmeans_router.py
from fastapi import APIRouter, Depends, HTTPException
from ..controllers.kmeans_controller import get_useful_lessons
from ..controllers.kmeans_controller import get_absent_lessons
from ..controllers.kmeans_controller import get_advice

kmeans_router = APIRouter(
    tags=["kmeans"],
)


@kmeans_router.get("/kmeans/useful-lessons")
def predict_sector_from_query_useful(formation: str = None):
    try:
        if formation is None : 
            formation = "ALL"
        file = get_useful_lessons(formation)
        return file
    except HTTPException as e:
        raise e

@kmeans_router.get("/kmeans/absent-lessons")
def predict_sector_from_query_absent(formation: str = None):
    try:
        if formation is None : 
            formation = "ALL"
        file = get_absent_lessons(formation)
        return file
    except HTTPException as e:
        raise e
    
@kmeans_router.get("/kmeans/advice")
def predict_sector_from_query_advice(formation: str = None):
    try:
        if formation is None : 
            formation = "ALL"
        file = get_advice(formation)
        return file
    except HTTPException as e:
        raise e