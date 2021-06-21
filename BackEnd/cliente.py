from database.sql import busca_cliente, cadastrar_cliente

class Cliente(object):

	@staticmethod
	def buscarCliente(cpf, cursor):
		cursor.execute(busca_cliente.format(cpf))
		cliente = list(cursor)
		if(len(cliente) != 0):
			return cliente[0][0]
		return None

	@staticmethod
	def cadastrarPessoa(nome, sobrenome, cpf, cursor):
		if(Cliente.buscarCliente(cpf, cursor) == None):
			cursor.execute(cadastrar_cliente.format(nome, sobrenome, cpf))
			return True
		return False
