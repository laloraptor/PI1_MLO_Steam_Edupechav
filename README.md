# PI1_MLO_Steam_Edupechav
<image src="https://blog.soyhenry.com/content/images/2021/02/HEADER-BLOG-NEGRO-01.jpg" alt="henry">
Repositorio para entregar proyecto de Machine Learning Operations individual No.1 Para evaluacion Soy Henry.

## Introducción a Steam
<image src="https://mmos.com/wp-content/uploads/2021/07/steam-logo-welcome-banner.jpg" alt="steam">

[Steam](https://store.steampowered.com/), de la empresa Valve Corporation, es la plataforma líder indiscutida en la distribución digital de videojuegos a nivel global. Cuenta con una base instalada de más de 325 millones de usuarios activos y un amplio catálogo de más de 25.000 títulos de diversos géneros.

## Objetivo del Proyecto
Ante la gran cantidad de datos e interacciones generadas diariamente por los usuarios en la plataforma, este proyecto planteó desarrollar un sistema de recomendación automatizado capaz de mejorar la experiencia del cliente y potenciar las ventas de juegos mediante sugerencias personalizadas según sus comportamientos, gustos y opiniones.

Específicamente, el proyecto busca aplicar técnicas de ciencia de datos sobre los extensos datos de la comunidad Steam para extraer insights de valor. El objetivo principal es preparar y exponer estos datos y análisis a través de una API, poniendo a disposición funcionalidades útiles para otros equipos técnicos. Entre estas funcionalidades se incluye un modelo de recomendación basado en calcular la similitud entre items.


## Rol del Desarrollador
<image src="https://www.kdnuggets.com/wp-content/uploads/c_role_mlops_engineer_organization_1.png" alt="mlops">

En este trabajo se ejercita el papel un un MLOps Engineer, combinando habilidades de Data Engineer y Data Scientist. Esto incluye tareas como la recolección y limpieza de datos, análisis exploratorio, desarrollo de modelos, implementación de API, despliegue a producción y monitorización; con el fin de preparar y exponer los datos de la mejor forma posible para su posterior explotación.

## Fuentes de Datos

La data utilizada para el desarrollo provino de 3 archivos JSON proporcionados por SOy Henry:

- Uno con las **reseñas** de los **usuarios australianos** sobre los diferentes juegos.
- Otro con el **historial detallado de consumo de juegos** por cada usuario incluyendo **horas de juego**.  
- Finalmente un archivo con **información técnica** (features, requerimientos, géneros, etc.) de **todos los juegos disponibles** en la plataforma de Steam.  

Se puede encontrar el detalle específico en el [Dicionario de variables](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit#gid=0).


## Proceso de Desarrollo

Antes de aplicar técnicas avanzadas de machine learning y procesamiento de lenguaje natural se realizó una exhaustiva limpieza, transformación y normalización de los datos detallada en 3 notebooks de Jupyter dedicados a cada fuente de datos.

## ETL
A continuación se señalan las libretas donde se llevó a cabo la extracción, la transformación y la limpieza de los datos. En este proceso se buscó limpiar valores nulos, eliminar duplicados, establecer tipos de variables adecuadas, entre otros.

[1. EPC_ETL_1_steam_games.ipynb](1.%20EPC_ETL_1_steam_games.ipynb) Contiene la limpieza del archivo steam_games  
[2. EPC_ETL_2_Users_review.ipynb](2.%20EPC_ETL_2_Users_review.ipynb) Contiene la limpieza del archivo que procesa las reviews, mismas que se encontraban anidadas y tuvieron que ser desagregadas  
[3. EPC_ETL_3_User_items.ipynb](3.%20EPC_ETL_3_User_items.ipynb) Contiene informacion sobre los juegos, como por ejemplo el género, el desarrollador y el precio. También tuvo que ser desagregada.

## Análisis de sentimientos

Luego, utilizando la biblioteca TextBlob se añadió una categorización de sentimientos a cada reseña analizada identificándola como positiva, neutral o negativa, según una escala que se proporcionó. Este análisis se encuentra en [4. EPC_FE_analisis_sentimientos.ipynb](4.%20EPC_FE_analisis_sentimientos.ipynb).

## EDA
Limpiados los datos se desarrollo el análisis exploratorio. En él se obtuvo información valiosa sobre la distribución de los datos, sus tendencias, sus valores medios y atípicos. También se construyó una escala que permitiera modelar la similitud entre juegos, utilizando la combinación de escalas de análisis de sentimiento y si los usuarios recomendaron o no los juegos. El análisis se encuentra en [5. EPC_EDA.ipynb](5.%20EPC_EDA.ipynb)

## Modelo de ML
Posterior a ello se implementó un modelo de ML para recomendar juegos parecidos basado en la similitud del coseno, donde ésta se estimó a partir de la escala señalada justo arriba. La base para ello se preparó en [6. Preparacion base modelo.ipynb](6.%20Preparacion%20base%20modelo.ipynb). Mientras que la función para el modelo se puede consultar en [8. funcion item-similarity.ipynb](8.%20funcion%20item-similarity.ipynb).

## Funciones para consulta
Como parte de este ejercicio, se han desarrollado cinco funciones dentro de la API FastAPI para realizar consultas específicas en el conjunto de datos de Steam. 

1. PlayTimeGenre:  

Acepta el género de un videojuego y devuelve el año de lanzamiento con la mayor cantidad de horas jugadas.

2. UserForGenre:  

Proporciona información del usuario con más horas por género y horas jugadas por año.

3. UsersRecommend:   

Devuelve el top 3 de juegos más recomendados por usuarios para un año dado.   

4. UsersWorstDeveloper:

Proporciona el top 3 de desarrolladores menos recomendados por usuarios en un año.

5. sentiment_analysis:  

Análisis de sentimientos en reseñas por desarrollador.  

Estas funciones buscan exponer insights específicos sobre los datos que puedan ser de utilidad para otros equipos.

EL desarrollo de las funciones y la construcción de sus bases se encuentra en [7. Funciones y sus bases .ipynb](7.%20Funciones%20y%20sus%20bases%20.ipynb)

## Implementación y Despliegue

La API fue implementada con FastAPI y desplegada en Google Cloud. Puede ser consultada [aquí](http://34.133.172.102:10000/) aunque la disponibilidad puede variar. También se proporcionan los archivos [main.py](main.py) y [functionsedu.py](functionsedu.py) para ejecutarse localmente con uvicorn.  

Dado que se trata de una demostración inicial, la API puede presentar intermitencias por lo que se recomienda reintentar la ejecución. El video de funcionamiento está [aquí](https://youtu.be/EunBt0w5xjQ). 


## Conclusión  

El proyecto funciona muy bien como demostración de valor, mostrando cómo explotar analíticamente los extensos datos de Steam para mejorar la satisfacción del usuario y potenciar el volumen de negocio. Como ejercicio permite apreciar las complejidades y los beneficios de aplicar ciencia de datos en un caso real.