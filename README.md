# Proyecto UOC Sound Dynamics

Repositorio correspondiente a la PEC4 de Programación para la Ciencia de Datos (Master en Ciencia de Datos, UOC). Disponible en GitHub desde [aquí](https://github.com/PabloRomanjo/UOC_Sound_Dynamics).

## Autor

[Pablo Román-Naranjo Varela](https://es.linkedin.com/in/pablo-rom%C3%A1n-naranjo-varela-22741860)

## Introducción

Se nos pide realizar un proyecto cuya finalidad es crear una **aplicación para descubrir artistas musicales**. El proyecto se encuentra en una fase inicial dónde se deben analizar los datos existentes. Para ello se debe crear un paquete de Python que lea los datos, los prepare para el análisis, calcule algunas estadísticas básicas y finalmente, cree visualizaciones para comparar diferentes artistas.

Los datos que se utilizaran en el análisis contienen **información sobre canciones, sobre los álbumes que las contienen y sobre los artistas** que las han creado. A parte de detalles básicos como por ejemplo, el nombre de los artistas o el título de las canciones, los datos más interesantes que serán la base del análisis son las **audio features** que nos proporciona Spotify.

## El repositorio

El repositorio se divide en **diferentes carpetas con archivos planos de python**. Estos archivos incluyen diferentes funciones que **se invocan desde el archivo main.py para obtener los resultados pedidos por la PEC4**. Los ficheros y funciones se han dividido en diferentes carpetas:

+ **Carpeta 'data'**: Incluye los archivos necesarios para el funcionamiento del código en un fichero .zip (data.zip). Además, también se incluye el archivo 'artist_audiodb.csv' generado en esta PEC.

+ **Carpeta 'figures'**: Incluye las figuras generadas al lanzar el archivo main.py.

+ **Carpeta 'preprocess'**. Incluye un archivo plano llamado preprocessing.py con **funciones para resolver el preprocesado de los datasets originales (tarea 1)**, incluidos en la carpeta data (data/data.zip). Funciones incluidas:
  + **artist_capitalize()**: Recibe un dataframe que contiene una colunma 'name'. Devuelve la columna 'name' con cada palabra del nombre en mayúsculas.
  + **mean_pop()**:  Recibe un dataframe que incluye canciones y sus features. En la columna 'popularity', sustituye los valores perdidos (NA) por la popularidad media del dataset. Además, devuelve el número de valores perdidos (NA) sustituidos de esta manaera.
  + **rename_columns()**: Renombra las columnas en los archivos data/albums_norm y data/artist_norm añadiendo el prefijo 'album_' o 'artist_', según el dataframe que reciba.
  + **merge_dataset()**: Genera el dataset con el cual se trabaja en esta práctica. Une los datasets data/tracks_norm.csv, data/albums_norm.csv y data/artists_norm.csv.


+ **Carpeta 'read_files'**: Incluye tres archivos planos para resolver la **tarea 2**, es decir, para **explorar alternativas de lectura de ficheros**. En este caso, hemos comparado la lectura de columnas con pandas y con [polars](https://github.com/pola-rs/polars). Estos ficheros incluyen las funciones:
  + **get_column_pandas()**: Recibe la ruta de un archivo csv, lo lee con pandas, y guarda una columna en una lista.
  + **get_column_polars()**: Recibe la ruta de un archivo csv, lo lee con polars, y guarda una columna en una lista.
  + **time_to_read()**: Recibe 'pandas' o 'polars'. Calcula el tiempo de ejecución de las funciones get_column_pandas o get_column_polars de acuerdo al método (method) elegido. El output permite generar un gráfico para comparar los tiempos de ejecución (figures/pandas_polar.png).


+ **Carpeta 'filter'**: Incluye un fichero plano llamado 'eda.py' para realizaz un **análisis exploratorio inicial** de los datos incluidos en el dataset 'tracks', correspondiente a la **tarea 3**. Este fichero incluye las funciones:
  + **count_track_artist()**: Recibe un dataframe incluyendo tracks, artists y albums y un artista. Devuelve el número de canciones del artísta especificado.
  + **count_track_word()**: Recibe un dataframe incluyendo tracks, artists y albums y una palabra. Devuelve el número de canciones con esa palabra en el título.
  + **count_track_decade()**: Recibe un dataframe incluyendo tracks, artists y albums y una década. Devuelve el número de canciones de albumes publicados en esa década.
  + **most_popular_track()**: Recibe un dataframe incluyendo tracks, artists y albums y un número de años. Devuelve una lista con las canciones más populares desde hace el número de años indicado.
  + **active_artists()**: Recibe un dataframe incluyendo tracks, artists y albums y una década. Devuelve una lista de artistas en activo desde la década indicada.


+ **Carpeta 'audio_features'**: Incluye tres archivos planos, llamados accessory_funcions.py, compare.py y stats.py. Estos archivos incluyen las **funciones para tratar datos sobre audio features y resolver las tareas 4, 5, 6 y 7**:
  + **minmaxmean()**: Calcular el mínimo, la media y el máximo de una feature elegida para el artista indicado en el parámetro 'artist'.
  + **plot_album()**: Calcula la media de la característica deseada de un artista y genera un histograma para visualizar el resultado.
  + **density_feature_artist()**: Genera un histograma de densidad de probabilidad de una característica para las canciones de un artista determinado.
  + **features_to_vector()**: Calcula la media de las columnas de un dataframe y las almacena en una lista.
  + **comp_2artist_feat()**: Compara dos artistas de acuerdo a una característica de audio (audio feature). Representa un histograma que muestra la densidad de probabilidad para ambos artistas.
  + **similarities()**: Calcula la distancia Euclidea o Cosine entre los vectores de diferentes artistas según el valor del parámetro 'method'. Estos vectores incluyen la media de los características de audio del artista. Se devuleve un heatmap para la visualizar la distancia entre los artistas.
  
+ **Carpeta 'Extra'**: Incluye un archivo plano, llamado apidb.py, que contiene una función llamada **api_selected_artist()** para resolver la **tarea 8** (opcional). Esta función extrae los datos de la api de AudioDB de los artistas incluidos en la lista introducida. Se genera un dataset con los datos de artist_name, formed_year, country.

## Antes de comenzar

Antes de ejecutar el código, será necesario instalar las dependencias necesarias especificadas en el archivo requirements.txt

```
pip install -r requirements.txt
```

## Ejecución

Para ejecutar la herramienta deberá clonar o descargar como zip y descomprimir este repositorio. Una vez hecho esto, podrá obtener las respuestas a la PEC de la siguiente manera:

```
pithon3 main.py
```

## Licencia
Este proyecto y los datasets derivados son publicados bajo licencia CC BY-NC-SA 4.0. [Más info](https://github.com/avicenteg/euraxess_scraping/blob/master/LICENSE.md)
This project and all the datasets derived from it are realesed under CC BY-NC-SA 4.0 License. [See more](https://github.com/PabloRomanjo/UOC_Sound_Dynamics/blob/main/LICENSE.md)



