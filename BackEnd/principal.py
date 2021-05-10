#Dependencias
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow

#FrontEnd
from FrontEnd.multitela import Ui_MultiTelas

#BackEnd
from BackEnd.cliente import Cliente
from BackEnd.conta import Conta
from BackEnd.banco import Banco

class Principal(Ui_MultiTelas):
	def setupUi(self, Main: QMainWindow):
		super().setupUi(Main)
		self.banco = Banco()
		self.usuario = None

		#Tela Login
		self.telaLogin.pushButton_Cadastrar.clicked.connect(self.botaoTelaCadastrar)
		self.telaLogin.pushButton_Login.clicked.connect(self.botaoAutenticaLogin)

		#Tela Cadastro
		self.telaCadastro.pushButton_Voltar.clicked.connect(self.botaoRetornoTelaLogin)
		self.telaCadastro.pushButton_Cadastrar.clicked.connect(self.botaoCadastrar)

		#Tela Usuário
		self.telaUsuario.pushButton_Voltar.clicked.connect(self.botaoRetornoTelaLogin)


	def botaoRetornoTelaLogin(self):
		self.QtStack.setCurrentIndex(0)

	def botaoRetornoTelaUsuario(self, conta: Conta):
		self.telaUsuario.lineEdit_Nome.setText(conta.titular.nome)
		self.telaUsuario.lineEdit_Saldo.setText(str(conta.saldo))
		self.QtStack.setCurrentIndex(2)

	def botaoTelaCadastrar(self):
		self.QtStack.setCurrentIndex(1)

	def botaoTelaDepositar(self):
		self.QtStack.setCurrentIndex(3)






	def botaoCadastrar(self):
		nome = self.telaCadastro.lineEdit_Nome.text()
		sobrenome = self.telaCadastro.lineEdit_Sobrenome.text()
		cpf = self.telaCadastro.lineEdit_CPF.text()
		senha = self.telaCadastro.lineEdit_Senha.text()

		if not(nome =='' or sobrenome == '' or cpf == '' or senha == ''):
			cliente = Cliente(nome, sobrenome, cpf)
			conta = Conta(1, cliente, senha)
			if(self.banco.cadastrar(conta)):
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
		conta = self.banco.buscar(cpf)
		if(conta):
			autenticado = conta.autenticaSenha(senha)
			if(autenticado):
				self.telaLogin.lineEdit_CPF.setText('')
				self.telaLogin.lineEdit_Senha.setText('')
				self.usuario = conta
				self.botaoRetornoTelaUsuario(conta)
			else:
				QMessageBox.information(None, "Falha", "Senha Inválida")
		else:
			QMessageBox.information(None, "Falha", "CPF Inválido")
