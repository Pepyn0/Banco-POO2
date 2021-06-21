from database.sql import cadastrar_historico, mostra_historico

class Historico(object):

	@staticmethod
	def inserirHistorico(id_conta, transacao, cursor):
		cursor.execute(cadastrar_historico.format(id_conta, transacao))

	@staticmethod
	def mostrarHistorico(id_conta, cursor):
		cursor.execute(mostra_historico.format(id_conta))
		listaHistorico = list(cursor)
		texto = ""
		for t in listaHistorico:
			texto += (t[0]) + '\n'
		return texto
