
import json
import pandas as pd
from numpy import loadtxt


with open("/home/cristian/Descargas/Universidad/6_2022-2/PI/Research-practice-1/Codigo/Codigo_final/BERTopic/tweets.json", "r") as fp:
    diccionario_tweets = json.load(fp)

    print("\ns: Con algún transtorno.")
    print("n: Sin transtorno.")
    print("Ingresa espacio en blanco para terminar.")

    entrada = "a"

    llaves = list(diccionario_tweets['data'].keys())
    cont = 0
    #clasificacion = queue.Queue()
    tweets = []
    clasificacion = []

    while entrada != "":
        with open('mi_fichero.txt', 'a') as f:
            print("\n" + diccionario_tweets['data'][llaves[cont]]['text'])
            entrada = input()
            cont += 1

            if entrada != "":
                f.write(entrada + "\n")


    lines = list(loadtxt("mi_fichero.txt", dtype=str))
    print(lines)

    for i in lines:
        print(i)

