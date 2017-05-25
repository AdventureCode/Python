#!/usr/bin/python
#-*- coding: utf-8 -*-
arquivo = float(input("Informe o tamanho do arquivo em MB: "))
velocidade = float(input("Informe a velocidade do link de internet em Mbps: "))

resultado = arquivo / (velocidade * 60)

print("O tempo aproximado de download do arquivo é de %.2f minutos." %resultado)

