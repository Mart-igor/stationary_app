import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                              QVBoxLayout, QWidget, QMessageBox, QFileDialog)
from PySide6.QtCore import QStandardPaths, QFile, QIODevice

class DownloadWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Кнопка для скачивания тестовых данных
        btn_download = QPushButton("Скачать тестовые данные", self)
        btn_download.clicked.connect(self.download_sample_file)
        layout.addWidget(btn_download)
        
        self.setWindowTitle("Скачивание файлов")
        self.resize(300, 150)
    
    def download_sample_file(self):
        """Скачивание вашего CSV файла с выбором места сохранения"""
        # Путь к вашему исходному CSV-файлу
        source_file = r"D:\projects\qt_designer\stationary_app\data\Igor2.csv"
        
        # Проверяем существует ли исходный файл
        if not os.path.exists(source_file):
            QMessageBox.critical(self, "Ошибка", f"Исходный файл не найден:\n{source_file}")
            return
        
        # Получаем путь к папке "Загрузки" на Windows
        downloads_path = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
        
        # Предлагаем сохранить файл
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить CSV файл",
            os.path.join(downloads_path, "Igor2.csv"),  # Имя файла по умолчанию
            "CSV Files (*.csv);;All Files (*)"
        )
        
        if not file_path:
            return  # Пользователь отменил
        
        try:
            # Копируем файл побайтно
            with open(source_file, 'rb') as src_file:
                with open(file_path, 'wb') as dst_file:
                    dst_file.write(src_file.read())
            
            # Показываем сообщение об успехе с кнопкой "Открыть папку"
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Успешно")
            msg.setText(f"Файл успешно сохранен:\n{file_path}")
            msg.addButton("OK", QMessageBox.AcceptRole)
            open_button = msg.addButton("Открыть папку", QMessageBox.ActionRole)
            msg.exec_()
            
            if msg.clickedButton() == open_button:
                os.startfile(os.path.dirname(file_path))  # Открываем папку с файлом
                
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл:\n{str(e)}")

if __name__ == "__main__":
    # Настройки для корректного отображения в Windows
    if sys.platform == "win32":
        import ctypes
        myappid = 'mycompany.myproduct.subproduct.version'  # Уникальный ID
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    app = QApplication(sys.argv)
    window = DownloadWindow()
    window.show()
    sys.exit(app.exec())