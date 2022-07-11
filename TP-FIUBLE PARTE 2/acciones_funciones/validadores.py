from configuraciones.estilos_widgets import msg_error,msg_warning
from configuraciones.datos_iniciales import formatear_linea,condiciones_iniciales
"La funcion de validadores se encarga de validar el nombre que imgresa el usuario,su contraseña"
"si cumple con los requisitos dados ,valida el inicio de sesion si es indicado,valida texto? ,formatea la palabra para el uso correcto de validacion y verifica "
"y por ultimo valida si la palabra esta dentro de los parametros establecidos"
"Autor Cristian Roldan"
def nombre(nombre,textos):
    if 4<= len(nombre) <=15:
        caracteres_validos = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyzáÁéÉíÍóÓúÚ0123456789_"
        i = 0
        error = False
        while i<len(nombre) and not error:
            if nombre[i] not in caracteres_validos:
                error = True
            i +=1
        if error:
            msg_error(textos["MSJ_ERROR_NOMBRE"],textos)#
            res = False
        else:
            res = True
    else:
        msg_warning(textos["MSJ_ERROR_RANGO_NOMBRE"],textos)#
        res = False
    return res

def contrasenia(password,textos,error = False,exceso_char=False):
    
    
    caracteres_validos ={
  "A":1,"Á":1,
  "B":2,
  "C":3,
  "D":4,
  "E":5,"É":5,
  "F":6,
  "G":7,
  "H":8,
  "I":9,"Í":9,
  "J":10,
  "K":11,
  "L":12,
  "M":13,
  "N":14,
  "Ñ":15,
  "O":16,"Ó":16,
  "P":17,
  "Q":18,
  "R":19,
  "S": 20,
  "T":21,
  "U":22,"Ú":22,
  "V":23,
  "W":24,
  "X":25,
  "Y":26,
  "Z":27,
  "a":28,"á":28,
  "b":29,
  "c":30,
  "d":31,
  "e":32,"é":32,
  "f":33,
  "g":34,
  "h":35,
  "i":36,"í":36,
  "j":37,
  "k":38,
  "l":39,
  "m":40,
  "n":41,
  "ñ":42,
  "o":43,"ó":43,
  "p":44,
  "q":45,
  "r":46,
  "s":47,
  "t":48,
  "u":49,"ú":49,
  "v":50,
  "w":51,
  "x":52,
  "y":53,
  "z":54,
  "-":55,
  "_":56,
  "0":57,
  "1":58,
  "2":59,
  "3":60,
  "4":61,
  "5":62,
  "6":63,
  "7":64,
  "8":65,
  "9":66

}    
    if 8<= len(password)<=12:
        i = 0
        cont_mayusculas = 0
        cont_minusculas = 0
        cont_numero = 0
        cont_guion = 0
        cont_guion_bajo = 0

        while i<len(password) and not error and not exceso_char:
            if caracteres_validos.get(password[i]):
                if 1<= caracteres_validos[password[i]]<=27:
                    cont_mayusculas +=1
                if 28 <= caracteres_validos[password[i]] <=54:
                    cont_minusculas +=1
                if caracteres_validos[password[i]] ==55:
                    cont_guion +=1
                if caracteres_validos[password[i]] ==56:
                    cont_guion_bajo +=1
                if 57 <= caracteres_validos[password[i]] <=66:
                    cont_numero +=1
                if cont_guion >0 and cont_guion_bajo>0:
                    exceso_char = True
                if cont_guion_bajo >1:
                    exceso_char = True
                if cont_guion >1:
                    exceso_char = True
            else:
                error = True
            i+=1

        if not error:
            if cont_mayusculas == 0:
                msg_error(textos["MSJ_ERROR_CONTRASEÑA_MAYUSCULAS"],textos)
                res = False
            elif cont_minusculas == 0:
                msg_error(textos["MSJ_ERROR_CONTRASEÑA_MINUSCULAS"],textos)
                res = False
            elif cont_numero == 0:
                msg_error(textos["MSJ_ERROR_CONTRASEÑA_NUMERO"],textos)
                res = False
            elif (cont_guion >0 and cont_guion_bajo >0):
                msg_error(textos["MSJ_ERROR_CONTRASEÑA_AMBOS_ESPECIAL"],textos)
                res = False
            elif cont_guion == 0 and cont_guion_bajo==0:
                msg_error(textos["MSJ_ERROR_CONTRASEÑA_MIN_ESPECIAL"],textos)
                res = False
            elif (cont_guion>1 and cont_guion_bajo==0) or (cont_guion_bajo>1 and cont_guion ==0):
                msg_error(textos["MSJ_ERROR_CONTRASEÑA_UNO_ESPECIAL"],textos)
                res =False
            else:
                res = True
        else:
            msg_error(textos["MSJ_ERROR_CONTRASEÑA_CARACTER_INVALIDO"],textos)
            res = False
            error = True
    else:
        msg_error(textos["MSJ_ERROR_CONTRASEÑA_CANTIDAD_CARACTERES"],textos)
        res = False

  
    return res

def texto(valor,textos):
  try:
    valor_a_validar = int(valor)
  except ValueError:
    msg_error(textos["MSJ_CARACTER_INVALIDO_SOLO_NUMEROS"],textos)
    valor_a_validar = False
  else:
    if valor_a_validar <= 0:
      msg_warning(textos["MSJ_NUMEROS_NEGATIVOS"],textos)
      valor_a_validar = False
  return valor_a_validar

def usuario(nombre):
  existe = False

  try:
    with open("archivos/jugadores.csv","r") as archivo_csv:
      jugador = archivo_csv.readline().strip("\n").split(",")[0]
      while jugador !="" and not existe:
        if jugador == nombre:
          existe  = True
        jugador = archivo_csv.readline().strip("\n").split(",")[0]
  except FileNotFoundError:
    with open("archivos/jugadores.csv","w") as archivo_csv:
      pass
    
  return existe

def sesion(nombre,contrasenia,textos):
  existe = False
  try:
    with open("archivos/jugadores.csv","r") as archivo_csv:
      jugador,password = formatear_linea(archivo_csv.readline())
      while jugador !="" and not existe:
        if jugador == nombre and password == contrasenia:
          existe  = True
        jugador,password = formatear_linea(archivo_csv.readline())
  except FileNotFoundError:
    msg_error(textos["MSJ_ERROR_SIN_USUARIOS"],textos)
    
    
  return existe

def formatear_palabra(palabra):
    letras = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u"
    }

    lista = [x for x in palabra]
    for i in range(len(lista)):
        if lista[i] in list(letras.keys()):
            lista[i] = letras[lista[i]]
    return "".join(lista)

def validar_condicion_palabra(textos):


    
    MAX_LETRAS = condiciones_iniciales()["cantidad_letras"]
  
    palabra=input(textos["INGRESAR_PALABRA_TABLERO"])
    while len(palabra)!=MAX_LETRAS or (not palabra.isalpha()):
        if len(palabra)!=MAX_LETRAS:
            print(f"{textos['INFORMA_MAX_LETRAS']} {MAX_LETRAS} {textos['CONCATENADO_MAX_LETRAS']}{len(palabra)}")
        elif not palabra.isalpha() :
            print(textos["INFORMA_PALABRAS_SOLO_LETRAS"])
        palabra=input(textos["INGRESAR_PALABRA_TABLERO"]) 
        palabra = formatear_palabra(palabra)
    
    return palabra.upper() 
  