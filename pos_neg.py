#!/usr/bin/env python3

numero = 50

if numero < 0:
	message = "negativo"
	print (numero, message) 
elif numero == 0:
	print (numero, 'o numero é zero')
else: 
	message = "positivo"
	print (numero, message) 
	if numero < 50:
		if (numero % 2) == 0:
			print (numero, 'é positivo, menor que 50 e par') 
		else:
			print (numero, 'é positivo, menor que 50 e impar')
	elif numero == 50:
		print ('o número é 50') 
	else:
		if (numero % 3) == 0:
			print (numero, 'é maior que 50 e divisível por 3')
		else:
			print (numero, 'é maior que 50 e não é divisível por 3')


