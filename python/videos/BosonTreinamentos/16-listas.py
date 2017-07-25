#!/usr/bin/python
#-*- coding:utf-8-*-

# Criação, inserção e alteração de itens. Método append e outros

# Criar lista vazia
L = []

# Criar lista 
L = [0, 1, 2, 3, 4]

L = ["a", "b", "c", "d"]

L = ["a", ["b", "c", "d"]]

# concatenar lista
L2 = [5, 6, 7, 8]
list(L + L2)

# repetir
list(L2 * 5)

# Verificar existência
2 in L
7 in L

# iteração
for x in L:
	print(x)

# Acrescentar itens
L.append(9)
list(L)

# Acrescentar itens na posição L.insert(pos, x)
L.insert(3, 12)

# Busca de posição por valor L.index(pos, x)
L.index(12)
# Contagem de ocorrências de x
L.count(2)
