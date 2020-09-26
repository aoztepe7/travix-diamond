import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from ui.ui_panel import Ui_MainPanel
from area.area import AreaWindow
from guide.guide import GuideWindow
from opr.operator import OperatorWindow
import db.db_user

class PanelWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainPanel()
        self.ui.setupUi(self)
        self.userAuth()
        self.buttonWorks()
        self.show()

    def openAreaDefPanel(self):
        self.window = AreaWindow()
        self.window.show()
        self.hide()

    def openGuideDefPanel(self):
        self.window = GuideWindow()
        self.window.show()
        self.hide()

    def openOperatorDefPanel(self):
        self.window = OperatorWindow()
        self.window.show()
        self.hide()

    def userAuth(self):
        role = db.db_user.GL_USER_ROLE
        if(role == 'USER'):
            self.ui.btn_calculate.setEnabled(False)
            self.ui.btn_receive.setEnabled(False)
            self.ui.btn_target.setEnabled(False)
            self.ui.groupBox_2.setEnabled(False)

    def buttonWorks(self):
        # AREA DEF BUTTON
        self.ui.btn_area.clicked.connect(lambda:self.openAreaDefPanel())

        # GUIDE DEF BUTTON
        self.ui.btn_guide.clicked.connect(lambda: self.openGuideDefPanel())

        # OPERATOR DEF BUTTON
        self.ui.btn_operator.clicked.connect(lambda: self.openOperatorDefPanel())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PanelWindow()
    sys.exit(app.exec_())