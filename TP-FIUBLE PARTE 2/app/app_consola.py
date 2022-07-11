from datetime import datetime
from app.inicia_juego import inicia_juego
from configuraciones.formatear import formatear_configuracion_archivo
"Esta funcion se encarga de una vez finalizada la partida,mostrarnos los resultados,con sus respectivos valores"
"y grabarlo en partidas para utilziarlo de estadistica luego"
"Autor Juan Pedro Basualdo"
def inicia_app(jugadores,textos):  

    estadisticas_finales_jugadores = inicia_juego(jugadores,textos)
    
    print("\n\n","*"*75)
    print("*"*30,textos["JUEGO_FINALIZADO"],"*"*30,"\n")
  
    lista_puntucaciones = list(estadisticas_finales_jugadores.values())
    lista_puntucaciones.sort(reverse=True)
  
    for jugador,data in estadisticas_finales_jugadores.items():
        hora_finalizacion = datetime.today().strftime("%H:%M:%S")
        estadisticas_finales_jugadores[jugador][2] =hora_finalizacion
        if data[0] == lista_puntucaciones[0][0]:
            print(f"{textos['TEXTO_GANADOR']}: {jugador} ----> {textos['TEXTO_OBTUVO']}: {data[0]}")
  
    print("\n","*"*75)
    input(f"\n\n{textos['TEXTO_FINALIZAR']}")
  
    archivo = open("archivos/partidas.csv","a+")
    for jugador,data in estadisticas_finales_jugadores.items():
        archivo.write(f"{data[1]},{data[2]},{jugador},{data[3]},{data[4]},{data[0]}\n")
    
    archivo.close() 
    
    formatear_configuracion_archivo(7,5,False)
    

    

  