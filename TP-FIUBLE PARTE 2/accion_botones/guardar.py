from configuraciones.estilos_widgets import msg_warning,msg_info,msg_confirm,msg_error
from acciones_funciones.validadores import contrasenia,usuario,nombre as nombres
from accion_botones.volver import volver
"la funcion se encarga de recibir mediante la entrada del usuario ,el nombre y la contraseña"
"Y en el caso de que falte alguna o se repita el nombre,lo informe"
"Autor Sebastian Olaran"
def guardar(argumentos):
  
  form_registro,cuadro_botones,nombre_entry,clave_entry,clave_entry_repeat,textos = argumentos
  nombre = nombre_entry.get()
  password = clave_entry.get()
  password_repeat = clave_entry_repeat.get()
  if nombre =="" and password =="":
    msg_warning(textos["MSJ_CONTRASEÑA_USUARIO_REQUERIDOS"],textos)
  elif nombre =="":
    msg_warning(textos["MSJ_NOMBRE_REQUERIDO"],textos)
  elif password =="":
    msg_warning(textos["MSJ_CONTRASEÑA_REQUERIDA"],textos)
  elif password !=password_repeat:
    msg_error(textos["MSJ_CONTRASEÑAS_NO_COINCIDEN"],textos)
  else:
    if nombres(nombre,textos) and contrasenia(password,textos):
      if usuario(nombre):
        msg_warning(textos["MSJ_USUARIO_YA_EXISTE"],textos)
      else:
        with open("archivos/jugadores.csv","a") as jugadores:
            jugadores.write(f"{nombre},{password}\n")
        
        msg_info(textos["MSJ_USUARIO_REGISTRADO_EXITO"],textos)
        res = msg_confirm(textos["MSJ_REGISTRAR_OTRO_USUARIO"],textos)
        if res:
          nombre_entry.delete(0,"end")
          clave_entry.delete(0,"end")
          clave_entry_repeat.delete(0,"end")
        else:
          volver([form_registro,cuadro_botones,textos])#

