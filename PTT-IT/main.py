# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_LoginPage import Ui_LoginPage
from ui_employeeDashboard import Ui_employeeDashboard
from ui_managerDashboard import Ui_managerDashboard
from ui_purchaseDialog import Ui_purchaseDialog

class LoginPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginPage()
        self.ui.setupUi(self)

class EmployeeDashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_employeeDashboard()
        self.ui.setupUi(self)

class ManagerDashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_managerDashboard()
        self.ui.setupUi(self)

class purchaseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_purchaseDialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Login = LoginPage()
    Login.show()
    Employee = EmployeeDashboard()
    Employee.show()
    Manager = ManagerDashboard()
    Manager.show()
    Purchase = purchaseDialog()
    Purchase.show()
    sys.exit(app.exec())
