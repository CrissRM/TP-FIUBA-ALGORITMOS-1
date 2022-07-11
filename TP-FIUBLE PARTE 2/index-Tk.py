import os
from pathlib import Path
from accion_botones.registrar import registrarse
from accion_botones.ingresar import ingresar
from configuraciones.estilos_widgets import *
from formularios.formulario_registro import formulario_registro
from formularios.formulario_configuracion_personalizada import formulario_configuracion_personalizada as personalizado
from formularios.formulario_configuracion_defecto import formulario_configuracion_defecto as defecto
from configuraciones.textos import texto

"Autor Cristian Roldan"

def interfaz_grafica():
    textos = texto("es")
    
    with open("archivos/configuracion.csv","w+") as archivo: 
            archivo.write("LONGITUD_PALABRA_SECRETA,7\n")
            archivo.write("MAXIMO_PARTIDAS,5\n")
            archivo.write("REINICIAR_ARCHIVO_PARTIDAS,False\n")
            archivo.write("CREDITOS_MAX,5\n")
            archivo.write("CANTIDAD_MAX_JUGADORES,2\n")
            
    root = interfaz()
    
    lista_textos = []
    for archivos in  os.scandir("archivos/textos"):
        archivo = Path(archivos.name)
        if archivo.suffix == ".csv" or archivo.suffix == ".txt":
            lista_textos.append(archivos.name)
    
    if len(lista_textos) == 0: 
        msg_error(textos["MSJ_ERROR_SIN_ARCHIVO"],textos)
        msg_info(textos["MSJ_CERRAR_PROGRAMA"],textos)
        root.destroy()
    else:
        titulo_aplicacion(root)

        botones = marco_visible(root)
        boton_registar(botones,registrarse,[formulario_registro,root,botones,textos]) 
        boton_ingresar(botones,ingresar,[botones,defecto(root,botones,textos),personalizado(root,botones,textos),textos])

    root.mainloop()

interfaz_grafica()