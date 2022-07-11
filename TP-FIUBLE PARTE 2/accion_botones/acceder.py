from acciones_funciones.validadores import sesion
from configuraciones.estilos_widgets import msg_warning,msg_info,msg_error
"La funcion acceder conecta los botones de entrada e inicio de sesion.En el caso de que se haya iniciado"
"anteriromente,informara que la sesion ya fue iniciada,una ve q alcanza la cantidad de usuarios ingresados,inicia app"
"Autor Juan Pedro Basualdo"
def acceder(argumentos):
    
    nombre_entry,clave_entry,jugadores,cant,inicia_app,root,textos = argumentos 
    nombre = nombre_entry.get()
    password = clave_entry.get()
  
    if sesion(nombre,password,textos):
        if nombre in jugadores:
            msg_warning(f'{nombre}{textos["MSJ_ADVERTENCIA_SESION_YA_INICIADA"]}',textos)
        else:
            jugadores.append(nombre)
            msg_info(textos["MSJ_INFORMACION_SESION"],textos)
            nombre_entry.delete(0,"end")
            clave_entry.delete(0,"end")
            
    else:
        msg_error(textos["MSJ_ERROR_USUARIO_CONTRASEÑA"],textos)

    if len(jugadores) == cant:
        root.destroy()
        inicia_app(jugadores,textos)

