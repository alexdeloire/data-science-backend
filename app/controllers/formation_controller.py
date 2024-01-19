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


def count_response(file_path, column, json_file_path):
    try:
        # Check if precalculated data exists
        if check_json_existence(json_file_path):
            print("JSON file exists")
            # Load data from the existing JSON file
            return load_from_json(json_file_path)
        else:
            df = pd.read_excel(file_path)
            formations = df[column].tolist()
            count = len(formations)
            to_send = {"count": count}
            # Save the calculated data to a JSON file
            save_to_json(to_send, json_file_path)
            return to_send
        
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading Excel file: {str(e)}")
    

def count_sexe_by_formation(file_path,column_name, json_file_path):
    try:
        # Check if precalculated data exists
        if check_json_existence(json_file_path):
            # Load data from the existing JSON file
            return load_from_json(json_file_path)
        else:
            df = pd.read_excel(file_path)
            formations = df["formation"].tolist()
            sexe = df[column_name].tolist()
            result_dict = {}

            for form, sex in zip(formations, sexe):
                if form not in result_dict:
                    result_dict[form] = {}
                if sex not in result_dict[form]:
                    result_dict[form][sex] = 1
                else:
                    result_dict[form][sex] += 1
                    
            # Save the calculated data to a JSON file
            save_to_json(result_dict, json_file_path)
                    
            return result_dict

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading Excel file: {str(e)}")


def count_by_formation(file_path, column_name, json_file_path):
    
    try:
        # Check if precalculated data exists
        if check_json_existence(json_file_path):
            # Load data from the existing JSON file
            return load_from_json(json_file_path)
        else:
            df = pd.read_excel(file_path)
            formations = df["formation"].tolist()
            #print("Noms de colonnes disponibles dans le DataFrame:\n", df.columns.tolist())
            #print("\n\n", df[column_name])
            
            # Convertir les valeurs de satisfaction en chaînes de caractères
            satisfaction = df[column_name].astype(str).tolist()
            
            result_dict = {}

            for form, sat in zip(formations, satisfaction):
                if form not in result_dict:
                    result_dict[form] = {}
                
                # Vérifier si la valeur de satisfaction n'est pas NaN
                if sat != 'nan':
                    if sat not in result_dict[form]:
                        result_dict[form][sat] = 1
                    else:
                        result_dict[form][sat] += 1
            
            # Save the calculated data to a JSON file
            save_to_json(result_dict, json_file_path)
                    
            return result_dict

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading Excel file: {str(e)}")
    

def count_by_text_response(file_path, question, json_file_path):
    try:
        # Check if precalculated data exists
        if check_json_existence(json_file_path):
            # Load data from the existing JSON file
            return load_from_json(json_file_path)
        else:
            df = pd.read_excel(file_path)
            formations = df["formation"].tolist()
            responses = df[question].tolist()
            
            result_dict = {}

            for form, resp in zip(formations, responses):
                # Vérifier si la valeur de la réponse n'est pas NaN et est une chaîne de caractères non vide
                if not pd.isna(resp) and isinstance(resp, str) and resp.strip():
                    key = "true"
                else:
                    key = "false"
                
                result_dict.setdefault(form, { "true": 0, "false": 0 })
                result_dict[form][key] += 1

            # Save the calculated data to a JSON file
            save_to_json(result_dict, json_file_path)
                
            return result_dict

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading Excel file: {str(e)}")


import os
import json

def check_json_existence(file_path):
    """
    Check if a JSON file exists.

    Parameters:
    - file_path (str): Path to the JSON file.

    Returns:
    - bool: True if the file exists, False otherwise.
    """
    return os.path.exists(file_path)

def save_to_json(data, file_path):
    """
    Save data to a JSON file.

    Parameters:
    - data (dict): Data to be saved.
    - file_path (str): Path to the JSON file.
    """
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)

def load_from_json(file_path):
    """
    Load data from a JSON file.

    Parameters:
    - file_path (str): Path to the JSON file.

    Returns:
    - dict: Loaded data.
    """
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

    
if __name__ == "__main__":
    print(read_excel("formatted_data/2023.xlsx", "formation"))
    


