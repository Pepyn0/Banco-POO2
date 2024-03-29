# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela-login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_Login(object):
    def setupUi(self, Tela_Login):
        Tela_Login.setObjectName("Tela_Login")
        Tela_Login.resize(340, 340)
        Tela_Login.setMinimumSize(QtCore.QSize(340, 340))
        Tela_Login.setMaximumSize(QtCore.QSize(340, 340))
        Tela_Login.setStyleSheet("QFrame {\n"
"    color: rgb(40, 40, 40)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Tela_Login)
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
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_Cadastrar = QtWidgets.QPushButton(self.frame)
        self.pushButton_Cadastrar.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_Cadastrar.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Cadastrar.setFont(font)
        self.pushButton_Cadastrar.setStyleSheet("QPushButton {\n"
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
        self.pushButton_Cadastrar.setObjectName("pushButton_Cadastrar")
        self.horizontalLayout_3.addWidget(self.pushButton_Cadastrar)
        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)
        self.labelBanco = QtWidgets.QLabel(self.frame)
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
        self.gridLayout.addWidget(self.labelBanco, 0, 0, 1, 1)
        self.labelLogin = QtWidgets.QLabel(self.frame)
        self.labelLogin.setEnabled(True)
        self.labelLogin.setMinimumSize(QtCore.QSize(0, 40))
        self.labelLogin.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelLogin.setFont(font)
        self.labelLogin.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.labelLogin.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLogin.setObjectName("labelLogin")
        self.gridLayout.addWidget(self.labelLogin, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Login = QtWidgets.QPushButton(self.frame)
        self.pushButton_Login.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_Login.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Login.setFont(font)
        self.pushButton_Login.setStyleSheet("QPushButton {\n"
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
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.horizontalLayout_2.addWidget(self.pushButton_Login)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_CPF = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_CPF.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_CPF.sizePolicy().hasHeightForWidth())
        self.lineEdit_CPF.setSizePolicy(sizePolicy)
        self.lineEdit_CPF.setMinimumSize(QtCore.QSize(280, 40))
        self.lineEdit_CPF.setStyleSheet("QLineEdit {\n"
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
        self.lineEdit_CPF.setMaxLength(60)
        self.lineEdit_CPF.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_CPF.setObjectName("lineEdit_CPF")
        self.horizontalLayout_4.addWidget(self.lineEdit_CPF)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_Senha = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Senha.sizePolicy().hasHeightForWidth())
        self.lineEdit_Senha.setSizePolicy(sizePolicy)
        self.lineEdit_Senha.setMinimumSize(QtCore.QSize(280, 40))
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
        self.lineEdit_Senha.setObjectName("lineEdit_Senha")
        self.horizontalLayout_5.addWidget(self.lineEdit_Senha)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        Tela_Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tela_Login)
        QtCore.QMetaObject.connectSlotsByName(Tela_Login)

    def retranslateUi(self, Tela_Login):
        _translate = QtCore.QCoreApplication.translate
        Tela_Login.setWindowTitle(_translate("Tela_Login", "V&V Login"))
        self.pushButton_Cadastrar.setText(_translate("Tela_Login", "Cadastrar"))
        self.labelBanco.setText(_translate("Tela_Login", "V&V Bank"))
        self.labelLogin.setText(_translate("Tela_Login", "Login"))
        self.pushButton_Login.setText(_translate("Tela_Login", "Login"))
        self.lineEdit_CPF.setPlaceholderText(_translate("Tela_Login", "CPF"))
        self.lineEdit_Senha.setPlaceholderText(_translate("Tela_Login", "SENHA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_Login = QtWidgets.QMainWindow()
    ui = Ui_Tela_Login()
    ui.setupUi(Tela_Login)
    Tela_Login.show()
    sys.exit(app.exec_())
