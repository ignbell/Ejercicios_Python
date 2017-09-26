#-*- coding:utf-8 -*-
num = int(input("Please provide an int number\n"))
for i in range(1, num + 1, 1):
	for j in range (1, num + 1, 1):
		if (i == j):
			print ( 1 )
		else:
			print ( 0 )	
