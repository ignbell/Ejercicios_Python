#-*- coding:utf-8 -*-

#Ejercicio 2.1. Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés
#y un número de años y muestre como resultado el monto final a obtener. La fórmula a utilizar es:
#Cn = C × (1 + x/100) n
#Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.


c = int (input ("Cantidad de pesos\n"))
x = int (input ("Tasa de interes\n"))
n = int (input ("anios\n"))

def formula( c, x, n ):
	resultado = c * (( 1 + x/100) ** n)
	return resultado

resultado = formula(c, x, n) 
print (resultado)



