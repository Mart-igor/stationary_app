import sys
import pandas as pd
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                             QWidget, QPushButton, QTableWidget, 
                             QTableWidgetItem, QFileDialog, QMessageBox)
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtGui import (QTextDocument, QTextCursor, QTextTableFormat, 
                          QTextCharFormat, QColor, QTextFrameFormat)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Создаем тестовый DataFrame
        self.data = pd.DataFrame({
            'ID': [1, 2, 3, 4],
            'Название': ['Товар A', 'Товар B', 'Товар C', 'Товар D'],
            'Цена': [10.5, 20.3, 15.2, 8.7],
            'Наличие': [1, 0, 1, 0]  # 1 = есть, 0 = нет
        })
        
        self.setup_ui()
    
    def setup_ui(self):
        """Настройка интерфейса"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Кнопка экспорта в PDF
        btn_pdf = QPushButton("Экспорт в PDF", self)
        btn_pdf.clicked.connect(self.export_to_pdf)
        layout.addWidget(btn_pdf)
        
        # Кнопка экспорта в CSV
        btn_csv = QPushButton("Экспорт в CSV", self)
        btn_csv.clicked.connect(self.export_to_csv)
        layout.addWidget(btn_csv)
        
        # Таблица для отображения данных
        self.table = QTableWidget()
        self.update_table()
        layout.addWidget(self.table)
        
        self.setWindowTitle("Экспорт данных")
        self.resize(600, 400)
    
    def update_table(self):
        """Обновление таблицы"""
        self.table.setRowCount(len(self.data))
        self.table.setColumnCount(len(self.data.columns))
        self.table.setHorizontalHeaderLabels(self.data.columns)
        
        for i, row in self.data.iterrows():
            for j, value in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(value)))
    
    def export_to_pdf(self):
        """Экспорт в PDF"""
        filename, _ = QFileDialog.getSaveFileName(
            self, "Сохранить PDF", "", "PDF Files (*.pdf)")
        
        if filename:
            try:
                printer = QPrinter(QPrinter.HighResolution)
                printer.setOutputFormat(QPrinter.PdfFormat)
                printer.setOutputFileName(filename)
                
                doc = QTextDocument()
                cursor = QTextCursor(doc)
                
                # Заголовок
                title_format = QTextCharFormat()
                title_format.setFontPointSize(14)
                title_format.setFontWeight(75)
                cursor.insertText("Отчет\n", title_format)
                
                # Таблица
                table_format = QTextTableFormat()
                table_format.setAlignment(Qt.AlignHCenter)
                table_format.setBorderStyle(QTextFrameFormat.BorderStyle_Solid)
                
                table = cursor.insertTable(
                    self.data.shape[0] + 1, 
                    self.data.shape[1], 
                    table_format
                )
                
                # Заголовки
                for col in range(self.data.shape[1]):
                    cursor.insertText(self.data.columns[col])
                    cursor.movePosition(QTextCursor.NextCell)
                
                # Данные
                for row in range(self.data.shape[0]):
                    for col in range(self.data.shape[1]):
                        cursor.insertText(str(self.data.iloc[row, col]))
                        cursor.movePosition(QTextCursor.NextCell)
                
                doc.print_(printer)
                QMessageBox.information(self, "Успех", "PDF успешно сохранен!")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")
    
    def export_to_csv(self):
        """Экспорт в CSV"""
        filename, _ = QFileDialog.getSaveFileName(
            self, "Сохранить CSV", "", "CSV Files (*.csv)")
        
        if filename:
            try:
                self.data.to_csv(filename, index=False, encoding='utf-8-sig', sep=';')
                QMessageBox.information(self, "Успех", "CSV успешно сохранен!")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())