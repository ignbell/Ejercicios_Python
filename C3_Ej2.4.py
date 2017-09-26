#-*- coding:utf-8 -*-

#Ejercicio 2.4. Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

j = int(input("Por favor ingresar el numero mas bajo del rango\n"))
q = int(input("Por faovr ingresar el numero mas alto del rango\n"))
print("\nResultado:")

def par(num):
	if (num%2 == 0): 
        	result=num
		print(result)



for i in range (j,q,1):
	par(i)

