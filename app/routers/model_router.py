# routers/model_router.py
from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from ..controllers.model_controller import predict_sector
from app.controllers.globals import (
    get_tokenizer,
    get_encoder,
    get_model,
    get_encoderPolyChatA,
    get_encoderPolyChatI,
    get_encoderPolyChatR,
    get_encoderPolyChatU,
    get_modelPolyChatA,
    get_modelPolyChatI,
    get_modelPolyChatR,
    get_modelPolyChatU,
    get_tokenizerPolyChatA,
    get_tokenizerPolyChatI,
    get_tokenizerPolyChatR,
    get_tokenizerPolyChatU
)

model_router = APIRouter(
    tags=["formations"],
)

class Query(BaseModel):
    query: str

@model_router.post("/predict_sector/")
def predict_sector_from_query(query: Query, request: Request):
    try:
        query = query.query
        predicted_sector = predict_sector(query, request.app.state.tokenizer, request.app.state.encoder, request.app.state.model)
        return {"predicted_sector": predicted_sector}
    except HTTPException as e:
        raise e

# Enseignements absents qui auraient ete utiles
@model_router.post("/predict_sectorPolyChatA/")
def predict_sector_from_queryPolyChatA(query: Query, request: Request):
    try:
        query = query.query
        predicted_sector = predict_sector(query, get_tokenizerPolyChatA(), get_encoderPolyChatA(), get_modelPolyChatA())
        return {"predicted_sector": predicted_sector}
    except HTTPException as e:
        raise e
    
# Enseignements presents inutiles
@model_router.post("/predict_sectorPolyChatI/")
def predict_sector_from_queryPolyChatI(query: Query, request: Request):
    try:
        query = query.query
        predicted_sector = predict_sector(query, get_tokenizerPolyChatI(), get_encoderPolyChatI(), get_modelPolyChatI())
        return {"predicted_sector": predicted_sector}
    except HTTPException as e:
        raise e
    
# Enseignements presents a renforcer
@model_router.post("/predict_sectorPolyChatR/")
def predict_sector_from_queryPolyChatR(query: Query, request: Request):
    try:
        query = query.query
        predicted_sector = predict_sector(query, get_tokenizerPolyChatR(), get_encoderPolyChatR(), get_modelPolyChatR())
        return {"predicted_sector": predicted_sector}
    except HTTPException as e:
        raise e

# Enseignements presents utiles
@model_router.post("/predict_sectorPolyChatU/")
def predict_sector_from_queryPolyChatU(query: Query, request: Request):
    try:
        query = query.query
        predicted_sector = predict_sector(query, get_tokenizerPolyChatU(), get_encoderPolyChatU(), get_modelPolyChatU())
        return {"predicted_sector": predicted_sector}
    except HTTPException as e:
        raise e
    
    
