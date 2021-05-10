#Dependencias
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

#Conexão
from BackEnd.principal import Principal

if __name__ == "__main__":
	app = QApplication(sys.argv)
	MainWindow = QMainWindow()
	ui = Principal()
	ui.setupUi(MainWindow)
	sys.exit(app.exec_())
