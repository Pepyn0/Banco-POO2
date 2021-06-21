from datetime import datetime
from historico import Historico
from cliente import Cliente

from database.sql import busca_conta, cadastrar_conta, autentica_senha, busca_valores, atualizar_saldo


class Conta(object):

	@property
	def historico (self):
		return self._historico
		
	@historico.setter
	def historico (self,historico):
		self._historico = historico

	@staticmethod
	def depositar(id_conta, valor, cursor):
		cursor.execute(busca_valores.format(id_conta))
		saldo = list(cursor)[0][1]
		saldo += valor
		cursor.execute(atualizar_saldo.format(saldo, id_conta))
		Historico.inserirHistorico(id_conta, "Deposito de {}".format(valor), cursor)

	@staticmethod
	def saca(id_conta, valor, cursor):
		cursor.execute(busca_valores.format(id_conta))
		lista = list(cursor)
		saldo = lista[0][1]
		limite = lista[0][2]

		if((saldo + limite) < valor):
			return False
		else:
			saldo -= valor
			cursor.execute(atualizar_saldo.format(saldo, id_conta))
			Historico.inserirHistorico(id_conta, "Saque de {}".format(valor), cursor)
			return True

	@staticmethod
	def transferirConta(id_conta, id_conta_destino, valor, cursor):
		retirou = Conta.saca(id_conta, valor, cursor)
		if(retirou):
			Conta.depositar(id_conta_destino, valor, cursor)
			nomeDestino = Conta.buscarValores(id_conta_destino, cursor)
			Historico.inserirHistorico(id_conta, "Tranferencia de {} para a conta {}".format(valor, nomeDestino[0][0]), cursor)
			return True
		else:
			return False

	@staticmethod
	def buscarConta(cpf, cursor):
		cursor.execute(busca_conta.format(cpf))
		conta = list(cursor)
		if(len(conta) != 0):
			return conta[0][0]
		return None

	@staticmethod
	def cadastrarConta(cpf, senha, cursor):
		if(Conta.buscarConta(cpf, cursor) == None):
			id_cliente = Cliente.buscarCliente(cpf, cursor)
			cursor.execute(cadastrar_conta.format(id_cliente, 0, senha, 1000))
			id_conta = Conta.buscarConta(cpf, cursor)
			Historico.inserirHistorico(id_conta, "Conta aberta em {}".format(str(datetime.now().strftime('%d/%m/%Y %H:%M'))), cursor)
			return True
		return False

	@staticmethod
	def autenticaSenha(id_conta, senha, cursor):
		cursor.execute(autentica_senha.format(id_conta, senha))
		conta = list(cursor)
		if(len(conta) != 0):
			return True
		return False

	@staticmethod
	def buscarValores(id_conta, cursor):
		cursor.execute(busca_valores.format(id_conta))
		conta = list(cursor)
		return conta
