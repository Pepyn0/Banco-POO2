
import socket

HOST = 'localhost'
PORT = 8000

class ConexaoClient(object):
	def __init__(self):
	"""
		AUTHOR: Pablo Duarte da Silva e Vitoria Karolina Ferreira de Sousa

	"""
		self.addr = None
		self.clientSocket = None


	def conectar(self):
		"""
		DESCRIPTION: Função responsável pela conexão do cliente ao servidor

		"""
		self.addr = ((HOST, PORT))
		self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.clientSocket.connect(self.addr)


	def comunicar(self, dadosEnviados: str):
		"""
		DESCRIPTION: Nesta função ocorre o envio dos dados informados pelo cliente na rede.

		"""
		self.clientSocket.send(dadosEnviados.encode())
		dadosRecebidos = self.clientSocket.recv(1024).decode()
		return dadosRecebidos


	def fechar(self):
		"""
		DESCRIPTION: Função de encerramento de conexão e envio de dados.

		"""
		self.clientSocket.close()
