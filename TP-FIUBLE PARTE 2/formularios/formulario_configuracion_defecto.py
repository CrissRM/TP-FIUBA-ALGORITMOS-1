from accion_botones.confirmar_defecto import confirmar
from accion_botones.volver import volver 
from configuraciones.estilos_widgets import *

"Autor Juan Pedro Basualdo"

def formulario_configuracion_defecto(root,botones,textos):
    
    entrada_jugadores = marco_invisible(root)
    #------------------------------------------------------------------------------
    jugadores = marco_visible(entrada_jugadores)
    etiqueta(jugadores,textos["LABEL_JUGADORES"])
    players_entry = entrada_texto(jugadores)
    #-----------------------------------------------------------------------------
    marco_botones = marco_visible(entrada_jugadores)
    boton_confirmar_defecto(marco_botones,confirmar,[players_entry,entrada_jugadores,root,botones,textos]) 

    boton_volver(marco_botones,volver,[entrada_jugadores,botones,textos])
  
    return entrada_jugadores
