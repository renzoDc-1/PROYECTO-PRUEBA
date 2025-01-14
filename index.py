import os
from module.sum import suma
from module.resta import resta
from module.multiplicar import multiplicar
from module.division import division

os.system("cls")

def message():
    print("Tenia que ser ")

message()


def llamar_suma():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = suma(a, b)
    print(f"La suma de {a} y {b} es {resultado}")

llamar_suma()

def llamar_resta():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = resta(a,b)
    print(f"La resta de {a} y {b} es {resultado}")

llamar_resta()

def llamar_multiplicacion():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = multiplicar(a, b)
    print(f"La multiplicacion de {a} y {b} es {resultado}")

llamar_multiplicacion()

def llamar_division():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = division(a, b)
    print(f"La division de {a} y {b} es {resultado}")

llamar_division()

