import pandas as pd


def artist_capitalize(artists_file):
    """Nombre en mayúsculas

    :param artists_file: Dataframe de archivo csv que contiene una colunma 'name'
    :return: Devuelve la columna 'name' con cada palabra del nombre
    en mayúsculas
    """
    artists_file["name"] = artists_file["name"].str.title()
    return None


def mean_pop(tracks_file):
    """ En la columna 'popularity', sustituye valores perdidos (NA)
     por popularidad media.

    :param tracks_file: Dataframe que incluye canciones y sus features
    :return: Devuelve valores perdidos (NA) en columna 'popularity'
    """

    mean = tracks_file["popularity"].mean()
    sum_na = tracks_file["popularity"].isna().sum()
    tracks_file["popularity"].fillna(mean, inplace=True)
    return sum_na


def rename_columns(df):
    """Renombra las columnas en los archivos albums_norm y artist_norm
    añadiendo el prefijo 'album_' o 'artist_', según el dataframe que
    reciba.

    :param df: Dataframe generado de albums_norm.csv o artist_norm.csv
    :return: Sin retorno
    """

    prefix_artist = {"name", "popularity", "followers", "total_albums"}
    prefix_album = {"name", "popularity", "release_year", "total_tracks"}
    if "total_tracks" in df.columns:
        df.rename(columns={col: 'album_' + col for col in prefix_album}, inplace=True)
    elif "followers" in df.columns:
        df.rename(columns={col: 'artist_' + col for col in prefix_artist}, inplace=True)
    return None


def merge_dataset(tracks, albums, artists):
    """Crea un dataset final apartir de los dataframes de tracks_norm.cvs,
    albums_norm.csv y artists_norm.csv

    :param tracks: Dataframe de tracks_norm.cvs
    :param albums: Dataframe de albums_norm.csv
    :param artists: Dataframe de artists_norm.csv
    :return: Dataframe de los archivos relacionados (tracks, albums & artists)
    """

    tracks_artist = pd.merge(tracks, artists, on='artist_id')
    final_df = pd.merge(tracks_artist, albums, on=['artist_id', 'album_id'])
    return final_df
