
import json
from numpy import loadtxt
import os



with open("/home/cristian/Descargas/Universidad/6_2022-2/PI/Research-practice-1/Codigo/Codigo_final/BERTopic/tweets.json", "r") as fp:
    diccionario_tweets = json.load(fp)

    nombre_archivo_clasificacion = "clasificacion.txt"

    print("\ns: Con algún transtorno.")
    print("n: Sin transtorno.")
    print("Ingresa espacio en blanco para terminar.")

    entrada = "a"

    llaves = list(diccionario_tweets['data'].keys())
    cont = 0
    clasificacion = list()
    if os.path.exists(nombre_archivo_clasificacion):
        with open(nombre_archivo_clasificacion, 'r+') as archivo:
            clasificacion = archivo.readlines()

        cont = int(clasificacion.pop())


    while entrada != "\n":
        print("\n" + diccionario_tweets['data'][llaves[cont]]['text'])
        entrada = input() + "\n"
        cont += 1

        if entrada != "\n":
            clasificacion.append(entrada)

    with open(nombre_archivo_clasificacion, 'w') as archivo:
        clasificacion.append(str(cont-1))
        archivo.writelines(clasificacion)
