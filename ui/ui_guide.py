# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guide.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 696)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 85, 127);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_5)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.search_text_frame = QtWidgets.QFrame(self.frame_6)
        self.search_text_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.search_text_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.search_text_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.search_text_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_text_frame.setObjectName("search_text_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.search_text_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.search_text_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 85, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.txt_search_name = QtWidgets.QLineEdit(self.search_text_frame)
        self.txt_search_name.setMinimumSize(QtCore.QSize(0, 25))
        self.txt_search_name.setObjectName("txt_search_name")
        self.verticalLayout_2.addWidget(self.txt_search_name)
        self.verticalLayout_4.addWidget(self.search_text_frame)
        self.search_text_frame_2 = QtWidgets.QFrame(self.frame_6)
        self.search_text_frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.search_text_frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.search_text_frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.search_text_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_text_frame_2.setObjectName("search_text_frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.search_text_frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.search_text_frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 85, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.cmb_search_type = QtWidgets.QComboBox(self.search_text_frame_2)
        self.cmb_search_type.setMinimumSize(QtCore.QSize(0, 25))
        self.cmb_search_type.setObjectName("cmb_search_type")
        self.cmb_search_type.addItem("")
        self.cmb_search_type.setItemText(0, "")
        self.cmb_search_type.addItem("")
        self.cmb_search_type.addItem("")
        self.cmb_search_type.addItem("")
        self.verticalLayout_3.addWidget(self.cmb_search_type)
        self.verticalLayout_4.addWidget(self.search_text_frame_2)
        self.frame_20 = QtWidgets.QFrame(self.frame_6)
        self.frame_20.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.btn_search = QtWidgets.QPushButton(self.frame_20)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/loupe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon1)
        self.btn_search.setObjectName("btn_search")
        self.verticalLayout_21.addWidget(self.btn_search)
        self.verticalLayout_4.addWidget(self.frame_20)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.search_button_frame = QtWidgets.QFrame(self.frame_2)
        self.search_button_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.search_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_button_frame.setObjectName("search_button_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.search_button_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_delete = QtWidgets.QPushButton(self.search_button_frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon2)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.btn_update = QtWidgets.QPushButton(self.search_button_frame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_update.setIcon(icon3)
        self.btn_update.setObjectName("btn_update")
        self.horizontalLayout.addWidget(self.btn_update)
        self.btn_new = QtWidgets.QPushButton(self.search_button_frame)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/add-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_new.setIcon(icon4)
        self.btn_new.setObjectName("btn_new")
        self.horizontalLayout.addWidget(self.btn_new)
        self.btn_back = QtWidgets.QPushButton(self.search_button_frame)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon5)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.btn_back)
        self.verticalLayout_6.addWidget(self.search_button_frame)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.entry_frame = QtWidgets.QFrame(self.frame)
        self.entry_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.entry_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.entry_frame.setObjectName("entry_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.entry_frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.entry_frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 85, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.verticalLayout_8.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.txt_name = QtWidgets.QLineEdit(self.frame_8)
        self.txt_name.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_name.setFont(font)
        self.txt_name.setObjectName("txt_name")
        self.verticalLayout_10.addWidget(self.txt_name)
        self.verticalLayout_8.addWidget(self.frame_8)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.frame_11 = QtWidgets.QFrame(self.entry_frame)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_11.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 85, 127);")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5)
        self.verticalLayout_11.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.txt_phone = QtWidgets.QLineEdit(self.frame_13)
        self.txt_phone.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_phone.setFont(font)
        self.txt_phone.setObjectName("txt_phone")
        self.verticalLayout_13.addWidget(self.txt_phone)
        self.verticalLayout_11.addWidget(self.frame_13)
        self.verticalLayout_7.addWidget(self.frame_11)
        self.frame_14 = QtWidgets.QFrame(self.entry_frame)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_14.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_6 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 85, 127);")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_15.addWidget(self.label_6)
        self.verticalLayout_14.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.txt_mail = QtWidgets.QLineEdit(self.frame_16)
        self.txt_mail.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_mail.setFont(font)
        self.txt_mail.setObjectName("txt_mail")
        self.verticalLayout_16.addWidget(self.txt_mail)
        self.verticalLayout_14.addWidget(self.frame_16)
        self.verticalLayout_7.addWidget(self.frame_14)
        self.frame_17 = QtWidgets.QFrame(self.entry_frame)
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_17.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_18 = QtWidgets.QFrame(self.frame_17)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_18.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_7 = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 85, 127);")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_18.addWidget(self.label_7)
        self.verticalLayout_17.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame_17)
        self.frame_19.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_19.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.cmb_type = QtWidgets.QComboBox(self.frame_19)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmb_type.setFont(font)
        self.cmb_type.setObjectName("cmb_type")
        self.cmb_type.addItem("")
        self.cmb_type.setItemText(0, "")
        self.cmb_type.addItem("")
        self.cmb_type.addItem("")
        self.cmb_type.addItem("")
        self.verticalLayout_19.addWidget(self.cmb_type)
        self.verticalLayout_17.addWidget(self.frame_19)
        self.verticalLayout_7.addWidget(self.frame_17)
        self.frame_9 = QtWidgets.QFrame(self.entry_frame)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_save = QtWidgets.QPushButton(self.frame_9)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/floppy-disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon6)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_4.addWidget(self.btn_save)
        self.verticalLayout_7.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.entry_frame)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_7.addWidget(self.frame_10)
        self.horizontalLayout_2.addWidget(self.entry_frame)
        self.verticalLayout_20.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TRAVIX - DIAMOND"))
        self.label.setText(_translate("MainWindow", "REHBERLER"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ADI SOYADI"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PHONE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MAIL"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "GUIDE TYPE"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "VERSION"))
        self.label_2.setText(_translate("MainWindow", "Rehber Adı Soyadı"))
        self.label_3.setText(_translate("MainWindow", "Rehber Türü"))
        self.cmb_search_type.setItemText(1, _translate("MainWindow", "BAĞLI REHBER"))
        self.cmb_search_type.setItemText(2, _translate("MainWindow", "KİRALIK REHBER"))
        self.cmb_search_type.setItemText(3, _translate("MainWindow", "OTEL REHBERİ"))
        self.btn_search.setText(_translate("MainWindow", "Ara"))
        self.btn_delete.setText(_translate("MainWindow", "Sil"))
        self.btn_update.setText(_translate("MainWindow", "Güncelle"))
        self.btn_new.setText(_translate("MainWindow", "Yeni Ekle"))
        self.btn_back.setText(_translate("MainWindow", "Geri"))
        self.label_4.setText(_translate("MainWindow", "Adı - Soyadı"))
        self.label_5.setText(_translate("MainWindow", "Telefonu"))
        self.label_6.setText(_translate("MainWindow", "E-Posta Adresi"))
        self.label_7.setText(_translate("MainWindow", "Rehberlik Türü"))
        self.cmb_type.setItemText(1, _translate("MainWindow", "BAĞLI REHBER"))
        self.cmb_type.setItemText(2, _translate("MainWindow", "KİRALIK REHBER"))
        self.cmb_type.setItemText(3, _translate("MainWindow", "OTEL REHBERİ"))
        self.btn_save.setText(_translate("MainWindow", "Kaydet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

