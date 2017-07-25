#!/usr/bin/python
#-*- coding:utf-8-*-

# Método pop, remove, sort, função len, map e etc.

# Criar lista vazia
L = []

# Criar lista 
L = [0, 1, 2, 3, 4]

#L = ["a", "b", "c", "d"]

#L = ["a", ["b", "c", "d"]]

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

# Ordena os elementos da lista
L.sort()

# Reverter a lista
L.reverse()

# Remove a primeira ocorrência do item
L.remove(2)

# Remove item na posição de índice especificada
L.pop(2)

# Remove item na posição de índice especificada
del L[2]

# Remove os itens da posição i até j-1
del L[4:6]

# Atribuir valor à posição i: L[i] = valor
L[2] = 100

# Atribuir valores ao intervalo: L[i:j] = [x1, x2, x3]
L[1:3] = [200, 2, 130]

# Criar a lista L2 com os elementos de L incrementados: L2 = [x + 1 for x in L]
L2 = [2 + 1 for x in L]

# Retorna o tamanho da lista
len(L)

# Retorna os elementos da lista
list(L)

# Aplica a função f a cada um dos elementos da lista; Para ver o resultado, combine com list()
map(f, lista)
