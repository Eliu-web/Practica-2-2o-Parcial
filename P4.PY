print("")#Salto de linea
print ("Velazquez Mares Jesus Eliu 3W 1276")
print("")#Salto de linea

def factura(sin_iva, iva=21): #Define factura como una funcion
    total = sin_iva * (1 + iva / 100) #Calcula el total de una factura incluyendo IVA. 
    return total

print(factura(100))
