from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit
from ui_form import Ui_Widget
from ui_config import Ui_Form
import sys
import subprocess
import configparser

class ConfigDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.load_settings()

    def load_settings(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Получаем настройки из конфига
        api_key = config.get('API', 'api_key')
        api_key2 = config.get('API', 'api_key2')
        promt = config.get('API', 'promt')
        max_attempts = config.get('API', 'max_attempts')
        detail = config.get('API', 'detail')
        model = config.get('API', 'model')
        temp = config.get('API', 'temp')
        max_tokens = config.get('API', 'max_tokens')

        # Отображаем настройки в Line Edit
        self.ui.lineEdit.setText(api_key)
        self.ui.lineEdit_2.setText(api_key2)
        self.ui.lineEdit_3.setText(promt)
        self.ui.lineEdit_4.setText(max_attempts)
        self.ui.lineEdit_5.setText(detail)
        self.ui.lineEdit_6.setText(model)
        self.ui.lineEdit_7.setText(temp)
        self.ui.lineEdit_8.setText(max_tokens)

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.config_dialog = ConfigDialog()  # Создаем экземпляр диалогового окна

        # Добавляем слоты к кнопкам
        self.ui.pushButton.clicked.connect(self.on_config_button_clicked)
        self.ui.pushButton_2.clicked.connect(self.on_start_button_clicked)

    # Слоты для каждой кнопки
    def on_config_button_clicked(self):
        self.config_dialog.show()  # Показываем диалоговое окно

    def on_start_button_clicked(self):
        subprocess.Popen(["python", "Main.py"])

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
