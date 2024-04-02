from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from ui_form import Ui_Widget
from ui_ui_config import Ui_Form
import sys
import subprocess

class ConfigDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

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
