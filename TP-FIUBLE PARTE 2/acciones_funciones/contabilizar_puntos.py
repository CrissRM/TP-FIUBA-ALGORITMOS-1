from acciones_funciones.msg_puntos_parciales import msg_puntos_parciales

def contabilizar_puntos(contador_credito,ganador_parcial,turno,dicc_jugadores,ronda_terminada,textos,max_oportunidad): 
    """
    La funcion se encarga de analizar el resultado del juego,y asignar sus valores,dependiendo
  del resultad y devolver los puntos acumulados en la jugada.
  La funcion recibira un numero entero en puntos,luego el nombre del jugador ganador o False en caso de 
  que no exista un ganador,el nombre del jugador del turno ,y un diccionario que tendra como clave el nombre
  del jugador y como valor los puntos del mismo.
  Nos devuelve un diccionario con el nombre de los jugadores y los puntos finales

  >>> contabilizar_puntos(10,False,"Juan",{"Juan":30,"Alan":20})
  {'Juan': 40, 'Alan': 80}
  
  correspondientes puntos del jugador 1 y 2,respectivamente
  Autor Omar jaldin

  """
    if contador_credito == max_oportunidad:
        puntos = (-10)*max_oportunidad*2
    else:
        puntos = ( max_oportunidad-contador_credito)*10
    
    if not ganador_parcial:
        
        for key in dicc_jugadores:
            if key == turno:
                dicc_jugadores[key][0] += puntos 
            else:
                dicc_jugadores[key][0] += puntos+(-10)*max_oportunidad*2
    
    else:
        
        for key in dicc_jugadores:
            if key == turno:
                dicc_jugadores[key][0] += puntos
            else:
                dicc_jugadores[key][0] += -puntos
    
    msg_puntos_parciales(puntos,ronda_terminada,dicc_jugadores,textos)

    
    return dicc_jugadores
