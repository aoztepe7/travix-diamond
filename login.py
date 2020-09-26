import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from ui.ui_login import Ui_LoginPanel
from panel.panel import PanelWindow
import db.db_user
import pyautogui

class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoginPanel()
        self.ui.setupUi(self)
        self.buttonWorks()
        self.show()

    def openPanel(self):
        self.window = PanelWindow()
        self.window.show()
        self.hide()


    def loginUser(self,username,password):
        result = db.db_user.logIn(username,password)
        if(result):
            self.openPanel()
        else:
            pyautogui.alert("Giriş Hatalı")


    def buttonWorks(self):
        # LOG IN BUTTON
        self.ui.btn_login.clicked.connect(
            lambda: self.loginUser(self.ui.txt_username.text(), self.ui.txt_password.text()))

        # CLOSE BUTTON
        self.ui.btn_close.clicked.connect(lambda: self.close())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())