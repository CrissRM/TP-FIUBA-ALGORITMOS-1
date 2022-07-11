import operator
import os
from pathlib import Path
from configuraciones.datos_iniciales import condiciones_iniciales

dicc_palabra = {}
"Esta funcion se encarga de luego de leer las palabras respectivas de cada texto y armar un diccionario con la palabra"
"como clave y la cantidad de veces que aparece en cada texto ,ordenarlas y devolver una lista de listas de palabras correspondientes al largo de palabra indicado"
"Autor Sebastian Olaran"

def diccionario_de_palabras():
    LONG_PALABRA = condiciones_iniciales()["cantidad_letras"]
    archivos = []
    with open("archivos/palabras.csv","w") as palabras:
        for archivo in os.scandir("archivos/textos"):
            archivo = Path(archivo.name)
            if archivo.suffix == ".csv" or archivo.suffix == ".txt":
                archivos.append(open(f"archivos/textos/{archivo.name}"))
        
        for i in range(len(archivos)):
            analizador_texto(archivos[i],i+1,LONG_PALABRA)
        
        ordenar_palabras(palabras)

        for i in range(len(archivos)):
            archivos[i].close()

def leer_Archivo(archivo):
    linea = archivo.readline()
    if linea !="":
        respuesta=linea.rstrip('\n').rstrip(',').rstrip('.').rstrip(';').rstrip('!').rstrip('¡').rstrip("?").rstrip('¿').rstrip('-').rstrip('_').rstrip('"').rstrip('*').rstrip('<<').rstrip('>>').split(' ') 
    else :
        respuesta=""
    return respuesta

def grabar_Nuevo(archivo,palabra,cantidad1,cantidad2,cantidad3):
    archivo.write(str(palabra) + ',' + str(cantidad1) +","+ str(cantidad2) +","+ str(cantidad3) +'\n')

def analizador_texto(texto,num_text,LONG):
  palabras=leer_Archivo(texto)
  while (palabras !=""):
    for palabra in palabras :
      if (palabra.isalpha()) and (palabra!="") and (len(palabra)==LONG) :
        if palabra.upper() in dicc_palabra:
          if num_text ==1:
            dicc_palabra[palabra.upper()][0]+=1
          elif num_text ==2:
            dicc_palabra[palabra.upper()][1]+=1
          else:
            dicc_palabra[palabra.upper()][2]+=1
        else:
          if num_text ==1:
            dicc_palabra.setdefault(palabra.upper(),[1,0,0])
          elif num_text ==2:
            dicc_palabra.setdefault(palabra.upper(),[0,1,0])
          else:
            dicc_palabra.setdefault(palabra.upper(),[0,0,1])
    palabras=leer_Archivo(texto)

def ordenar_palabras(archivo_4):
    palabras_ordenadas=sorted(dicc_palabra.items(),key=operator.itemgetter(0))
    for elementos in palabras_ordenadas:
      palabra=elementos[0]
      cant_1=elementos[1][0]
      cant_2=elementos[1][1]
      cant_3=elementos[1][2]
      grabar_Nuevo(archivo_4,palabra,cant_1,cant_2,cant_3)
    return palabras_ordenadas

