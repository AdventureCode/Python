#!/usr/bin/env python
# -*- coding: utf-8 -*-

tamanho = int(input("Informe a área em metros quadrados: "))
litros = tamanho / 3

if(tamanho % 54 == 0):
	latas = tamanho / 54
else:
	latas = int(tamanho / 54) + 1

preco = latas * 80
print("%d Latas" %latas)
print("R$ %.2f" %preco)
