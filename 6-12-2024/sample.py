# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QLineEdit

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("ComboBox to LineEdit Example")
#         self.setGeometry(100, 100, 300, 200)

#         # Create a central widget and set a layout
#         central_widget = QWidget()
#         layout = QVBoxLayout(central_widget)
#         self.setCentralWidget(central_widget)

#         # Create a combo box and add items
#         self.combo_box = QComboBox()
#         self.combo_box.addItems(["Select an option", "Show LineEdit", "Another option"])
#         layout.addWidget(self.combo_box)

#         # Create a line edit and initially hide it
#         self.line_edit = QLineEdit()
#         self.line_edit.setPlaceholderText("Input here...")
#         self.line_edit.hide()
#         layout.addWidget(self.line_edit)

#         # Connect the combo box selection change signal to a slot
#         self.combo_box.currentIndexChanged.connect(self.on_combobox_changed)

#     def on_combobox_changed(self, index):
#         if self.combo_box.itemText(index) == "Show LineEdit":
#             self.line_edit.show()
#         else:
#             self.line_edit.hide()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())

# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox, QLineEdit, QHBoxLayout

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Product Selection Example")
#         self.setGeometry(100, 100, 400, 300)

#         # Create a central widget and set a layout
#         central_widget = QWidget()
#         self.layout = QVBoxLayout(central_widget)
#         self.setCentralWidget(central_widget)

#         # Create a button to add product selection widgets
#         self.add_product_button = QPushButton("Add Product")
#         self.add_product_button.clicked.connect(self.add_product_widget)
#         self.layout.addWidget(self.add_product_button)

#     def add_product_widget(self):
#         # Create a horizontal layout to hold the combo box and line edit
#         product_layout = QHBoxLayout()

#         # Create a combo box and add items
#         combo_box = QComboBox()
#         combo_box.addItems(["Motherboard", "RAM", "CPU"])
#         product_layout.addWidget(combo_box)

#         # Create a line edit for quantity input
#         line_edit = QLineEdit()
#         line_edit.setPlaceholderText("Enter quantity")
#         product_layout.addWidget(line_edit)

#         # Add the product layout to the main layout
#         self.layout.addLayout(product_layout)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())

import sys
#import psycopg2
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox, QLineEdit, QHBoxLayout

# Sample data for product categories and their respective items
product_categories = {
    "Motherboard": ["ASUS", "Gigabyte", "MSI"],
    "RAM": ["Corsair", "Kingston", "G.Skill"],
    "CPU": ["Intel", "AMD"]
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Product Selection Example")
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget and set a layout
        central_widget = QWidget()
        self.layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Create a button to add product selection widgets
        self.add_product_button = QPushButton("Add Product")
        self.add_product_button.clicked.connect(self.add_product_widget)
        self.layout.addWidget(self.add_product_button)

        # List to store product selection widgets
        self.product_widgets = []

    def add_product_widget(self):
        if len(self.product_widgets) >= 5:
            self.add_product_button.setEnabled(False)
            return
        # Create a horizontal layout to hold the combo boxes and line edit
        product_layout = QHBoxLayout()

        # Create a category combo box and add categories
        category_combo_box = QComboBox()
        category_combo_box.addItems(product_categories.keys())
        product_layout.addWidget(category_combo_box)

        # Create a product combo box, initially empty
        product_combo_box = QComboBox()
        product_layout.addWidget(product_combo_box)

        # Update the product combo box based on the selected category
        category_combo_box.currentIndexChanged.connect(
            lambda: self.update_product_combo_box(category_combo_box, product_combo_box)
        )
        self.update_product_combo_box(category_combo_box, product_combo_box)

        # Create a line edit for quantity input
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Enter quantity")
        product_layout.addWidget(line_edit)

        # Add the product layout to the main layout
        self.layout.addLayout(product_layout)

         # Create a button to remove the product widget
        remove_button = QPushButton("X")
        remove_button.clicked.connect(lambda: self.remove_product_widget(product_layout))
        product_layout.addWidget(remove_button)

        # Add the product layout to the main layout
        self.layout.addLayout(product_layout)

        # Store the widgets in a list for later retrieval
        self.product_widgets.append((category_combo_box, product_combo_box, line_edit))

        # Save the current product selection to the database
        #self.save_to_database(category_combo_box.currentText(), product_combo_box.currentText(), line_edit.text())

    def remove_product_widget(self, product_layout):
        # Find the index of the product layout in the main layout
        index = self.layout.indexOf(product_layout)

        # Remove the layout and its widgets
        if index != -1:
            item = self.layout.itemAt(index)
            self.clear_layout(item.layout())
            self.layout.removeItem(item)
            self.product_widgets.pop(index - 1)

        # Enable the add product button if the number of product widgets is less than 5
        if len(self.product_widgets) < 5:
            self.add_product_button.setDisabled(False)

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


    def update_product_combo_box(self, category_combo_box, product_combo_box):
        # Get the selected category
        selected_category = category_combo_box.currentText()

        # Clear the current items in the product combo box
        product_combo_box.clear()

        # Add the products corresponding to the selected category
        if selected_category in product_categories:
            product_combo_box.addItems(product_categories[selected_category])

    def save_to_database(self, category, product_name, quantity):
        # Database connection parameters
        conn = psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        cursor = conn.cursor()

        # Insert the product selection into the database
        cursor.execute(
            "INSERT INTO product_selections (product_name, quantity) VALUES (%s, %s)",
            (product_name, quantity)
        )

        # Commit the transaction and close the connection
        conn.commit()
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
# from PySide6.QtWidgets import QApplication, QMessageBox

# def show_message(error_message):
#     app = QApplication.instance() or QApplication([])
#     message_box = QMessageBox()
#     message_box.setIcon(QMessageBox.Icon.Critical)
#     message_box.setText(error_message)
#     message_box.setWindowTitle('Error')
#     message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    
#     # Apply style sheet
#     message_box.setStyleSheet("""
#         QMessageBox {
#             background-color: #2d2d2d;
#             color: #ffffff;
#             font-size: 14px;
#         }
#         QPushButton {
#             background-color: #5b5b5b;
#             color: #ffffff;
#             border-radius: 5px;
#             padding: 5px 10px;
#             font-size: 14px;
#         }
#         QPushButton:hover {
#             background-color: #777777;
#         }
#     """)
    
#     message_box.exec()

# if __name__ == "__main__":
#     show_message("This is a styled error message.")


# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QDialog, QLabel, QLineEdit, QHBoxLayout, QWidget

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Product Table')
#         self.setGeometry(100, 100, 600, 400)

#         # Main layout
#         layout = QVBoxLayout()
#         self.table = QTableWidget(2, 5)  # 2 rows, 5 columns
#         self.table.setHorizontalHeaderLabels(['Product Name', 'PC Part', 'Price', 'Quantity', 'Actions'])
        
#         # Add sample data
#         products = [
#             {'name': 'cpu1', 'part': 'CPU', 'price': 1.0, 'quantity': 14},
#             {'name': 'ram1', 'part': 'RAM', 'price': 1.0, 'quantity': 21},
#         ]

#         for i, product in enumerate(products):
#             self.table.setItem(i, 0, QTableWidgetItem(product['name']))
#             self.table.setItem(i, 1, QTableWidgetItem(product['part']))
#             self.table.setItem(i, 2, QTableWidgetItem(str(product['price'])))
#             self.table.setItem(i, 3, QTableWidgetItem(str(product['quantity'])))

#             order_button = QPushButton('Order')
#             order_button.clicked.connect(lambda _, row=i: self.order_product(row))
#             self.table.setCellWidget(i, 4, order_button)

#         layout.addWidget(self.table)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#         # Order dialog
#         self.order_dialog = QDialog(self)
#         self.order_dialog.setWindowTitle('Order Dialog')
#         self.order_layout = QVBoxLayout()
        
#         self.customer_name_label = QLabel("Customer Name")
#         self.customer_name_input = QLineEdit()
        
#         self.order_table = QTableWidget(0, 4)  # Empty table initially
#         self.order_table.setHorizontalHeaderLabels(['Product Name', 'Price', 'Quantity', 'Actions'])
        
#         self.confirm_button = QPushButton('Confirm Order')
#         self.cancel_button = QPushButton('Cancel Order')
        
#         self.order_layout.addWidget(self.customer_name_label)
#         self.order_layout.addWidget(self.customer_name_input)
#         self.order_layout.addWidget(self.order_table)
#         self.order_layout.addWidget(self.confirm_button)
#         self.order_layout.addWidget(self.cancel_button)
        
#         self.order_dialog.setLayout(self.order_layout)

#     def order_product(self, row):
#         product_name = self.table.item(row, 0).text()
#         price = self.table.item(row, 2).text()
#         quantity = self.table.item(row, 3).text()
        
#         # Add product to order table
#         order_row_count = self.order_table.rowCount()
#         self.order_table.insertRow(order_row_count)
#         self.order_table.setItem(order_row_count, 0, QTableWidgetItem(product_name))
#         self.order_table.setItem(order_row_count, 1, QTableWidgetItem(price))
#         self.order_table.setItem(order_row_count, 2, QTableWidgetItem(quantity))
        
#         # Disable the order button in the main table
#         order_button = self.table.cellWidget(row, 4)
#         order_button.setDisabled(True)

#         # Show the order dialog
#         self.order_dialog.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
