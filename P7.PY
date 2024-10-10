print("")#Salto de linea
print ("Velazquez Mares Jesus Eliu 3W 1276")
print("")#Salto de linea

def longitud(texto):#Define longitud como una funcion
    palabras = texto.split()#Devuelve la longitud de la última palabra.
    if palabras:
        return len(palabras[-1])
    return 0

print(longitud("Hello gays")) 
