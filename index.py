import os
from module.sum import suma

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

def resta(a, b):
    return a - b

print(resta(2, 3))

def multiplicar(a, b):
    return a * b

print(multiplicar(2, 3))