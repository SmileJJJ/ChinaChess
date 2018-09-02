# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\thirdly_interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import global_var
import qdarkstyle

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #构建计时器
        self.timer = QtCore.QBasicTimer()
        self.timer.start(1000,self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(315, 620)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setLineWidth(1)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(5)
        self.splitter_2.setObjectName("splitter_2")
        self.input_txt = QtWidgets.QTextEdit(self.splitter_2)
        self.input_txt.setObjectName("input_txt")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.send_botton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.send_botton.setFont(font)
        self.send_botton.setObjectName("send_botton")
        self.stand_by_1 = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.stand_by_1.setFont(font)
        self.stand_by_1.setObjectName("stand_by_1")
        self.stand_by2 = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.stand_by2.setFont(font)
        self.stand_by2.setObjectName("stand_by2")
        self.quit_button = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.quit_button.setFont(font)
        self.quit_button.setObjectName("quit_button")
        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)
        self.output_txt = QtWidgets.QTextBrowser(Dialog)
        self.output_txt.setObjectName("output_txt")
        self.gridLayout.addWidget(self.output_txt, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.send_botton.clicked.connect(Dialog.send_action)
        self.stand_by_1.clicked.connect(Dialog.standby_1)
        self.stand_by2.clicked.connect(Dialog.change_skin)
        self.quit_button.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.input_txt, self.stand_by2)
        Dialog.setTabOrder(self.stand_by2, self.quit_button)
        Dialog.setTabOrder(self.quit_button, self.send_botton)
        Dialog.setTabOrder(self.send_botton, self.stand_by_1)
        Dialog.setTabOrder(self.stand_by_1, self.output_txt)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        msg = "游戏房间    昵称:"+global_var.login_count
        Dialog.setWindowTitle(_translate("Dialog", msg))
        self.send_botton.setText(_translate("Dialog", "发送"))
        self.stand_by_1.setText(_translate("Dialog", "备用1"))
        self.stand_by2.setText(_translate("Dialog", "换肤"))
        self.quit_button.setText(_translate("Dialog", "退出"))

    def timerEvent(self,*args,**kwargs):    
        for i in global_var.room_recive_chat_message:
            self.output_txt.append(i + '\n')
        global_var.room_recive_chat_message = []

    def send_action(self):
        if not self.input_txt.toPlainText().isspace(): 
            global_var.room_send_chat_message = self.input_txt.toPlainText()
        else:
            print(QtWidgets.QMessageBox.information(self, 
                                                    "提示", 
                                                    "发送内容为空，请重新输入!", 
                                                    QtWidgets.QMessageBox.Yes, 
                                                    QtWidgets.QMessageBox.Yes))
        self.input_txt.setPlainText('')
    # def quit_action(self):
    #     # self.closeEvent(event):
    #     pass
    def standby_1(self):
        pass
    def change_skin(self):
        global_var.skin += 1
        if global_var.skin >= global_var.skin_all:
            global_var.skin = 0

    def closeEvent(self,event):
        if global_var.board_status:
            reply = QtWidgets.QMessageBox.question(self,
                                                '游戏离开？',
                                                "离开游戏视对方胜利！",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        else:
            reply = QtWidgets.QMessageBox.question(self,
                                                '游戏离开？',
                                                "退出游戏房间",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)           

        if reply == QtWidgets.QMessageBox.Yes:
            global_var.interface_rank = 2
            event.accept()
        else:
            event.ignore()
