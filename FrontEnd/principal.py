#Dependencias
from PyQt5.QtWidgets import QMessageBox, QMainWindow

#FrontEnd
from conexaoCliente import ConexaoClient
from multitela import Ui_MultiTelas


class Principal(Ui_MultiTelas):
	def setupUi(self, Main: QMainWindow):
		super().setupUi(Main)
		self.usuarioCPF = None
		self.conexaoCliente = ConexaoClient()
		self.conexaoCliente.conectar()

		#Tela Login
		self.telaLogin.pushButton_Cadastrar.clicked.connect(self.botaoTelaCadastrar)
		self.telaLogin.pushButton_Login.clicked.connect(self.botaoAutenticaLogin)

		#Tela Cadastro
		self.telaCadastro.pushButton_Voltar.clicked.connect(self.botaoRetornoTelaLogin)
		self.telaCadastro.pushButton_Cadastrar.clicked.connect(self.botaoCadastrar)

		#Tela Usuário
		self.telaUsuario.pushButton_Voltar.clicked.connect(self.botaoRetornoTelaLogin)
		self.telaUsuario.pushButton_TelaDeposito.clicked.connect(self.botaoTelaDepositar)
		self.telaUsuario.pushButton_TelaSaque.clicked.connect(self.botaoTelaSaque)
		self.telaUsuario.pushButton_TelaTransferencia.clicked.connect(self.botaoTelaTransferencia)
		self.telaUsuario.pushButton_TelaHistorico.clicked.connect(self.botaoTelaExtrato)

		#Tela Deposito
		self.telaDeposito.pushButton_Voltar.clicked.connect(self.botaoRetornoTelaUsuario)
		self.telaDeposito.pushButton_Depositar.clicked.connect(self.botaoDepositar)

		#Tela Saque
		self.telaSaque.pushButton_Voltar.clicked.connect(self.botaoRetornoTelaUsuario)
		self.telaSaque.pushButton_Sacar.clicked.connect(self.botaoSacar)

		#Tela Transferencia
		self.telaTransferencia.pushButton_Voltar.clicked.connect(self.botaoRetornoTelaUsuario)
		self.telaTransferencia.pushButton_Transferir.clicked.connect(self.botaoTranferir)

		#Tela Extrato
		self.telaExtrato.pushButton_Voltar.clicked.connect(self.botaoRetornoTelaUsuario)


	def botaoRetornoTelaLogin(self):
		self.QtStack.setCurrentIndex(0)

	def botaoRetornoTelaUsuario(self):
		dadosEnviados = "{}/{}".format(3, self.usuarioCPF)#Buscar nome e saldo
		dadosRecebidos = self.conexaoCliente.comunicar(dadosEnviados)
		dadosRecebidos = dadosRecebidos.split('/')

		self.telaUsuario.lineEdit_Nome.setText(dadosRecebidos[0])
		self.telaUsuario.lineEdit_Saldo.setText(dadosRecebidos[1])
		self.QtStack.setCurrentIndex(2)

	def botaoTelaCadastrar(self):
		self.QtStack.setCurrentIndex(1)

	def botaoTelaDepositar(self):
		self.QtStack.setCurrentIndex(3)

	def botaoTelaSaque(self):
		dadosEnviados = "{}/{}".format(4, self.usuarioCPF)#Buscar saldo
		dadosRecebidos = self.conexaoCliente.comunicar(dadosEnviados)
		self.telaSaque.lineEdit_Saldo.setText(dadosRecebidos)
		self.QtStack.setCurrentIndex(4)

	def botaoTelaTransferencia(self):
		self.QtStack.setCurrentIndex(5)

	def botaoTelaExtrato(self):
		dadosEnviados = "{}/{}".format(5, self.usuarioCPF)#Buscar histórico
		dadosRecebidos = self.conexaoCliente.comunicar(dadosEnviados)

		self.telaExtrato.textEdit_Historico.setText(dadosRecebidos)
		self.QtStack.setCurrentIndex(6)


	def botaoCadastrar(self):
		nome = self.telaCadastro.lineEdit_Nome.text()
		sobrenome = self.telaCadastro.lineEdit_Sobrenome.text()
		cpf = self.telaCadastro.lineEdit_CPF.text()
		senha = self.telaCadastro.lineEdit_Senha.text()

		if not(nome =='' or sobrenome == '' or cpf == '' or senha == ''):

			dadosEnviados = "{}/{}/{}/{}/{}".format(1, nome, sobrenome, cpf, senha)#cadastrar
			dadosRecebidos = self.conexaoCliente.comunicar(dadosEnviados)

			if(dadosRecebidos == "True"):
				QMessageBox.information(None, "Sucesso", "Cadastro realizado com sucesso!")
				self.telaCadastro.lineEdit_Nome.setText('')
				self.telaCadastro.lineEdit_Sobrenome.setText('')
				self.telaCadastro.lineEdit_CPF.setText('')
				self.telaCadastro.lineEdit_Senha.setText('')
				self.botaoRetornoTelaLogin()
			else:
				QMessageBox.information(None, "Falha", "CPF Inválido")

	def botaoAutenticaLogin(self):
		cpf = self.telaLogin.lineEdit_CPF.text()
		senha = self.telaLogin.lineEdit_Senha.text()

		dadosEnviados = "{}/{}/{}".format(2, cpf, senha)#verificar se existe
		dadosRecebidos = self.conexaoCliente.comunicar(dadosEnviados)

		if(dadosRecebidos == "True"):
			self.telaLogin.lineEdit_CPF.setText('')
			self.telaLogin.lineEdit_Senha.setText('')
			self.usuarioCPF = cpf
			self.botaoRetornoTelaUsuario()
		else:
			QMessageBox.information(None, "Falha", "Dados Inválidos")

	def botaoDepositar(self):
		valor = self.telaDeposito.lineEdit_Valor.text()
		if not(valor == ''):

			dadosEnviados = "{}/{}/{}".format(6, self.usuarioCPF, valor)#Depositar
			self.conexaoCliente.comunicar(dadosEnviados)

			self.telaDeposito.lineEdit_Valor.setText('')
			QMessageBox.information(None, "Sucesso", "Valor Depositado com sucesso!")
			self.botaoRetornoTelaUsuario()
		else:
			QMessageBox.information(None, "Falha", "Valor inválido!")

	def botaoSacar(self):
		valor = self.telaSaque.lineEdit_Valor.text()
		senha = self.telaSaque.lineEdit_Senha.text()

		if not(valor ==''):

			dadosEnviados = "{}/{}/{}/{}".format(7, self.usuarioCPF, senha, valor)#Autenticar e sacar
			dadosRecebidos = self.conexaoCliente.comunicar(dadosEnviados)

			if(dadosRecebidos == "True"):
				self.telaSaque.lineEdit_Valor.setText('')
				self.telaSaque.lineEdit_Senha.setText('')
				QMessageBox.information(None, "Sucesso", "Valor sacado com sucesso!")
				self.botaoRetornoTelaUsuario()
			else:
				QMessageBox.information(None, "Falha", "Valor inválido!")

	def botaoTranferir(self):
		valor = self.telaTransferencia.lineEdit_Valor.text()
		cpfDestino = self.telaTransferencia.lineEdit_CPFDestino.text()
		senha = self.telaTransferencia.lineEdit_Senha.text()

		if not(valor == ''):

			dadosEnviados = "{}/{}/{}/{}/{}".format(8, self.usuarioCPF, senha, cpfDestino, valor)#verificar senha verificar destinatário e transferir
			dadosRecebidos = self.conexaoCliente.comunicar(dadosEnviados)

			if(dadosRecebidos == "True"):
				self.telaTransferencia.lineEdit_Valor.setText('')
				self.telaTransferencia.lineEdit_CPFDestino.setText('')
				self.telaTransferencia.lineEdit_Senha.setText('')
				QMessageBox.information(None, "Sucesso", "Tranferencia realizada com sucesso!")
				self.botaoRetornoTelaUsuario()
			else:
				QMessageBox.information(None, "Falha", "Dados inválido!")
		else:
			QMessageBox.information(None, "Falha", "Dados inválido!")
