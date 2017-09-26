#-*- coding:utf-8 -*-

#Ejercicio 2.4. Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
acum=0
n = int(input("Por favor ingresar la cantidad de numeros triangulares que desea.\n"))

def triangular(num):
	result=float(num*((num+1.0)/2.0))
	return result

print("\nResultado sin formula:")
for i in range (1,n+1,1):
	acum=acum+i
	print(str(i) + "-" + str(acum))

print("\nResultado con formula:")
for j in range (1,n+1,1):
	valor=int(triangular(j))
	print(str(j) + "-" + str(valor))

print("\nResultado 2 sin formula:")
for i in range (1,n+1,1):
	acum=0
	for j in range (1,i+1,1):
		acum=acum+j
	print(str(i) + "-" + str(acum))



print("\nResultado 3 sin formula:")
for i in range (1,i+1,1):
	acum=0
	num=0
	for j in range (1,i+1,1):
		acum=acum+1
		num=acum+num
	print(str(i) + "-" + str(num))


