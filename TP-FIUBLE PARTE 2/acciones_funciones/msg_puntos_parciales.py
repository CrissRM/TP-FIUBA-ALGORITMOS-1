from configuraciones.formatear import formatear_tiempo

"Recibe por parametro diccionario con los jugadores y sus respectivos puntos como valores,los puntos"
"que se obtuvieron en la ronda y cuando la ronda finaliza en forma de su respectivo tiempo que "
"conllevo la ronda"
"Mostrara por pantalla los datos obtenidos de la ronda,y luego mostrar los puntos finales de cada jugada"
"autor sebastian olaran"
   
def msg_puntos_parciales(puntos,ronda_terminada,dicc_jugadores,textos):

  if not ronda_terminada["ganador_parcial"]:
    mensaje_para_usurio(dicc_jugadores,puntos,ronda_terminada,textos)
  else:
    mensaje_para_usurio(dicc_jugadores,puntos,ronda_terminada,textos)

def sumar_acierto(ronda_terminada,dicc_jugadores):
  jugador_acerto = ronda_terminada["ganador_parcial"]
  for jugador,data in dicc_jugadores.items():
    if jugador == jugador_acerto:
      data[3] +=1

def mensaje_if_red(jugador,puntos_ronda,puntos):
  print("\n"," "*20,f"{jugador:15} | {puntos_ronda:6} | \x1b[31m{puntos:9}\x1b[0m |")

def mensaje_if_green(jugador,puntos_ronda,puntos):
  print("\n"," "*20,f"{jugador:15} | {puntos_ronda:6} | \x1b[32m{puntos:9}\x1b[0m |")

def mensaje_for(dicc_jugadores,puntos_ronda,ronda_terminada):
  
  for jugador,data in dicc_jugadores.items():

      puntos = data[0]
      if puntos<0:
        if ronda_terminada["ganador_parcial"] == jugador:
          mensaje_if_red(jugador,puntos_ronda,puntos)
        else:
          mensaje_if_red(jugador,-puntos_ronda,puntos)
      else:
        if ronda_terminada["ganador_parcial"] == jugador:
          mensaje_if_green(jugador,puntos_ronda,puntos)
        else:
          mensaje_if_green(jugador,-puntos_ronda,puntos)

def mensaje_para_usurio(dicc_jugadores,puntos_ronda,ronda_terminada,textos):
  print("\n\x1b[33m","*"*33,{textos["CABECERA_PUNTAJES"]},"*"*33,"\x1b[0m")
  print("\n\x1b[33m"," "*20,f'{textos["COL_JUGADOR"]:15} | {textos["COL_PUNTOS"]:6} | {textos["COL_ACOMULADO"]:9} |\x1b[0m')
  
  if ronda_terminada["ganador_parcial"]:
    sumar_acierto(ronda_terminada,dicc_jugadores)
    mensaje_for(dicc_jugadores,puntos_ronda,ronda_terminada)
    print(f"\n          {textos['TIEMPO_ADIVINA_PALABRA']} {formatear_tiempo(ronda_terminada)}") 

  else:
    mensaje_for(dicc_jugadores,puntos_ronda,ronda_terminada)
  input(f"\n {textos['INPUT_CONTINUAR']}")

    
