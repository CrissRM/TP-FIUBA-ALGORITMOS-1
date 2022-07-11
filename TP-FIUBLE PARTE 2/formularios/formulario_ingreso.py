from accion_botones.acceder import acceder
from accion_botones.volver import volver 
from configuraciones.estilos_widgets import *

"Autor Nahuel Cabrera"

def formulario_ingreso(root,botones,jugadores,cant,inicia_app,textos): 
  
  formulario_ingreso = marco_invisible(root) 
  #-----------------------------------------------------------------------------
  data_nombre = marco_visible(formulario_ingreso)
  
  etiqueta(data_nombre,textos["LABEL_NOMBRE"])
  nombre_entry = entrada_texto(data_nombre)
  
  #-----------------------------------------------------------------------------
  data_clave = marco_visible(formulario_ingreso)
  
  etiqueta(data_clave,textos["LABEL_CONTRASEÑA"])
  clave_entry = entrada_clave(data_clave)
  
  #-----------------------------------------------------------------------------
  botones = marco_visible(formulario_ingreso)
#   boton_volver(botones,volver,[formulario_ingreso,botones,textos])
  boton_acceder(botones,acceder,[nombre_entry,clave_entry,jugadores,cant,inicia_app,root,textos])
  #----------------------------------------------------------------------------
  
  return formulario_ingreso
  