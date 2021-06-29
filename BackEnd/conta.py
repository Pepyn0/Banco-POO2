from datetime import datetime
from historico import Historico
from cliente import Cliente

import threading

from database.sql import busca_conta, cadastrar_conta, autentica_senha, busca_valores, atualizar_saldo


class Conta(object):
	"""
		AUTHOR: Pablo Duarte da Silva e Vitoria Karolina Ferreira de Sousa

	"""
	def __init__(self):
		self.th = threading.Lock()
		self.cliente = Cliente()
		self.historico = Historico()

	def depositar(self, id_conta, valor, cursor):
		"""
		DESCRIPTION: A função depositar utiliza a função de busca para uma listagem
		de informações anteriores armazenadas no banco de dados, acrescenta o valor
		adicionado a determinada conta e armazena as novas informações no banco. 

		"""
		self.th.acquire()
		cursor.execute(busca_valores.format(id_conta))
		self.th.release()
		saldo = list(cursor)[0][1]
		saldo += valor
		self.th.acquire()
		cursor.execute(atualizar_saldo.format(saldo, id_conta))
		self.th.release()
		self.historico.inserirHistorico(id_conta, "Deposito de {}".format(valor), cursor)

	def saca(self, id_conta, valor, cursor):
		"""
		DESCRIPTION: A função utiliza a função de busca para uma listagem de
		informações anteriores armazenadas no banco de dados logo após é feita 
		uma atualização das informações no banco de acordo com o valor retirado. 

		"""
		self.th.acquire()
		cursor.execute(busca_valores.format(id_conta))
		self.th.release()
		lista = list(cursor)
		saldo = lista[0][1]
		limite = lista[0][2]

		if((saldo + limite) < valor):
			return False
		else:
			saldo -= valor
			self.th.acquire()
			cursor.execute(atualizar_saldo.format(saldo, id_conta))
			self.th.release()
			self.historico.inserirHistorico(id_conta, "Saque de {}".format(valor), cursor)
			return True

	def transferirConta(self, id_conta, id_conta_destino, valor, cursor):
		"""
		DESCRIPTION: Esta função primeiro é feita uma listagem das informações da conta
		original no banco de dados e nela é feita a atualização de acordo com o valor que
		foi retirado, na conta destino também ocorre uma listagem de informações armazenadas
		no banco de dados,caso o valor de busca seja existente, e nela é feita uma atualização
		no banco de dados.

		"""
		retirou = self.saca(id_conta, valor, cursor)
		if(retirou):
			self.depositar(id_conta_destino, valor, cursor)
			nomeDestino = self.buscarValores(id_conta_destino, cursor)
			self.historico.inserirHistorico(id_conta, "Tranferencia de {} para a conta {}".format(valor, nomeDestino[0][0]), cursor)
			return True
		else:
			return False


	def buscarConta(self, cpf, cursor):
		"""
		DESCRIPTION: A função busca no banco de dados através do CPF informado,
		caso seja válido ele retornará o ID da conta buscada.

		"""
		self.th.acquire()
		cursor.execute(busca_conta.format(cpf))
		self.th.release()
		conta = list(cursor)
		if(len(conta) != 0):
			return conta[0][0]
		return None

	def cadastrarConta(self, cpf, senha, cursor):
		"""
		DESCRIPTION: A função é responsavel pelo cadastro e armazenamento dos dados
		cadastrais no banco de dados. Para tal é necessário a função anterior de busca
		para verificar se o CPF já está em uso.

		"""
		if(self.buscarConta(cpf, cursor) == None):
			id_cliente = self.cliente.buscarCliente(cpf, cursor)
			self.th.acquire()
			cursor.execute(cadastrar_conta.format(id_cliente, 0, senha, 1000))
			self.th.release()
			id_conta = self.buscarConta(cpf, cursor)
			self.historico.inserirHistorico(id_conta, "Conta aberta em {}".format(str(datetime.now().strftime('%d/%m/%Y %H:%M'))), cursor)
			return True
		return False

	def autenticaSenha(self, id_conta, senha, cursor):
		"""
		DESCRIPTION: Função responsável pela verificação da senha informada. 

		"""
		self.th.acquire()
		cursor.execute(autentica_senha.format(id_conta, senha))
		self.th.release()
		conta = list(cursor)
		if(len(conta) != 0):
			return True
		return False

	def buscarValores(self, id_conta, cursor):
		"""
		DESCRIPTION: A função realiza uma busca no banco de dados 
		e retona uma lista de informaçoes da conta.

		"""
		self.th.acquire()
		cursor.execute(busca_valores.format(id_conta))
		self.th.release()
		conta = list(cursor)
		return conta
