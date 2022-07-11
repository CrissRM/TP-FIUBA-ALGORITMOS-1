from accion_botones.volver import volver
from accion_botones.guardar import guardar
from configuraciones.estilos_widgets import entrada_texto,entrada_clave,etiqueta,boton_volver,boton_guardar_registro,marco_visible,marco_invisible

"Autor Nahuel Cabrera"
def formulario_registro(root,cuadro_botones,textos):
    formulario_registro = marco_invisible(root)
  
  #-----------------------------------------------------------------------------
    data_nombre = marco_visible(formulario_registro)
  
    etiqueta(data_nombre,textos["LABEL_NOMBRE"])
    nombre_entry = entrada_texto(data_nombre)

  #-----------------------------------------------------------------------------
    data_clave = marco_visible(formulario_registro)
    etiqueta(data_clave,textos["LABEL_CONTRASEÑA"])
    clave_entry = entrada_clave(data_clave)
  #-----------------------------------------------------------------------------
    data_clave_repeat =marco_visible(formulario_registro)
    etiqueta(data_clave_repeat,textos["LABEL_REPETIR_CONTRASEÑA"])
    clave_entry_repeat = entrada_clave(data_clave_repeat)
  
  #-----------------------------------------------------------------------------
  
# --------------------------BOTONES OPCIONES--------------------------
    botones = marco_visible(formulario_registro)
    boton_volver(botones,volver,[formulario_registro,cuadro_botones,textos])
    boton_guardar_registro(botones,guardar,[formulario_registro,cuadro_botones,nombre_entry,clave_entry,clave_entry_repeat,textos])
  
  
    return formulario_registro