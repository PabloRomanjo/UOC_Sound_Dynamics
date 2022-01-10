import statistics
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

available_features = ['energy', 'key', 'loudness', 'mode', 'speechiness',
                      'acousticness', 'instrumentalness', 'liveness',
                      'valence', 'tempo', 'time_signature', 'danceability']
save_path = "./figures/"


def minmaxmean(df, feature, artist):
    """Calcular el mínimo, la media y el máximo de la feature elegica para el
    artista indicado en el parámetro 'artist'

    :param df: Dataframe incluyendo tracks, artists y albums
    :param feature: Característica (feature) de interés
    :param artist: Artista incluido en el dataset
    :return: Mínimo, media y máximo de feature elegida
    """

    if feature in available_features:
        feature_values = list(df[df['artist_name'] == artist][feature])
        min_feature = min(feature_values)
        max_feature = max(feature_values)
        mean_feature = statistics.mean(feature_values)
        return print(" Min {} value in {}'s tracks: {}\n".format(feature,
                                                                 artist,
                                                                 min_feature),
                     "Max {} value in {}'s tracks: {}\n".format(feature,
                                                                artist,
                                                                max_feature),
                     "Mean {} value in {}'s tracks: {}\n".format(feature,
                                                                 artist,
                                                                 mean_feature))
    else:
        return print("Please, select an audio feature from the list:",
                     available_features)


def plot_album(df, feature, artist):
    """Calcula la media de la característica deseada de un artista y genera un
    histograma para visualizar el resultado

    :param df: Dataframe incluyendo tracks, artists y albums
    :param feature: Característica (feature) de interés
    :param artist: Artista incluido en el dataset
    :return: Histograma (media feature vs Album)
    """

    if feature in available_features:
        subdf = df[df['artist_name'] == artist][['album_name', feature]]
        albums = list(set(subdf['album_name']))
        means = []
        for album in albums:
            values = subdf[subdf['album_name'] == album][feature]
            means.append(statistics.mean(values))
        result = pd.DataFrame({'albums': albums, feature: means})
        sns.barplot(x=means, y=albums, data=result,
                    orient='h').\
            set_title("{}'s albums: Mean {} ".format(artist, feature))
        plt.xlabel('mean {}'.format(feature))
        figure = plt.gcf()  # get current figure
        figure.set_size_inches(20, 20)
        plt.savefig(save_path + "{}_{}_albums.png".format(artist, feature))
        return plt.show()
    else:
        return print("Please, select an audio feature from the list:",
                     available_features)


def density_feature_artist(df, feature, artist):
    """Genera un histograma de densidad de probabilidad de una característica
    para las canciones de un artista determinado.

    :param df: Dataframe incluyendo tracks, artists y albums
    :param feature: Característica (feature) de interés
    :param artist: Artista incluido en el dataset
    :return: Histograma de densidad de probabilidad (Feature vs artist)
    """

    if feature in available_features:
        subdf = df[df['artist_name'] == artist][['name', feature]]
        plot_dens = sns.displot(subdf[feature], bins=20,
                                stat="probability", color="lightblue")
        plot_dens.set(title="{} tracks' {}".format(artist, feature))
        figure = plt.gcf()
        figure.set_size_inches(10, 10)
        plt.savefig(save_path + "{}_{}_density.png".format(artist, feature))
        return plt.show()
    else:
        return print("Please, select an audio feature from the list:",
                     available_features)
