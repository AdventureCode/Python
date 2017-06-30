#!/usr/bin/python
#-*- coding: utf-8 -*-

salario = float(input("Informe o salario do trabalhador: "))

if(salario <= 280):
	percentual = 20
	aumento = salario * (percentual / 100)
	novoSalario = salario + aumento
elif(salario > 280 and salario <= 700):
	percentual = 15
	aumento = salario * (percentual / 100)
	novoSalario = salario + aumento
elif(salario > 700 and salario <= 1500):
	percentual = 10
	aumento = salario * (percentual / 100)
	novoSalario = salario + aumento
else:
	percentual = 5
	aumento = salario * (percentual / 100)
	novoSalario = salario + aumento

print("Salário anterior: %.2f \nAumento : %d%% \nValor do aumento : %.2f \nNovo salário : %.2f" %(salario ,percentual ,aumento ,novoSalario))
