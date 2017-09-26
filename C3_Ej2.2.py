# -*- coding:utf-8 -*-

#Ejercicio 2.2. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
#Recordar que la fórmula para la conversión es: F = 9/5 * C + 32

C = float(input("Please insert the amount of degrees in Celcius that you want converted into Fahrenheit.\n"))

def convert(CELCIUS):
        F = ((9.0/5.0) * CELCIUS) + 32.0
        return F

result=convert(C)
print(result)


