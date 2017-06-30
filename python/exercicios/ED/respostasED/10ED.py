#!/usr/bin/python
#-*- coding: utf-8 -*-

turno = input("Informe o turno que você estuda: M-matutino ou V-Vespertino ou N- Noturno.")

turno = turno.upper()

if(turno == 'M'):
	print("Bom dia!")
elif(turno == 'V'):
	print("Boa Tarde!")
elif(turno == 'N'):
	print("Boa noite!")
else:
	print("Valor Inválido!")

