#-*- coding:utf-8 -*-

def calcular_hora(num):
	h = 0
	m = 0
	s = 0
	h = int(num/3600)
	m=int((num-(h*3600))/60)
	s=int(num-(h*3600)-(m*60))
	#if ( m >= 59):
	#	m = int(m / 60)
	#	s = int(m % 60)
	#	h = int(h + ((m / 60)))
	#if ( s >= 59):
	#	s = int(m % 60)
	#	m = int(m + (s/60))
	print ("La hora es= "+str(h)+":"+str(m)+":"+str(s))

# if (num)
# minutos=(num / 60)
# segundos=(num % 60)
# if (minutos > 60):
# minutos=(min%60)
# if ((min%60) > 60)
# hora=(min/60)-1
# minutos=(min%60)
# else
# hora=(min/60)
# minutos=(min%60)

#segundos=3600
segundos = int(input("Please insert seconds "\n))
calcular_hora(segundos)
