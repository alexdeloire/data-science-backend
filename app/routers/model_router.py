# routers/model_router.py
from fastapi import APIRouter, Depends, HTTPException, Request
from ..controllers.model_controller import predict_sector

model_router = APIRouter(
    tags=["formations"],
)

@model_router.post("/predict_sector/")
def predict_sector_from_query(query: str, request: Request):
    try:
        predicted_sector = predict_sector(query, request.app.state.tokenizer, request.app.state.encoder, request.app.state.model)
        return {"predicted_sector": predicted_sector}
    except HTTPException as e:
        raise e

