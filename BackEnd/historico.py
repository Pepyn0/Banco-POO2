from database.sql import cadastrar_historico, mostra_historico

class Historico(object):
	"""
		AUTHOR: Pablo Duarte da Silva e Vitoria Karolina Ferreira de Sousa

	"""

	@staticmethod
	def inserirHistorico(id_conta, transacao, cursor):
		"""
		DESCRIPTION: Função responsavél pela inserção de uma nova operação ao histórico

		"""
		cursor.execute(cadastrar_historico.format(id_conta, transacao))

	@staticmethod
	def mostrarHistorico(id_conta, cursor):
		"""
		DESCRIPTION: A função é responsável por listar as operações armazenadas por 
		determinado usuário no banco de dados.

		"""
		cursor.execute(mostra_historico.format(id_conta))
		listaHistorico = list(cursor)
		texto = ""
		for t in listaHistorico:
			texto += (t[0]) + '\n'
		return texto
