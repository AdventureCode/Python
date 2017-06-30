#!/usr/bin/python
#-*- coding: utf-8 -*-

a = int(input("Informe um numero: "))
b = int(input("Informe um numero: "))
c = int(input("Informe um numero: "))

if(a > b and a > c):
	if(b > c):
		meio = b
		menor = c
	else:
		meio = c
		menor = b
	print(a, meio, menor)
elif(b > a and b > c):
	if(a > c):
		meio = a
		menor = c
	else:
		meio = c
		menor = a
	print(b, meio, menor)
else:
	if(a > b):
		meio = a
		menor = b
	else:
		meio = b
		menor = a;
	print(c, meio, menor)
