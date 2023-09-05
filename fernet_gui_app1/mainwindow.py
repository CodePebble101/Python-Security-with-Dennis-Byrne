import logging
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_form import Ui_MainWindow
from cryptography.fernet import Fernet


class FernetCrypto(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.encription_key = None
        self.fernet = None
        self.connect_buttons()
        self.msg = QMessageBox()

    def create_messagebox(self, title: str, text: str, icon) -> None:
        self.msg.setWindowTitle(title)
        self.msg.setText(text)
        self.msg.setIcon(icon)
        self.msg.exec()

    def save_exist_key(self) -> None:
        try:
            self.encription_key = Fernet(self.ui.exist_key_editor.toPlainText().replace(" ", ""))
            print(self.encription_key.__sizeof__())
            self.ui.exist_key_editor.setEnabled(False)
        except Exception as e:
            logging.error(e)
            self.create_messagebox("Ошибка", "Ключ не прошел валидацию. Попробуйте другой ключ или сгенерируйте новый.", QMessageBox.Warning)

    def generate_new_key(self) -> None:
        try:
            key = Fernet.generate_key()
            self.encription_key = Fernet(key)
            self.ui.generated_key_editor.setText(key.decode("utf8"))
            self.ui.exist_key_editor.setText(key.decode("utf8"))
            self.ui.exist_key_editor.setEnabled(False)
            self.ui.key_input_button.setEnabled(False)
            self.ui.key_generate_button.setEnabled(False)
        except Exception as e:
            logging.error(e)
            self.create_messagebox("Ошибка", "Ошибка при генерации нового ключа", QMessageBox.Warning)

    def encrypt_data(self) -> None:
        try:
            text_to_encrypt = self.ui.encrypt_input_editor.toPlainText()
            encrypted_text = self.encription_key.encrypt(data=text_to_encrypt.encode("utf-8"))
            self.ui.encrypt_output_editor.setText(encrypted_text.decode("utf8"))
        except Exception as e:
            logging.error(e)
            self.create_messagebox("Ошибка", "Ошибка при зашифровывании данных", QMessageBox.Warning)

    def decrypt_data(self) -> None:
        try:
            token_to_decrypt = self.ui.decrypt_input_editor.toPlainText()
            decrypted_text = self.encription_key.decrypt(token_to_decrypt.encode("utf-8"))
            self.ui.decrypt_output_editor.setText(decrypted_text.decode("utf8"))
        except Exception as e:
            logging.error(e)
            self.create_messagebox("Ошибка", "Ошибка при расшифровывании данных", QMessageBox.Warning)

    def connect_buttons(self) -> None:
        self.ui.key_input_button.clicked.connect(self.save_exist_key)
        self.ui.key_generate_button.clicked.connect(self.generate_new_key)
        self.ui.encrypt_button.clicked.connect(self.encrypt_data)
        self.ui.decrypt_button.clicked.connect(self.decrypt_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = FernetCrypto()
    widget.show()
    sys.exit(app.exec())
