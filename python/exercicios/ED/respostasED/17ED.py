#!/usr/bin/python
#-*- coding: utf-8 -*-

# Para ser bissexto o ano deve ser divisivel por 4 ou por 400 e não pode ser divisivel por 100

ano = int(input("Informe um ano: "))

if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
	print("%d é bissexto!" %ano)
else:
	print("%d não é bissexto!" %ano)
