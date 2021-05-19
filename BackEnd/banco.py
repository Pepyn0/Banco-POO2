from conta import Conta
class Banco(object):

	_totalContas = 0
	__slots__ = ["_contas"]

	def __init__(self):
		self._contas = []

	@staticmethod
	def getTotalContas():
		return Banco._totalContas

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
			Banco._totalContas += 1
			return True
