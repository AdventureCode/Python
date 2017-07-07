#!/usr/bin/python
#-*- coding: utf-8 -*-

a = float(input("Informe o lado do triangulo: "))
b = float(input("Informe o lado do triangulo: "))
c = float(input("Informe o lado do triangulo: "))


if(a + b < c):
	print("Essas medidas não formam um triangulo!")
	exit()
	
if(a == b and b == c):
	print("É um triangulo Equilátero!")
elif(a == b or a == c or b == c):
	print("É um triangulo Isóceles!")
else:
	print("É um triangulo escaleno!")
