# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'planIN.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
##修改暂停，遇到倒入问题了，待处理
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from APservice import service
import pymysql
# from APdatabase import plan
# sys.path.append("../") # 返回上层路径
# import login
# from APdatabase.plan import planid_x,kemu_x,neirong_x,shichang_x,date_x
# from APdatabase.plan import *

class Ui_planEDIT(QMainWindow):
    _signal = QtCore.pyqtSignal(str)#改造的代码：定义信号
    # print("此为planedit加宅打印：",planid_x, kemu_x, neirong_x, shichang_x, date_x)
    def __init__(self):
        super(Ui_planEDIT, self).__init__()
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)
        self.retranslateUi(self)
        self.saveBNT.clicked.connect(self.slot1)##信号传递的案例代码：
        print(1)

    def slot1(self):#信号传递的案例代码：
        data_str = self.lineEdit.text()#信号传递的案例代码：
        print(2)
        self._signal.emit(data_str)#信号传递的案例代码：
        print(3,2,data_str)


    def setupUi(self, planUI):
        planUI.setObjectName("planUI")
        planUI.resize(594, 407)
        self.groupBox = QtWidgets.QGroupBox(planUI)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 391, 291))
        self.groupBox.setObjectName("groupBox")


        self.kemuIN = QtWidgets.QLineEdit(self.groupBox)
        self.kemuIN.setGeometry(QtCore.QRect(140, 60, 113, 21))
        self.kemuIN.setObjectName("kemuIN")


        self.neirongIN = QtWidgets.QLineEdit(self.groupBox)
        self.neirongIN.setGeometry(QtCore.QRect(140, 140, 113, 21))
        self.neirongIN.setObjectName("neirongIN")

        self.shichangIN = QtWidgets.QSpinBox(self.groupBox)
        self.shichangIN.setGeometry(QtCore.QRect(140, 220, 81, 22))
        self.shichangIN.setMaximum(120)
        self.shichangIN.setObjectName("shichangIN")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(230, 220, 58, 16))
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 69, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.dataIN = QtWidgets.QDateEdit(planUI)
        self.dataIN.setGeometry(QtCore.QRect(90, 340, 110, 22))
        self.dataIN.setObjectName("dataIN")


        self.saveBNT = QtWidgets.QPushButton(planUI)
        self.saveBNT.setGeometry(QtCore.QRect(460, 340, 100, 32))
        self.saveBNT.setObjectName("saveBNT")

        self.label_5 = QtWidgets.QLabel(planUI)
        self.label_5.setGeometry(QtCore.QRect(30, 340, 41, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(planUI)
        self.label_6.setGeometry(QtCore.QRect(230, 340, 58, 16))
        self.label_6.setObjectName("label_6")
        self.lcdNumber = QtWidgets.QLCDNumber(planUI)
        self.lcdNumber.setGeometry(QtCore.QRect(330, 340, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label.setBuddy(self.kemuIN)
        self.label_2.setBuddy(self.neirongIN)
        self.label_3.setBuddy(self.shichangIN)
        self.label_5.setBuddy(self.dataIN)

        self.retranslateUi(planUI)

        self.saveBNT.clicked.connect(self.save)
        print(3)

        QtCore.QMetaObject.connectSlotsByName(planUI)
        print(4)



    # def add(self):
    #     kemu = self.kemuIN.text()
    #     neirong = self.neirongIN.text()
    #     time_long = self.shichangIN.text()
    #     date = self.dataIN.text()
    #     result = service.exec("insert into tb_plan(kemu,neirong,shichang,date ) values (%s,%s,%s,%s)",
    #                           (kemu, neirong, time_long,date))
    #     # connection.commit()#问题
    #     if result > 0:  # 如果结果大于0，说明添加成功
    #         # service.query()  # 在表格中显示最新数据
    #
    #         QMessageBox.information(None, '提示', '信息添加成功！', QMessageBox.Ok)
    #         # self.query()
    #         self.close()
    #         self.m = plan.Ui_MainWindow()
    #
    #         self.m.show()

            # plan.Ui_MainWindow.show()#存在问题，无法刷新
    def save(self):
        # pass
        # print(3, planID)
        # planID = t
        kemu = self.kemuIN.text()
        print(4, kemu)
        neirong = self.neirongIN.text()
        time_long = self.shichangIN.text()
        date = self.dataIN.text()

        # 执行修改操作
        result = service.exec("update tb_plan set kemu=%s ,neirong= %s,shichang= %s,date= %s where planID=%s",
                              (kemu, neirong, time_long, date, planID))

        # # self.m.show()
        # try:
        #     print(111)
        #
        #     if plan.select != "":  # 判断是否选择了要修改的数据
        #         print(2)
        #         planID = t  # 记录要修改的计划编号
        #         print(3,planID)
        #         kemu = self.kemuIN.text()
        #         print(4,kemu)
        #         neirong = self.neirongIN.text()
        #         time_long = self.shichangIN.text()
        #         date = self.dataIN.text()
        #
        #         # 执行修改操作
        #         result = service.exec("update tb_plan set kemu=%s ,neirong= %s,shichang= %s,date= %s where planID=%s",
        #                               (kemu, neirong, time_long, date, planID))
        #         print(5)
        #         if result > 0:  # 如果结果大于0，说明修改成功
        #             print(6)
        #             # self.query()  # 在表格中显示最新数据
        #             QMessageBox.information(None, '提示', '信息修改成功！', QMessageBox.Ok)
        # except:
        #     QMessageBox.warning(None, '警告', '请先选择要修改的数据！', QMessageBox.Ok)


    def retranslateUi(self, planUI):
        _translate = QtCore.QCoreApplication.translate
        planUI.setWindowTitle(_translate("planUI", "计划录入"))
        self.groupBox.setTitle(_translate("planUI", "输入界面"))
        self.label_4.setText(_translate("planUI", "分钟"))
        self.label.setText(_translate("planUI", "科      目："))
        self.label_2.setText(_translate("planUI", "内       容："))
        self.label_3.setText(_translate("planUI", "计划时长："))
        self.saveBNT.setText(_translate("planUI", "保存"))
        self.label_5.setText(_translate("planUI", "日期"))
        self.label_6.setText(_translate("planUI", "可用时长"))