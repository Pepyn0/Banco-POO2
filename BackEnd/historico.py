import datetime

class Historico(object):
	def __init__(self):
		self.abertura = datetime.datetime.today()
		self.trasacoes = []

	def imprime(self):
		print('abretura: {}'.format(self.abertura))
		print('transações: ')
		for t in self.trasacoes:
			print("-", t)
