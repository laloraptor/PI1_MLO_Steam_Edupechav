# lriberias a importar
import importlib
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, HTMLResponse
import functionsedu as fe
importlib.reload(fe)

# instanciar aplicacion
app = FastAPI()

# Funciones de la api

@app.get(path="/", 
         response_class=HTMLResponse,
         tags=["Home"])
def home():
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
            <h1>Apasionado de los videojuegos y los datos</h1>
            <h1>Eres bienvenido a esta API de Steam</h1>
            <p>MI nombre es Eduardo Pérez Chavarría</p>
            <p>e hice esto como un proyecto para Soy Henry</p>
            <p>Adéntrate en el maravilloso mundo de la ciencia de datos</p>
            <p>INSTRUCCIONES:</p>
            <p>Escribe <span style="background-color: lightgray;">/docs</span> al final de la URL de esta página para interactuar con la API.</p>
            
            <p>Visita mi perfil en <a href="https://www.linkedin.com/in/eduardo-p%C3%A9rez-chavarr%C3%ADa-0962b1140/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin"></a></p>
            <p>Te invito a visitar mi perfil de Github <a href="https://github.com/laloraptor"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github"></a></p>
            <p style="color: #ff7e00; font-size: 20px; font-weight: bold; margin-top: 40px;">Estas son las consultas que podrás realizar al interactuar con la API</p>
<ul>
    <li><strong>Obtener el año con más horas jugadas para un género</strong></li>
    <li><strong>Obtener al usuario con más horas jugadas por género</strong></li>
    <li><strong>Obtener el top 3 de juegos más recomendados por año</strong></li>
    <li><strong>Obtener el top 3 de desarrolladoras menos recomendadas por año</strong></li>
    <li><strong>Obtener la cantidad de valoraciones negativas, neutrales y positivas por desarrolladora</strong></li>
    <li><strong>Modelo de Aprendizaje Automático: Recomendación de juegos</strong></li>
</ul>
<a href="http://34.133.172.102:10000/docs" target="_blank">Las consultas por internet pueden realizarse aquí</a>
<a href="http://127.0.0.1:10000/docs" target="_blank">Las consultas de la impplementación local pueden realizarse aquí</a>/
        </body>
    </html>
    '''

@app.get('/playtime_genre',
         description=""" <font color="blue">
                    1. Haga click en "Quiero probar".<br>
                    2. Ingrese el género del juego en la caja que se encuentra abajo.<br>
                    3. Muevase hacia abajo para para ver el año con más horas jugadas para ese género y la acumulación de horas por año.
                    </font>
                    """,
         tags=["Consultas Generales"])
def playtime_genre(genero: str = Query(..., 
                            description="Género del videojuego", 
                            example='Action')):
    return fe.playtime_genre(genero)

@app.get('/user_for_genre',
         description=""" <font color="blue">
                    1. Haga click en "Quiero probar".<br>
                    2. Ingrese el género en la caja que se encuentra abajo.<br>
                    3. Muevase hacia abajo para para ver el usuario con más horas jugadas para ese género y sus horas jugadas por año.
                    </font>
                    """,
         tags=["Consultas Generales"])
def user_for_genre(genero: str = Query(..., 
                            description="Género del videojuego", 
                            example='Action')):
    return fe.user_for_genre(genero)

@app.get('/users_recommend',
         description=""" <font color="blue">
                    1. Haga click en "Quiero probar".<br>
                    2. Ingrese el año en en la caja que se encuentra abajo.<br>
                    3. Muevase hacia abajo para ver los juegos más recomendados por los usuarios en ese año.
                    </font>
                    """,
         tags=["Consultas Generales"])
def get_users_recommend(year: int = Query(..., 
                                description="Año para filtrar las recomendaciones", 
                                example=2013)):
    resultado = fe.users_recommend(year)
    return resultado

@app.get('/worst_developer',
         description=""" <font color="blue">
                    1. Haga click en "Quiero probar".<br>
                    2. Ingrese el año en en la caja que se encuentra abajo.<br>
                    3. Muevase hacia abajo ver las desarrolladoras menos recomendadas por los usuarios en ese año.
                    </font>
                    """,
         tags=["Consultas Generales"])
def users_worst_developer(year: int = Query(...,
                                description="Año para filtrar las desarrolladoras", 
                                example=2010)):
    return fe.users_worst_developer(year)

@app.get('/sentiment_analysis',
         description=""" <font color="blue">
                    INSTRUCCIONES<br>
                    1. Haga click en "Quiero probar".<br>
                    2. Ingrese el desarrollador en la caja que se encuentra abajo.<br>
                    3. Muevase hacia abajo para ver el análisis de sentimientos de las reseñas para ese desarrollador.
                    </font>
                    """,
         tags=["Consultas Generales"])
def sentiment_analysis(developer: str = Query(..., 
                                description="Desarrollador del videojuego", 
                                example='valve')):
    return fe.sentiment_analysis(developer)

@app.get('/recomendacion_juego',
         description=""" <font color="blue">
                    INSTRUCCIONES<br>
                    1. Haga click en "Quiero probar".<br>
                    2. Ingrese el juego en la caja que se encuentra abajo.<br>
                    3. Muevase hacia abajo para obtener 5 recomendaciones de juegos similares.
                    </font>
                    """,       
         tags=["Modelo de recomendación"])
def recomendacion_juego(nombre_juego: str = Query(..., 
                                    description="Nombre del juego para el cual se desea obtener recomendaciones", 
                                    example='Killing Floor')):
    resultado = fe.recomendacion_juego(nombre_juego)
    juegos_recomendados = resultado.tolist()
    return JSONResponse(content={"juegos_recomendados": juegos_recomendados})
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)