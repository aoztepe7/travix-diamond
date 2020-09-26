import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from ui.ui_operator import Ui_MainWindow
from opr.obj_operator import Operator
import panel.panel
from db.db_operator import update,create,delete,list
import pyautogui
GL_UPDATE = 0

class OperatorWindow(QMainWindow):
    def backToMainPanel(self):
        self.window = panel.panel.PanelWindow()
        self.window.show()
        self.hide()

    def mousePressEv(self):
        if(len(self.ui.tableWidget.selectedItems()) != 0):
            self.fillTextBoxes()

    def enableEntryFrame(self):
        global GL_UPDATE
        GL_UPDATE = 1
        self.ui.entry_frame.setEnabled(True)

    def clearTextBoxes(self):
        self.ui.txt_name.setText("")
        self.ui.txt_chief_com.setText("")

    def newEntry(self):
        global GL_UPDATE
        GL_UPDATE = 0
        self.clearTextBoxes()
        self.ui.entry_frame.setEnabled(True)

    def fieldChecker(self):
        if(self.ui.txt_name.text()=="" or self.ui.txt_chief_com.text()==""):
            return False
        else:
            return True

    def decimalControl(self,number):
        convertedNumber = number
        if(str(number).__contains__(",")):
           convertedNumber = str(number).replace(",",".")
        return float(convertedNumber)

    def save(self):
        fieldControl = self.fieldChecker()
        chiefCom = self.decimalControl(self.ui.txt_chief_com.text())
        if(fieldControl == False):
            pyautogui.alert("Operatör Adı ve Şef Komisyon Oranı Boş Olamaz!")
            return
        else:
            if(GL_UPDATE == 1):
                result = pyautogui.confirm("Seçilen Operatör Güncellenecek. Onaylıyor Musunuz?")
                if (result == "OK"):
                    self.ui.tableWidget.setColumnHidden(0, False)
                    self.ui.tableWidget.setColumnHidden(2, False)
                    self.ui.tableWidget.setColumnHidden(3, False)
                    item = self.ui.tableWidget.selectedItems()
                    operator = Operator(
                        id= item[0].text(),
                        name= self.ui.txt_name.text(),
                        chief_com= chiefCom,
                        version=item[3].text()
                    )
                    self.ui.tableWidget.setColumnHidden(0, True)
                    self.ui.tableWidget.setColumnHidden(2, True)
                    self.ui.tableWidget.setColumnHidden(3, True)
                    result = update(operator)
                    if(result):
                        pyautogui.alert("Operatör Güncellendi")
                        self.fillTable()
                        self.clearTextBoxes()
                        self.disabeEntryFrame()
                        return
                    else:
                        pyautogui.alert("Operatör Güncellenirken Bir Sorun Oluştu.Lütfen Daha Sonra Tekrar Deneyiniz!")
                        return
            else:
                result = pyautogui.confirm("Yeni Bir Operatör Eklenecek. Onaylıyor Musunuz?")
                if (result == "OK"):
                    operator = Operator(
                        id= None,
                        name=self.ui.txt_name.text(),
                        chief_com=chiefCom,
                        version=1
                    )
                    result = create(operator)
                    if (result):
                        pyautogui.alert("Operatör Eklendi")
                        self.fillTable()
                        self.clearTextBoxes()
                        self.disabeEntryFrame()
                        return
                    else:
                        pyautogui.alert("Operatör Oluşturulurken Bir Sorun Oluştu.Lütfen Daha Sonra Tekrar Deneyiniz!")
                        return

    def delete(self):
        if(len(self.ui.tableWidget.selectedItems())<1):
            pyautogui.alert("Lütfen Silmek İstediğiniz Operatör Seçiniz!")
            return
        else:
            result = pyautogui.confirm("Seçilen Operatör Silinecek. Onaylıyor Musunuz?")
            if (result == "OK"):
                self.ui.tableWidget.setColumnHidden(0, False)
                self.ui.tableWidget.setColumnHidden(2, False)
                self.ui.tableWidget.setColumnHidden(3, False)
                item = self.ui.tableWidget.selectedItems()
                operator = Operator(
                    id=item[0].text(),
                    name=None,
                    chief_com=None,
                    version=item[3].text()
                )
                self.ui.tableWidget.setColumnHidden(0, True)
                self.ui.tableWidget.setColumnHidden(2, True)
                self.ui.tableWidget.setColumnHidden(3, True)
                result = delete(operator.id,operator.version)
                if (result):
                    pyautogui.alert("Operatör Silindi")
                    self.fillTable()
                    self.clearTextBoxes()
                    self.disabeEntryFrame()
                    return
                else:
                    pyautogui.alert("Operatör Silinirken Bir Sorun Oluştu.Lütfen Daha Sonra Tekrar Deneyiniz!")
                    return


    def disabeEntryFrame(self):
        self.ui.entry_frame.setEnabled(False)

    def fillTextBoxes(self):
        if(len(self.ui.tableWidget.selectedItems())>0):
            self.disabeEntryFrame()
            self.ui.tableWidget.setColumnHidden(0, False)
            self.ui.tableWidget.setColumnHidden(2, False)
            self.ui.tableWidget.setColumnHidden(3, False)
            item = self.ui.tableWidget.selectedItems()
            self.ui.txt_name.setText(item[1].text())
            self.ui.txt_chief_com.setText(item[2].text())
            self.ui.tableWidget.setColumnHidden(0, True)
            self.ui.tableWidget.setColumnHidden(2, True)
            self.ui.tableWidget.setColumnHidden(3, True)

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnHidden(0, True)
        self.ui.tableWidget.setColumnHidden(2, True)
        self.ui.tableWidget.setColumnHidden(3, True)
        self.ui.tableWidget.setColumnHidden(4, True)
        self.ui.tableWidget.setColumnHidden(5, True)
        self.buttonWorks()
        self.ui.entry_frame.setEnabled(False)
        self.ui.txt_chief_com.setValidator(QtGui.QDoubleValidator())
        self.show()

    def fillTable(self):
        guideList = list(self.queryBuilder())
        if(guideList):
            self.ui.tableWidget.setRowCount(0)
            for row, item in enumerate(guideList):
                self.ui.tableWidget.insertRow(row)
                for column, item in enumerate(item):
                    qtItem = QTableWidgetItem(str(item))
                    qtItem.setTextAlignment(Qt.AlignHCenter)
                    self.ui.tableWidget.setItem(row,column,qtItem)




    def queryBuilder(self):
        baseQuery = "SELECT * FROM OPERATOR WHERE "
        if(self.ui.txt_search_name.text() !=""):
            baseQuery = baseQuery + "name like '%"+self.ui.txt_search_name.text()+ "%' and "
        return baseQuery + "status = true"


    def buttonWorks(self):
        self.ui.btn_search.clicked.connect(lambda : self.fillTable())
        self.ui.tableWidget.clicked.connect(lambda: self.mousePressEv())
        self.ui.tableWidget.itemSelectionChanged.connect(lambda: self.fillTextBoxes())
        self.ui.btn_update.clicked.connect(lambda :self.enableEntryFrame())
        self.ui.btn_save.clicked.connect(lambda : self.save())
        self.ui.btn_new.clicked.connect(lambda: self.newEntry())
        self.ui.btn_back.clicked.connect(lambda :self.backToMainPanel())
        self.ui.btn_update_2.clicked.connect(lambda :self.delete())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OperatorWindow()
    sys.exit(app.exec_())