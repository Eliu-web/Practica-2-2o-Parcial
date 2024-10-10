print("")#Salto de linea
print ("Velazquez Mares Jesus Eliu 3W 1276")
print("")#Salto de linea

def distanciapuntos(p1, p2):#Define distanciapuntos como una funcion
    x1, y1 = p1
    x2, y2 = p2
    return (x2 - x1, y2 - y1)#Calcula la distancia entre dos puntos.

print(distanciapuntos((1, 2), (4, 6))) 