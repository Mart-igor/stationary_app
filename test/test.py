from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                              QWidget, QPushButton, QTableWidget, 
                              QTableWidgetItem, QFileDialog)
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtGui import (QTextDocument, QTextCursor, QTextTableFormat, 
                          QTextCharFormat, QColor, QTextFrameFormat)
from PySide6.QtCore import Qt
import pandas as pd
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Создаем тестовый DataFrame
        self.data = pd.DataFrame({
            'ID': [1, 2, 3, 4],
            'Name': ['Item A', 'Item B', 'Item C', 'Item D'],
            'Value': [10.5, 20.3, 15.2, 8.7],
            'Status': [1, 0, 1, 0]  # 1 = активен, 0 = неактивен
        })
        
        
        # Настройка интерфейса
        self.setup_ui()
        
    
    def setup_ui(self):
        """Инициализация пользовательского интерфейса"""
        # Основной виджет и layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Кнопка экспорта в PDF
        btn_export = QPushButton("Экспорт в PDF")
        btn_export.clicked.connect(self.export_to_pdf)
        layout.addWidget(btn_export)
        
        # Таблица для отображения данных
        self.table = QTableWidget()
        self.table.setRowCount(len(self.data))
        self.table.setColumnCount(len(self.data.columns))
        self.table.setHorizontalHeaderLabels(self.data.columns)
        
        # Заполняем таблицу данными
        for i, row in self.data.iterrows():
            for j, value in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(value)))
        
        layout.addWidget(self.table)
    
    def export_to_pdf(self):
        """Экспорт DataFrame в PDF"""
        filename, _ = QFileDialog.getSaveFileName(
            self, "Сохранить как PDF", "", "PDF Files (*.pdf)")
        
        if not filename:
            return  # Пользователь отменил
        
        # Создаем принтер и документ
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(filename)
        
        doc = QTextDocument()
        cursor = QTextCursor(doc)
        
        # Форматирование
        title_format = QTextCharFormat()
        title_format.setFontPointSize(14)
        title_format.setFontWeight(75)  # Bold
        
        # Добавляем заголовок
        cursor.insertText("Отчет по данным\n", title_format)
        cursor.insertBlock()
        
        # Создаем таблицу в документе
        table_format = QTextTableFormat()
        table_format.setAlignment(Qt.AlignHCenter)
        table_format.setCellPadding(4)
        table_format.setCellSpacing(0)
        table_format.setBorder(1)
        table_format.setBorderStyle(QTextFrameFormat.BorderStyle_Solid)
        
        table = cursor.insertTable(
            self.data.shape[0] + 1,  # +1 для заголовков
            self.data.shape[1],
            table_format
        )
        
        # Добавляем заголовки столбцов
        for col in range(self.data.shape[1]):
            cursor.insertText(self.data.columns[col])
            cursor.movePosition(QTextCursor.NextCell)
        
        # Добавляем данные
        for row in range(self.data.shape[0]):
            for col in range(self.data.shape[1]):
                cursor.insertText(str(self.data.iloc[row, col]))
                cursor.movePosition(QTextCursor.NextCell)
        
        # Печатаем документ
        doc.print_(printer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec())