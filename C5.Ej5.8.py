# -*- encoding:utf-8 -*-

#Ejercicio 5.8.
# Escribir un programa que le pida al usuario que ingrese una sucesión de números naturales.\
# (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición de salida).
# Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.

cont=0
suma=0

data=int(input("Ingrese un numero natural o '-1' para abortar\n: "))
if data == -1:
    exit(0)
else:
    while data != -1:
        data=int(input("Ingrese un numero natural o '-1' para abortar\n: "))
        if data != -1:
            cont+=1
            suma+=int(data)
            promedio=suma/cont
        if data == -1:
            print "Cantidad de numeros ingresados " + str(cont)
            print "La suma total de los numeros ingresados es de " + str(suma)
            print "El promedio es " + str(promedio)

    exit(0)


