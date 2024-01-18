from fastapi import HTTPException
import json
import os

folder_useful_lessons = "kmeans/result_enseignements_utiles"
folder_absent_lessons = "kmeans/result_enseignements_absent"
folder_advice = "kmeans/result_conseil"

def get_useful_lessons(formation):
    file_path = folder_useful_lessons + "/" + formation.upper() + ".json"
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail=f"Formation {formation} not found")
    try:
        with open(file_path, 'r') as f:
            file = json.load(f)
        return file
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {e}")
    
def get_absent_lessons(formation):
    file_path = folder_absent_lessons + "/" + formation.upper() + ".json"
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail=f"Formation {formation} not found")
    try:
        with open(file_path, 'r') as f:
            file = json.load(f)
        return file
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {e}")
    
def get_advice(formation):
    file_path = folder_advice + "/" + formation.upper() + ".json"
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail=f"Formation {formation} not found")
    try:
        with open(file_path, 'r') as f:
            file = json.load(f)
        return file
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {e}")