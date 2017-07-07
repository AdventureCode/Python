#!/usr/bin/python
#-*- coding: utf-8 -*-

# Para teste
# delta < 0, a = 1, b = -4 e c = 5
# delta = 0, a = 4, b = -4 e c = 1
# delta > 0, a = 1, b = -5 e c = 6

from math import sqrt # Módulo para calcular a raiz quadrada

print("Equação do segundo grau! ax^2 + bx + c")

a = int(input("Informe o valor de A: "))

if(a == 0):
	print("Não é uma equacão do segundo grau!")
	exit()

b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))

# Calculando Delta
delta = b**2 - 4 * a * c

# Para delta negativo ele não possui raizes reais
if(delta < 0):
	print("A equação não tem raizes reais!")
	exit()

# Para delta igual a zero ele possui uma raiz real
elif(delta == 0):
	print("A equação tem apenas uma raiz!")
	x = (-b + sqrt(delta)) / (2 * a)
	print("A raiz da equação é %d" %x)

# Para delta maior que zero, ele possui duas raizes reais
else:
	x1 = (-b + sqrt(delta)) / (2 * a)
	x2 = (-b - sqrt(delta)) / (2 * a)
	print("As raizes da equação é x¹ = %d, x² = %d " %(x1, x2))



