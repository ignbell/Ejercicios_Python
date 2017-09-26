#-*- coding:utf-8 -*-
#Dado un número natural, imprimir su tabla de multiplicar, desarrollada con sumas susesivas

number = long(input("Ingresar un numero natural. \n"))
suma = 0

if (number%int(number) != 0):
	print("ERROR = Usted no ha ingresado un numero natural")
else:
	for i in range (0, 11):
		#int(number)
		print(suma)
		suma=suma + number
		i=i+1
