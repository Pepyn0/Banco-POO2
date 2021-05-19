#Dependencias
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QStackedLayout

#Telas
from tela_login import Ui_Tela_Login
from tela_cadastrar import Ui_Tela_Cadastro
from tela_usuario import Ui_Tela_Usuario
from tela_deposito import Ui_Tela_Deposito
from tela_saque import Ui_Tela_Saque
from tela_transferencia import Ui_Tela_Tranferencia
from tela_extrato import Ui_Tela_Extrato

class Ui_MultiTelas(QtWidgets.QWidget):
	def setupUi(self, Main: QMainWindow):
		Main.setObjectName("Main")
		Main.resize(640, 480)

		self.QtStack = QStackedLayout()
		self.stack0 = QMainWindow()
		self.stack1 = QMainWindow()
		self.stack2 = QMainWindow()
		self.stack3 = QMainWindow()
		self.stack4 = QMainWindow()
		self.stack5 = QMainWindow()
		self.stack6 = QMainWindow()

		#Tela de Login
		self.telaLogin = Ui_Tela_Login()
		self.telaLogin.setupUi(self.stack0)

		#Tela de Cadastro
		self.telaCadastro = Ui_Tela_Cadastro()
		self.telaCadastro.setupUi(self.stack1)

		#Tela de Usuário
		self.telaUsuario = Ui_Tela_Usuario()
		self.telaUsuario.setupUi(self.stack2)

		#Tela de Deposito
		self.telaDeposito = Ui_Tela_Deposito()
		self.telaDeposito.setupUi(self.stack3)

		#Tela de Saque
		self.telaSaque = Ui_Tela_Saque()
		self.telaSaque.setupUi(self.stack4)

		#Tela de Tranferencia
		self.telaTransferencia = Ui_Tela_Tranferencia()
		self.telaTransferencia.setupUi(self.stack5)

		#Tela de Extrato
		self.telaExtrato = Ui_Tela_Extrato()
		self.telaExtrato.setupUi(self.stack6)

		self.QtStack.addWidget(self.stack0)
		self.QtStack.addWidget(self.stack1)
		self.QtStack.addWidget(self.stack2)
		self.QtStack.addWidget(self.stack3)
		self.QtStack.addWidget(self.stack4)
		self.QtStack.addWidget(self.stack5)
		self.QtStack.addWidget(self.stack6)
