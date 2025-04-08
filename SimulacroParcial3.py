#coding = utf-8
import random
from os import system
system("cls")
def calcula_total_ordenes(diccionario_ordenes, criterio_busqueda):
    total = 0
    for clave in diccionario_ordenes:
        for categoria, valor in diccionario_ordenes[clave].items():
            estado = valor[1]
            if estado == criterio_busqueda:
                total += 1
    return total
    
def asignar_estado(valor):
    if valor == 0:
        return "nula"
    elif valor == 10:
        return "prioritaria"
    else:
        return "normal"


diccionario_ordenes = {}
for i in range(1000):
    cimentacion = random.randint(0, 10)
    estructura = random.randint(0, 10)
    techos = random.randint(0, 10)
    acabados = random.randint(0, 10)
    tuberias = random.randint(0, 10)
    
    diccionario_ordenes[i] = {
        "Cimentación": [cimentacion, asignar_estado(cimentacion)],
        "Estructura": [estructura, asignar_estado(estructura)],
        "Techos": [techos, asignar_estado(techos)],
        "Acabados": [acabados, asignar_estado(acabados)],
        "Tuberías": [tuberias, asignar_estado(tuberias)]
    }

total_nulas = calcula_total_ordenes(diccionario_ordenes, "nula")
total_prioritarias = calcula_total_ordenes(diccionario_ordenes, "prioritaria")
total_normales = calcula_total_ordenes(diccionario_ordenes, "normal")

porcentaje_nulas = (total_nulas / ((len(diccionario_ordenes)*5)) * 100)
porcentaje_prioritarias = (total_prioritarias / ((len(diccionario_ordenes)*5)) * 100)
porcentaje_normales = (total_normales / ((len(diccionario_ordenes)*5)) * 100)

print("Total de ordenes nulas:", total_nulas)
print("Total de ordenes prioritarias:", total_prioritarias)
print("Total de ordenes normales:", total_normales)
print("Porcentaje de ordenes nulas:", porcentaje_nulas, "%")
print("Porcentaje de ordenes prioritarias:", porcentaje_prioritarias, "%")
print("Porcentaje de ordenes normales:", porcentaje_normales, "%")