import time
import pandas as pd
import requests


def api_selected_artist(artists):
    """Extrae los datos de los artistas incluidos en la lista introducida.
    Se genera un dataset con los datos de artist_name, formed_year, country.
    Los datos se extraen de la api de AudioDB.

    :param artists: lista de artistas
    :return: Dataframe con los datos especificados de los artistas
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/94.0.4606.81 Safari/537.36',
        'Accept-Language': 'en-GB,en;q=0.9,es-ES;q=0.8,es;q=0.7',
        'Referer': 'https://google.com',
        'DNT': '1'
    }
    template_url = "https://www.theaudiodb.com/api/v1/json/2/search.php?s="
    data = []
    for i in artists:
        print("Extrayendo datos de {}".format(i))
        api_response = requests.get(template_url + i, headers=headers)
        api_json = api_response.json()
        if api_json['artists'] is None:
            pass
        else:
            response_to_dict = api_json["artists"][0]
            data.append([response_to_dict["strArtist"],
                         response_to_dict["intFormedYear"],
                         response_to_dict["strCountry"]])
        time.sleep(3)
    df = pd.DataFrame(data)
    df.columns = ['Artist_name', 'Formed_Year', 'Country']
    df.index = pd.RangeIndex(len(df.index))
    print("¡Proceso completado!")
    return df
