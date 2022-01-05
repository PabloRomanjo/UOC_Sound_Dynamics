import pandas as pd


def get_column_pandas(file, column):
    """Lee de una columna usando pandas y la
    almacena en una lista.

    :param file: Ruta de archivo cvs separado por ";"
    :param column: Columna de archivo csv 'file'
    :return: Lista que contiente la columna elegida
    """

    data = pd.read_csv(file, sep=";")
    selected_col = list(data[column])
    return selected_col
