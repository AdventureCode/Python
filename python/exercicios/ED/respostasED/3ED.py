#!/usr/bin/python
#-*- coding: utf-8 -*-

sexo = input("F - Feminino; M - Masculino: ")

sexo = sexo.upper()

if(sexo == 'F'):
	print("Feminino")
elif(sexo == 'M'):
	print("Masculino")
else:
	print("Sexo invalido")
