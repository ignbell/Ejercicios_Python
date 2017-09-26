# -*- encoding:utf-8 -*-

#Ejercicio 4.1. Escribir funciones que resuelvan los siguientes problemas:
# a) Dado un número entero n, indicar si es o no par.
# b) Dado un número entero n, indicar si es o no primo.

def par(number):
	if (number%2 == 0) :
		print("El numero " + str(number) + " es par." )
		return 
	else :
		print("El numero " + str(number) + " es impar." )
		return 

def primo(number):
	cont=0
	for i in range(1, number, 1):
		print (i)
		if (number%i == 0):
			cont=cont+1
	if ((cont > 0) and (cont < 3)):
		print("El numero " + str(number) + " es primo")
	else:
		print("El numero " + str(number) + " no es primo")
		
		


num = int(input("Please provide an int number\n"))
par(num)
primo(num)
