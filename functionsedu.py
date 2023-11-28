# Funciones vinculadas al main.py

# Importaciones
from pathlib import Path
from fastapi import Query
import pandas as pd
import pyarrow.parquet as pq

#Datos para las funciones
# Directorio de entrada
# Directorio de entrada
directorio_entrada = Path("bases")

# Rutas completas de los archivos Parquet
ruta_archivo_parquet_f1 = directorio_entrada / "df_f1.parquet"
ruta_archivo_parquet_f2_f3 = directorio_entrada / "df_f2_f3.parquet"
ruta_archivo_parquet_f4_f5 = directorio_entrada / "df_f4_f5.parquet"
ruta_archivo_item_simi = 'bases/item_simi_df.parquet'

# Importar los DataFrames desde archivos Parquet
df_f1 = pd.read_parquet(ruta_archivo_parquet_f1)
df_f2_f3 = pd.read_parquet(ruta_archivo_parquet_f2_f3)
df_f4_f5 = pd.read_parquet(ruta_archivo_parquet_f4_f5)
df_item_simi = pq.read_table(ruta_archivo_item_simi).to_pandas()

def inicio():
    '''
    Página de inicio que muestra una presentación.

    Returns:
    str: Código HTML que muestra la página de inicio.
    '''
    return '''
    <html>
        <head>
            <title>EJECUCION LOCAL API STEAM SISTEMA DE RECOMENDACION ITEMS</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                p {
                    color: #666;
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>Bienvenido a la API Steam</h1>
            <p>Esta es la página de inicio de la API de Steam para consultas de videojuegos.</p>
            <p>INSTRUCCIONES:</p>
            <p>Escriba <span style="background-color: lightgray;">/docs</span> a continuación de la URL actual de esta página para interactuar con la API.</p>
            <p>Visita mi perfil en <a href="https://www.linkedin.com/in/ingambcarlapezzone/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin"></a></p>
            <p>El desarrollo de este proyecto está en <a href="https://github.com/IngCarlaPezzone/PI1_MLOps_videojuegos"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github"></a></p>
        </body>
    </html>
    '''


# Función PlayTimeGenre
def playtime_genre(genero: str):
    """
    Calcula las horas jugadas sumadas por año para un género específico.

    Parameters:
    - genero (str): Género de videojuegos.

    Returns:
    - dict: Año de lanzamiento con más horas jugadas para el género especificado.
    """

    filtered_df = df_f1[df_f1['genres'] == genero]

    # Agrupa por año y calcula las horas jugadas sumando
    grouped_df = filtered_df.groupby('year_release')['playtime_forever'].sum().reset_index()

    # Encuentra el año con más horas jugadas
    max_year = grouped_df.loc[grouped_df['playtime_forever'].idxmax()]['year_release']

    return {"Año de lanzamiento con más horas jugadas para {}: {}".format(genero, max_year)}

# Función UserForGenre
def user_for_genre(genero: str = Query(..., 
                                      description="Género de videojuegos", 
                                      example='Adventure')):
    """
    Encuentra al usuario con más horas jugadas para un género específico.

    Parameters:
    - genero (str): Género de videojuegos.

    Returns:
    - dict: Información sobre el usuario con más horas jugadas.
    """
    # Filtrar el DataFrame por el género específico
    df_genre = df_f2_f3[df_f2_f3['genres'] == genero]

    # Agrupar por usuario y año, sumar las horas jugadas
    grouped_df = df_genre.groupby(['user_id', 'year_release'])['playtime_forever'].sum().reset_index()

    # Encontrar al usuario con más horas jugadas
    max_user = grouped_df.loc[grouped_df['playtime_forever'].idxmax()]['user_id']

    # Filtrar el DataFrame original para obtener las horas jugadas por año del usuario máximo
    max_user_df = df_f2_f3[df_f2_f3['user_id'] == max_user]
    max_user_hours_by_year = max_user_df.groupby('year_release')['playtime_forever'].sum().reset_index()

    # Crear la lista de la acumulación de horas jugadas por año
    horas_jugadas_por_anio = [{"Año": int(anio), "Horas": int(horas)} for anio, horas in zip(max_user_hours_by_year['year_release'], max_user_hours_by_year['playtime_forever'])]

    # Crear el diccionario de retorno
    resultado = {"Usuario con más horas jugadas para Género " + genero: max_user, "Horas jugadas": horas_jugadas_por_anio}

    return resultado

# Función UsersRecommend
def users_recommend(year: int = Query(..., 
                                      description="Año de revisión", 
                                      example=2022)):
    """
    Encuentra los juegos más recomendados para un año específico.

    Parameters:
    - year (int): Año de revisión.

    Returns:
    - dict: Top 3 de juegos más recomendados.
    """
    # Filtrar por año
    df_filtered = df_f2_f3[df_f2_f3['year_review'] == year]

    # Filtrar por recomendaciones positivas/neutrales
    df_filtered = df_filtered[(df_filtered['recommend'] == True) & (df_filtered['Sentiment_Score'].isin([1, 2]))]

    # Obtener el top 3 de juegos más recomendados
    top_games = df_filtered.groupby('item_name')['recommend'].count().sort_values(ascending=False).head(3)

    # Crear el diccionario de resultados en el formato deseado
    top_games_dict = {f'Puesto {i+1}': juego for i, (juego, count) in enumerate(zip(top_games.index, top_games.values))}

    # Devolver el diccionario en el formato deseado
    return top_games_dict

# Función UsersWorstDeveloper
def users_worst_developer(year: int = Query(..., 
                                           description="Año de revisión", 
                                           example=2021)):
    """
    Encuentra las peores desarrolladoras según las recomendaciones y puntajes de sentimiento.

    Parameters:
    - year (int): Año de revisión.

    Returns:
    - list: Top 3 de peores desarrolladoras.
    """
    # Filtrar por el año deseado en la columna 'year_review'
    df_year = df_f4_f5[df_f4_f5['year_review'] == year]

    # Agrupar por desarrolladora y calcular las estadísticas
    grouped_stats = df_year.groupby('developer').agg({
        'recommend': lambda x: (x == False).sum(),
        'Sentiment_Score': lambda x: (x == 0).sum()
    }).reset_index()

    # Ordenar por la suma de juegos no recomendados en orden descendente
    sorted_stats = grouped_stats.sort_values(by=['recommend'], ascending=[False])

    # Seleccionar las top 3 desarrolladoras
    top3_developers = sorted_stats.head(3)

    # Crear el formato de retorno como un diccionario
    result = {f"Puesto {i}": developer for i, developer in enumerate(top3_developers['developer'], 1)}

    return result

# Función SentimentAnalysis
def sentiment_analysis(developer: str = Query(..., 
                                description="Desarrollador del videojuego", 
                                example='Valve')):
    """
    Realiza análisis de sentimiento para los videojuegos de un desarrollador específico.

    Parameters:
    - developer (str): Nombre del desarrollador del videojuego.

    Returns:
    - dict: Un diccionario con información de análisis de sentimiento.
    """
    # Filtrar el dataframe por la desarrolladora especificada
    developer_df = df_f4_f5[df_f4_f5['developer'] == developer]

    # Sumar los valores de Sentiment_Score para cada categoría
    negative_sum = developer_df[developer_df['Sentiment_Score'] == 0].shape[0]
    neutral_sum = developer_df[developer_df['Sentiment_Score'] == 1].shape[0]
    positive_sum = developer_df[developer_df['Sentiment_Score'] == 2].shape[0]

    # Crear el diccionario de salida
    result_dict = {
        developer: {
            'Negativo': negative_sum,
            'Neutral': neutral_sum,
            'Positivo': positive_sum
        }
    }

    return result_dict

# Funcion del modelo
def recomendacion_juego(nombre_juego: str = Query(..., 
                                                 description="Nombre del juego para el cual se desea obtener recomendaciones", 
                                                 example='Killing Floor')):
    """
    Retorna una lista con los nombres de los juegos recomendados basándose en la similitud del juego ingresado.

    Parameters:
    - nombre_juego (str): Nombre del juego para el cual se desea obtener recomendaciones.

    Returns:
    - list: Lista con los nombres de los juegos recomendados.
    """
    # Obtener la fila correspondiente al juego ingresado
    juego_row = df_item_simi.loc[nombre_juego]

    # Ordenar los índices de los juegos según la similitud (de mayor a menor)
    juegos_similares_indices = juego_row.argsort()[::-1]

    # Seleccionar los primeros 5 juegos más similares (excluyendo el propio juego)
    top_5_juegos = juegos_similares_indices[1:6]

    # Obtener nombres de los juegos recomendados
    juegos_recomendados = df_item_simi.index[top_5_juegos]

    return juegos_recomendados