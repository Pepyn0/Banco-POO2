from datetime import datetime
from historico import Historico
from cliente import Cliente

from database.sql import busca_conta, cadastrar_conta, autentica_senha, busca_valores, atualizar_saldo


class Conta(object):
	"""
		AUTHOR: Pablo Duarte da Silva e Vitoria Karolina Ferreira de Sousa

	"""

	@staticmethod
	def depositar(id_conta, valor, cursor):
		"""
		DESCRIPTION: A função depositar utiliza a função de busca para uma listagem
		de informações anteriores armazenadas no banco de dados, acrescenta o valor
		adicionado a determinada conta e armazena as novas informações no banco. 

		"""
		cursor.execute(busca_valores.format(id_conta))
		saldo = list(cursor)[0][1]
		saldo += valor
		cursor.execute(atualizar_saldo.format(saldo, id_conta))
		Historico.inserirHistorico(id_conta, "Deposito de {}".format(valor), cursor)

	@staticmethod
	def saca(id_conta, valor, cursor):
		"""
		DESCRIPTION: A função utiliza a função de busca para uma listagem de
		informações anteriores armazenadas no banco de dados logo após é feita 
		uma atualização das informações no banco de acordo com o valor retirado. 

		"""
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
		"""
		DESCRIPTION: Esta função primeiro é feita uma listagem das informações da conta
		original no banco de dados e nela é feita a atualização de acordo com o valor que
		foi retirado, na conta destino também ocorre uma listagem de informações armazenadas
		no banco de dados,caso o valor de busca seja existente, e nela é feita uma atualização
		no banco de dados.

		"""
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
		"""
		DESCRIPTION: A função busca no banco de dados através do CPF informado,
		caso seja válido ele retornará o ID da conta buscada.

		"""
		cursor.execute(busca_conta.format(cpf))
		conta = list(cursor)
		if(len(conta) != 0):
			return conta[0][0]
		return None

	@staticmethod
	def cadastrarConta(cpf, senha, cursor):
		"""
		DESCRIPTION: A função é responsavel pelo cadastro e armazenamento dos dados
		cadastrais no banco de dados. Para tal é necessário a função anterior de busca
		para verificar se o CPF já está em uso.

		"""
		if(Conta.buscarConta(cpf, cursor) == None):
			id_cliente = Cliente.buscarCliente(cpf, cursor)
			cursor.execute(cadastrar_conta.format(id_cliente, 0, senha, 1000))
			id_conta = Conta.buscarConta(cpf, cursor)
			Historico.inserirHistorico(id_conta, "Conta aberta em {}".format(str(datetime.now().strftime('%d/%m/%Y %H:%M'))), cursor)
			return True
		return False

	@staticmethod
	def autenticaSenha(id_conta, senha, cursor):
		"""
		DESCRIPTION: Função responsável pela verificação da senha informada. 

		"""
		cursor.execute(autentica_senha.format(id_conta, senha))
		conta = list(cursor)
		if(len(conta) != 0):
			return True
		return False

	@staticmethod
	def buscarValores(id_conta, cursor):
		"""
		DESCRIPTION: A função realiza uma busca no banco de dados 
		e retona uma lista de informaçoes da conta.

		"""
		cursor.execute(busca_valores.format(id_conta))
		conta = list(cursor)
		return conta
