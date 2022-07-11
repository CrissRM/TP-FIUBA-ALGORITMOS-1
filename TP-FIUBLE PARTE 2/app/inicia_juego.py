import os
from time import time
from random import choice
from configuraciones.datos_iniciales import condiciones_iniciales
from app.app import application
from datetime import datetime
from acciones_funciones.contabilizar_puntos import contabilizar_puntos
""" en esta funcion guarda los datos de los jugadores dependiendo de cuantos sean con un maximo de 5 fichas por intento
   guardando en un diccionario 
   -jugador 
   -puntos
   -fecha 
   -hora
   -aciertos 
   -intentos 
   """
"Autor Omar jaldin"

def inicia_juego(jugadores,textos):
  os.system("clear")
  os.system("cls")
  turno = choice(jugadores)  
  datos_jugadores = dict()#acumulador de jugadores
  for jugador in jugadores:
    puntos_iniciales = condiciones_iniciales()["puntos_acomulados_jugador"]
    fecha = datetime.today().strftime("%d-%m-%Y")
    hora_finalizacion = ""
    aciertos = 0
    intentos = 0
    # guarada los {jugador: puntos , fecha , fin_de_juego , aciertos ,intentos }
    datos_jugadores.setdefault(jugador,[puntos_iniciales,fecha,hora_finalizacion,aciertos,intentos])
  numero_partida = 0
                            # maximo es de 5 fichas 
  while numero_partida<condiciones_iniciales()["max_partidas"]:
    numero_partida +=1
    inicia_juego = time()  
    turno = choice ([jugador for jugador in jugadores if jugador != turno]) if len(jugadores) >1 else jugadores[0]   
    datos_iniciales = condiciones_iniciales() 
    datos_iniciales["jugadores"] = datos_jugadores
    datos_iniciales["turno"] = turno
    ronda_terminada = application(datos_iniciales,datos_jugadores,textos)  
    ronda_terminada["inicia_juego"] = inicia_juego  
    ganador_parcial = ronda_terminada["ganador_parcial"]
    turno_jugador = ronda_terminada["turno"]
    creditos = ronda_terminada["contador_credito"]
    max_opotunidades = datos_iniciales["contador_credito_max"]
    dicc_jugadores = contabilizar_puntos(creditos,ganador_parcial,turno_jugador,datos_jugadores,ronda_terminada,textos,max_opotunidades) 
    os.system("clear")
    os.system("cls") 
  
  return dicc_jugadores