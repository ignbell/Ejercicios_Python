# -*- encoding:utf-8 -*-

#Ejercicio 4.8. Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños y el programa le debe
# decir a que signo corresponde.
#Nota:
#Aries: 21 de marzo al 20 de abril.
#Tauro: 21 de abril al 20 de mayo.
#Geminis: 21 de mayo al 21 de junio.
#Cancer: 22 de junio al 23 de julio.
#Leo: 24 de julio al 23 de agosto.
#Virgo: 24 de agosto al 23 de septiembre.
#Libra: 24 de septiembre al 22 de octubre.
#Escorpio: 23 de octubre al 22 de noviembre.
#Sagitario: 23 de noviembre al 21 de diciembre.
#Capricornio: 22 de diciembre al 20 de enero.
#Acuario: 21 de enero al 19 de febrero.
#Piscis: 20 de febrero al 20 de marzo.

def diasdelmes(month):
	mdays=0
	if month==Enero:
		mdays=31
	if month==Febrero:
		mdays=28
	if month==Marzo:
		mdays=31
	if month==Abril:
		mdays=30
	if month==Mayo:
		mdays=31
	if month==Junio:
		mdays=30
	if month==Julio:
		mdays=31
	if month==Agosto:
		mdays=31
	if month==Septiembre:
		mdays=30
	if month==Octubre:
		mdays=31
	if month==Noviembre:
		mdays=30
	if month==Diciembre:
		mdays=31
	return mdays

day = int(raw_input("Por favor ingrese el dia se su cumpleaños.\n"))
month = str(raw_input("Por favor ingrese el mes se su cumpleaños.\n"))

if month == "Enero":
    if day >= 1 and day <= 20:
        signo = "Capricornio"
    if day >= 21 and day < diasdelmes:
        signo = "Acuario"
if month == "Febrero":
    if day >= 1 and day <= 19:
        signo = "Acuario"
    if day >= 20 and day < diasdelmes:
        signo = "Piscis"
if month == "Marzo":
    if day >= 1 and day <= 20:
        signo = "Aries"
    if day >= 21 and day < diasdelmes:
        signo = "Geminis"
if month == "Abril":
    if day >= 1 and day <= 20:
        signo = "Aries"
    if day >= 21 and day < diasdelmes:
        signo = "Tauro"
if month == "Mayo":
    if day >= 1 and day <= 21:
        signo = "Tauro"
    if day >= 22 and day < diasdelmes:
        signo = "Geminis"
if month == "Junio":
    if day >= 1 and day <= 21:
        signo = "Geminis"
    if day >= 22 and day < diasdelmes:
        signo = "Cancer"
if month == "Julio":
    if day >= 1 and day <= 23:
        signo = "Cancer"
    if day >= 24 and day < diasdelmes:
        Leo = "Leo"
if month == "Agosto":
    if day >= 1 and day <= 23:
        signo = "Leo"
    if day >= 24 and day < diasdelmes:
        signo = "Virgo"
if month == "Septiembre":
    if day >= 1 and day <= 23:
        signo = "Virgo"
    if day >= 24 and day < diasdelmes:
        signo = "Libra"
if month == "Octubre":
    if day >= 1 and day <= 22:
        signo = "Libra"
    if day >= 23 and day < diasdelmes:
        signo = "Escorpio"
if month == "Noviembre":
    if day >= 1 and day <= 22:
        signo = "Escorpio"
    if day >= 23 and day < diasdelmes:
        signo = "Sagitario"
if month == "Diciembre":
    if day >= 1 and day <= 21:
        signo = "Sagitario"
    if day >= 22 and day < diasdelmes:
        signo = "Capricornio"

print "Tu signo es: " + signo