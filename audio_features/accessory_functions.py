import numpy as np

available_features = ['energy', 'key', 'loudness', 'mode', 'speechiness',
                      'acousticness', 'instrumentalness', 'liveness',
                      'valence', 'tempo', 'time_signature', 'danceability']


def features_to_vector(df):
    """Calcula la media de las columnas de un dataframe y las almacena en
    una lista

    :param df: Dataframe
    :return: Lista con las medias de las columnas del dataframe
    """

    df_matrix = df.to_numpy(na_value=0)
    vector = np.mean(df_matrix, axis=0)
    return list(vector)
