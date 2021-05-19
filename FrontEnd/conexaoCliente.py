
import socket

HOST = 'localhost'
PORT = 8000

class ConexaoClient(object):
	def __init__(self):
		self.addr = None
		self.clientSocket = None


	def conectar(self):
		self.addr = ((HOST, PORT))
		self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.clientSocket.connect(self.addr)


	def comunicar(self, dadosEnviados: str):
		self.clientSocket.send(dadosEnviados.encode())
		dadosRecebidos = self.clientSocket.recv(1024).decode()
		return dadosRecebidos


	def fechar(self):
		self.clientSocket.close()
