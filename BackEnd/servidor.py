
import socket
import psycopg2
import threading

from database.sql import clientes, contas, historicos


from cliente import Cliente
from conta import Conta
from historico import Historico


bd = psycopg2.connect(
		user = 'postgres',
		password = 'toor',
		host = 'localhost',
		port = '5432',
		database = 'banco'
		)



class conexaoServidor(threading.Thread):
	"""
		AUTHOR: Pablo Duarte da Silva e Vitoria Karolina Ferreira de Sousa

	"""
	def __init__(self, clienteAddr, conexao, cursor):
		threading.Thread.__init__(self)

		self.clientAddr = clienteAddr
		self.conexao = conexao
		self.cliente = Cliente()
		self.conta = Conta()
		self.historico = Historico()
		self.cursor = cursor
		print("Nova conexão com {}!".format(self.clientAddr))

	def run(self):
		while(self.comunicar() != False):
			pass



	def comunicar(self):
		"""
		DESCRIPTION: A função comunicar possui um objeto conta recebe o cadastro e é dividida em partes:
		- É feito uma verificação se há uma conta cadastrada conforme o que foi atribuída, se o retorno for TRUE 
		irá ser informado uma mensagem ao cliente que a operação ocorreu, caso seja retornado FALSE irá ser imprimido
		uma mensagem de falha na operação.

		- Verifica-se a existência de uma conta cadastrada e uma variável para receber o campo de senha, 
		caso seja TRUE a operação informará uma mensagem de permissão de acesso ao usuário e caso seja FALSE
		será imprimido uma mensagem de erro na operação;
		
		-Obtido os dados do cliente como nome e saldo e é mostrado ao mesmo;

		-Caso seja acessado o extrato da conta, uma mensagem será imprimida informando a que conta foi acessado;

		-Em caso de depositos, uma mensagem será imprimida informando que a conta vinculada recebeu um depósito;

		-Saques são necessários autenticação de senha, caso seja permitido um saque será informado uma mensagem
		de que a conta vinculada realizou tal e caso retorne FALSE é imprimido uma mensagem de erro na operação;

		-Para realização da última etapa é preciso autenticação de senha e uma verificação da existencia de uma 
		conta destino, caso seja TRUE é mostrado uma mensagem de que a conta vinculada realizou uma transferência
		para a conta destino e se for FALSE nas duas verificações é informado uma mensagem de erro na operação.

		"""

		dados = self.conexao.recv(1024).decode()
		listaDados = dados.split('/')
		print("Dados vindo da conexão {}".format(self.clientAddr))

		if(listaDados[0] == '1'):	#Cadastrar

			self.cliente.cadastrarPessoa(listaDados[1], listaDados[2], listaDados[3], self.cursor)
			if(self.conta.cadastrarConta(listaDados[3], listaDados[4], self.cursor)):
				print("Conta de {} cadastrada".format(listaDados[3]))
				self.conexao.send("True".encode())
			else:
				print("Erro ao cadastrar conta")
				self.conexao.send("Erro ao cadastrar conta!".encode())

		elif(listaDados[0] == '2'):	#Autenticar

			id_conta = self.conta.buscarConta(listaDados[1], self.cursor) 

			if(id_conta):
				autenticado = self.conta.autenticaSenha(id_conta,listaDados[2], self.cursor)
				if(autenticado):
					print("Acesso permitido ao usuário")
					self.conexao.send("True".encode())
				else:
					print("Acesso negado ao usuário")
					self.conexao.send("Senha inválida".encode())
			else:
				print("Acesso negado ao usuário")
				self.conexao.send("CPF inválido".encode())

		elif(listaDados[0] == '3'):	#Obter nome e saldo

			id_conta = self.conta.buscarConta(listaDados[1], self.cursor)
			listaValores = self.conta.buscarValores(id_conta, self.cursor)
			retorno = "{}/{}".format(listaValores[0][0], listaValores[0][1])
			self.conexao.send(retorno.encode())

		elif(listaDados[0] == '4'):	#Obter saldo

			id_conta = self.conta.buscarConta(listaDados[1], self.cursor)
			listaValores = self.conta.buscarValores(id_conta, self.cursor)
			retorno = "{}".format(listaValores[0][1])
			self.conexao.send(retorno.encode())

		elif(listaDados[0] == '5'):	#Histórico
			id_conta = self.conta.buscarConta(listaDados[1], self.cursor)
			retorno = self.historico.mostrarHistorico(id_conta, self.cursor)
			self.conexao.send(retorno.encode())
			print("Conta de {} acessou historico".format(listaDados[1]))

		elif(listaDados[0] == '6'):	#Depositar
			id_conta = self.conta.buscarConta(listaDados[1], self.cursor)
			self.conta.depositar(id_conta, float(listaDados[2]), self.cursor)
			self.conexao.send("True".encode())
			print("Conta de {} realizou um deposito".format(listaDados[1]))

		elif(listaDados[0] == '7'):	#Sacar
			id_conta = self.conta.buscarConta(listaDados[1], self.cursor)
			if(self.conta.autenticaSenha(id_conta, listaDados[2], self.cursor)):
				if(self.conta.saca(id_conta, float(listaDados[3]), self.cursor)):
					print("Conta de {} realizou um saque".format(listaDados[1]))
					self.conexao.send("True".encode())
				else:
					self.conexao.send("Valor inválido".encode())
					print("Conta realizou saque mal-sucedido")
			else:
				self.conexao.send("Senha inválida".encode())
				print("Conta realizou saque mal-sucedido")

		elif(listaDados[0] == '8'):	#Transferir
			id_conta = self.conta.buscarConta(listaDados[1], self.cursor)
			if(self.conta.autenticaSenha(id_conta, listaDados[2], self.cursor)):
				id_contaDestino = self.conta.buscarConta(listaDados[3], self.cursor)
				if(id_contaDestino):
					self.conta.transferirConta(id_conta, id_contaDestino, float(listaDados[4]), self.cursor)
					self.conexao.send("True".encode())
					print("Conta de {} realizou uma transferencia para {}".format(listaDados[1], listaDados[3]))
				else:
					self.conexao.send("CPF não encontrado".encode())
					print("Conta realizou transferencia mal-sucedida")
			else:
				self.conexao.send("Senha inválida".encode())
				print("Conta realizou transferencia mal-sucedida")
		else:
			bd.commit()
			print("Conexão com {} finalizada.".format(self.clientAddr))
			return False
		bd.commit()


	def fechar(self):
		"""
		DESCRIPTION: Função responsavél pelo encerramento de uso de dados e finalização do socket.

		"""
		print("Conexão com {} finalizada.".format(self.clientAddr))
		self.serverSocket.close()



if __name__ == "__main__":

	cursor = bd.cursor()
	cursor.execute(clientes)
	cursor.execute(contas)
	cursor.execute(historicos)


	HOST = 'localhost'
	PORT = 8000

	addr = ((HOST, PORT))
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	serverSocket.bind(addr)

	print("Servidor iniciado!")
	print("Aguardando conexão...")
	rodando = True
	while(rodando):
		serverSocket.listen(1)
		conexao, clientAddr = serverSocket.accept()
		newThread = conexaoServidor(clientAddr, conexao, cursor)
		newThread.start()
