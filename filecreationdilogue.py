import os
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton,
    QLabel, QHBoxLayout, QWidget
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class ModernFileCreatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create New File")
        self.setGeometry(500, 300, 500, 200)

        # Modern styling: Minimal borders and decorations
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.CustomizeWindowHint)

        # Defer UI initialization to improve perceived load time
        self.central_widget = None
        self.initUI()

    def initUI(self):
        if self.central_widget is not None:
            return  # Avoid reinitializing UI

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Main vertical layout
        main_layout = QVBoxLayout()

        # Title label
        self.label = QLabel("Create a New File")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Segoe UI", 14, QFont.Bold))
        self.label.setStyleSheet("color: #2196F3;")  # Set color for heading (Blue)
        main_layout.addWidget(self.label)

        # Input field for file name
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Enter file name (e.g., example.txt)")
        self.input_box.setFont(QFont("Segoe UI", 16))
        self.input_box.setFixedHeight(50)
        self.input_box.setAlignment(Qt.AlignCenter)
        self.input_box.setStyleSheet("""
            QLineEdit {
                border: 2px solid #B0BEC5;
                border-radius: 10px;
                padding: 5px;
            }
            QLineEdit:focus {
                border: 2px solid rgba(238, 238, 238, 0.65);
            }
        """)
        main_layout.addWidget(self.input_box)

        # Buttons: Create and Cancel
        button_layout = QHBoxLayout()

        self.create_button = QPushButton("Create")
        self.create_button.setFont(QFont("Segoe UI", 10, QFont.Bold))
        self.create_button.setFixedSize(120, 40)
        self.create_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #2196F3;  /* Match heading color (Blue) */
                border: 2px solid transparent;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: rgba(0, 123, 255, 0.1); /* Light blue tint */
            }
            QPushButton:pressed {
                background-color: rgba(0, 123, 255, 0.2);
            }
        """)
        self.create_button.clicked.connect(self.create_file)
        button_layout.addWidget(self.create_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setFont(QFont("Segoe UI", 10, QFont.Bold))
        self.cancel_button.setFixedSize(120, 40)
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #2196F3;  /* Match heading color (Blue) */
                border: 2px solid transparent;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: rgba(255, 87, 34, 0.1); /* Light orange tint */
            }
            QPushButton:pressed {
                background-color: rgba(255, 87, 34, 0.2);
            }
        """)
        self.cancel_button.clicked.connect(self.close)
        button_layout.addWidget(self.cancel_button)

        main_layout.addLayout(button_layout)
        self.central_widget.setLayout(main_layout)

        # Keyboard shortcuts
        self.create_button.setShortcut("Return")  # Enter key for "Create"
        self.cancel_button.setShortcut("Escape")  # Escape key for "Cancel"

        # Bind Enter key to the create function when focused on the input field
        self.input_box.returnPressed.connect(self.create_file)

    def create_file(self):
        file_name = self.input_box.text().strip()
        if not file_name:
            return  # Do nothing if the file name is empty

        # Validate file name
        if any(c in file_name for c in r'\/:*?"<>|'):
            return  # Do nothing if the file name is invalid

        file_path = os.path.join(os.getcwd(), file_name)
        try:
            with open(file_path, "w") as file:
                pass
            self.close()  # Close the window immediately after file creation
        except Exception as e:
            pass  # Do nothing in case of an error


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernFileCreatorApp()
    window.show()
    sys.exit(app.exec_())
