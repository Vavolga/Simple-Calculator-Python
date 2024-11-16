import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QGridLayout, QWidget
from PyQt5 import uic
from PyQt5.QtCore import Qt

# Load the UI files created with Qt Designer
class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Halaman Masuk")
        self.setFixedSize(300, 150)
        
        # Layout untuk login
        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Masukkan Username")
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Masukkan Password")
        
        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.on_login)

        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def on_login(self):
        # Cek username dan password (untuk demo, username: admin dan password: admin)
        if self.username_input.text() == "admin" and self.password_input.text() == "admin":
            self.accept()
        else:
            self.username_input.clear()
            self.password_input.clear()

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator")
        self.setFixedSize(400, 500)

        # Set up kalkulator
        self.result = QLineEdit(self)
        self.result.setAlignment(Qt.AlignRight)
        self.result.setReadOnly(True)
        self.result.setFixedHeight(50)

        self.grid_layout = QGridLayout()

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]

        for button_text, row, col in buttons:
            button = QPushButton(button_text, self)
            button.clicked.connect(self.on_button_click)
            self.grid_layout.addWidget(button, row, col)

        self.quit_button = QPushButton("Keluar", self)
        self.quit_button.clicked.connect(self.on_quit)
        self.grid_layout.addWidget(self.quit_button, 4, 0, 1, 4)

        # Set layout untuk kalkulator
        main_widget = QWidget(self)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.result)
        main_layout.addLayout(self.grid_layout)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.current_input = ""
        self.setStyleSheet("font-size: 18px;")

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.current_input = ""
        elif text == '=':
            try:
                self.current_input = str(eval(self.current_input))
            except Exception as e:
                self.current_input = "Error"
        else:
            self.current_input += text

        self.result.setText(self.current_input)

    def on_quit(self):
        self.close()
        self.terima_kasih_dialog()

    def terima_kasih_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Terima Kasih")
        dialog.setFixedSize(250, 100)
        
        layout = QVBoxLayout()
        label = QLabel("Terima kasih telah menggunakan aplikasi kalkulator!", self)
        layout.addWidget(label)

        dialog.setLayout(layout)
        dialog.exec_()
        QApplication.quit()

def main():
    app = QApplication(sys.argv)

    login_window = LoginWindow()

    if login_window.exec_() == QDialog.Accepted:
        calculator_window = CalculatorWindow()
        calculator_window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
