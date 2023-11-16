import pandas as pd


def read_excel(path):
    """
    Read excel file
    :param path: path to excel file
    :return: pandas dataframe
    """
    try:
        return pd.read_excel(path)
    
    except FileNotFoundError:
        print(f"File {path} not found")

    except Exception as e:
        print(f"Error while reading file {path}: {e}")

    exit(1)


def series_type(sr):
    """
    return the type of a pandas Series
    :param sr: pandas Series
    """
    if sr.dtype == 'object':
        if sr.nunique() < 20:
            if sr.nunique() == 2:
                return 'binary'
            elif sr.count() > sr.nunique() * 2:
                return 'category'
        return 'text'
    elif sr.dtype in ['float64', 'float32', "int64", "int32"]:
        return 'number'
    elif sr.dtype == 'datetime64[ns]':
        return 'date'
    return 'unknown'


def series_type_description(sr, sr_type):
    """
    return a description of the type of a pandas Series
    :param sr: pandas Series, sr_type: type of the Series
    """
    if sr_type == "number":
        return f"max = {sr.max()}, min = {sr.min()}"
    elif sr_type == "date":
        return f"max = {sr.max()}, min = {sr.min()}"
    elif sr_type == "binary" or sr_type == "category":
        unique_values = sr.unique()
        unique_values = [str(value) for value in unique_values if str(value) != 'nan']
        return f"unique values = {' | '.join(unique_values)}"
    return ""

def series_infos(sr):
    """
    return a Series with the type(number, date, categorie, text), summary of values, the number of missing values, the number of values,
    the number of unique values
    :param sr: pandas Series
    """
    sr_info = pd.Series()
    sr_info['type'] = series_type(sr)
    sr_info['infos_values'] = series_type_description(sr, sr_info['type'])
    sr_info['number_missing_values'] = sr.isnull().sum()
    sr_info['number_values'] = sr.count()
    sr_info['number_unique_values'] = sr.nunique()
    return sr_info


def dataframe_infos(df):
    """
    return a dataframe with the type(number, date, categorie, text), summary of values, the number of missing values, the number of values,
    the number of unique values for each column of the dataframe
    :param df: pandas dataframe
    """
    df_infos = pd.concat([series_infos(df[column]) for column in df.columns], axis=1)
    df_infos.columns = df.columns
    df_infos = df_infos.transpose()
    return df_infos


def remove_missing_values(df, threshold=0.05):
    """
    remove colum with too much missing values
    :param df: pandas dataframe
    """
    df = df.dropna(axis=1, thresh=threshold*len(df))
    return df


def combine_dataframe(dataframes: [pd.DataFrame]):
    """
    create a new dataframe, the colum are in ./questions.txt and the rows are the dataframes
    :param dataframes: list of pandas dataframe
    """
    with open("questions.txt", "r", encoding="utf-8") as f:
        questions = f.readlines()
    df = pd.DataFrame(columns=questions)

    # TO DODO (j'avais une version mais trop mauvaise, je la refais plus tard)
    return df



if __name__ == "__main__":
    #data2018 = read_excel("data/extraction_finale_enquete_2018DS.xls")
    data2019 = read_excel("data/extraction_finale_enquete_2019DS.xlsx")
    #data2020 = read_excel("data/extraction_finale_enquete_2020DS.xlsx")
    #data2021 = read_excel("data/extraction_finale_enquete_2021DS.xlsx")
    #data2022 = read_excel("data/extraction_finale_enquete_2022_DS.xlsx")
    #data2023 = read_excel("data/Extraction finale_enquete 2023DS.xls")

    df_info_2019 = dataframe_infos(data2019)
    df_info_2019_2 = dataframe_infos(remove_missing_values(data2019))

    # export to excel
    df_info_2019.to_excel("infos_2019.xlsx")
    #df_info_2018_2.to_excel("infos_2018_2.xlsx")

