
import socket

from banco import Banco
from cliente import Cliente
from conta import Conta

HOST = 'localhost'
PORT = 8000

class conexaoServidor(object):
	def __init__(self):
		self.banco = Banco()
		self.addr = None
		self.serverSocket = None
		self.conexao = None


	def conectar(self):
		self.addr = ((HOST, PORT))
		self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.serverSocket.bind(self.addr)
		self.serverSocket.listen(2)
		print("Aguardando conexão...")

		self.conexao, _ = self.serverSocket.accept()
		print("Conectado!")
		print("Aguardando solicitações...")


	def comunicar(self):
		dados = self.conexao.recv(1024).decode()
		listaDados = dados.split('/')

		if(listaDados[0] == '1'):	#Cadastrar
			cliente = Cliente(listaDados[1], listaDados[2], listaDados[3])
			conta = Conta((self.banco.getTotalContas() + 1), cliente, listaDados[4])
			if(self.banco.cadastrar(conta)):
				print("Conta de {} cadastrada".format(conta.titular.nome))
				self.conexao.send("True".encode())
			else:
				print("Erro ao cadastrar conta")
				self.conexao.send("Erro ao cadastrar conta!".encode())

		elif(listaDados[0] == '2'):	#Autenticar
			conta = self.banco.buscar(listaDados[1])

			if(conta):
				autenticado = conta.autenticaSenha(listaDados[2])
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
			conta = self.banco.buscar(listaDados[1])
			retorno = "{}/{}".format(conta.titular.nome, conta.saldo)
			self.conexao.send(retorno.encode())

		elif(listaDados[0] == '4'):	#Obter saldo
			conta = self.banco.buscar(listaDados[1])
			retorno = "{}".format(conta.saldo)
			self.conexao.send(retorno.encode())

		elif(listaDados[0] == '5'):	#Histórico
			conta = self.banco.buscar(listaDados[1])
			retorno = conta.historico.imprime()
			self.conexao.send(retorno.encode())
			print("Conta {} acessou historico".format(conta.titular.nome))

		elif(listaDados[0] == '6'):	#Depositar
			conta = self.banco.buscar(listaDados[1])
			conta.depositar(float(listaDados[2]))
			self.conexao.send("True".encode())
			print("Conta {} realizou um deposito".format(conta.titular.nome))

		elif(listaDados[0] == '7'):	#Sacar
			conta = self.banco.buscar(listaDados[1])
			if(conta.autenticaSenha(listaDados[2])):
				if(conta.saca(float(listaDados[3]))):
					print("Conta {} realizou um saque".format(conta.titular.nome))
					self.conexao.send("True".encode())
				else:
					self.conexao.send("Valor inválido".encode())
					print("Conta realizou saque mal-sucedido")
			else:
				self.conexao.send("Senha inválida".encode())
				print("Conta realizou saque mal-sucedido")

		elif(listaDados[0] == '8'):	#Transferir
			conta = self.banco.buscar(listaDados[1])
			if(conta.autenticaSenha(listaDados[2])):
				contaDestino = self.banco.buscar(listaDados[3])
				if(contaDestino):
					conta.transfere(contaDestino, float(listaDados[4]))
					self.conexao.send("True".encode())
					print("Conta {} realizou uma transferencia para {}".format(conta.titular.nome,contaDestino.titular.nome))
				else:
					self.conexao.send("CPF não encontrado".encode())
					print("Conta realizou transferencia mal-sucedida")
			else:
				self.conexao.send("Senha inválida".encode())
				print("Conta realizou transferencia mal-sucedida")


	def fechar(self):
		self.serverSocket.close()
		print("Server finalizado.")


if __name__ == "__main__":
	server = conexaoServidor()
	server.conectar()
	rodando = True
	while(rodando):
		server.comunicar()
	server.fechar()
