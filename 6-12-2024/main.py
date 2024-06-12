# This Python file uses the following encoding: utf-8
import sys
import psycopg2 # type: ignore
from PySide6.QtCore import Qt, QRegularExpression, Signal
from PySide6.QtGui import QRegularExpressionValidator, QDoubleValidator
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QMessageBox, QTableWidgetItem, QHeaderView, QHBoxLayout, QPushButton, QSizePolicy

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
from ui_updateItemDialog import Ui_updateItemDialog
from ui_deleteItemDialog import Ui_deleteItemDialog
from ui_updateEmployeeDialog import Ui_updateEmployeeDialog
from ui_DetalisDialog import Ui_DetailsDialog

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
        self.addEmployee = addEmployee(dashboard=self)
        self.addItem = addItem(dashboard=self)
        self.product_loadTable()
        self.employee_loadTable()
        inventory_header = self.ui.products_2.horizontalHeader()
        inventory_header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        employee_header = self.ui.employees.horizontalHeader()
        employee_header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        employee_header.setSectionResizeMode(4, QHeaderView.ResizeMode.Interactive)
        history_header = self.ui.history.horizontalHeader()
        history_header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        history2_header = self.ui.history_2.horizontalHeader()
        history2_header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.logOutButton_2.clicked.connect(lambda: (self.close(), self.login.show()))
        self.ui.inventoryButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.employeeButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.historyButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.addEmployeeButton.clicked.connect(lambda: self.addEmployee.exec())
        self.ui.addItemButton_2.clicked.connect(lambda: self.addItem.exec())

    #Load table from employee
    def employee_loadTable(self):
        self.connection = psycopg2.connect(database="PTT-IT-Test",
                                           user="postgres",
                                           host="localhost",
                                           password="1190716",
                                           port=5432)
            
        self.cursor = self.connection.cursor()
        self.command = """
                            SELECT * FROM EMPLOYEE
                            ORDER BY EMPLOYEE_ID
                            """
            
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchall()
        self.ui.employees.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.ui.employees.insertRow(row_number)
            self.Empupdate_deleteButton = EmployeeButtonWidget(row_number, row_data, self)
            for column_number, column_data in enumerate(row_data):
                self.ui.employees.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))
                self.ui.employees.setCellWidget(row_number, 6, self.Empupdate_deleteButton)
                self.ui.employees.setRowHeight(row_number, 50)
        self.connection.close()
    
    #load table from products
    def product_loadTable(self):
        self.connection = psycopg2.connect(database="PTT-IT-Test",
                                           user="postgres",
                                           host="localhost",
                                           password="1190716",
                                           port=5432)
            
        self.cursor = self.connection.cursor()
        self.command = """
                            SELECT * FROM PRODUCTS
                            ORDER BY PRODUCT_ID
                            """
            
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchall()
        self.ui.products_2.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.ui.products_2.insertRow(row_number)
            self.update_deleteButton = ButtonWidget(row_number, row_data, self)
            for column_number, column_data in enumerate(row_data):
                self.ui.products_2.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))
                self.ui.products_2.setCellWidget(row_number, 5, self.update_deleteButton)
                self.ui.products_2.setRowHeight(row_number, 50)

        self.connection.close()

#creating class to display message
class DisplayMessage():
    def showMessage(self, error_message, icon_message):
        app = QApplication.instance() or QApplication([])
        message = QMessageBox()
        message.setIcon(icon_message)
        message.setText(error_message)
        message.setWindowTitle('Message')
        message.setStandardButtons(QMessageBox.StandardButton.Ok)
        message.exec()

class addEmployee(QDialog):
    def __init__(self, parent=None, dashboard=None):
        super().__init__(parent)
        self.ui = Ui_addEmployee()
        self.ui.setupUi(self)
        self.display_message = DisplayMessage()
        self.dashboard = dashboard
        regex = QRegularExpression(r"^\d{0,11}$") # validator to input only 11 digits
        validator = QRegularExpressionValidator(regex, self.ui.contactNumberInput)
        self.ui.contactNumberInput.setValidator(validator)
        self.ui.cancelButton.clicked.connect(lambda: self.close())
        self.ui.confirmButton.clicked.connect(self.insertEmployee)

    def insertEmployee(self):
        first_name = self.ui.employeeFNameInput.text().lstrip().upper()
        last_name = self.ui.employeeLNameInput_2.text().lstrip().upper()
        address = self.ui.addressInput.text().upper()
        contact_no = self.ui.contactNumberInput.text()
        if not first_name.strip() or not last_name.strip() or not address.strip() or not contact_no.strip():
            message = 'input fields'
            self.display_message.showMessage(message, QMessageBox.Icon.Critical)
            return
        if len(str(contact_no)) < 11:
            message = 'Please input 11 digits in contact number'
            self.display_message.showMessage(message, QMessageBox.Icon.Critical)
            return
        self.sqlconnection_addEmployee(first_name, last_name, address, contact_no)
        self.clearText()
        self.close()
        if self.dashboard:
            self.dashboard.employee_loadTable()
    
    def clearText(self):
        self.ui.employeeFNameInput.clear()
        self.ui.employeeLNameInput_2.clear()
        self.ui.addressInput.clear()
        self.ui.contactNumberInput.clear()

    def sqlconnection_addEmployee(self, first_name, last_name, address, contact_no):
        message = 'Successfully Added!'
        self.connection = psycopg2.connect(database="PTT-IT-Test",
                                           user="postgres",
                                           host="localhost",
                                           password="1190716",
                                           port=5432)
        
        self.cursor = self.connection.cursor()
        self.command = f"""
                            INSERT INTO EMPLOYEE(EMPLOYEE_LNAME, EMPLOYEE_FNAME, EMPLOYEE_ADDRESS, EMPLOYEE_CONT_NO)
                            VALUES('{last_name}', '{first_name}', '{address}', '{contact_no}')
                        """
        self.cursor.execute(self.command)
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        self.display_message.showMessage(message, QMessageBox.Icon.Information)

class addItem(QDialog):
    def __init__(self, parent=None, dashboard = None):
        super().__init__(parent)
        self.ui = Ui_addItemDialog()
        self.display_message = DisplayMessage()
        self.ui.setupUi(self)
        regex = QRegularExpression(r"^\d{0,32}$")
        quantity = QRegularExpressionValidator(regex, self.ui.quantityInput)
        self.ui.quantityInput.setValidator(quantity)
        regex_price = QDoubleValidator(bottom=0.0, top=99, decimals=2)
        #price = QRegExpValidator(QRegExp("[^\d\-+\.]"))
        self.ui.priceInput.setValidator(regex_price)
        self.ui.cancelButton.clicked.connect(lambda: self.close())
        self.ui.confirmButton.clicked.connect(self.insertItem)
        self.dashboard = dashboard

    def clearText(self):
        self.ui.itemNameInput.clear()
        self.ui.quantityInput.clear()
        self.ui.priceInput.clear()
        self.ui.categoryDropdown.setCurrentIndex(0)

    def insertItem(self):
        quantity = self.ui.quantityInput.text()
        name = self.ui.itemNameInput.text().lstrip().upper()
        price = self.ui.priceInput.text()
        category = self.ui.categoryDropdown.currentText()
        specs_field = self.ui.textEdit.toPlainText().lstrip()
        if not quantity.strip() or not name.strip() or not price.strip() or not specs_field.strip():
            message = 'input fields'
            self.display_message.showMessage(message, QMessageBox.Icon.Critical)
            return
        self.sqlconnection(quantity, name, price, category)
        self.clearText()
        self.close()
        if self.dashboard:
            self.dashboard.product_loadTable()

    def sqlconnection(self, quantity, name, price, category):
        message = 'Successfuly Added!'
        self.connection = psycopg2.connect(database="PTT-IT-Test",
                                           user="postgres",
                                           host="localhost",
                                           password="1190716",
                                           port=5432)
        
        self.cursor = self.connection.cursor()
        self.command = f""" INSERT INTO PRODUCTS(PRODUCT_NAME, PRODUCT_QTY, PROD_CATEGORY, PRODUCT_PRICE)
                            VALUES('{name}', '{quantity}', '{category}', '{price}')
                        """
        self.cursor.execute(self.command)
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        self.display_message.showMessage(message, QMessageBox.Icon.Information)

class purchaseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_purchaseDialog()
        self.ui.setupUi(self)

class deleteItemDialog(QDialog):
    data_update = Signal()
    def __init__(self, product_data,parent=None):
        super().__init__(parent)
        self.ui = Ui_deleteItemDialog()
        self.ui.setupUi(self)
        self.product_data = product_data

class DetailDialog(QDialog):
    data_update = Signal()
    def __init__(self, product_data,parent=None):
        super().__init__(parent)
        self.ui = Ui_DetailsDialog()
        self.ui.setupUi(self)
        self.product_data = product_data
        self.ui.categoryName.setReadOnly(True)
        self.ui.itemName.setReadOnly(True)
        self.ui.textEdit.setReadOnly(True)
        self.fields()
    
    def fields(self):
        item_name = self.ui.itemName.setText(self.product_data[1])
        category = self.ui.categoryName.setText(self.product_data[3])

class updateItemDialog(QDialog):
    data_update = Signal()
    def __init__(self, product_data,parent=None):
        super().__init__(parent)
        self.ui = Ui_updateItemDialog()
        self.ui.setupUi(self)
        self.display_message = DisplayMessage()
        regex = QRegularExpression(r"^\d{0,32}$")
        quantity = QRegularExpressionValidator(regex, self.ui.quantityInput)
        self.ui.quantityInput.setValidator(quantity)
        regex_price = QDoubleValidator(bottom=0.0, top=99, decimals=2)
        self.ui.priceInput.setValidator(regex_price)
        self.product_data = product_data
        self.fields()
        self.ui.confirmButton.clicked.connect(self.update_products)
    
    def fields(self):
        self.ui.itemNameInput.setText(self.product_data[1])
        self.ui.quantityInput.setText(str(self.product_data[2]))
        self.ui.priceInput.setText(str(self.product_data[4]))
        product = product_category = self.product_data[3]
        #specs_item = self.ui.textEdit.setText() wala pas database
        index = self.ui.categoryDropdown.findText(product_category)
        if index != -1:
            self.ui.categoryDropdown.setCurrentIndex(index)

    def update_products(self):
        #validate the fields
        item_name = self.ui.itemNameInput.text().lstrip()
        quantity = self.ui.quantityInput.text()
        price = self.ui.priceInput.text()
        category = self.ui.categoryDropdown.currentText()
        specs_item = self.ui.textEdit.toPlainText().lstrip()
        if not item_name.strip() or not quantity or not price or not specs_item.strip(): 
            message = 'input fields'
            self.display_message.showMessage(message, QMessageBox.Icon.Critical)
            return 
        self.sql_connection(item_name, quantity, price, category)

    def sql_connection(self, item_name, quantity, price, product):
        self.connection = psycopg2.connect(database="PTT-IT-Test",
                                           user="postgres",
                                           host="localhost",
                                           password="1190716",
                                           port=5432)

class updateEmployeeDialog(QDialog):
    data_update = Signal()
    def __init__(self, employee_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_updateEmployeeDialog()
        self.ui.setupUi(self)
        self.employee_data = employee_data
        self.fields()

    def fields(self):
        self.ui.employeeNameInput.setText(self.employee_data[2])
        self.ui.employeeNameInput_2.setText(self.employee_data[1])
        self.ui.addressInput.setText(str(self.employee_data[3]))
        self.ui.contactNumberInput.setText(str(self.employee_data[4]))

class EmployeeButtonWidget(QWidget):
    def __init__(self, row_number, row_data, manager):
        super().__init__()
        self.row_number = row_number
        self.row_data = row_data
        self.manager = manager
        #self.data = self.row_data[0]
    
        layout = QHBoxLayout(self)
        self.update_button = QPushButton("Update", self)
        self.update_button.setStyleSheet("background-color: blue;")
        self.update_button.setFixedSize(61,31)
        self.update_button.clicked.connect(self.update_dialog)

        # self.delete_button = QPushButton("Delete", self)
        # self.delete_button.setStyleSheet("background-color: red;")
        # self.delete_button.setFixedSize(61, 31)
        #self.delete_button.clicked.connect(self.delete)
        layout.addWidget(self.update_button)
        #layout.addWidget(self.delete_button)
    
    def update_dialog(self):
        self.update_emp = updateEmployeeDialog(self.row_data)
        self.update_emp.data_update.connect(self.manager.employee_loadTable)
        self.update_emp.exec()

class ButtonWidget(QWidget):
    def __init__(self, row_number, row_data, manager):
        super().__init__()
        self.row_number = row_number
        self.row_data = row_data
        self.manager = manager
        #self.data = self.row_data[0]

        layout = QHBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(5, 5, 5, 5)
        self.details_button = QPushButton("Details", self)
        self.details_button.setStyleSheet("background-color: grey;")
        self.details_button.setFixedSize(61,31)
        self.details_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.details_button.clicked.connect(self.details_dialog)

        self.update_button = QPushButton("Update", self)
        self.update_button.setStyleSheet("background-color: blue;")
        self.update_button.setFixedSize(61,31)
        self.update_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.update_button.clicked.connect(self.update_dialog)

        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setStyleSheet("background-color: red;")
        self.delete_button.setFixedSize(61, 31)
        self.delete_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.delete_button.clicked.connect(self.delete_dialog)
        layout.addWidget(self.details_button)
        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)

    
    def update_dialog(self):
        self.update_item = updateItemDialog(self.row_data)
        self.update_item.data_update.connect(self.manager.product_loadTable)
        self.update_item.exec()

    def delete_dialog(self):
        self.delete_item = deleteItemDialog(self.row_data)
        self.delete_item.data_update.connect(self.manager.product_loadTable)
        self.delete_item.exec()

    def details_dialog(self):
        self.details_item = DetailDialog(self.row_data)
        self.details_item.data_update.connect(self.manager.product_loadTable)
        self.details_item.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Login = LoginPage()
    # Login.show()
    Employee = EmployeeDashboard()
    Employee.show()
    Manager = ManagerDashboard()
    Manager.show()
    # Purchase = purchaseDialog()
    # Purchase.show()
    sys.exit(app.exec())
