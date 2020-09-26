# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import app_rc

class Ui_MainPanel(object):
    def setupUi(self, MainPanel):
        MainPanel.setObjectName("MainPanel")
        MainPanel.setWindowModality(QtCore.Qt.NonModal)
        MainPanel.resize(1002, 673)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainPanel.setWindowIcon(icon)
        MainPanel.setStyleSheet("QMainWindow {\n"
"    background-color: \n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(179, 179, 179, 255), stop:0.766169 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        MainPanel.setIconSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 30, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bnt_sale = QtWidgets.QPushButton(self.groupBox)
        self.bnt_sale.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.bnt_sale.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/shopping-cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bnt_sale.setIcon(icon1)
        self.bnt_sale.setObjectName("bnt_sale")
        self.verticalLayout.addWidget(self.bnt_sale)
        self.btn_calculate = QtWidgets.QPushButton(self.groupBox)
        self.btn_calculate.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.btn_calculate.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/accounting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_calculate.setIcon(icon2)
        self.btn_calculate.setObjectName("btn_calculate")
        self.verticalLayout.addWidget(self.btn_calculate)
        self.btn_receive = QtWidgets.QPushButton(self.groupBox)
        self.btn_receive.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.btn_receive.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/truck.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_receive.setIcon(icon3)
        self.btn_receive.setObjectName("btn_receive")
        self.verticalLayout.addWidget(self.btn_receive)
        self.btn_target = QtWidgets.QPushButton(self.groupBox)
        self.btn_target.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.btn_target.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/target.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_target.setIcon(icon4)
        self.btn_target.setObjectName("btn_target")
        self.verticalLayout.addWidget(self.btn_target)
        self.frame_inside_sale = QtWidgets.QFrame(self.groupBox)
        self.frame_inside_sale.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_inside_sale.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inside_sale.setObjectName("frame_inside_sale")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_inside_sale)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout.addWidget(self.frame_inside_sale)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_report = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_report.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.btn_report.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/wand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_report.setIcon(icon5)
        self.btn_report.setObjectName("btn_report")
        self.verticalLayout_4.addWidget(self.btn_report)
        self.frame_inside_sale_3 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_inside_sale_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_inside_sale_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inside_sale_3.setObjectName("frame_inside_sale_3")
        self.verticalLayout_4.addWidget(self.frame_inside_sale_3)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_area = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_area.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.btn_area.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/address.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_area.setIcon(icon6)
        self.btn_area.setObjectName("btn_area")
        self.verticalLayout_2.addWidget(self.btn_area)
        self.btn_guide = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_guide.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.btn_guide.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/guide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_guide.setIcon(icon7)
        self.btn_guide.setObjectName("btn_guide")
        self.verticalLayout_2.addWidget(self.btn_guide)
        self.btn_operator = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_operator.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.btn_operator.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/travel-agency.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_operator.setIcon(icon8)
        self.btn_operator.setObjectName("btn_operator")
        self.verticalLayout_2.addWidget(self.btn_operator)
        self.btn_shop = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_shop.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.btn_shop.setFont(font)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/online-shopping.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_shop.setIcon(icon9)
        self.btn_shop.setObjectName("btn_shop")
        self.verticalLayout_2.addWidget(self.btn_shop)
        self.btn_product = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_product.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.btn_product.setFont(font)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/earrings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_product.setIcon(icon10)
        self.btn_product.setObjectName("btn_product")
        self.verticalLayout_2.addWidget(self.btn_product)
        self.btn_shop_product = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_shop_product.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.btn_shop_product.setFont(font)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/shopping.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_shop_product.setIcon(icon11)
        self.btn_shop_product.setObjectName("btn_shop_product")
        self.verticalLayout_2.addWidget(self.btn_shop_product)
        self.btn_target_def = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_target_def.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.btn_target_def.setFont(font)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/dart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_target_def.setIcon(icon12)
        self.btn_target_def.setObjectName("btn_target_def")
        self.verticalLayout_2.addWidget(self.btn_target_def)
        self.frame_inside_sale_2 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_inside_sale_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_inside_sale_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inside_sale_2.setObjectName("frame_inside_sale_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_inside_sale_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addWidget(self.frame_inside_sale_2)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 191))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 191))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/traveyo_logo.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_5.addWidget(self.frame)
        MainPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainPanel)
        QtCore.QMetaObject.connectSlotsByName(MainPanel)

    def retranslateUi(self, MainPanel):
        _translate = QtCore.QCoreApplication.translate
        MainPanel.setWindowTitle(_translate("MainPanel", "TRAVIX DIAMOND"))
        self.groupBox.setTitle(_translate("MainPanel", "Satış"))
        self.bnt_sale.setText(_translate("MainPanel", "Satışlar"))
        self.btn_calculate.setText(_translate("MainPanel", "Komisyon Hesaplama"))
        self.btn_receive.setText(_translate("MainPanel", "Tahsilatlar"))
        self.btn_target.setText(_translate("MainPanel", "Hedefler"))
        self.groupBox_3.setTitle(_translate("MainPanel", "Raporlama"))
        self.btn_report.setText(_translate("MainPanel", "Rapor Sihirbazı"))
        self.groupBox_2.setTitle(_translate("MainPanel", "Tanımlar"))
        self.btn_area.setText(_translate("MainPanel", "Bölge"))
        self.btn_guide.setText(_translate("MainPanel", "Rehber"))
        self.btn_operator.setText(_translate("MainPanel", "Operatör"))
        self.btn_shop.setText(_translate("MainPanel", "Mağaza"))
        self.btn_product.setText(_translate("MainPanel", "Ürün"))
        self.btn_shop_product.setText(_translate("MainPanel", "Mağaza Ürünleri"))
        self.btn_target_def.setText(_translate("MainPanel", "Hedef"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainPanel = QtWidgets.QMainWindow()
    ui = Ui_MainPanel()
    ui.setupUi(MainPanel)
    MainPanel.show()
    sys.exit(app.exec_())

