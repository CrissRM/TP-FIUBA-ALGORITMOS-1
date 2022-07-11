from accion_botones.volver import volver
from accion_botones.confirmar_personalizada import confirmar
from configuraciones.estilos_widgets import *

"Autor Omar jaldin"
    
def formulario_configuracion_personalizada(root,botones,textos):
    configuraciones = marco_invisible(root) 

    #---CANT JUGADORES
    cantidad_jugadores = marco_visible(configuraciones)
    etiqueta(cantidad_jugadores,textos["LABEL_JUGADORES"])
    players_entry = entrada_texto(cantidad_jugadores)

    #--LONG PALABRA
    longitud_palabra = marco_visible(configuraciones)

    etiqueta(longitud_palabra,textos["LABEL_LETRAS"])
    letras_entry = entrada_texto(longitud_palabra)

    #--- CANT PARTIDAS
    cantidad_partidas = marco_visible(configuraciones)
    etiqueta(cantidad_partidas,textos["LABEL_PARTIDAS"])
    partidas_entry = entrada_texto(cantidad_partidas)
    #-----------------------------------------------------------------------------
    frame_botones = marco_visible(configuraciones)
    # entrada de cantidad de jugadores 
    boton_confirmar_personalizada(frame_botones,confirmar,[players_entry,configuraciones,root,botones,letras_entry,partidas_entry,textos]) 
    # vueve al inicio 
    boton_volver(frame_botones,volver,[configuraciones,botones,textos])

    return configuraciones