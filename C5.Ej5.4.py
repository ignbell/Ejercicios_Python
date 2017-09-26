# -*- encoding:utf-8 -*-
# Ejercicio 5.4.
#  Utilizando la función randrange del módulo random, escribir un programa que obtenga un número aleatorio
#  secreto, y luego permita al usuario ingresar números y le indique sin son menores o mayores que el número a adivinar,
#  hasta que el usuario ingrese el número correcto.

import random

numa=random.randrange(0,10)
print numa
numerob=int(input("Inserte un numero"))
while numa != numerob:
    print numa
    type(numa)
    print numerob
    type(numerob)
    if numa < numerob:
        print "El numero ingresado es mayor que el numero a encontrar."
    if numa > numerob:
        print "El numero ingresado es menor que el numero a encontrar."
    numerob = int(input("Inserte un numero"))
print"Usted ha encontrado el numero secreto"