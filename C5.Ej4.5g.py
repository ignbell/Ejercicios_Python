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



def bisiesto(year):
	if (((year%4==0) and (year%400==0)) and (year%100!=0)):
		days=366
		return
	else:
		days=365
		return days

def diasdelmes(year,month):
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
	if ( ((month >= 1 ) and (month <= 12)) and ( (day >= 1) and (day <= (diasmes(year,month)) )) ):
		return True
	else:
		return False

def diasfmes(year,month,day):
	totalmdays=diasdelmes(year,month)
	return (totalmdays - day)

def diastmes(year,month,day):
    result=diasdelmes(year,month,day) - diasfmes(year,month,day)
    return result

def diasfanio(year,month,day):
	diasquefaltanenelmes=diasfmes(year,month,day)
	cont=0
	for i in range(month+1, 12, 1):
		cont+=diasdelmes(year,i)
	cont=cont+diasquefaltanenelmes
	return cont

def diastanio(year,month,day):
    dfmes=( bisiesto(year) - diasfanio(year,month,day))
    return dfmes

def mesfanio(month):
    total=12-month
    return total

def mestanio(month):
    total=0+month
    return total




#def diffyears(year1,year2):
#    if year1 > year2:
#        total = (year1 -1) - year2
#    if year1 < year2:
#        total = (year2 -1) - year1
#    if year1 == year2:
#        total=0
#    return total
#
#def diffmonths(year1,month1,year2,month2):
#    if year1 < year2:
#        if month1 < month2:
#            #total = mesfanio(month2) - mestanio(month1)
#            total = month2-month1
#        if month1 > month2:
#            #total = mesfanio(month1) - mestanio(month2)
#            total = mesfanio(month1) + mestanio(month2)
#        if month1 == month2:
#            total = 0
#    if year1 > year2:
#        if month1 < month2:
#            total = mesfanio(month1) + month2
#            #total = mesfanio(month1) + mestanio(month2)
#            #total = month2 + month1
#        if month1 > month2:
#            total = mesfanio(month2) - mestanio(month1)
#            #total = month1 - month2
#        if month1 == month2:
#            total=0
#    if year1 == year2:
#        if month1 < month2:
#            total = month2 - month1
#        if month1 > month2:
#            total = month1 - month2
#        if month1 == month2:
#            total = 0
#    return total
#
##def diffmonths(month1,month2):
##    if month1 > month2:
##        diffmonths = month1 - month2
##        total = diffmonths
##    elif month1 < month2:
##        diffmonths = month2 - month1
##        total = diffmonths
##    else:
##        total=0
##    return total
#
#def diffdays(year1,month1,day1,year2,month2,day2):
#    if day1 > day2:
#        diffdias = day1 - day2
#        diasfaltantes = diasfanio(year1, month1, day1)
#        diastranscurridos = diastanio(year2, month2, day2)
#        total = diasfaltantes + diastranscurridos + diffdias
#    elif day1 < day2:
#        diffdias = day2 - day1
#        diasfaltantes = diasfanio(year2, month2, day2)
#        diastranscurridos = diastanio(year1, month1, day1)
#        total = diasfaltantes + diastranscurridos + diffdias
#    else:
#        total = 0
#    return total


yearB=1980
monthB=10
dayB=1

yearA=1981
monthA=11
dayA=1



print (yearA,monthA,dayA)
print (yearB,monthB,dayB)

if yearA == yearB:
	if monthA < monthB:
		totalmonth = monthB - monthA
	if monthA > monthB:
		totalmonth = monthA - monthB
	if monthA == monthB:
		totalmonth = 0
	totalyear = yearA - yearB
#
if yearA < yearB:
	if monthA < monthB:
		totalmonth = monthB - monthA
		keyyear = 0
	if monthA > monthB:
		totalmonth = mesfanio(monthB) - monthA
		keyyear = 1
	if monthA == monthB:
		totalmonth = 0
		keyyear = 0
	totalmonth=abs(totalmonth)
	totalyear = abs(yearB - yearA - keyyear)
#
if yearA > yearB:
	if monthA < monthB:
		totalmonth = mesfanio(monthB) - monthA
		keyyear = -1
		if totalmonth < -6:
			totalmonth=monthB-monthA
	if monthA > monthB:
		totalmonth = monthB - monthA
		keyyear = 0
	if monthA == monthB:
		totalmonth = 0
		keyyear = 0
	totalmonth=abs(totalmonth)
	totalyear = abs(yearB - yearA - keyyear)



#print "La diferencia entre ambas fechas es de " + totalyear + " años " + totalmonth + " meses " + totaldays + " dias."
print "La diferencia entre ambas fechas es de " + str(totalyear) + " años " + str(totalmonth) + " meses "


#print "La diferencia entre ambas fechas es de " + str(diffyears(yearA, yearB)) + " años " + str(diffmonths(yearA,monthA,yearB,monthB)) + " meses " + str(diffdays(yearA,monthA,dayA,yearB,monthB,dayB)) + " dias."
#else:
	#print ("Error - Usted ingreso una fecha incorrecta.")
#   if DayA > DayB:
#       diffdias = DayA - DayB
#       diasfaltantes = diasfanio(yearA, monthA, DayA)
#       diastranscurridos = diastanio(yearB, monthB, DayB)
#       total = diasfaltantes + diastranscurridos + diffdias
#   elif DayA < DayB:
#       diffdias = DayB - DayA
#       diasfaltantes = diasfanio(yearB, monthB, DayB)
#       diastranscurridos = diastanio(yearA, monthA, DayA)
#       total = diasfaltantes + diastranscurridos + diffdias
#   else:
#       total = 0
#   return total


#yearA=int(input("Ingrese el año A.\n"))
#monthA=int(input("Ingrese el mes A.\n"))
#dayA=int(input("Ingrese el dia A.\n"))

#yearB=int(input("Ingrese el año B.\n"))
#monthB=int(input("Ingrese el mes B.\n"))
#dayB=int(input("Ingrese el dia B.\n"))

#if validate(yearA, monthA, dayA) == True and validate(yearB, monthB, dayB) == True :