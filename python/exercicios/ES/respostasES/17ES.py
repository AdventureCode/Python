#!/usr/bin/env python
# -*- coding: utf-8 -*-

tamanho = int(input("Informe a área em metros quadrados: "))
litros = tamanho / 6


if(tamanho % 108 == 0):
	litros_lata = tamanho / 108
	litros_gal = litros / 3.6
else:
	litros_lata = int(tamanho / 108) + 1
	litros_gal = int(tamanho / 3.6) + 1

precoLatas = litros_lata * 80
precoGaloes = litros_gal * 25
print("Quantidade de litros necessarios: %.2f" %litros)
print("Total de latas: %.0f " %litros_lata)
print("Total de galões: %.0f " %litros_gal)
print("Preço das latas: R$%.2f " %precoLatas)
print("Preço dos galões: R$%.2f " %precoGaloes)
