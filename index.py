import os
from module.sum import suma
from module.resta import resta

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


def multiplicar(a, b):
    return a * b

print(multiplicar(2, 3))

def llamar_resta():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = resta(a,b)
    print(f"La resta de {a} y {b} es {resultado}")

llamar_resta()