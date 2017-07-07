#!/usr/bin/python
#-*- coding: utf-8 -*-

a = int(input("Informe um numero: "))
b = int(input("Informe um numero: "))
c = int(input("Informe um numero: "))

if(a > b and a > c):
	print(a)
elif(b > a and b > c):
	print(b)
else:
	print(c)
