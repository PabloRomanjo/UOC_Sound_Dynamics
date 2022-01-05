import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import euclidean_distances, cosine_distances

from audio_features import accessory_functions as af

available_features = ['energy', 'key', 'loudness', 'mode', 'speechiness',
                      'acousticness', 'instrumentalness', 'liveness', 'valence',
                      'tempo', 'time_signature', 'danceability']
save_path = "./figures/"


def comp_2artist_feat(df, feature, artist1, artist2):
    """Compara dos artistas de acuerdo a una característica de audio (audio feature).
    Representa un histograma que muestra la densidad de probabilidad.

    :param df: Dataframe incluyendo tracks, artists y albums
    :param feature: Característica de audio
    :param artist1: Nombre de un artista incluido en el dataset
    :param artist2: Nombre de otro artista incluido en el dataset
    :return: Histograma que muestra la densidad de probabilidad.
    """

    if feature in available_features:
        artists = [artist1, artist2]
        subdf = df[df['artist_name'].isin(artists)][['name', feature, 'artist_name']]
        plot_comp = sns.displot(data=subdf, x=feature, bins=20,
                                hue="artist_name", stat="probability")
        plot_comp.set(title="{}: {} vs {}".format(feature, artist1, artist2))
        figure = plt.gcf()
        figure.set_size_inches(10, 10)
        plt.savefig(save_path + "{}_{}_{}_comp.png".format(artist1, artist2, feature))
        return plt.show()
    else:
        return print("Please, select an audio feature from the list:", available_features)


def similarities(df, method, list_artists='all'):
    """Calcula la distancia Euclidea o Cosine entre los vectores de diferentes artistas.
    Estos vectores incluyen la media de los caracteríscticas de audio del artista.

    :param df: Dataframe incluyendo tracks, artists y albums
    :param method: 'Euclidean' o 'Cosine'
    :param list_artists: Lista de artistas incluidos en el dataset. Por defecto muestra
    la comparación entre todos los artistas.
    :return: Heatmap que representa la distancia entre artistas
    """

    if list_artists == 'all':
        artists = list(set(df['artist_name']))
        print(artists)
    else:
        artists = list_artists
    artist_features = []
    for artist in artists:
        sub_df = df[df['artist_name'] == artist][available_features]
        artist_vector = af.features_to_vector(sub_df)
        artist_features.append(artist_vector)
    if method == 'Euclidean':
        dist = euclidean_distances(artist_features)
    elif method == 'Cosine':
        dist = cosine_distances(artist_features)
    else:
        print("Please, use 'Euclidean' or 'Cosine' as method")
    heat = sns.heatmap(dist, xticklabels=artists, yticklabels=artists)
    heat.set_title('{} distances between artists'.format(method))
    figure = plt.gcf()  # get current figure
    figure.set_size_inches(20, 20)
    plt.savefig(save_path + "artists_heatmap_{}.png".format(method))
    return plt.show()
