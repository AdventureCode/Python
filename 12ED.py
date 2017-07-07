#!/usr/bin/python
#-*- coding: utf-8 -*-

valorHora = float(input("Informe o valor da hora de trabalho: "))
horasTrabalho = int(input("Informe a quantidade mensal de horas trabalhadas: "))

salarioBruto = valorHora * horasTrabalho

INSS = 10
SINDICATO = 3
FGTS = 11

descontoINSS = salarioBruto * (INSS / 100)
descontoFGTS = salarioBruto * (FGTS / 100)
descontoSINDICATO = salarioBruto * (SINDICATO / 100)

if(salarioBruto <= 900):
	IR = 0
	descontoIR = salarioBruto * (IR / 100)
elif(salarioBruto <= 1500):
	IR = 5
	descontoIR = salarioBruto * (IR / 100)
elif(salarioBruto <= 2500):
	IR = 10
	descontoIR = salarioBruto * (IR / 100)
else:
	IR = 20
	descontoIR = salarioBruto * IR

descontoTotal = descontoIR + descontoINSS + descontoSINDICATO
salarioLiquido = salarioBruto - descontoTotal

print("Salário Bruto: (%d * %.2f)		: R$ %.2f" %(valorHora, horasTrabalho, salarioBruto))
print("(-) IR (%.2d)				: R$ %.2f" %(IR, descontoIR))
print("(-) INSS (%.2d)				: R$ %.2f" %(INSS, descontoINSS))
print("FGTS (%.2d)				: R$ %.2f" %(FGTS, descontoFGTS))
print("Total de descontos			: R$ %.2f" %descontoTotal)
print("Salário Liquido				: R$ %.2f" %salarioLiquido)
