print("")#Salto de linea
print ("Velazquez Mares Jesus Eliu 3W 1276")
print("")#Salto de linea

import math
def circulo(radio):
    return math.pi * radio ** 2#Calcula el área de un círculo.

def cilindro(radio, altura):
    area = circulo(radio)#Calcula el volumen de un cilindro.
    return area * altura

print(circulo(5)) 
print(cilindro(5, 10)) 
