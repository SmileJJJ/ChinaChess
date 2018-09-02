# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\second_interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import global_var
import qdarkstyle
import thirdly_interface

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #构建计时器
        self.timer = QtCore.QBasicTimer()
        self.timer.start(1000,self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(750, 450))
        Dialog.setMaximumSize(QtCore.QSize(750, 450))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_4 = QtWidgets.QSplitter(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_4.sizePolicy().hasHeightForWidth())
        self.splitter_4.setSizePolicy(sizePolicy)
        self.splitter_4.setMinimumSize(QtCore.QSize(730, 220))
        self.splitter_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.date_weiget = QtWidgets.QCalendarWidget(self.splitter_3)
        self.date_weiget.setObjectName("date_weiget")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_online = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_online.setFont(font)
        self.label_online.setObjectName("label_online")
        self.online_Number = QtWidgets.QLCDNumber(self.splitter_2)
        self.online_Number.setObjectName("online_Number")
        self.recive_text = QtWidgets.QTextEdit(self.splitter_4)
        self.recive_text.setMinimumSize(QtCore.QSize(500, 0))
        self.recive_text.setObjectName("recive_text")
        self.gridLayout.addWidget(self.splitter_4, 0, 0, 1, 2)
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setEnabled(True)
        self.splitter.setMinimumSize(QtCore.QSize(570, 200))
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Table1_1 = QtWidgets.QTextEdit(self.layoutWidget)
        self.Table1_1.setObjectName("Table1_1")
        self.horizontalLayout.addWidget(self.Table1_1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.Table_botton_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.Table_botton_1.setObjectName("Table_botton_1")
        self.horizontalLayout.addWidget(self.Table_botton_1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Table1_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.Table1_2.setLineWidth(1)
        self.Table1_2.setObjectName("Table1_2")
        self.horizontalLayout.addWidget(self.Table1_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Table2_1 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.Table2_1.setObjectName("Table2_1")
        self.horizontalLayout_2.addWidget(self.Table2_1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.Table_botton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.Table_botton_2.setObjectName("Table_botton_2")
        self.horizontalLayout_2.addWidget(self.Table_botton_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.Table2_2 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.Table2_2.setObjectName("Table2_2")
        self.horizontalLayout_2.addWidget(self.Table2_2)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Table3_1 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.Table3_1.setObjectName("Table3_1")
        self.horizontalLayout_4.addWidget(self.Table3_1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.Table_botton_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.Table_botton_3.setObjectName("Table_botton_3")
        self.horizontalLayout_4.addWidget(self.Table_botton_3)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.Table3_2 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.Table3_2.setObjectName("Table3_2")
        self.horizontalLayout_4.addWidget(self.Table3_2)
        self.layoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Table4_1 = QtWidgets.QTextEdit(self.layoutWidget_3)
        self.Table4_1.setObjectName("Table4_1")
        self.horizontalLayout_5.addWidget(self.Table4_1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.Table_botton_4 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.Table_botton_4.setObjectName("Table_botton_4")
        self.horizontalLayout_5.addWidget(self.Table_botton_4)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.Table4_2 = QtWidgets.QTextEdit(self.layoutWidget_3)
        self.Table4_2.setObjectName("Table4_2")
        self.horizontalLayout_5.addWidget(self.Table4_2)
        self.layoutWidget_4 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Table5_1 = QtWidgets.QTextEdit(self.layoutWidget_4)
        self.Table5_1.setObjectName("Table5_1")
        self.horizontalLayout_6.addWidget(self.Table5_1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.Table_botton_5 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.Table_botton_5.setObjectName("Table_botton_5")
        self.horizontalLayout_6.addWidget(self.Table_botton_5)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.Table5_2 = QtWidgets.QTextEdit(self.layoutWidget_4)
        self.Table5_2.setObjectName("Table5_2")
        self.horizontalLayout_6.addWidget(self.Table5_2)
        self.layoutWidget_5 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Table6_1 = QtWidgets.QTextEdit(self.layoutWidget_5)
        self.Table6_1.setObjectName("Table6_1")
        self.horizontalLayout_7.addWidget(self.Table6_1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.Table_botton_6 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.Table_botton_6.setObjectName("Table_botton_6")
        self.horizontalLayout_7.addWidget(self.Table_botton_6)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.Table6_2 = QtWidgets.QTextEdit(self.layoutWidget_5)
        self.Table6_2.setObjectName("Table6_2")
        self.horizontalLayout_7.addWidget(self.Table6_2)
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        self.splitter_6 = QtWidgets.QSplitter(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_6.sizePolicy().hasHeightForWidth())
        self.splitter_6.setSizePolicy(sizePolicy)
        self.splitter_6.setMinimumSize(QtCore.QSize(150, 200))
        self.splitter_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.send_text = QtWidgets.QTextEdit(self.splitter_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_text.sizePolicy().hasHeightForWidth())
        self.send_text.setSizePolicy(sizePolicy)
        self.send_text.setObjectName("send_text")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_5.sizePolicy().hasHeightForWidth())
        self.splitter_5.setSizePolicy(sizePolicy)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.send_botton = QtWidgets.QPushButton(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_botton.sizePolicy().hasHeightForWidth())
        self.send_botton.setSizePolicy(sizePolicy)
        self.send_botton.setObjectName("send_botton")
        self.clear_botton = QtWidgets.QPushButton(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_botton.sizePolicy().hasHeightForWidth())
        self.clear_botton.setSizePolicy(sizePolicy)
        self.clear_botton.setObjectName("clear_botton")
        self.standby1 = QtWidgets.QPushButton(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.standby1.sizePolicy().hasHeightForWidth())
        self.standby1.setSizePolicy(sizePolicy)
        self.standby1.setObjectName("standby1")
        self.standby2 = QtWidgets.QPushButton(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.standby2.sizePolicy().hasHeightForWidth())
        self.standby2.setSizePolicy(sizePolicy)
        self.standby2.setObjectName("standby2")
        self.standby3 = QtWidgets.QPushButton(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.standby3.sizePolicy().hasHeightForWidth())
        self.standby3.setSizePolicy(sizePolicy)
        self.standby3.setObjectName("standby3")
        self.gridLayout.addWidget(self.splitter_6, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.Table_botton_1.clicked.connect(Dialog.Table_1_action)
        self.Table_botton_2.clicked.connect(Dialog.Table_2_action)
        self.Table_botton_3.clicked.connect(Dialog.Table_3_action)
        self.Table_botton_4.clicked.connect(Dialog.Table_4_action)
        self.Table_botton_5.clicked.connect(Dialog.Table_5_action)
        self.Table_botton_6.clicked.connect(Dialog.Table_6_action)
        self.send_botton.clicked.connect(Dialog.send_action)
        self.clear_botton.clicked.connect(Dialog.clear_action)
        self.standby1.clicked.connect(Dialog.standby_action)
        self.standby2.clicked.connect(Dialog.standby_action)
        self.standby3.clicked.connect(Dialog.standby_action)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.recive_text, self.send_text)
        Dialog.setTabOrder(self.send_text, self.date_weiget)
        Dialog.setTabOrder(self.date_weiget, self.Table1_1)
        Dialog.setTabOrder(self.Table1_1, self.Table_botton_1)
        Dialog.setTabOrder(self.Table_botton_1, self.Table1_2)
        Dialog.setTabOrder(self.Table1_2, self.Table2_1)
        Dialog.setTabOrder(self.Table2_1, self.Table_botton_2)
        Dialog.setTabOrder(self.Table_botton_2, self.Table2_2)
        Dialog.setTabOrder(self.Table2_2, self.Table3_1)
        Dialog.setTabOrder(self.Table3_1, self.Table_botton_3)
        Dialog.setTabOrder(self.Table_botton_3, self.Table3_2)
        Dialog.setTabOrder(self.Table3_2, self.Table4_1)
        Dialog.setTabOrder(self.Table4_1, self.Table_botton_4)
        Dialog.setTabOrder(self.Table_botton_4, self.Table4_2)
        Dialog.setTabOrder(self.Table4_2, self.Table5_1)
        Dialog.setTabOrder(self.Table5_1, self.Table_botton_5)
        Dialog.setTabOrder(self.Table_botton_5, self.Table5_2)
        Dialog.setTabOrder(self.Table5_2, self.Table6_1)
        Dialog.setTabOrder(self.Table6_1, self.Table_botton_6)
        Dialog.setTabOrder(self.Table_botton_6, self.Table6_2)
        Dialog.setTabOrder(self.Table6_2, self.send_botton)
        Dialog.setTabOrder(self.send_botton, self.clear_botton)
        Dialog.setTabOrder(self.clear_botton, self.standby1)
        Dialog.setTabOrder(self.standby1, self.standby2)
        Dialog.setTabOrder(self.standby2, self.standby3)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        msg = "游戏大厅    昵称:"+global_var.login_count
        Dialog.setWindowTitle(_translate("Dialog", msg))
        Dialog.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.label_online.setText(_translate("Dialog", "在线人数"))
        self.label_2.setText(_translate("Dialog", "- - - - -"))
        self.Table_botton_1.setText(_translate("Dialog", "Table1"))
        self.label.setText(_translate("Dialog", "- - - - -"))
        self.label_3.setText(_translate("Dialog", "- - - - -"))
        self.Table_botton_2.setText(_translate("Dialog", "Table2"))
        self.label_4.setText(_translate("Dialog", "- - - - -"))
        self.label_7.setText(_translate("Dialog", "- - - - -"))
        self.Table_botton_3.setText(_translate("Dialog", "Table3"))
        self.label_8.setText(_translate("Dialog", "- - - - -"))
        self.label_9.setText(_translate("Dialog", "- - - - -"))
        self.Table_botton_4.setText(_translate("Dialog", "Table4"))
        self.label_10.setText(_translate("Dialog", "- - - - -"))
        self.label_11.setText(_translate("Dialog", "- - - - -"))
        self.Table_botton_5.setText(_translate("Dialog", "Table5"))
        self.label_12.setText(_translate("Dialog", "- - - - -"))
        self.label_13.setText(_translate("Dialog", "- - - - -"))
        self.Table_botton_6.setText(_translate("Dialog", "Table6"))
        self.label_14.setText(_translate("Dialog", "- - - - -"))
        self.send_botton.setText(_translate("Dialog", "发送"))
        self.clear_botton.setText(_translate("Dialog", "清屏"))
        self.standby1.setText(_translate("Dialog", "备用1"))
        self.standby2.setText(_translate("Dialog", "备用2"))
        self.standby3.setText(_translate("Dialog", "备用3"))

    def timerEvent(self,*args,**kwargs):
        if global_var.get_in_table == 1:
            print(QtWidgets.QMessageBox.information(self, 
                                                    "提示", "该桌人数已满!", 
                                                    QtWidgets.QMessageBox.Yes, 
                                                    QtWidgets.QMessageBox.Yes))
        elif global_var.get_in_table == 2:
            global_var.get_in_table = 0
            global_var.interface_rank = 3
            self.hide()
            self.interface_3 = thirdly_interface.Ui_Dialog()
            self.interface_3.exec_()
            if global_var.interface_rank == 2:
                self.show() 
        for i in global_var.recive_chat_message:
            global_var.tset_num += 1
            # print('show message to interface count------>',global_var.tset_num2)
            self.recive_text.append(i+'\n')
        global_var.recive_chat_message = []
        self.online_Number.setProperty("value",global_var.online_num)
        for i in global_var.lobby_list:       
            tabl_mes = i.split(' ')
            if tabl_mes[0] == '1':
                try:
                    self.Table1_1.setPlainText(tabl_mes[1])
                    self.Table1_2.setPlainText(tabl_mes[2])
                except IndexError:
                    pass
            elif tabl_mes[0] == '2':
                try:
                    self.Table2_1.setPlainText(tabl_mes[1])
                    self.Table2_2.setPlainText(tabl_mes[2])
                except IndexError:
                    pass
            elif tabl_mes[0] == '3':
                try:
                    self.Table3_1.setPlainText(tabl_mes[1])
                    self.Table3_2.setPlainText(tabl_mes[2])
                except IndexError:
                    pass
            elif tabl_mes[0] == '4':
                try:
                    self.Table4_1.setPlainText(tabl_mes[1])
                    self.Table4_2.setPlainText(tabl_mes[2])
                except IndexError:
                    pass
            elif tabl_mes[0] == '5':
                try:
                    self.Table5_1.setPlainText(tabl_mes[1])
                    self.Table5_2.setPlainText(tabl_mes[2])
                except IndexError:
                    pass
            elif tabl_mes[0] == '6':
                try:
                    self.Table6_1.setPlainText(tabl_mes[1])
                    self.Table6_2.setPlainText(tabl_mes[2])
                except IndexError:
                    pass

    def Table_1_action(self):
        global_var.get_table_num = 1
    def Table_2_action(self):
        global_var.get_table_num = 2
    def Table_3_action(self):
        global_var.get_table_num = 3
    def Table_4_action(self):
        global_var.get_table_num = 4
    def Table_5_action(self):
        global_var.get_table_num = 5
    def Table_6_action(self):
        global_var.get_table_num = 6
    def send_action(self):  
        if not self.send_text.toPlainText().isspace(): 
            global_var.send_chat_message = self.send_text.toPlainText()
        else:
            print(QtWidgets.QMessageBox.information(self, 
                                                    "提示", 
                                                    "发送内容为空，请重新输入!", 
                                                    QtWidgets.QMessageBox.Yes, 
                                                    QtWidgets.QMessageBox.Yes))
        self.send_text.setPlainText('')
        
    def clear_action(self):
        self.recive_text.setPlainText('')
    def standby_action(self):
        pass

    def closeEvent(self,event):
        reply = QtWidgets.QMessageBox.question(self,
                                               '游戏大厅',
                                               "是否要退出游戏大厅？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            global_var.interface_rank = 1
            event.accept()
        else:
            event.ignore()

