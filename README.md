# PI1_MLO_Steam_Edupechav
Repositorio para entregar proyecto de Machine Learning Operations individual No.1 Para evalucion Soy Henry

## Introducción a Steam
Steam, de la empresa Valve Corporation, es la plataforma líder indiscutida en la distribución digital de videojuegos a nivel global. Cuenta con una base instalada de más de 325 millones de usuarios activos y un amplio catálogo de más de 25.000 títulos de diversos géneros.

## Objetivo del Proyecto
Ante la gran cantidad de datos e interacciones generadas diariamente por los usuarios en la plataforma, este proyecto planteó desarrollar un sistema de recomendación automatizado capaz de mejorar la experiencia del cliente y potenciar las ventas de juegos mediante sugerencias personalizadas según sus comportamientos, gustos y opiniones.

Así, en este trabajo se ejercita el papel un unMLOps Engineer (en otras palabras, aplicando habilidades dde Data Engeniier y Data Scientist) 

## Datos Utilizados
La data utilizada para el desarrollo provino de 3 archivos JSON proporcionados por SOy Henry: uno con las reseñas de los usuarios australianos sobre los diferentes juegos, otro con el historial detallado de consumo de juegos por cada usuario incluyendo horas de juego, y finalmente un archivo con información técnica (features, requerimientos, géneros, etc.) de todos los juegos disponibles en la plataforma de Steam. El detalle específico se puede encontrar en el [Dicionario de variables](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit#gid=0)


## Proceso de Desarrollo
Antes de aplicar técnicas avanzadas de machine learning y procesamiento de lenguaje natural se realizó una exhaustiva limpieza, transformación y normalización de los datos detallada en 3 notebooks de Jupyter dedicados a cada fuente de datos.

## ETL
A continuación se señalan las libretas donde se llevó a cabo la extracción, la transformación y la limpieza de los datos. En este proceso se buscó limpiar valores nulos, eliminar duplicados, establecer tipos de variables adecuadas, entre otros.

[1. EPC_ETL_1_steam_games.ipynb](1.%20EPC_ETL_1_steam_games.ipynb) Contiene la limepiza del archivo steam_games
[2. EPC_ETL_2_Users_review.ipynb](2.%20EPC_ETL_2_Users_review.ipynb) Contiene la limpieza del archivo que procesa las reviews, mismas que se encontraban anidadas y tuvieron que ser desagregadas
[3. EPC_ETL_3_User_items.ipynb](3.%20EPC_ETL_3_User_items.ipynb) Contiene informacion sobre los juegos, como por ejemplo el género, el desarrollador y el precio. También tuvo que ser desagregada.

## Análisis de sentimientos

Luego, utilizando la biblioteca TextBlob se añadió una categorización de sentimientos a cada reseña analizada identificándola como positiva, neutral o negativa, segun una escala que se proporcionó. Este analisis se encuentra en [4. EPC_FE_analisis_sentimientos.ipynb](4.%20EPC_FE_analisis_sentimientos.ipynb).

## EDA
Limpiados los datos se desarrollo el análisis exploratorio. EN él se obtuvo información valiosa sobre la distribución de los datos, sus tendencias, sus valores medios y atipicos y se enfrentó la dificultar de transformaciones específicas para lograr visualizaciones correctas. En este apartado también se construyó una escala que permitiera construir el modelo de ML en torno a la similitud de los juegos, utilizando para ello la combinación entre las escalas de analisis de sentimiento y si los usuarios recomendaron o no los juegos. El análisis se encuentra en [5. EPC_EDA.ipynb](5.%20EPC_EDA.ipynb)

## Modelo de ML
Posterior a ello se implementó un modelo de ML para basado en la similitud del coseno entre características de los ítems con el fin de recomendar juegos parecidos a algún título que se desee. La base para ello se preparó en [6. Preparacion base modelo.ipynb](6.%20Preparacion%20base%20modelo.ipynb). Mientras que la función para el modelo se puede consultar en [8. funcion item-similarity.ipynb](8.%20funcion%20item-similarity.ipynb). 

## Funciones para consulta
Como parte de este ejercicio, se han desarrollado cinco funciones dentro de la API FastAPI para realizar consultas específicas en el conjunto de datos de Steam. Cada función tiene un propósito único:

1. PlayTimeGenre:

Esta función acepta el género de un videojuego como entrada y devuelve el año de lanzamiento con la mayor cantidad de horas jugadas para ese género en particular.

3. UserForGenre:

Solicita el género de un videojuego como entrada y proporciona información sobre el usuario que ha acumulado la mayor cantidad de horas jugadas para ese género. Además, devuelve una lista que muestra la acumulación de horas jugadas por año para ese usuario.

4. UsersRecommend:

Para un año específico, esta función devuelve el top 3 de juegos más recomendados por los usuarios. Utiliza información de revisiones marcadas como recomendadas y comentarios positivos o neutrales.

5. UsersWorstDeveloper:

Similar a la función anterior, pero se centra en las desarrolladoras. Proporciona el top 3 de desarrolladoras con juegos menos recomendados por usuarios para un año dado, basándose en revisiones marcadas como no recomendadas y comentarios negativos.

6. sentiment_analysis:

Esta función toma como entrada el nombre de una empresa desarrolladora y realiza un análisis de sentimientos en las reseñas asociadas con esa empresa. Devuelve un diccionario que muestra la cantidad total de registros de reseñas categorizados como negativos, neutrales y positivos.
Estas funciones se han diseñado para ofrecer una variedad de consultas útiles sobre datos de juegos en Steam y proporcionar a los usuarios una comprensión detallada de aspectos como el tiempo de juego, las recomendaciones y el sentimiento asociado con las reseñas de los usuarios.

EL desarrollo de las funciones y la construcción de sus bases se encuentra en [7. Funciones y sus bases .ipynb](7.%20Funciones%20y%20sus%20bases%20.ipynb)

## Implementación y Despliegue

Finalmente, la funcionalidad de análisis de sentimientos y recomendaciones generada se expuso a través de una API implementada sobre el potente framework FastAPI de Python. Fue puesta a disposición en google cloud y puede ser consultada en el siguiente enlace (aunque la disponibilidad del mismo puede variar) . [Accede a la API aquí](http://34.133.172.102:10000/docs). Del mismo modo, puede ejecutarse en local utilizando uvicorn, para ello se proporcionan los archivos [main.py](main.py) y [functionsedu.py](functionsedu.py). Se recomienda intentar varias veces. Por cuestiones de robustés y limitaciones no siempre la ejecución funciona a la primera. EL video de su fucionamiento se puede apreciar [aquí] (https://youtu.be/ZuMUvXwCX-A)


## Conclusión
El proyecto funciona muy bien como demostración de valor, mostrando cómo explotar analíticamente los extensos datos generados por la comunidad Steam para mejorar la satisfacción de usuario y potenciar el volumen de negocio de la compañía. Como ejercicio permite apreciar las dificultades y la maravilla que es la ciencia de datos.

