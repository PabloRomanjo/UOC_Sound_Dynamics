from datetime import date


def count_track_artist(df, artist):
    tracks = df[df['artist_name'] == artist]
    return print("Tracks recorded by {}:".format(artist), len(tracks))


def count_track_word(df, word):
    tracks = df[df['name'].str.contains(word)]
    return print("Name of tracks including the string {}:".format(word),
                 len(tracks))


def count_track_decade(df, decade):
    if decade % 10 == 0:
        tracks = df[df['album_release_year'].between(decade, decade + 9)]
        return print("Number of tracks published in {}'s decade:".format(decade),
                     len(tracks))
    else:
        return print('Please, select a correct decade (e.g. 1970, 1990, 2000)')


todays_year = date.today().year


def most_popular_track(df, year):
    tracks = df[df['album_release_year'].between(todays_year - year, todays_year)]
    mostpopular = tracks[tracks['popularity'] == max(tracks['popularity'])]['name']
    return print("The most popular track in the last {} years is".format(year),
                 list(mostpopular)[0])


def active_artists(df, decade):
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
