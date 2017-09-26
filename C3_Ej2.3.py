# -*- coding:utf-8 -*-

#Ejercicio 2.3. Utilice el programa anterior para generar una tabla de conversión de temperaturas, desde 0◦ F hasta 120◦ F, de 10 en 10.


def convert(CELCIUS):
        F = ((9.0/5.0) * CELCIUS) + 32.0
        return F

for i in range(0, 121, 10):
	result=convert(i)
	print("Celcius=" + str(i) + " = " + "Farhenheit=" + str(result))


