from time import time
from random import choice
from acciones_funciones.validadores import validar_condicion_palabra
from configuraciones.datos_iniciales import obtener_color


"Esta funcion es la encargada de conectar las funcione para el correcto funcionamiento de la aplicacion"
"comparando para ver si dentro de la partida hubo un ganador , si los intentos fueron agotados o cambair de turno de participantes"
"Autor Juan pedro Basualdo"
   
def application(datos_iniciales,dicc_jugadores,textos):
    
    print("\x1b[33m","*"*50,"\x1b[0m")
    print("\x1b[33m","*"*10,textos["JUEGO_INICIALIZADO"],"*"*10,"\x1b[0m")
    
    contador_credito = datos_iniciales["contador_credito"]
    jugadores = list(datos_iniciales["jugadores"].keys())
    turno = datos_iniciales["turno"]
    
    print(datos_iniciales["palabra_secret"])
  
    while (not datos_iniciales["es_ganador"]) and (contador_credito<datos_iniciales["contador_credito_max"]):
        
        turno = choice([jugador for jugador in jugadores if jugador != turno]) if len(jugadores) >1 else  jugadores[0]
        
        print(f"\n\nTurno de ---> {turno}")
        
        ganador_parcial = False
        
        palabra = validar_condicion_palabra(textos)
        
        for player,data in dicc_jugadores.items():
            if player == turno:
                data[4] +=1


        if palabra==datos_iniciales["palabra_secret"]:
            datos_iniciales["es_ganador"]=True 
            ganador_parcial = turno
            datos_iniciales["tablero"][contador_credito] = [obtener_color( letra,"Verde" ) for letra in palabra]
            finaliza_juego = time()
        
        else:
            #Analizamos la plabra, coloreando las letras de acuerdo a lo especificado por el trabajo.
            lista_2=[]
            for i in range(len(palabra)):
                if palabra[i] in datos_iniciales["palabra_secret"][i]:
                    lista_2.append(obtener_color( palabra[i],"Verde" ))
                elif palabra[i] in datos_iniciales["palabra_secret"]:
                    lista_2.append( obtener_color( palabra[i],"Amarillo" ))
                else:
                    lista_2.append( obtener_color( palabra[i],"Rojo" )) 
    
        
            datos_iniciales["tablero"][contador_credito]=lista_2 
        
        if not datos_iniciales["es_ganador"]:
            contador_credito+=1
        
        if contador_credito>=datos_iniciales["contador_credito_max"]:
            finaliza_juego = time()
        
        for i in range(datos_iniciales["cantidad_letras"]): 
            print(" ".join(datos_iniciales["tablero"][i]))  

    return {
        "finaliza_juego": finaliza_juego,
        "contador_credito": contador_credito,
        "ganador_parcial": ganador_parcial,
        "turno": turno,
        "cambiar_turno": choice([jugador for jugador in jugadores if jugador != turno]) if len(jugadores) >1 else  jugadores[0]
    }

    
    
    

    