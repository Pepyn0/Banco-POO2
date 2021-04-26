from historico import Historico


class Conta(object):
	def __init__(self, numero, cliente, saldo, limite=1000):
		self._numero = numero
		self._titular = cliente
		self._saldo = saldo
		self._limite = limite
		self._historico = Historico()

	@property
	def numero (self):
		return self._numero

	@numero.setter
	def numero(self,numero):
		self._numero = numero

	@property
	def titular (self):
		return self._titular

	@titular.setter
	def titular (self,titular):
		self._titular = titular

	@property
	def limite (self):
		return self._limite

	@limite.setter
	def limite (self,limite):
		self._limite = limite

	@property
	def historico (self):
		return self._historico
		
	@historico.setter
	def historico (self,historico):
		self._historico = historico

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
