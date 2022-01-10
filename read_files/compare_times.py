from timeit import Timer
import pandas as pd
from read_files.get_column_pandas import get_column_pandas
from read_files.get_column_polars import get_column_polars

files = ['./data/artists_norm.csv',
         './data/albums_norm.csv',
         './data/tracks_norm.csv']


def time_to_read(method):
    """Calcula el tiempo de ejecución de las funciones get_column_pandas o
    get_column_polars de acuerdo al método (method) elegido, recibiendo
    estas funciones los ficheros especificicados en la variable 'files'.

    :param method: 'pandas' o 'polars'
    :return: Dataframe con los tiempos de ejecución para cada fichero
    """
    if method == "pandas":
        t_pandas_1 = Timer(lambda:
                           get_column_pandas(files[0],
                                             'artist_id')).timeit(number=1)
        size_pandas_1 = len(get_column_pandas(files[0], 'artist_id'))
        t_pandas_2 = Timer(lambda:
                           get_column_pandas(files[1],
                                             'album_id')).timeit(number=1)
        size_pandas_2 = len(get_column_pandas(files[1], 'album_id'))
        t_pandas_3 = Timer(lambda:
                           get_column_pandas(files[2],
                                             'track_id')).timeit(number=1)
        size_pandas_3 = len(get_column_pandas(files[2], 'track_id'))
        return pd.DataFrame({'nrows': [size_pandas_1, size_pandas_2,
                                       size_pandas_3],
                             'pandas_time': [t_pandas_1, t_pandas_2,
                                             t_pandas_3]})

    elif method == "polar":
        t_polar_1 = Timer(lambda:
                          get_column_polars(files[0],
                                            'artist_id')).timeit(number=1)
        size_polar_1 = len(get_column_polars(files[0], 'artist_id'))
        t_polar_2 = Timer(lambda:
                          get_column_polars(files[1],
                                            'album_id')).timeit(number=1)
        size_polar_2 = len(get_column_polars(files[1], 'album_id'))
        t_polar_3 = Timer(lambda:
                          get_column_polars(files[2],
                                            'track_id')).timeit(number=1)
        size_polar_3 = len(get_column_polars(files[2], 'album_id'))
        return pd.DataFrame({'nrows': [size_polar_1, size_polar_2,
                                       size_polar_3],
                             'polar_time': [t_polar_1, t_polar_2,
                                            t_polar_3]})
    else:
        return print("Please, type 'pandas' or 'polar' as method.")
