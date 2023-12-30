import os
import pandas as pd
from extraction import series_type


folder_path = '../new_data'

for file_name in os.listdir(folder_path):
    if (file_name.endswith('.xlsx') or file_name.endswith('.xls')) :
        excel_file_path = os.path.join(folder_path, file_name)
        print(f'Processing {excel_file_path}...')
        
        df = pd.read_excel(excel_file_path)

        # Iterate through each column
        for column_name in df.columns:
            if column_name == 'Date':
                continue
            # Check if the column is of type text, category or binary
            if series_type(df[column_name]) == 'text' or series_type(df[column_name]) == 'category' or series_type(df[column_name]) == 'binary':
                # Apply the specified operations
                df[column_name] = df[column_name].str.replace(',', '')
                df[column_name] = df[column_name].str.replace('\r\n', '')
                df[column_name] = df[column_name].str.replace('\r', '')
                df[column_name] = df[column_name].str.replace('È', 'é')
                df[column_name] = df[column_name].str.replace('Ê', 'ê')
                df[column_name] = df[column_name].str.replace('Ë', 'ë')
                df[column_name] = df[column_name].str.replace('_x000D_', '')
                
                # Now remove all accents
                df[column_name] = df[column_name].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
            
            # Do the same for the column name
            new_column_name = column_name.replace('È', 'é')
            new_column_name = new_column_name.replace('Ê', 'ê')
            new_column_name = new_column_name.replace('Ë', 'ë')
            
            # Remove accents
            new_column_name = new_column_name.replace('é', 'e')
            new_column_name = new_column_name.replace('ê', 'e')
            new_column_name = new_column_name.replace('ë', 'e')
            new_column_name = new_column_name.replace('è', 'e')
            new_column_name = new_column_name.replace('à', 'a')
            new_column_name = new_column_name.replace('â', 'a')
            new_column_name = new_column_name.replace('î', 'i')
            new_column_name = new_column_name.replace('ï', 'i')
            new_column_name = new_column_name.replace('ô', 'o')
            new_column_name = new_column_name.replace('ù', 'u')
            new_column_name = new_column_name.replace('û', 'u')
            new_column_name = new_column_name.replace('ç', 'c')
            new_column_name = new_column_name.replace('œ', 'oe')
            new_column_name = new_column_name.replace('æ', 'ae')
            new_column_name = new_column_name.replace('Æ', 'ae')
            new_column_name = new_column_name.replace('Å', 'a')
            new_column_name = new_column_name.replace('ø', 'o')
            new_column_name = new_column_name.replace('Ø', 'o')
            new_column_name = new_column_name.replace('Å', 'a')
            
            # Lowercase
            new_column_name = new_column_name.lower()
            
            df = df.rename(columns={column_name: new_column_name})

        # Get the name before the extension
        new_file_name = file_name.split('.')[0]
        # Save the modified DataFrame back to Excel
        df.to_excel(f'../formatted_data/{new_file_name}.xlsx', index=False)

