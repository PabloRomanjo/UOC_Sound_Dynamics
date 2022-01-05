import polars as pl


def get_column_polars(file, column):
    """Lee una columna usando polars y la
    almacena en una lista.

    :param file: Ruta de archivo cvs separado por ";"
    :param column: Columna de archivo csv 'file'
    :return: Lista que contiente la columna elegida
    """

    data = pl.read_csv(file, sep=";")
    selected_col = list(data[column])
    return selected_col
