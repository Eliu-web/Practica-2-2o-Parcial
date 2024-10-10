print("")#Salto de linea
print ("Velazquez Mares Jesus Eliu 3W 1276")
print("")#Salto de linea

def factorial(k):#Define factorial como una funcion
    if k < 0:#este programa calcula el factorial de un número positivo entero.
        return "Numero invalido"
    if k == 0:
        return 1
    factorial = 1
    for i in range(1, k + 1):
        factorial *= i
    return factorial

print(factorial(3)) 
