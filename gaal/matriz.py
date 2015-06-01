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

def _la_place(M):
	"""Função auxiliar para o cálculo do determinante"""
	if M.n_linha == 1 and M.n_coluna == 1:
		return M[0][0]
	
	if M.n_linha == 2 and M.n_coluna == 2:
		return M[0][0] * M[1][1] - M[0][1] * M[1][0]
	
	det = 0
	for i in range(M.n_coluna):
		det += M.cofator(0,i)

	return det

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
	
	def submatriz(self, i, j):
		"""Retorna a submatriz sem a linha i e a coluna j"""
		if (i == None or j == None) or (self.n_linha <= 1 and self.n_coluna <= 1):
			return None

		M = Matriz(self.n_linha - 1, self.n_coluna - 1);
		
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
	
	def cofator(self, i, j):
		"""Retorna o cofator i j"""
		#i+j e par?
		if i+j%2 == 0:
			aij = self[i][j]
		else:
			aij = self[i][j]*(-1)

		aij *= self.submatriz(i, j).det()

		return aij


	def matriz_de_cofatores(self):
		"""Retorna a matriz de cofatores"""
		pass

	#adjunta
	def matriz_adjunta(self):
		"""Retorna matriz adjunta"""
		pass
		

	#DETERMINANTE
	def det(self):
		"""
		Retorna o inteiro determinante associado a matriz
		Método de laplace
		"""
		if not self.quadrada() :
			return False

		return _la_place(self)
