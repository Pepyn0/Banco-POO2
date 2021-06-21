from database.sql import busca_cliente, cadastrar_cliente

class Cliente(object):

	@staticmethod
	def buscarCliente(cpf, cursor):
		"""
		DESCRIPTION: A função busca no banco de dados se aquele cliente está
		armazenado no banco de dados e retona o ID do mesmo.

		"""
		cursor.execute(busca_cliente.format(cpf))
		cliente = list(cursor)
		if(len(cliente) != 0):
			return cliente[0][0]
		return None

	@staticmethod
	def cadastrarPessoa(nome, sobrenome, cpf, cursor):
		"""
		DESCRIPTION: A função é responsavel pelo cadastro e armazenamento do
		ID do cliente no banco de dados.

		"""
		if(Cliente.buscarCliente(cpf, cursor) == None):
			cursor.execute(cadastrar_cliente.format(nome, sobrenome, cpf))
			return True
		return False
