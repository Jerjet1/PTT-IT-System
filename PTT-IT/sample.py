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

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox, QLineEdit, QHBoxLayout

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

    def add_product_widget(self):
        # Create a horizontal layout to hold the combo box and line edit
        product_layout = QHBoxLayout()

        # Create a combo box and add items
        combo_box = QComboBox()
        combo_box.addItems(["Motherboard", "RAM", "CPU"])
        product_layout.addWidget(combo_box)

        # Create a line edit for quantity input
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Enter quantity")
        product_layout.addWidget(line_edit)

        # Add the product layout to the main layout
        self.layout.addLayout(product_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())