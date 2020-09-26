import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from ui.ui_area import Ui_MainWindow
from area.obj_area import Area
import panel.panel
from db.db_area import update,create,delete,list
import pyautogui
GL_UPDATE = 0

class AreaWindow(QMainWindow):
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

    def newEntry(self):
        global GL_UPDATE
        GL_UPDATE = 0
        self.clearTextBoxes()
        self.ui.entry_frame.setEnabled(True)

    def fieldChecker(self):
        if(self.ui.txt_name.text()==""):
            return False
        else:
            return True

    def save(self):
        fieldControl = self.fieldChecker()
        if (fieldControl == False):
            pyautogui.alert("Bölge Adı Boş Olamaz!")
            return
        else:
            if(GL_UPDATE == 1):
                result = pyautogui.confirm("Seçilen Bölge Güncellenecek. Onaylıyor Musunuz?")
                if (result == "OK"):
                    self.ui.tableWidget.setColumnHidden(0, False)
                    self.ui.tableWidget.setColumnHidden(2, False)
                    item = self.ui.tableWidget.selectedItems()
                    area = Area(
                        id= item[0].text(),
                        name= self.ui.txt_name.text(),
                        version=item[2].text()
                    )
                    self.ui.tableWidget.setColumnHidden(0, True)
                    self.ui.tableWidget.setColumnHidden(2, True)
                    result = update(area)
                    if(result):
                        pyautogui.alert("Bölge Güncellendi")
                        self.fillTable()
                        self.clearTextBoxes()
                        self.disabeEntryFrame()
                        return
                    else:
                        pyautogui.alert("Bölge Güncellenirken Bir Sorun Oluştu.Lütfen Daha Sonra Tekrar Deneyiniz!")
                        return
            else:
                result = pyautogui.confirm("Yeni Bir Bölge Eklenecek. Onaylıyor Musunuz?")
                if (result == "OK"):
                    self.ui.tableWidget.setColumnHidden(0, False)
                    self.ui.tableWidget.setColumnHidden(2, False)
                    area = Area(
                        id=None,
                        name=self.ui.txt_name.text(),
                        version=1
                    )
                    self.ui.tableWidget.setColumnHidden(0, True)
                    self.ui.tableWidget.setColumnHidden(2, True)
                    result = create(area)
                    if (result):
                        pyautogui.alert("Bölge Eklendi")
                        self.fillTable()
                        self.clearTextBoxes()
                        self.disabeEntryFrame()
                        return
                    else:
                        pyautogui.alert("Bölge Oluşturulurken Bir Sorun Oluştu.Lütfen Daha Sonra Tekrar Deneyiniz!")
                        return

    def delete(self):
        if(len(self.ui.tableWidget.selectedItems())<1):
            pyautogui.alert("Lütfen Silmek İstediğiniz Bölgeyi Seçiniz!")
            return
        else:
            result = pyautogui.confirm("Seçilen Bölge Silinecek. Onaylıyor Musunuz?")
            if (result == "OK"):
                self.ui.tableWidget.setColumnHidden(0, False)
                self.ui.tableWidget.setColumnHidden(2, False)
                item = self.ui.tableWidget.selectedItems()
                area = Area(
                    id=item[0].text(),
                    name=item[1].text(),
                    version=item[2].text()
                )
                self.ui.tableWidget.setColumnHidden(0, True)
                self.ui.tableWidget.setColumnHidden(2, True)
                result = delete(area.id,area.version)
                if (result):
                    pyautogui.alert("Bölge Silindi")
                    self.fillTable()
                    self.clearTextBoxes()
                    self.disabeEntryFrame()
                    return
                else:
                    pyautogui.alert("Bölge Silinirken Bir Sorun Oluştu.Lütfen Daha Sonra Tekrar Deneyiniz!")
                    return


    def disabeEntryFrame(self):
        self.ui.entry_frame.setEnabled(False)

    def fillTextBoxes(self):
        if(len(self.ui.tableWidget.selectedItems())>0):
            self.disabeEntryFrame()
            self.ui.tableWidget.setColumnHidden(0, False)
            self.ui.tableWidget.setColumnHidden(2, False)
            item = self.ui.tableWidget.selectedItems()
            self.ui.txt_name.setText(item[1].text())
            self.ui.tableWidget.setColumnHidden(0, True)
            self.ui.tableWidget.setColumnHidden(2, True)

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnHidden(0, True)
        self.ui.tableWidget.setColumnHidden(2, True)
        self.buttonWorks()
        self.ui.entry_frame.setEnabled(False)
        self.show()

    def fillTable(self):
        areaList = list(self.queryBuilder())
        if(areaList):
            self.ui.tableWidget.setRowCount(0)
            for row, item in enumerate(areaList):
                self.ui.tableWidget.insertRow(row)
                for column, item in enumerate(item):
                    qtItem = QTableWidgetItem(str(item))
                    qtItem.setTextAlignment(Qt.AlignHCenter)
                    self.ui.tableWidget.setItem(row,column,qtItem)




    def queryBuilder(self):
        baseQuery = "SELECT * FROM AREA WHERE "
        if(self.ui.txt_search_area.text() !=""):
            return baseQuery + "name like '%"+self.ui.txt_search_area.text()+ "%' and status = true"
        else:
            return baseQuery + "status = true"


    def buttonWorks(self):
        self.ui.btn_search.clicked.connect(lambda : self.fillTable())
        self.ui.tableWidget.clicked.connect(lambda: self.mousePressEv())
        self.ui.tableWidget.itemSelectionChanged.connect(lambda: self.fillTextBoxes())
        self.ui.btn_update.clicked.connect(lambda :self.enableEntryFrame())
        self.ui.btn_save.clicked.connect(lambda : self.save())
        self.ui.btn_new.clicked.connect(lambda: self.newEntry())
        self.ui.btn_back.clicked.connect(lambda :self.backToMainPanel())
        self.ui.btn_back_2.clicked.connect(lambda :self.delete())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AreaWindow()
    sys.exit(app.exec_())