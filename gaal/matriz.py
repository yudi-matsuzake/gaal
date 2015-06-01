# -*- coding: utf-8 -*-

#----------Operações-----------
#generico
def _operacao(A, B, op):
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
def _adicao(A, B, op):
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
def _multiplicacao(A, B):
	if A.n_coluna != B.n_linha:
		return None
	M = Matriz(A.n_linha, B.n_coluna)

	for i in range(A.n_linha):
		for j in range(B.n_coluna):
			for k in range(A.n_coluna):
				M[i][j] += A[i][k]*B[k][j]
	
	return M


#LAPLACE
#def _la_range(i, k):
#	"""
#	Criar uma lista de i até n, sem o j. Essa função é pra evitar uma comparação em toda iteração
#	"""
#
#	L = []
#	for k in range(M.n_coluna):
#		if k != j
#			L.append(k)
#	return L
#
#def _la_place(M, i=None, j=0):
#	"""Função auxiliar para o cálculo do determinante"""
#
#	if i == None:
#		i = range(M.n_coluna)
#	
#	if len(i) <=1 :
#		return i[0]
#	
#	det=0
#
#	for k in i:
#		mul = 1 if ((k + j)%2) == 0 else -1
#		det += M[k][j] * mul * _la_place(M, _la_range(M, i, k), j+1)



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
		"""
		Imprime a matriz de um jeito bonito :3
		"""
		maiortamanho_coluna = [0]*self.n_coluna
		
		#cria uma lista com os maiores tamanho de cada coluna, para depois tabular certinho
		for i in self.matriz:
			for j in range(len(i)):
				cel_size = len(str(i[j]))
				if cel_size > maiortamanho_coluna[j]:
					maiortamanho_coluna[j] = cel_size

		string_format = ""
		
		#cria strings de formataço de cada coluna utilizando informações da iteração anterior
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
			M = _operacao(self, other, '+')
		else:
			if (self.n_linha == other.n_linha) and (self.n_coluna == other.n_coluna):
				M = _adicao(self, other, '+')

		return M

	#SUBTRAÇÃO
	def __sub__(self, other):
		"""Subtrai duas matrizes Amxn, Bmxn. Ou uma matriz e uma constante."""
		M = None
		if (not isinstance(other, Matriz)) :
			M = _operacao(self, other, '-')
		else:
			if (self.n_linha == other.n_linha) and (self.n_coluna == other.n_coluna):
				M = _adicao(self, other, '-')

		return M

	#NEGAÇÃO
	def __neg__(self):
		return self*(-1)

	#MULTIPLICAÇÃO
	def __mul__(self, other):
		"""Multiplica duas matrizes Aaxb Bbxc e retorna uma matriz Caxc"""
		M = None
		if (not isinstance(other, Matriz)):
			M = _operacao(self, other, '*')
		else:
			M = _multiplicacao(self, other)

		return M
	

	#COMPARAÇÃO ==
	def __eq__(self, other):
		"""Compara duas matrizes"""
		#Estou comparando matriz com matriz?
		if (not isinstance(other, Matriz)):
			#Se a constante for zero, a verificar se a matriz é nula
			if other == 0:
				for i in self:
					for j in i:
						if j != 0:
							return False

				return True
			
			return False
		
		#Tem a mesma ordem?
		if (self.n_linha == other.n_linha) and (self.n_coluna == other.n_coluna):
			for i in range(self.n_linha):
				for j in range(self.n_coluna):
					if self[i][j] != other[i][j]:
						return False

			return True
		return False
	
	def __ne__(self, other):
		return not (self == other)
	#Iterator
	def __iter__(self):
		"""Retorna um iterador da lista da matriz"""
		return self.matriz.__iter__()
	
	def transposta(self):
		"""Retorna a matriz transposta de M"""
		M = Matriz(self.n_coluna, self.n_linha)
		for i in range(M.n_linha):
			for j in range(M.n_coluna):
				M[i][j] = self[j][i]
		return M
	
	#É quadrada?
	def quadrada(self):
		"""Retorna true se a matriz é quadrada e false, se não"""
		return self.n_linha == self.n_coluna
	
	def matriz_de_cofator(self, i, j):
		"""Retorna a matriz de cofator i, j"""
		if (i == None or j == None) or (self.n_linha <= 1 and self.n_coluna <= 1):
			return None

		M = Matriz(self.n_coluna - 1, self.n_linha - 1);
		
		# Tira a linha i
		if i == 0:
			M.matriz = self.matriz[1:]
		elif i >= self.n_linha-1:
			M.matriz = self.matriz[:self.n_linha-1]
		else:
			M.matriz = self.matriz[:i] + self.matriz[i+1:]

		# Tira a coluna j
		for x in range(M.n_linha):
			if j == 0:
				M.matriz[x] = M.matriz[x][1:]
			elif j >= self.n_coluna-1:
				M.matriz[x] = M.matriz[x][:M.n_coluna]
			else:
				M.matriz[x] = M.matriz[x][:j] + M.matriz[x][j+1:]
		
		return M

	#DETERMINANTE
	def det(self):
		"""
		Retorna o inteiro determinante associado a matriz
		Método de laplace
		"""
		if not self.quadrada() :
			return False

		return _la_place(self)
