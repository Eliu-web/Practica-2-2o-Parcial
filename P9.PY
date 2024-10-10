print("")#Salto de linea
print ("Velazquez Mares Jesus Eliu 3W 1276")
print("")#Salto de linea

def suma(numeros):#Define suma como una funcion
    total = 0
    for numero in numeros:#Suma todos los números de una lista.
        total += numero
    return total

def multiplicar(numeros): #Define multiplicar como una funcion 
    resultado = 1
    for numero in numeros:#Multiplica todos los números de una lista.
        resultado *= numero
    return resultado

print(suma([1, 2, 3, 4])) 
print(multiplicar([1, 2, 3, 4])) 
