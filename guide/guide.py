import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from ui.ui_guide import Ui_MainWindow
from guide.obj_guide import Guide
import panel.panel
from db.db_guide import update,create,delete,list
import pyautogui
GL_UPDATE = 0

class GuideWindow(QMainWindow):
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
        self.ui.txt_phone.setText("")
        self.ui.txt_mail.setText("")
        self.ui.cmb_type.setCurrentIndex(-1)

    def newEntry(self):
        global GL_UPDATE
        GL_UPDATE = 0
        self.clearTextBoxes()
        self.ui.entry_frame.setEnabled(True)

    def fieldChecker(self):
        if(self.ui.cmb_type.currentIndex()<1 or self.ui.txt_name.text()==""):
            return False
        else:
            return True

    def save(self):
        fieldControl = self.fieldChecker()
        if(fieldControl == False):
            pyautogui.alert("Rehber Adı-Soyadı ve Rehberlik Türü Boş Olamaz!")
            return
        else:
            if(GL_UPDATE == 1):
                result = pyautogui.confirm("Seçilen Rehber Güncellenecek. Onaylıyor Musunuz?")
                if (result == "OK"):
                    self.ui.tableWidget.setColumnHidden(0, False)
                    self.ui.tableWidget.setColumnHidden(2, False)
                    self.ui.tableWidget.setColumnHidden(3, False)
                    self.ui.tableWidget.setColumnHidden(4, False)
                    self.ui.tableWidget.setColumnHidden(5, False)
                    item = self.ui.tableWidget.selectedItems()
                    guide = Guide(
                        id= item[0].text(),
                        fullName= self.ui.txt_name.text(),
                        phone= self.ui.txt_phone.text(),
                        mail= self.ui.txt_mail.text(),
                        guide_type= self.ui.cmb_type.currentText(),
                        version=item[5].text()
                    )
                    self.ui.tableWidget.setColumnHidden(0, True)
                    self.ui.tableWidget.setColumnHidden(2, True)
                    self.ui.tableWidget.setColumnHidden(3, True)
                    self.ui.tableWidget.setColumnHidden(4, True)
                    self.ui.tableWidget.setColumnHidden(5, True)
                    result = update(guide)
                    if(result):
                        pyautogui.alert("Rehber Güncellendi")
                        self.fillTable()
                        self.clearTextBoxes()
                        self.disabeEntryFrame()
                        return
                    else:
                        pyautogui.alert("Rehber Güncellenirken Bir Sorun Oluştu.Lütfen Daha Sonra Tekrar Deneyiniz!")
                        return
            else:
                result = pyautogui.confirm("Yeni Bir Rehber Eklenecek. Onaylıyor Musunuz?")
                if (result == "OK"):
                    guide = Guide(
                        id=None,
                        fullName=self.ui.txt_name.text(),
                        phone=self.ui.txt_phone.text(),
                        mail=self.ui.txt_mail.text(),
                        guide_type=self.ui.cmb_type.currentText(),
                        version=1
                    )
                    result = create(guide)
                    if (result):
                        pyautogui.alert("Rehber Eklendi")
                        self.fillTable()
                        self.clearTextBoxes()
                        self.disabeEntryFrame()
                        return
                    else:
                        pyautogui.alert("Rehber Oluşturulurken Bir Sorun Oluştu.Lütfen Daha Sonra Tekrar Deneyiniz!")
                        return

    def delete(self):
        if(len(self.ui.tableWidget.selectedItems())<1):
            pyautogui.alert("Lütfen Silmek İstediğiniz Rehberi Seçiniz!")
            return
        else:
            result = pyautogui.confirm("Seçilen Rehber Silinecek. Onaylıyor Musunuz?")
            if (result == "OK"):
                self.ui.tableWidget.setColumnHidden(0, False)
                self.ui.tableWidget.setColumnHidden(2, False)
                self.ui.tableWidget.setColumnHidden(3, False)
                self.ui.tableWidget.setColumnHidden(4, False)
                self.ui.tableWidget.setColumnHidden(5, False)
                item = self.ui.tableWidget.selectedItems()
                guide = Guide(
                    id=item[0].text(),
                    fullName=None,
                    phone=None,
                    mail=None,
                    guide_type=None,
                    version=item[5].text()
                )
                self.ui.tableWidget.setColumnHidden(0, True)
                self.ui.tableWidget.setColumnHidden(2, True)
                self.ui.tableWidget.setColumnHidden(3, True)
                self.ui.tableWidget.setColumnHidden(4, True)
                self.ui.tableWidget.setColumnHidden(5, True)
                result = delete(guide.id,guide.version)
                if (result):
                    pyautogui.alert("Rehber Silindi")
                    self.fillTable()
                    self.clearTextBoxes()
                    self.disabeEntryFrame()
                    return
                else:
                    pyautogui.alert("Rehber Silinirken Bir Sorun Oluştu.Lütfen Daha Sonra Tekrar Deneyiniz!")
                    return


    def disabeEntryFrame(self):
        self.ui.entry_frame.setEnabled(False)

    def fillTextBoxes(self):
        if(len(self.ui.tableWidget.selectedItems())>0):
            self.disabeEntryFrame()
            self.ui.tableWidget.setColumnHidden(0, False)
            self.ui.tableWidget.setColumnHidden(2, False)
            self.ui.tableWidget.setColumnHidden(3, False)
            self.ui.tableWidget.setColumnHidden(4, False)
            self.ui.tableWidget.setColumnHidden(5, False)
            item = self.ui.tableWidget.selectedItems()
            self.ui.txt_name.setText(item[1].text())
            self.ui.txt_phone.setText(item[2].text())
            self.ui.txt_mail.setText(item[3].text())
            self.ui.cmb_type.setCurrentText(item[4].text())
            self.ui.tableWidget.setColumnHidden(0, True)
            self.ui.tableWidget.setColumnHidden(2, True)
            self.ui.tableWidget.setColumnHidden(3, True)
            self.ui.tableWidget.setColumnHidden(4, True)
            self.ui.tableWidget.setColumnHidden(5, True)

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
        self.ui.txt_phone.setInputMask("(000)-000-00-00")
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
        baseQuery = "SELECT * FROM GUIDE WHERE "
        if(self.ui.txt_search_name.text() !=""):
            baseQuery = baseQuery + "fullname like '%"+self.ui.txt_search_name.text()+ "%' and "
        if(self.ui.cmb_search_type.currentIndex()>0):
            baseQuery = baseQuery + "guide_type= '"+self.ui.cmb_search_type.currentText()+"' and "
        return baseQuery + "status = true"


    def buttonWorks(self):
        self.ui.btn_search.clicked.connect(lambda : self.fillTable())
        self.ui.tableWidget.clicked.connect(lambda: self.mousePressEv())
        self.ui.tableWidget.itemSelectionChanged.connect(lambda: self.fillTextBoxes())
        self.ui.btn_update.clicked.connect(lambda :self.enableEntryFrame())
        self.ui.btn_save.clicked.connect(lambda : self.save())
        self.ui.btn_new.clicked.connect(lambda: self.newEntry())
        self.ui.btn_back.clicked.connect(lambda :self.backToMainPanel())
        self.ui.btn_delete.clicked.connect(lambda :self.delete())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GuideWindow()
    sys.exit(app.exec_())