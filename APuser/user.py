# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from APservice import service
import pymysql


class Ui_Form(QMainWindow):
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(623, 405)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 270, 58, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 220, 58, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 180, 58, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(270, 110, 58, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(90, 110, 58, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(80, 310, 58, 16))
        self.label_6.setObjectName("label_6")

        self.nameIN = QtWidgets.QLineEdit(Form)
        self.nameIN.setGeometry(QtCore.QRect(150, 110, 113, 21))
        self.nameIN.setObjectName("nameIN")

        self.passwordIN = QtWidgets.QLineEdit(Form)
        self.passwordIN.setGeometry(QtCore.QRect(310, 110, 113, 21))
        self.passwordIN.setObjectName("passwordIN")

        self.saveBNT = QtWidgets.QPushButton(Form)
        self.saveBNT.setGeometry(QtCore.QRect(330, 360, 100, 32))
        self.saveBNT.setObjectName("saveBNT")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 170, 271, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.schollIN = QtWidgets.QLineEdit(self.layoutWidget)
        self.schollIN.setObjectName("schollIN")
        self.verticalLayout.addWidget(self.schollIN)

        self.gradeIN = QtWidgets.QLineEdit(self.layoutWidget)
        self.gradeIN.setObjectName("gradeIN")
        self.verticalLayout.addWidget(self.gradeIN)

        self.classIN = QtWidgets.QLineEdit(self.layoutWidget)
        self.classIN.setObjectName("classIN")
        self.verticalLayout.addWidget(self.classIN)

        self.xuehaoID = QtWidgets.QLineEdit(self.layoutWidget)
        self.xuehaoID.setObjectName("xuhaoID")
        self.verticalLayout.addWidget(self.xuehaoID)

        self.label.setBuddy(self.classIN)
        self.label_2.setBuddy(self.gradeIN)
        self.label_3.setBuddy(self.schollIN)
        self.label_4.setBuddy(self.passwordIN)
        self.label_5.setBuddy(self.nameIN)
        self.label_6.setBuddy(self.xuehaoID)

        self.retranslateUi(self)
        self.saveBNT.clicked.connect(self.save)
        QtCore.QMetaObject.connectSlotsByName(self)

    def save(self):

        userName = self.nameIN.text()
        userPwd = self.passwordIN.text()
        userschool = self.schollIN.text()
        usergrade = self.gradeIN.text()
        userclass = self.classIN.text()
        userxuhao = self.xuehaoID.text()

        result = service.exec("insert into tb_user(userName,userPwd,userschool,usergrade,userclass,userxuhao) values (%s,%s,%s,%s,%s,%s)",(userName,userPwd,userschool,usergrade,userclass,userxuhao))

        # service.query()
        if result>0:


            QMessageBox.information(None,"??????","?????????????????????",QMessageBox.Ok)
            self.close()
            # plan.query()
        else:
            QMessageBox.information(None, "??????", "????????????????????????", QMessageBox.Ok)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "??????"))
        self.label_2.setText(_translate("Form", "??????"))
        self.label_3.setText(_translate("Form", "??????"))
        self.label_4.setText(_translate("Form", "??????"))
        self.label_5.setText(_translate("Form", "?????????"))
        self.label_6.setText(_translate("Form", "??????"))
        self.saveBNT.setText(_translate("Form", "??????"))
