from database.sql import cadastrar_historico, mostra_historico

import threading

class Historico(object):
	"""
		AUTHOR: Pablo Duarte da Silva e Vitoria Karolina Ferreira de Sousa

	"""

	def __init__(self):
		self.th = threading.Lock()

	def inserirHistorico(self, id_conta, transacao, cursor):
		"""
		DESCRIPTION: Função responsavél pela inserção de uma nova operação ao histórico

		"""
		self.th.acquire()
		cursor.execute(cadastrar_historico.format(id_conta, transacao))
		self.th.release()

	def mostrarHistorico(self, id_conta, cursor):
		"""
		DESCRIPTION: A função é responsável por listar as operações armazenadas por 
		determinado usuário no banco de dados.

		"""
		self.th.acquire()
		cursor.execute(mostra_historico.format(id_conta))
		self.th.release()
		listaHistorico = list(cursor)
		texto = ""
		for t in listaHistorico:
			texto += (t[0]) + '\n'
		return texto
