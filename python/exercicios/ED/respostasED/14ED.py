#!/usr/bin/python
#-*- coding: utf-8 -*-

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))

media = (n1 + n2) / 2

if(media > 9.0 and media <= 10.0):
	conseito = 'A'
	status = "Aprovado"
elif(media > 7.5 and media <= 9.0):
	conseito = 'B'
	status = "Aprovado"
elif(media > 6.0 and media <= 7.5):
	conseito = 'C'
	status = "Aprovado"
elif(media > 4.0 and media <= 6.0):
	conseito = 'D'
	status = "Reprovado"
elif(media > 0 and media <= 5.0):
	conseito = 'E'
	status = "Reprovado"

print("|Nota1\t|Nota2\t|Media\t|Status\t\t|Conseito|")
print("|%.2f \t|%.2f\t|%.2f\t|%s\t|%c\t |"%(n1, n2, media, status, conseito))
