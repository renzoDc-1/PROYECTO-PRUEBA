import os
from module.sum import suma
from module.resta import resta
from module.multiplicar import multiplicar
from module.division import division

os.system("cls")
os.system("color a")

def message():
    print("CALCULOS BASICOS AUTOMATICOS ")

def calcular(a, b, signo):
    if signo == '+':
        return suma(a, b)
    elif signo == '-':
        return resta(a, b)
    elif signo == '*':
        return multiplicar(a, b)
    elif signo == '/':
        return division(a, b)
    else:
        return "Signo no válido"

def obtener_entrada():
    a = int(input("Ingrese el primer número: "))
    signo = input("Ingrese el signo (+, -, *, /): ")
    b = int(input("Ingrese el segundo número: "))
    return a, signo, b

def mostrar_resultado(a, signo, b, resultado):
    print(f"El resultado de {a} {signo} {b} es {resultado}")

message()
a, signo, b = obtener_entrada()
resultado = calcular(a, b, signo)
mostrar_resultado(a, signo, b, resultado)
