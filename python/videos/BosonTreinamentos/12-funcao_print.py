#!/usr/bin/python
# -*-coding: utf-8
# Função Print(), formatação de strings e método str.format()

a = "pizza"
b = 30

print(a)
print(b)

print("Vou pedir uma %s" %a)
print("Ela custa %d reais" % b)
print("a %s custa %d reais" %(a, b))

#################################
# Tipos para conversão			#
#################################
#	d	Decimal inteiro			#
#	f	Decimal ponto-flutuante	#
#	o 	octal					#
#	x	Hexadecimal(min)		#
#	X	Hexadecimal(mai)		#
#	c	Um caractere			#
#	s	string					#
#################################

# Método str.format
# Realiza uma operação de dormatação de string
# 	A string onde o método é chamado pode conter texto literal ou campos 
# de substituição delimitados por chaves.
#	Esses campos podem conter um índice numérico de um argumento posicional

print("A {0} custa {1} reais".format(a,b))
print("Gosto de {0}, mas {1} reais está caro pra uma {0}!".format(a, b))



