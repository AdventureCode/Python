#!/usr/bin/python
#-*- coding: utf-8 -*-

a = int(input("Informe um numero: "))
b = int(input("Informe um numero: "))
c = int(input("Informe um numero: "))

if(a > b and a > c):
	if(b > c):
		menor = c
	else:
		menor = b
	print(a, menor)
elif(b > a and b > c):
	if(a > c):
		menor = c
	else:
		menor = a
	print(b, menor)
else:
	if(a > b):
		menor = b
	else:
		menor = a;
	print(c, menor)
