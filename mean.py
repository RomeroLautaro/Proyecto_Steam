from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import funcion_api as af

app = FastAPI()

# Funciones
@app.get(path="/", 
         response_class=HTMLResponse,
         tags=["Home"])
def home():
    '''
    Página de inicio que muestra una presentación.

    Returns:
    HTMLResponse: Respuesta HTML que muestra la presentación.
    '''
    return af.presentacion()

@app.get(path = '/userdata',
          description = """ <font color="blue">
                        INSTRUCCIONES<br>
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el user_id en el box abajo.<br>
                        3. Scrollear a "Resposes" para ver la cantidad de dinero gastado por el usuario, el porcentaje de recomendación que realiza el usuario y cantidad de items que tiene el mismo.
                        </font>
                        """,
         tags=["Consultas Generales"])
def userdata(user_id: str = Query(..., 
                                description="Identificador único del usuario", 
                                examples="EchoXSilence")):
        
    return af.userdata(user_id)
    

@app.get(path = '/userforgenre',
          description = """ <font color="blue">
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el género en el box abajo.<br>
                        3. Scrollear a "Resposes" para ver Top 5 de usuarios con más horas de juego en el género dado, con su URL y user_id.
                        </font>
                        """,
         tags=["Consultas Generales"])
def userforgenre(genero: str = Query(..., 
                            description="Género del videojuego", 
                            examples='Simulation')):
    return af.userforgenre(genero)

@app.get(path = '/developer',
          description = """ <font color="blue">
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el nombre del desarrollador en el box abajo.<br>
                        3. Scrollear a "Resposes" para ver la cantidad de items y porcentaje de contenido Free por año de ese desarrollador.
                        </font>
                        """,
         tags=["Consultas Generales"])
def developer(desarrollador: str = Query(..., 
                            description="Desarrollador del videojuego", 
                            examples='Valve')):
    return af.developer(desarrollador)



@app.get('/recomendacion_juego',
         description=""" <font color="blue">
                    INSTRUCCIONES<br>
                    1. Haga clik en "Try it out".<br>
                    2. Ingrese el nombre de un juego en box abajo.<br>
                    3. Scrollear a "Resposes" para ver los juegos recomendados.
                    </font>
                    """,
         tags=["Recomendación"])
def recomendacion_juego(game: str = Query(..., 
                                         description="Juego a partir del cuál se hace la recomendación de otros juego", 
                                         examples="Killing Floor")):
    return af.recomendacion_juego(game)


@app.get('/recomendacion_usuario',
         description=""" <font color="blue">
                    INSTRUCCIONES<br>
                    1. Haga clik en "Try it out".<br>
                    2. Ingrese el id del usuario en box abajo.<br>
                    3. Scrollear a "Resposes" para ver los juegos recomendados para ese usuario.
                    </font>
                    """,
         tags=["Recomendación"])
def recomendacion_usuario(user: str = Query(..., 
                                         description="Usuario a partir del cuál se hace la recomendación de los juego", 
                                         examples="76561197970982479")):
    return af.recomendacion_usuario(user) 

