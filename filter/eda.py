from datetime import date


def count_track_artist(df, artist):
    """Cuenta el número de canciones de un artista.

    :param df: Dataframe incluyendo tracks, artists y albums
    :param artist: Nombre de un artista (ej: 'Extremoduro')
    :return: Número de canciones del artísta especificado
    """
    
    tracks = df[df['artist_name'] == artist]
    return print("Tracks recorded by {}:".format(artist), len(tracks))


def count_track_word(df, word):
    """Cuenta las canciones en cuyo título aparezca una palabra específica

    :param df: Dataframe incluyendo tracks, artists y albums
    :param word: Una palabra (ej: 'police')
    :return: Número de canciones con la palabra especificada.
    """
    
    tracks = df[df['name'].str.contains(word)]
    return print("Name of tracks including the string {}:".format(word),
                 len(tracks))


def count_track_decade(df, decade):
    """Cuenta el número de canciones de los albumes publicados en una década especifica

    :param df: Dataframe incluyendo tracks, artists y albums
    :param decade: Decada (ej: 1990)
    :return: Número de albumes en la decada especificada
    """
    
    if decade % 10 == 0:
        tracks = df[df['album_release_year'].between(decade, decade + 9)]
        return print("Number of tracks published in {}'s decade:".format(decade),
                     len(tracks))
    else:
        return print('Please, select a correct decade (e.g. 1970, 1990, 2000)')


todays_year = date.today().year


def most_popular_track(df, year):
    """ Devuelve una lista con las canciones más populares en los últimos x años

    :param df: Dataframe incluyendo tracks, artists y albums
    :param year: Número de años (ej: 10)
    :return: Devuelve una lista con las canciones más populares de los últimos años
    """
    
    tracks = df[df['album_release_year'].between(todays_year - year, todays_year)]
    mostpopular = tracks[tracks['popularity'] == max(tracks['popularity'])]['name']
    return print("The most popular track in the last {} years is".format(year),
                 list(mostpopular)[0])


def active_artists(df, decade):
    """Devuelve una lista de artistas en activo desde una década específica.

    :param df: Dataframe incluyendo tracks, artists y albums
    :param decade: Década (ej: 1960)
    :return: Lista de artistas en activo
    """
    
    if decade % 10 == 0:
        df['decade'] = [year - (year % 10) for year in df["album_release_year"]]
        subdf = df[['artist_name', 'decade']]
        artists = list(set(subdf[subdf['decade'] == decade]['artist_name']))
        if len(artists) == 0:
            print("No active artists since {}'s decade".format(decade))
        else:
            selected = []
            for artist in range(len(artists)):
                test = []
                for i in range(decade, todays_year, 10):
                    if i in list(subdf[subdf['artist_name'] == artists[artist]]['decade']):
                        test.append("yes")
                    else:
                        test.append("no")
                if "no" not in test:
                    selected.append(artists[artist])
            return print("Active artists since {}'s decade:".format(decade), selected)
    else:
        return print('Please, select a correct decade (e.g. 1970, 1990, 2000)')
