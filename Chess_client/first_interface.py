# -*- coding: utf-8 -*-
# QT界面

from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle
import sys
import time
import global_var
import webbrowser
import second_interface
import thirdly_interface

class Ui_MainWindow(QtWidgets.QMainWindow,QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        #构建计时器
        self.timer = QtCore.QBasicTimer()
        self.timer.start(1000,self)
        self.step = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 347)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_4.addWidget(self.calendarWidget)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 3, 5, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.online_count = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(26)
        self.online_count.setFont(font)
        self.online_count.setTextFormat(QtCore.Qt.AutoText)
        self.online_count.setObjectName("online_count")
        self.horizontalLayout.addWidget(self.online_count)
        self.online_num = QtWidgets.QLCDNumber(self.centralwidget)
        self.online_num.setObjectName("online_num")
        self.horizontalLayout.addWidget(self.online_num)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 3, 2, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.count_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.count_edit.setObjectName("count_edit")
        self.verticalLayout_2.addWidget(self.count_edit)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.passwd_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwd_edit.setObjectName("passwd_edit")
        self.verticalLayout.addWidget(self.passwd_edit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 24, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(48)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(48)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(48)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(48)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 7, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setTextVisible(False)
        self.gridLayout.addWidget(self.progressBar, 0, 1, 1, 2)
        self.login_botton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login_botton.setFont(font)
        self.login_botton.setObjectName("login_botton")
        self.gridLayout.addWidget(self.login_botton, 4, 1, 3, 2)
        self.register_botton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.register_botton.setFont(font)
        self.register_botton.setObjectName("register_botton")
        self.gridLayout.addWidget(self.register_botton, 3, 1, 1, 2)
        self.calendarWidget.raise_()
        self.online_num.raise_()
        self.progressBar.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.label.raise_()
        self.count_edit.raise_()
        self.login_botton.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.login_botton.raise_()
        self.register_botton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label.setBuddy(self.count_edit)
        self.label_2.setBuddy(self.passwd_edit)

        # 设置验证
        # reg = QtCore.QRegExp("PB[0~9]{8}")
        # pValidator = QRegExpValidator(self)
        # pValidator.setRegExp(reg)
        # self.lineEdit1.setValidator(pValidator)

        # reg = QtCore.QRegExp("[a-zA-z0-9]+$")
        # pValidator.setRegExp(reg)
        # self.lineEdit2.setValidator(pValidator)
        # self.formlayout = QtWidgets.QFormLayout()

        self.passwd_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(MainWindow)
        self.login_botton.clicked.connect(MainWindow.login_action)
        self.register_botton.clicked.connect(MainWindow.register_action)
        self.count_edit.returnPressed.connect(MainWindow.login_action)
        self.passwd_edit.returnPressed.connect(MainWindow.login_action)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.count_edit, self.passwd_edit)
        MainWindow.setTabOrder(self.passwd_edit, self.login_botton)
        MainWindow.setTabOrder(self.login_botton, self.calendarWidget)

        self.online_num.setProperty("value",global_var.online_num)

    def retranslateUi(self, MainWindow ):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "中国象棋"))
        MainWindow.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.online_count.setText(_translate("MainWindow", "在线人数"))
        self.label.setText(_translate("MainWindow", "账号："))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.label_3.setText(_translate("MainWindow", "中"))
        self.label_4.setText(_translate("MainWindow", "国"))
        self.label_5.setText(_translate("MainWindow", "象"))
        self.label_6.setText(_translate("MainWindow", "棋"))
        self.login_botton.setText(_translate("MainWindow", "登录"))
        self.register_botton.setText(_translate("MainWindow", "注册"))

    def timerEvent(self,*args,**kwargs):
        # self.step += 1
        # if self.step >= 100:
        #     self.timer.stop()
        #     self.step = 0
        #     print(QtWidgets.QMessageBox.information(self, "提示", "登录超时!", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Yes))
        # self.progressBar.setValue(self.step)
        if global_var.login_status == 1:
            print('load success')
            self.timer.stop()
            global_var.login_status = 0
            global_var.interface_rank = 2
            # 切换二级界面
            self.hide()
            self.interface_2 = second_interface.Ui_Dialog()
            self.interface_2.exec_()
            if global_var.interface_rank == 1:
                self.show()  
        elif global_var.login_status == 2:
            global_var.login_status = 0  
            print(QtWidgets.QMessageBox.information(self,
                                                     "登录失败", 
                                                     "密码错误!", 
                                                     QtWidgets.QMessageBox.Yes, 
                                                     QtWidgets.QMessageBox.Yes
                                                     ))
        elif global_var.login_status == 3:
            global_var.login_status = 0   
            print(QtWidgets.QMessageBox.information(self, 
                                                    "登录失败", 
                                                    "账号不存在!", 
                                                    QtWidgets.QMessageBox.Yes, 
                                                    QtWidgets.QMessageBox.Yes)) 
        elif global_var.login_status == 4:
            global_var.login_status = 0   
            print(QtWidgets.QMessageBox.information(self, 
                                                    "登录失败", 
                                                    "账号以在线!", 
                                                    QtWidgets.QMessageBox.Yes, 
                                                    QtWidgets.QMessageBox.Yes))                         
        

    def login_action(self):
        count = self.count_edit.text()
        passwd = self.passwd_edit.text()
        if not count:
            print(QtWidgets.QMessageBox.information(self, 
                                                    "提示", 
                                                    "账号不能为空!",
                                                     QtWidgets.QMessageBox.Yes, 
                                                     QtWidgets.QMessageBox.Yes))
            return
        elif not passwd:
            print(QtWidgets.QMessageBox.information(self, 
                                                    "提示", 
                                                    "密码不能为空!", 
                                                    QtWidgets.QMessageBox.Yes, 
                                                    QtWidgets.QMessageBox.Yes))
            return
        else:
            global_var.login_message = ('L',count,passwd)
            self.timer.start(100,self)

    def register_action(self):
        webbrowser.open(global_var.WEB_ADD, new=0, autoraise=True)

def first_interface_main():
    app = QtWidgets.QApplication(sys.argv)
    interface_1 = Ui_MainWindow()
    interface_1.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    first_interface_main()