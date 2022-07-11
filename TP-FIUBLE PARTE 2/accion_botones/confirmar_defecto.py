from configuraciones.datos_iniciales import condiciones_iniciales
from acciones_funciones.validadores import texto
from acciones_funciones.diccionario_de_palabras import diccionario_de_palabras
from formularios.formulario_ingreso import formulario_ingreso
from app.app_consola import inicia_app
from configuraciones.estilos_widgets import msg_warning
# cuando apretamos  boton ingresar 
"La funcion se encarga de validar  cantidad de jugadores, y verificar que este cargado "
"Dentro de los parametros permitidos para el uso del juego en defecto maximo 2"
"Autor Omar jaldin"
def confirmar(lista):

    players_entry,entrada_jugadores,root,botones,textos = lista
    MAX_JUGADORES = condiciones_iniciales()["cantidad_jugadores"]# 2
    # pide por consola ingreso de jugadores
    cantidad = texto(players_entry.get(),textos)# false o numero

    if cantidad and (cantidad <= MAX_JUGADORES):#deja jugar si es 1 o 2 jugadores me muestra mensaje 
        entrada_jugadores.pack_forget()
        jugadores = []
        # carga las palabras
        diccionario_de_palabras()
        # muestra formulario de ingreso
        formulario_ingreso(root,botones,jugadores,cantidad,inicia_app,textos).pack() 
    else:
        msg_warning(f'{textos["MSJ_MAXIMO_JUGADORES"]} {MAX_JUGADORES}',textos)
        # si pongo 5000 jugadores me muestra mensaje  
        # muestra mensaje maximo 2 jugadores por defecto
