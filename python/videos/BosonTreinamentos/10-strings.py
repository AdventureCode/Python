#!/usr/bin/python
#-*- coding: utf-8 -*-
# Concatenação, repetição, imutabilidade ea função len()

s = "pizza"

# informa o tamanho da string
x = len(s)
print(x)

print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# Função Slicing "fatiamento"

# Retorna todos os elementos da string
print(s[:])

print(s[1:3])

# Conta da direita para a esquerda é ciclico
print(s[-2])

# Concatenar
print(s + " portuguesa")

# Repetição
print(s * 6)
# Colocando espaço em branco
print((s + " ") * 6)

# Imutabilidade não pode ser substituida para isso existe uma função 
s[0] = "b"


