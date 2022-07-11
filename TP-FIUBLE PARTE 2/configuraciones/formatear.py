import math
"Esta funcion recauda todas las funciones que se encargan de formatear los datos para que en la aplicacion sean leidos de forma correcta"
"Autor Sebatian Olaran"
def formatear_linea(linea):
    return linea.strip("\n").split(",") if linea !="" else [""]*2

def formatear_palabra(palabra):
    letras = {
    "Á": "A",
    "É": "E",
    "Í": "I",
    "Ó": "O",
    "Ú": "U"
    }

    lista = [x for x in palabra]
    for i in range(len(lista)):
        if lista[i] in list(letras.keys()):
            lista[i] = letras[lista[i]]
    return "".join(lista)

def formatear_tiempo(ronda_terminada): 
  """ 
  """
  inicia_juego = ronda_terminada["inicia_juego"]
  finaliza_juego = ronda_terminada["finaliza_juego"]
  time = math.floor(finaliza_juego-inicia_juego)
  horas=math.floor(time/3600)
  minutos= math.floor((time-horas*3600)/60)
  segundos= math.floor((((time-horas*3600)/60)-minutos)*60)

  return f"{horas} horas {minutos} minutos {segundos} segundos" if horas != 0 else f"{minutos} minutos {segundos} segundos"

def formatear_configuracion_archivo(c_letras,cmax_partidas,reiniciar):
    lista_1=["LONGITUD_PALABRA_SECRETA","MAXIMO_PARTIDAS","REINICIAR_ARCHIVO_PARTIDAS"
    ,"CREDITOS_MAX","CANTIDAD_MAX_JUGADORES"]
    
    lista_2=[c_letras,cmax_partidas,reiniciar,"5","2"]
    archivo_config=open("archivos/configuracion.csv","w")
    for i in range (0,5) :
        archivo_config.write(str(lista_1[i])+","+str(lista_2[i])+"\n")
    archivo_config.close()  

