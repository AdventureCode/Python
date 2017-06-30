#!/usr/bin/python
#-*- coding: utf-8 -*-

n1 = float(input("Informe a primeira nota do aluno: "))
n2 = float(input("Informe a segunda nota do aluno: "))

media = (n1 + n2) / 2

if(media == 10):
	print("Aprovado com destinção")
elif(media >= 7):
	print("Aprovado")
else:
	print("Reprovado")

