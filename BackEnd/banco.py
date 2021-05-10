from BackEnd.conta import Conta
class Banco(object):
	__slots__ = ["_contas"]

	def __init__(self):
		self._contas = []

	def buscar(self,cpf):
		for p in self._contas:
			if(p.titular.cpf == cpf):
				return p
		return None

	def cadastrar(self,conta: Conta):
		existe = self.buscar(conta.titular.cpf)
		if (existe):
			return False
		else:
			self._contas.append(conta)
			return True
