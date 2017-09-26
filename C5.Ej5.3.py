# -*- encoding:utf-8 -*-

# Ejercicio 5.3. Manejo de contraseñas
# a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la con-traseña, y no le permita continuar hasta que la haya ingresado correctamente.
# b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
# c) Modificar el programa anterior para que después de cada intento agregue una pausa cada vez mayor, utilizando la función sleep del módulo time.
# d) Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).

import time


def secu(data,passw,attempts):
            cont = 0
            resultado=False
            #while ((data != passw) or (cont != int(attempts))):
            while (cont != attempts):
                cont+= 1
                print cont
                print attempts
                data=raw_input("Password again: ")
                if data == passw:
                    resultado = True
                    break
                else:
                    resultado = False
            return resultado


data = str(raw_input('Password: '))
passw='passguord'
attempts = int(3)
if secu(data,passw,attempts) == True:
    print "You inserted the right password."
else:
    print "You did't insert the right password."



