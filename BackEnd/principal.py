#Dependencias
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow

#FrontEnd
from FrontEnd.multitela import Ui_MultiTelas

#BackEnd
from BackEnd.cliente import Cliente
from BackEnd.conta import Conta

class Principal(Ui_MultiTelas):
	def setupUi(self, Main: QMainWindow):
		super().setupUi(Main)
