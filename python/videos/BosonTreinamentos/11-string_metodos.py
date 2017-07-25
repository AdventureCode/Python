#!/usr/bin/python
#-*- coding: utf-8 -*-

# Métodos em string
s = "pizza"

# Enconstra a posição de uma substring
print(s.find("iz"))

# Substitui ocorrências de uma substring por outra
print(s.replace("zza", "nhão"))

# Conversão para maiúsculas
print(s.upper())

# Conversão para minúsculas
print(s.lower())

# Teste de conteúdo é alfabética
print(s.isalpha())

# Teste de conteúdo é alfanumérica
print(s.isalnum())

# Retorna uma cópia da string com caracteres à esquerda removidos. Se não  forem
# especificados, elimina espaçoes em branco
# lstrip elimina o argumento a esquerda rstrip elimina o argumento a direita e 
# somente a função strip elimina os dois lados ao mesmo tempo
print(s.lstrip())

# Retorna a string com o primeiro caractere em maiúsculo
print(s.capitalize())

s = "a, b, c, d, e, f, g, h"
# Retorna uma lista de itens delimitada pelo caractere especificado.
print(s.split(","))





