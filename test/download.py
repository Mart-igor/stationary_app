import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                              QVBoxLayout, QWidget, QMessageBox, QFileDialog)
from PySide6.QtCore import QStandardPaths, QFile, QIODevice

class CsvDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.csv_file = "D:\projects\qt_designer\stationary_app\data\Igor2.csv"  # Имя вашего CSV-файла в папке проекта
        self.setup_ui()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        btn_download = QPushButton("Скачать CSV файл", self)
        btn_download.clicked.connect(self.download_csv)
        layout.addWidget(btn_download)
        
        self.setWindowTitle("Скачивание CSV")
        self.resize(300, 150)
    
    def get_csv_path(self):
        """Получает полный путь к CSV-файлу в папке проекта"""
        # Получаем путь к директории скрипта
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Возвращаем полный путь к файлу
        return os.path.join(script_dir, self.csv_file)
    
    def download_csv(self):
        """Копирует CSV файл из папки проекта в выбранное место"""
        source_path = self.get_csv_path()
        
        # Проверяем существует ли исходный файл
        if not os.path.exists(source_path):
            QMessageBox.critical(self, "Ошибка", f"Файл не найден:\n{source_path}")
            return
        
        # Предлагаем выбрать место сохранения
        downloads_path = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить CSV файл",
            os.path.join(downloads_path, self.csv_file),
            "CSV Files (*.csv);;All Files (*)"
        )
        
        if not file_path:
            return  # Пользователь отменил
        
        try:
            # Копируем файл
            with open(source_path, 'rb') as src, open(file_path, 'wb') as dst:
                dst.write(src.read())
            
            # Показываем сообщение об успехе
            self.show_success_message(file_path)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл:\n{str(e)}")
    
    def show_success_message(self, file_path):
        """Показывает сообщение об успешном сохранении"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Успешно")
        msg.setText(f"CSV файл сохранен:\n{os.path.basename(file_path)}")
        msg.setDetailedText(f"Полный путь: {file_path}")
        
        open_button = msg.addButton("Открыть папку", QMessageBox.ActionRole)
        msg.addButton("OK", QMessageBox.AcceptRole)
        
        msg.exec_()
        
        if msg.clickedButton() == open_button:
            # Открываем папку с файлом в проводнике Windows
            os.startfile(os.path.dirname(file_path))

if __name__ == "__main__":
    # Настройки для Windows
    if sys.platform == "win32":
        import ctypes
        ctypes.windll.shell32.Set