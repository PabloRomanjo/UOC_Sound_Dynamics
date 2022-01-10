# importing required modules
import zipfile as zp
import preprocess.preprocessing as pp
from read_files.compare_times import time_to_read as tr
from filter.eda import *
from audio_features.stats import *
from audio_features.compare import *
from Extra.apidb import api_selected_artist


def main():
    # unzip the dataset
    with zp.ZipFile('data/data.zip', "r") as zip_ref:
        zip_ref.extractall("data")
    # read files
    tracks_file = pd.read_csv("data/tracks_norm.csv", sep=';')
    albums_file = pd.read_csv("data/albums_norm.csv", sep=';')
    artists_file = pd.read_csv("data/artists_norm.csv", sep=';')
    # PREPROCESS (Tarea 1)
    # capitalize artists names
    pp.artist_capitalize(artists_file)
    # tracks popularity: fill NA values with mean
    corrected = pp.mean_pop(tracks_file)
    print("Corrected 'popularity' NA values: {}".format(corrected))
    # rename albums_file and artist_file dataframe
    pp.rename_columns(albums_file)
    pp.rename_columns(artists_file)
    # merge dataset (tracks, albums & artists)
    merged_df = pp.merge_dataset(tracks_file, albums_file, artists_file)
    print("Total tracks: {}".format(len(merged_df)))
    print("Merged DF total columns: {}".format(len(merged_df.columns)))
    # ALTERNATIVE TO PANDAS (Tarea 2)
    times = pd.merge(tr('pandas'), tr('polar'), on='nrows')
    plot_time = times.plot(x='nrows', y=['pandas_time', 'polar_time'])
    plot_time.set_ylabel("Time (s)")
    plot_time.set_title("Time to read a column: Pandas vs Polar")
    plt.savefig("figures/pandas_polar.png")
    plt.show()
    # EDA (Tarea 3)
    # Artist number of tracks
    count_track_artist(merged_df, 'Radiohead')
    # Count tracks with a word
    count_track_word(merged_df, 'Police')
    # Count tracks in a decade
    count_track_decade(merged_df, 1990)
    # Most popular track last x years
    most_popular_track(merged_df, 10)
    # Active artist from decade x
    active_artists(merged_df, 1960)
    # AUDIO FEATURES (Tareas 4, 5, 6, y 7)
    # Min max and mean of feature from artist (Tarea 4)
    minmaxmean(merged_df, 'energy', 'Metallica')
    # Hist artist feature (Tarea 4)
    plot_album(merged_df, 'danceability', 'Coldplay')
    # Density plot artist feature (Tarea 5)
    density_feature_artist(merged_df, 'acousticness', 'Ed Sheeran')
    # Comparison two artist features (Tarea 6)
    comp_2artist_feat(merged_df, 'energy', 'Adele', 'Extremoduro')
    # Euclidean and cosine similarities between artist (Tarea 7)
    similarities(merged_df, 'Euclidean',
                 ['Metallica', 'Extremoduro', 'Hans Zimmer', "Ac/Dc"])
    similarities(merged_df, 'Cosine',
                 ['Metallica', 'Extremoduro', 'Hans Zimmer', "Ac/Dc"])
    print("Generando el dataset y mostrando la respuesta a Tarea 8...")
    tarea8 = api_selected_artist(["Radiohead", "David Bowie", "Måneskin"])
    print(tarea8)
    print("Generando el dataset artists_audiodb.csv...")
    list_of_artists = list(set(artists_file['artist_name']))
    artist_audio_db = api_selected_artist(list_of_artists)
    print("Guardando el dataset en carpeta data...")
    artist_audio_db.to_csv("data/artists_audiodb.csv")
    print("¡Dataset guardado!")
    print("¡PEC4 finalizada! ¡Feliz año!")


if __name__ == '__main__':
    main()
