class Cliente(object):
	def __init__(self, nome, sobrenome, cpf):
		self._nome = nome
		self._sobrenome = sobrenome
		self._cpf = cpf

	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, nome):
		self._nome = nome

	@property
	def sobrenome(self):
		return self._sobrenome

	@sobrenome.setter
	def sobrenome(self, sobrenome):
		self._sobrenome = sobrenome