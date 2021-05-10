import datetime

class Historico(object):
	def __init__(self):
		self.abertura = datetime.datetime.today()
		self.trasacoes = []

	def imprime(self):
		texto = ""
		texto+= 'abretura: {}\n'.format(self.abertura)
		texto+= 'transações:\n'
		for t in self.trasacoes:
			texto+= t+'\n'
		return texto

