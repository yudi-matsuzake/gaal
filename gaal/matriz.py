# -*- coding: utf-8 -*-

#----------Operações-----------
#generico
def operacao(A, B, op):
	M = Matriz(A.n_linha, A.n_coluna)

	func = None

	if 		op == '+':
		func = lambda x,y: x+y
	elif 	op == '-':
		func = lambda x,y: x-y
	elif 	op == '*':
		func = lambda x,y: x*y

	for i in range (A.n_linha):
		for j in range(A.n_coluna):
			M[i][j] = func(A.matriz[i][j], B)

	return M
	
#Adição
def adicao(A, B, op):
	func = None
	if op == '+':
		func = lambda x,y : x+y
	elif op == '-':
		func = lambda x,y : x-y

	M = Matriz(A.n_linha, A.n_coluna)

	for i in range(A.n_linha):
		for j in range(A.n_coluna):
			M[i][j] = func(A[i][j], B[i][j])

	return M

#Multiplicação
def multiplicacao(A, B):
	pass	

#---Estruturas---#
class Matriz:
	"""Representa a estrutura matemática de uma matriz"""
	def __init__(self, n_linha=0, n_coluna=0, valor_padrao=0):
		self.n_linha=n_linha
		self.n_coluna=n_coluna
		self.matriz=[[ valor_padrao for i in range(n_coluna) ] for j in range(n_linha)]

	def ordem(self):
		"""
		Retorna uma tupla com o número de linha e o número de colunas
		Ou seja, dado uma Matriz Amxn, será retornado uma tupla (m,n)
		"""
		return (self.n_linha, self.n_coluna)

	def __str__(self):
		maiortamanho_coluna = [0]*self.n_coluna

		for i in self.matriz:
			for j in range(len(i)):
				cel_size = len(str(i[j]))
				if cel_size > maiortamanho_coluna[j]:
					maiortamanho_coluna[j] = cel_size

		string_format = ""

		for i in range(self.n_coluna):
			string_format = string_format + ( '{' + str(i) + ':' + str(maiortamanho_coluna[i]) + 'd' + '} ' )

		if self.n_linha == 1:
			primeiro 	= '['
			ultimo		= ']'
		else:
			primeiro	= '⎡'
			ultimo		= '⎤'

		m = ""
		
		for i in range(self.n_linha):
			formato = primeiro + string_format + ultimo
			m += ( formato.format(*self.matriz[i]) + '\n' );

			if (i+2) >= self.n_linha:
				primeiro	= '⎣'
				ultimo		= '⎦'
			else:
				primeiro	= '⎢'
				ultimo		= '⎥'

		m = m + str(self.n_linha) + 'x' + str(self.n_coluna)
		return m

	def __getitem__(self, key):
		return self.matriz[key]


	def __repr__(self):
		return str(self)

	#ADIÇÃO
	def __add__(self, other):
		"""Soma duas matrizes Amxn, Bmxn. Ou uma matriz e uma constante."""
		M = None
		if (not isinstance(other, Matriz)) :
			M = operacao(self, other, '+')
		else:
			if (self.n_linha == other.n_linha) and (self.n_coluna == other.n_coluna):
				M = adicao(self, other, '+')

		return M

	#SUBTRAÇÃO
	def __sub__(self, other):
		"""Subtrai duas matrizes Amxn, Bmxn. Ou uma matriz e uma constante."""
		M = None
		if (not isinstance(other, Matriz)) :
			M = operacao(self, other, '-')
		else:
			if (self.n_linha == other.n_linha) and (self.n_coluna == other.n_coluna):
				M = adicao(self, other, '-')

		return M


	#MULTIPLICAÇÃO
	def __mul__(self, other):
		"""Multiplica duas matrizes Aaxb Bbxc e retorna uma matriz Caxc"""
		M = None
		if (not isinstance(other, Matriz)):
			M = operacao(self, other, '*')
		else:
			if (self.n_linha == other.n_linha) and (self.n_coluna == other.n_coluna):
				M = multiplicacao(self, other)

		return M
