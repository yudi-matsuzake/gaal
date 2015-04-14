# -*- coding: utf-8 -*-

from matriz import *
import random

def identidade(n_linha=1, n_coluna=1):
	"""Cria e retorna uma matriz identidade"""
	M = Matriz(n_linha, n_coluna)

	for i in range(M.n_linha):
		for j in range(M.n_coluna):
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