from random import choice
from configuraciones.formatear import formatear_linea,formatear_palabra
"Esta funcion se encarga principalmente de obtener las palabras validas e inclurilas en una lisa para luego de forma aleatoria elegir una"
"tambien,se encraga de retener los valores de uso primordial para el funcionamiento del juego y de escribir el archivo configuraciones de 0"
"Autor Cristian Roldan"
def iniciar_tablero(cantidad_letras):
  tablero=[]
  for i in range(cantidad_letras):
    tablero.append([ "?" for l in range(cantidad_letras)])
  return tablero

def obtener_color(letra,color):
  colores = {
  "Verde" : "\x1b[32m",
  "Amarillo" : "\x1b[33m",
  "GrisOscuro" : "\x1b[90m",
  "Defecto" : "\x1b[39m" ,
  "Rojo" : "\x1b[31m",
  "ENDC": "\x1b[0m"
  }
  return colores[color] + letra + colores["ENDC"]

def obtener_palabras_validas():
    lista_palabra_secreta = []
    try:
        with  open("archivos/palabras.csv") as archivo:
            palabra = archivo.readline().split(",")[0]

            while palabra !="":
                lista_palabra_secreta.append(formatear_palabra(palabra)) 
                palabra = archivo.readline().split(",")[0]
    except FileNotFoundError:
        lista_palabra_secreta.append(["Default,0,0,0"])


    

    return lista_palabra_secreta 

def condiciones_iniciales():
    with open("archivos/configuracion.csv") as archivo: 
        configuraciones = []
        linea = formatear_linea(archivo.readline())[1] 
        while linea !="":
            configuraciones.append(linea)
            linea = formatear_linea(archivo.readline())[1]
    

    LONGITUD_PALABRA_SECRETA,MAXIMO_PARTIDAS,REINICIAR_ARCHIVO_PARTIDAS,CREDITOS_MAX,CANTIDAD_MAX_JUGADORES = configuraciones
  
  
    return {
        "tablero": iniciar_tablero(int(LONGITUD_PALABRA_SECRETA)),
        "palabra_secret": choice(obtener_palabras_validas()),
        "es_ganador": False,
        "contador_credito": 0,
        "contador_credito_max": int(LONGITUD_PALABRA_SECRETA), 
        "puntos_acomulados_jugador": 0,
        "cantidad_jugadores": int(CANTIDAD_MAX_JUGADORES),
        "cantidad_letras": int(LONGITUD_PALABRA_SECRETA),
        "max_partidas": int(MAXIMO_PARTIDAS),
        "reiniciar_archivo_partidas": bool(REINICIAR_ARCHIVO_PARTIDAS),
        "max_long_letras": 12 
    }
