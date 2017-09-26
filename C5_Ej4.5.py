#-*- encoding:utf-8 -*-

# Ejercicio 4.5. Escribir funciones que resuelvan los siguientes problemas:
# a) Dado un año indicar si es bisiesto.
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto
# que también sea divisible por 400.
# b) Dado un mes, devolver la cantidad de días correspondientes.
# c) Dada una fecha (día, mes, año), indicar si es válida o no.
# d) Dada una fecha, indicar los días que faltan hasta fin de mes.
# e) Dada una fecha, indicar los días que faltan hasta fin de año.
# f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
# g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre
# ambas, en años, meses y días.
# Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.



def bisiesto(num):
	if (((num%4==0) and (num%400==0)) and (num%100!=0)):
		#print("El año es bisiesto")
		days=366
		return 
	else:
		#print ("El año no es bisiesto")
		days=365
		return days 
	#print ("La cantidad de dias en el año " + str(num) + " es " + str(days) + ".")

def diasmes(year,month):
	mdays=0
	if month==1:
		mdays=31
	if month==2:
		bis=bisiesto(year)
		if 366 == bis:
			mdays=29
		else:
			mdays=28
	if month==3:
		mdays=31
	if month==4:
		mdays=30
	if month==5:
		mdays=31
	if month==6:
		mdays=30
	if month==7:
		mdays=31
	if month==8:
		mdays=31
	if month==9:
		mdays=30
	if month==10:
		mdays=31
	if month==11:
		mdays=30
	if month==12:
		mdays=31
	#print ("La cantidad de dias en el mes " + str(month) + " es " + str(mdays) + ".")
	return mdays


def validate(year,month,day):
	if ( ( (month >= 1 ) and (month <= 12) ) and ( (day >= 1) and (day <= diasmes(year,month)) ) ):
		return True
	else:
		return False		 

def diasfmes(year,month,day):
	totalmdays=diasmes(year,month)  
	return (totalmdays - day)


def diasfanio(year,month,day):
	diasquefaltanenelmes=diasfmes(year,month,day)
	cont=0
	for i in range(month+1, 13, 1):
		cont+=diasmes(year,i)
	cont=cont+diasquefaltanenelmes
	return cont

def diastanio(year,month,day):
	dfmes=( bisiesto(year) - diasfanio(year,month,day)) 
	return dfmes




#year=int(input("Ingrese el año.\n"))
#month=int(input("Ingrese el mes.\n"))
#day=int(input("Ingrese el dia.\n"))

year=1982
month=1
day=1

if validate(year, month, day) == True:
	print (bisiesto(int(year)))
	print (diasmes(year,month))
	print (diasfmes(year,month,day))
	print (diasfanio(year,month,day))
	print (diastanio(year,month,day))

else:
	print ("Error - Usted ingreso una fecha incorrecta.")
