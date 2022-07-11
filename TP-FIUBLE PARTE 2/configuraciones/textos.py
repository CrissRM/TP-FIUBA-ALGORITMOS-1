def texto(idioma):
    if idioma == "es":
    
        diccionario_mensajes = {
        "TIEMPO_ADIVINA_PALABRA": "Tiempo en adividinar la palabra: ",
        
        "CABECERA_PUNTAJES": "PUNTAJES",
        
        "COL_JUGADOR": "JUGADOR",
        
        "COL_PUNTOS": "PUNTOS",
        
        "COL_ACOMULADO": "ACOMULADO",
        
        "MSJ_ERROR_NOMBRE": "El nombre solo acepta caracteres alfabéticos, numéricos y el guión bajo",
        
        "MSJ_ERROR_RANGO_NOMBRE": "El nombre debe no puede tener menos de 4 o más de 15 caracteres",

        "MSJ_ERROR_CONTRASEÑA_MAYUSCULAS": "La contraseña debe contener por lo menos una letra mayúsculas",

        "MSJ_ERROR_CONTRASEÑA_MINUSCULAS": "La contraseña debe contener por lo menos una letra minúscula",

        "MSJ_ERROR_CONTRASEÑA_NUMERO": "La contraseña debe contener por lo menos un numero",

        "MSJ_ERROR_CONTRASEÑA_AMBOS_ESPECIAL":"La contraseña debe contener alguno de los caracteres '-' o '_'  pero no ambos",

        "MSJ_ERROR_CONTRASEÑA_MIN_ESPECIAL":"La contraseña debe contener alguno de los caracteres '-' o '_'",

        "MSJ_ERROR_CONTRASEÑA_UNO_ESPECIAL":"La contraseña no puede tener mas un un'-' ó un '_'",

        "MSJ_ERROR_CONTRASEÑA_CARACTER_INVALIDO":"La contraseña debe estar compuesta solo por caracteres alfanuméricos excepto por alguno de los caractres '_' ó '-'",

        "MSJ_ERROR_CONTRASEÑA_CANTIDAD_CARACTERES": "La contraseña debe tener mas de 8 caracteres y menos de 12",

        "MSJ_CARACTER_INVALIDO_SOLO_NUMEROS": "No es valido. Ingresar números enteros",

        "MSJ_NUMEROS_NEGATIVOS":"No es un valor, válido",

        "MSJ_ERROR_SIN_USUARIOS": "No hay usuarios registrados",

        "INGRESAR_PALABRA_TABLERO": "Arriesgo: ",

        "INFORMA_PALABRAS_SOLO_LETRAS": "La palabra debe contener solo letras",

        "INFORMA_MAX_LETRAS": "La palabra solo debe tener ",

        "CONCATENADO_MAX_LETRAS": " y tiene ",

        "MSJ_ADVERTENCIA_SESION_YA_INICIADA": " Ya tiene la sesión iniciada",

        "MSJ_INFORMACION_SESION": "Sesión iniciada correctamente",

        "MSJ_ERROR_USUARIO_CONTRASEÑA": "Contraseña y/o usuario no son incorrectas",

        "MSJ_MAXIMO_JUGADORES": "El juego está implementado para un máximo de jugadores: ",

        "MSJ_MAX_LETRAS_PALABRA": "La cantidad de letras por palabra no puede ser mayor",

        "MSJ_MAX_PARTIDAS": "El juego no puede tener un numero de partidas mayor a ",

        "MSJ_USUARIO_YA_EXISTE": "El usuario ya existe",

        "MSJ_CONTRASEÑA_USUARIO_REQUERIDOS": "Los camos nombre y contraseña son requeridos",

        "MSJ_NOMBRE_REQUERIDO": "El campo nombre es requerido",

        "MSJ_CONTRASEÑA_REQUERIDA": "El campo contraseña es requerido",

        "MSJ_CONTRASEÑAS_NO_COINCIDEN": "Las contraseñas no coinciden",

        "MSJ_USUARIO_REGISTRADO_EXITO": "Usuario registrado con éxito",

        "MSJ_REGISTRAR_OTRO_USUARIO": "¿Quiere registrar otro usuario?",

        "MSJ_CONFIRMAR_CONFIG_DEFECTO":"¿Quiere usar las configuraciones por defecto ?",

        "WIDGET_ERROR_TITULO": "Error",

        "WIDGET_WARNING_TITULO": "Advertencia",

        "WIDGET_INFO_TITULO": "Informativo",

        "WIDGET_CONFIRM_TITULO": "Confirmar",

        "MSJ_ERROR_SIN_ARCHIVO":"Para iniciar el juego, debe haber cargado un archivo te texto como mínimo",

        "MSJ_CERRAR_PROGRAMA": "El programa, se cerrará",

        "JUEGO_INICIALIZADO": "JUEGO INICIADO",

        "JUEGO_FINALIZADO": "FIN DEL JUEGO",

        "TEXTO_GANADOR": "GANADOR",

        "TEXTO_OBTUVO": "OBTUVO",

        "TEXTO_FINALIZAR": "Enter para finalizar...",

        "LABEL_NOMBRE": "Nombre: ",

        "LABEL_CONTRASEÑA": "Contraseña: ",

        "LABEL_REPETIR_CONTRASEÑA": "Repetir contraseña: ",

        "LABEL_JUGADORES": "Jugadores: ",

        "LABEL_LETRAS": "Letras: ",

        "LABEL_PARTIDAS": "Partidas: ",

        "BOTON_REGISTRAR": "REGISTRASE",

        "BOTON_INGRESAR": "INGRESAR",

        "BOTON_VOLVER": "VOLVER",

        "BOTON_GUARDAR_REGISTRO": "GUARDAR",

        "BOTON_ACCEDER": "ACCEDER",

        "BOTON_CONFIRMAR": "CONFIRMAR",
        "INPUT_CONTINUAR":"ENTER_PARA CONTINUAR"
    }
    
    elif idioma == "en":
        """
        DEBERIAMOS TRADUCIR

        diccionario_mensajes = {
        "TIEMPO_ADIVINA_PALABRA": "Tiempo en adividinar la palabra: ",
        
        "CABECERA_PUNTAJES": "PUNTAJES",
        
        "COL_JUGADOR": "JUGADOR",
        
        "COL_PUNTOS": "PUNTOS",
        
        "COL_ACOMULADO": "ACOMULADO",
        
        "MSJ_ERROR_NOMBRE": "El nombre solo acepta caracteres alfabéticos, numéricos y el guión bajo",
        
        "MSJ_ERROR_RANGO_NOMBRE": "El nombre debe no puede tener menos de 4 o más de 15 caracteres",

        "MSJ_ERROR_CONTRASEÑA_MAYUSCULAS": "La contraseña debe contener por lo menos una letra mayúsculas",

        "MSJ_ERROR_CONTRASEÑA_MINUSCULAS": "La contraseña debe contener por lo menos una letra minúscula",

        "MSJ_ERROR_CONTRASEÑA_NUMERO": "La contraseña debe contener por lo menos un numero",

        "MSJ_ERROR_CONTRASEÑA_AMBOS_ESPECIAL":"La contraseña debe contener alguno de los caracteres '-' o '_'  pero no ambos",

        "MSJ_ERROR_CONTRASEÑA_MIN_ESPECIAL":"La contraseña debe contener alguno de los caracteres '-' o '_'",

        "MSJ_ERROR_CONTRASEÑA_UNO_ESPECIAL":"La contraseña no puede tener mas un un'-' ó un '_'",

        "MSJ_ERROR_CONTRASEÑA_CARACTER_INVALIDO":"La contraseña debe estar compuesta solo por caracteres alfanuméricos excepto por alguno de los caractres '_' ó '-'",

        "MSJ_ERROR_CONTRASEÑA_CANTIDAD_CARACTERES": "La contraseña debe tener mas de 8 caracteres y menos de 12",

        "MSJ_CARACTER_INVALIDO_SOLO_NUMEROS": "No es valido. Ingresar números enteros",

        "MSJ_NUMEROS_NEGATIVOS":"No es un valor, válido",

        "MSJ_ERROR_SIN_USUARIOS": "No hay usuarios registrados",

        "INGRESAR_PALABRA_TABLERO": "Arriesgo: ",

        "INFORMA_PALABRAS_SOLO_LETRAS": "La palabra debe contener solo letras",

        "INFORMA_MAX_LETRAS": "La palabra solo debe tener ",

        "CONCATENADO_MAX_LETRAS": " y tiene ",

        "MSJ_ADVERTENCIA_SESION_YA_INICIADA": " Ya tiene la sesión iniciada",

        "MSJ_INFORMACION_SESION": "Sesión iniciada correctamente",

        "MSJ_ERROR_USUARIO_CONTRASEÑA": "Contraseña y/o usuario no son incorrectas",

        "MSJ_MAXIMO_JUGADORES": "El juego está implementado para un máximo de jugadores: ",

        "MSJ_MAX_LETRAS_PALABRA": "La cantidad de letras por palabra no puede ser mayor",

        "MSJ_MAX_PARTIDAS": "El juego no puede tener un numero de partidas mayor a ",

        "MSJ_USUARIO_YA_EXISTE": "El usuario ya existe",

        "MSJ_CONTRASEÑA_USUARIO_REQUERIDOS": "Los camos nombre y contraseña son requeridos",

        "MSJ_NOMBRE_REQUERIDO": "El campo nombre es requerido",

        "MSJ_CONTRASEÑA_REQUERIDA": "El campo contraseña es requerido",

        "MSJ_CONTRASEÑAS_NO_COINCIDEN": "Las contraseñas no coinciden",

        "MSJ_USUARIO_REGISTRADO_EXITO": "Usuario registrado con éxito",

        "MSJ_REGISTRAR_OTRO_USUARIO": "¿Quiere registrar otro usuario?",

        "MSJ_CONFIRMAR_CONFIG_DEFECTO":"¿Quiere usar las configuraciones por defecto ?",

        "WIDGET_ERROR_TITULO": "Error",

        "WIDGET_WARNING_TITULO": "Advertencia",

        "WIDGET_INFO_TITULO": "Informativo",

        "WIDGET_CONFIRM_TITULO": "Confirmar",

        "MSJ_ERROR_SIN_ARCHIVO":"Para iniciar el juego, debe haber cargado un archivo te texto como mínimo",

        "MSJ_CERRAR_PROGRAMA": "El programa, se cerrará",

        "JUEGO_INICIALIZADO": "JUEGO INICIADO",

        "JUEGO_FINALIZADO": "FIN DEL JUEGO",

        "TEXTO_GANADOR": "GANADOR",

        "TEXTO_OBTUVO": "OBTUVO",

        "TEXTO_FINALIZAR": "Enter para finalizar...",

        "LABEL_NOMBRE": "Nombre: ",

        "LABEL_CONTRASEÑA": "Contraseña: ",

        "LABEL_REPETIR_CONTRASEÑA": "Repetir contraseña: ",

        "LABEL_JUGADORES": "Jugadores: ",

        "LABEL_LETRAS": "Letras: ",

        "LABEL_PARTIDAS": "Partidas: ",

        "BOTON_REGISTRAR": "REGISTRASE",

        "BOTON_INGRESAR": "INGRESAR",

        "BOTON_VOLVER": "VOLVER",

        "BOTON_GUARDAR_REGISTRO": "GUARDAR",

        "BOTON_ACCEDER": "ACCEDER",

        "BOTON_CONFIRMAR": "CONFIRMAR"
        }
        """
        pass
    

    return diccionario_mensajes