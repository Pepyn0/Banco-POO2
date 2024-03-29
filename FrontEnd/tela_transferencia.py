# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela-transferencia.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_Tranferencia(object):
    def setupUi(self, Tela_Tranferencia):
        Tela_Tranferencia.setObjectName("Tela_Tranferencia")
        Tela_Tranferencia.resize(340, 340)
        Tela_Tranferencia.setMinimumSize(QtCore.QSize(340, 340))
        Tela_Tranferencia.setMaximumSize(QtCore.QSize(340, 340))
        Tela_Tranferencia.setStyleSheet("QFrame {\n"
"    color: rgb(40, 40, 40)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Tela_Tranferencia)
        self.centralwidget.setMinimumSize(QtCore.QSize(340, 340))
        self.centralwidget.setMaximumSize(QtCore.QSize(340, 340))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(340, 340))
        self.frame.setMaximumSize(QtCore.QSize(340, 340))
        self.frame.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 341, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelBanco = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelBanco.setEnabled(True)
        self.labelBanco.setMinimumSize(QtCore.QSize(0, 40))
        self.labelBanco.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.labelBanco.setFont(font)
        self.labelBanco.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.labelBanco.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBanco.setObjectName("labelBanco")
        self.horizontalLayout.addWidget(self.labelBanco)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 289, 341, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Voltar = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_Voltar.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_Voltar.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Voltar.setFont(font)
        self.pushButton_Voltar.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(94, 53, 177);\n"
"    border: 2px solid rgb(81, 45, 168);\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(40, 40, 40);\n"
"    border: 2px solid rgb(81, 45, 168);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_Voltar.setObjectName("pushButton_Voltar")
        self.horizontalLayout_2.addWidget(self.pushButton_Voltar)
        self.pushButton_Transferir = QtWidgets.QPushButton(self.frame)
        self.pushButton_Transferir.setGeometry(QtCore.QRect(120, 250, 100, 40))
        self.pushButton_Transferir.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_Transferir.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Transferir.setFont(font)
        self.pushButton_Transferir.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(94, 53, 177);\n"
"    border: 2px solid rgb(81, 45, 168);\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(40, 40, 40);\n"
"    border: 2px solid rgb(81, 45, 168);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_Transferir.setObjectName("pushButton_Transferir")
        self.labelTransferencia = QtWidgets.QLabel(self.frame)
        self.labelTransferencia.setEnabled(True)
        self.labelTransferencia.setGeometry(QtCore.QRect(0, 60, 341, 40))
        self.labelTransferencia.setMinimumSize(QtCore.QSize(0, 40))
        self.labelTransferencia.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelTransferencia.setFont(font)
        self.labelTransferencia.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.labelTransferencia.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTransferencia.setObjectName("labelTransferencia")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 100, 341, 146))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_Valor = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Valor.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Valor.sizePolicy().hasHeightForWidth())
        self.lineEdit_Valor.setSizePolicy(sizePolicy)
        self.lineEdit_Valor.setMinimumSize(QtCore.QSize(280, 40))
        self.lineEdit_Valor.setMaximumSize(QtCore.QSize(280, 40))
        self.lineEdit_Valor.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(94, 53, 177);\n"
"}")
        self.lineEdit_Valor.setMaxLength(60)
        self.lineEdit_Valor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_Valor.setObjectName("lineEdit_Valor")
        self.horizontalLayout_4.addWidget(self.lineEdit_Valor)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_CPFDestino = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_CPFDestino.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_CPFDestino.sizePolicy().hasHeightForWidth())
        self.lineEdit_CPFDestino.setSizePolicy(sizePolicy)
        self.lineEdit_CPFDestino.setMinimumSize(QtCore.QSize(280, 40))
        self.lineEdit_CPFDestino.setMaximumSize(QtCore.QSize(280, 40))
        self.lineEdit_CPFDestino.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(94, 53, 177);\n"
"}")
        self.lineEdit_CPFDestino.setText("")
        self.lineEdit_CPFDestino.setMaxLength(60)
        self.lineEdit_CPFDestino.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_CPFDestino.setObjectName("lineEdit_CPFDestino")
        self.horizontalLayout_3.addWidget(self.lineEdit_CPFDestino)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_Senha = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Senha.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Senha.sizePolicy().hasHeightForWidth())
        self.lineEdit_Senha.setSizePolicy(sizePolicy)
        self.lineEdit_Senha.setMinimumSize(QtCore.QSize(280, 40))
        self.lineEdit_Senha.setMaximumSize(QtCore.QSize(280, 40))
        self.lineEdit_Senha.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(94, 53, 177);\n"
"}")
        self.lineEdit_Senha.setMaxLength(60)
        self.lineEdit_Senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Senha.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_Senha.setObjectName("lineEdit_Senha")
        self.horizontalLayout_5.addWidget(self.lineEdit_Senha)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addWidget(self.frame)
        Tela_Tranferencia.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tela_Tranferencia)
        QtCore.QMetaObject.connectSlotsByName(Tela_Tranferencia)

    def retranslateUi(self, Tela_Tranferencia):
        _translate = QtCore.QCoreApplication.translate
        Tela_Tranferencia.setWindowTitle(_translate("Tela_Tranferencia", "V&V Trasnferencia"))
        self.labelBanco.setText(_translate("Tela_Tranferencia", "V&V Bank"))
        self.pushButton_Voltar.setText(_translate("Tela_Tranferencia", "Voltar"))
        self.pushButton_Transferir.setText(_translate("Tela_Tranferencia", "Transferir"))
        self.labelTransferencia.setText(_translate("Tela_Tranferencia", "Transferência"))
        self.lineEdit_Valor.setPlaceholderText(_translate("Tela_Tranferencia", "R$"))
        self.lineEdit_CPFDestino.setPlaceholderText(_translate("Tela_Tranferencia", "CPF DO DESTINATÁRIO"))
        self.lineEdit_Senha.setPlaceholderText(_translate("Tela_Tranferencia", "SUA SENHA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_Tranferencia = QtWidgets.QMainWindow()
    ui = Ui_Tela_Tranferencia()
    ui.setupUi(Tela_Tranferencia)
    Tela_Tranferencia.show()
    sys.exit(app.exec_())
