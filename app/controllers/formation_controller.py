# controllers/formations_controller.py
from fastapi import HTTPException
import pandas as pd

def read_excel(file_path, column_name):
    try:
        df = pd.read_excel(file_path)
        formations = df[column_name].tolist()
        # Transform the list of formations into a list of dictionaries
        # Dictionary keys are the the values and the values are the count of the formations
        formations = [{key: formations.count(key)} for key in set(formations)]
        # Merge the dictionaries into one
        formations = {k: v for d in formations for k, v in d.items()}
        return formations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading Excel file: {str(e)}")


if __name__ == "__main__":
    print(read_excel("formatted_data/2023.xlsx", "formation"))
    