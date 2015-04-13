# -*- coding: latin-1 -*-
class Matriz:
	"""Representa a estrutura matemática de uma matriz"""
	def __init__(self, n_linha=0, n_coluna=0):
		self.n_linhas=n_linha
		self.n_colunas=n_coluna
		self.matriz=[[0]*n_coluna]*n_linha

	def ordem(self):
		return (self.n_linha, self.n_coluna)
