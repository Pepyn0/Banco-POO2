from database.sql import busca_cliente, cadastrar_cliente

import threading
class Cliente(object):
	"""
		AUTHOR: Pablo Duarte da Silva e Vitoria Karolina Ferreira de Sousa

	"""

	def __init__(self):
		self.th = threading.Lock()

	def buscarCliente(self, cpf, cursor):
		"""
		DESCRIPTION: A função busca no banco de dados se aquele cliente está
		armazenado no banco de dados e retona o ID do mesmo.

		"""
		self.th.acquire()
		cursor.execute(busca_cliente.format(cpf))
		self.th.release()
		cliente = list(cursor)
		if(len(cliente) != 0):
			return cliente[0][0]
		return None

	def cadastrarPessoa(self, nome, sobrenome, cpf, cursor):
		"""
		DESCRIPTION: A função é responsavel pelo cadastro e armazenamento do
		ID do cliente no banco de dados.

		"""
		if(self.buscarCliente(cpf, cursor) == None):
			self.th.acquire()
			cursor.execute(cadastrar_cliente.format(nome, sobrenome, cpf))
			self.th.release()
			return True
		return False
