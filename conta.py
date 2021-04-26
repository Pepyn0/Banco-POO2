from historico import Historico


class Conta(object):
	def __init__(self, numero, cliente, saldo, limite=1000):
		self.numero = numero
		self.titular = cliente
		self.saldo = saldo
		self.limite = limite
		self.historico = Historico()

	def depositar(self, valor):
		self.saldo += valor
		self.historico.trasacoes.append("deposito de {}".format(valor))

	def saca(self, valor):
		if (self.saldo < valor):
			return False
		else:
			self.saldo -= valor
			self.historico.trasacoes.append("saque de {}".format(valor))
			return True

	def extrato(self):
		print("numero: {}\nsaldo: {}".format(self.numero, self.saldo))
		self.historico.trasacoes.append("extrato - saldo de {}".format(self.saldo))

	def transfere(self, destino, valor):
		retirou = self.saca(valor)
		if(retirou):
			destino.depositar(valor)
			self.historico.trasacoes.append("tranferencia de {} para a conta {}".format(valor, destino.numero))
			return True
		else:
			return False
