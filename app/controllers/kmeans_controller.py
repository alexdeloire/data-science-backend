from fastapi import HTTPException
import json
import os

folder_useful_lessons = "kmeans/result_enseignements_utiles"

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