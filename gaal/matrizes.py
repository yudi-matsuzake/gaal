# -*- coding: utf-8 -*-

from matriz import *
import random

#----------Auxiliares----------
def num(x):
	"""Converte x para um número. Tenta pra int, se não der, float"""
	try:
		return int(x)
	except ValueError:
		return float(x)

#------------------------------
def identidade(ordem=1):
	"""Cria e retorna uma matriz identidade de ordem n (default 1) """
	M = Matriz(ordem, ordem)

	for i in range(ordem):
		for j in range(ordem):
			if i == j:
				M[i][j] = 1
			else:
				M[i][j] = 0

	return M

def aleatoria(n_linha=None, n_coluna=None, a=-100, b=100):
	"""
	Cria e retorna uma matriz Amxn aleatória com valores de de -100 (argumento a) até 100 (argumento b) por padrão.
	n_linha e n_coluna também serão aleatórios entre 1 e 100 se não forem dados.
	"""
	if n_linha == None:
		n_linha = random.randint(1, 100)
	if n_coluna == None:
		n_coluna = random.randint(1, 100)
	
	M = Matriz(n_linha, n_coluna)

	for i in range(n_linha):
		for j in range(n_coluna):
			M[i][j] = random.randint(a, b)

	return M


#drom stdin

def _build(L, n_coluna):
	n_linha = len(L)
	M = Matriz(n_linha, n_coluna, valor_padrao=None)
	for i in range(M.n_linha):
		for j in range(M.n_coluna):
			M[i][j] = L[i][j]
	return M

def pela_entrada_padrao():
	"""
	Lê a entrada padrão até o EOF e a transforma em uma matriz.
	Amxn=
	a00 .. a0n
	..  ..
	am0 .. amn
	"""
	n_largura=None
	n_coluna=None
	L = []
	try:
		#Lê da entrada padrão até dizer chega
			#ctrl+d (EOF) ou entrada vazia
		while True :
			#Pega a entrada e transforma em números
			l = ([ num(i) for i in str(raw_input()).split() ])

			#Se nenhum valor foi dado pra coluna, dê o tamanho da lista
			if n_coluna == None:
				n_coluna = len(l)

			#Se a entrada for nada
			if len(l) <= 0:
				return _build(L, n_coluna)

			#O número de coluna deve ser igual para todas as linhas
			if n_coluna != len(l):
				return None

			L.append(l)
	except EOFError:
		#EOF (ctrl+d)
		return _build(L, n_coluna)
		
