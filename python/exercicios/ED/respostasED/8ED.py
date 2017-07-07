#!/usr/bin/python
#-*- coding: utf-8 -*-

a = float(input("Informe o preço do produto: "))
b = float(input("Informe o preço do produto: "))
c = float(input("Informe o preço do produto: "))

if(a > b and a > c):
	if(b > c):
		menor = c
	else:
		menor = b
	print("Compre o produto que custa R$%.2f" %menor)
elif(b > a and b > c):
	if(a > c):
		menor = c
	else:
		menor = a
	print("Compre o produto que custa R$%.2f" %menor)
else:
	if(a > b):
		menor = b
	else:
		menor = a;
	print("Compre o produto que custa R$%.2f" %menor)
