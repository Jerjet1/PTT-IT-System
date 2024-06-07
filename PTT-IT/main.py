# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_LoginPage import Ui_LoginPage
from ui_employeeDashboard import Ui_employeeDashboard
from ui_managerDashboard import Ui_managerDashboard
from ui_purchaseDialog import Ui_purchaseDialog
from ui_addEmployee import Ui_addEmployee
from ui_addItemDialog import Ui_addItemDialog

class LoginPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginPage()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.verifyUser)
        self.ui.password.returnPressed.connect(self.verifyUser)

    def clearText(self):
        self.ui.user.clear()
        self.ui.password.clear()
        self.ui.errorMessage.clear()

    def verifyUser(self):
        self.username = self.ui.user.text()
        self.password = self.ui.password.text()

        if self.username == '' or self.password == '':
            self.ui.errorMessage.setText('Input user and password')
            return
        if self.username == 'admin' and self.password == '123456':
            self.clearText
            self.close()
            self.manager = ManagerDashboard()
            self.manager.show()
            return
        elif self.username == 'employee' and self.password == '54321':
            self.clearText
            self.close()
            self.employee = EmployeeDashboard()
            self.employee.show()
            return
        else:
            self.ui.errorMessage.setText('User or Password does not match!')


class EmployeeDashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_employeeDashboard()
        self.ui.setupUi(self)
        self.login = LoginPage()
        self.ui.logOutButton.clicked.connect(lambda: (self.close(), self.login.show()))


class ManagerDashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_managerDashboard()
        self.ui.setupUi(self)
        self.login = LoginPage()
        self.addEmployee = addEmployee()
        self.addItem = addItem()

        self.ui.logOutButton_2.clicked.connect(lambda: (self.close(), self.login.show()))
        self.ui.inventoryButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.employeeButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.historyButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.addEmployeeButton.clicked.connect(lambda: self.addEmployee.exec())
        self.ui.addItemButton_2.clicked.connect(lambda: self.addItem.exec())

class addEmployee(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_addEmployee()
        self.ui.setupUi(self)
        self.ui.cancelButton.clicked.connect(lambda: self.close())

class addItem(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_addItemDialog()
        self.ui.setupUi(self)
        self.ui.cancelButton.clicked.connect(lambda: self.close())


class purchaseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_purchaseDialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Login = LoginPage()
    Login.show()
    # Employee = EmployeeDashboard()
    # Employee.show()
    # Manager = ManagerDashboard()
    # Manager.show()
    # Purchase = purchaseDialog()
    # Purchase.show()
    sys.exit(app.exec())
