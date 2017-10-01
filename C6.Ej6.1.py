# -*- encoding:utf-8 -*-

# Ejercicio 6.1. Escribir funciones que dada una cadena de caracteres:
# a) Imprima los dos primeros caracteres.
# b) Imprima los tres últimos caracteres.
# c) Imprima dicha cadena cada dos caracteres. Ej.: ’recta’ debería imprimir ’rca’
# d) Dicha cadena en sentido inverso. Ej.: ’hola mundo!’ debe imprimir ’!odnum aloh’
# e) Imprima la cadena en un sentido y en sentido inverso. Ej: ’reflejo’ imprime
# ’reflejoojelfer’.

# a) Imprima los dos primeros caracteres.
def imprimir_2(string):
    print string[0:2]

# b) Imprima los tres últimos caracteres.
def imprimir_3_ultimos(string):
    print string[:3]

# c) Imprima dicha cadena cada dos caracteres. Ej.: ’recta’ debería imprimir ’rca’
def imprimir_cada_2_caracteres(string):
    print string[0::2]

# d) Dicha cadena en sentido inverso. Ej.: ’hola mundo!’ debe imprimir ’!odnum aloh’
def imprimir_doble_sentido(string):
    print string + string[::-1]

cadena = 'reflejo'
imprimir_2(cadena)
imprimir_3_ultimos(cadena)
imprimir_cada_2_caracteres(cadena)
imprimir_doble_sentido(cadena)

