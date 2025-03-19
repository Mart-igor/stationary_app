from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QFileDialog, QComboBox, QLabel
)
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.dates as mdates


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSV to Graph Example")
        self.setGeometry(100, 100, 800, 600)

        # Основной виджет и layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Кнопка для загрузки CSV
        self.load_button = QPushButton("Load CSV")
        self.load_button.clicked.connect(self.load_csv)
        self.layout.addWidget(self.load_button)

        # Выпадающие списки для выбора столбцов
        self.combo_x = QComboBox()
        self.combo_y = QComboBox()
        self.layout.addWidget(QLabel("Выберите столбец для оси X:"))
        self.layout.addWidget(self.combo_x)
        self.layout.addWidget(QLabel("Выберите столбец для оси Y:"))
        self.layout.addWidget(self.combo_y)

        # Кнопка для построения графика
        self.plot_button = QPushButton("Построить график")
        self.plot_button.clicked.connect(self.plot_graph)
        self.plot_button.setEnabled(False)  # Изначально кнопка неактивна
        self.layout.addWidget(self.plot_button)

        # Виджет для отображения графика
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Таблица для отображения данных (опционально)
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

    def load_csv(self):
        # Открываем диалог выбора файла
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")
        if not file_name:
            return

        # Чтение CSV-файла с помощью pandas
        self.df = pd.read_csv(file_name)

        # Преобразование столбца с датами (если он есть)
        for col in self.df.columns:
            if pd.api.types.is_string_dtype(self.df[col]):
                try:
                    self.df[col] = pd.to_datetime(self.df[col])
                except:
                    pass

        # Отображение данных в таблице (опционально)
        self.table.setRowCount(self.df.shape[0])
        self.table.setColumnCount(self.df.shape[1])
        self.table.setHorizontalHeaderLabels(self.df.columns)
        for i in range(self.df.shape[0]):
            for j in range(self.df.shape[1]):
                self.table.setItem(i, j, QTableWidgetItem(str(self.df.iat[i, j])))

        # Заполнение выпадающих списков названиями столбцов
        self.combo_x.clear()
        self.combo_y.clear()
        self.combo_x.addItems(self.df.columns)
        self.combo_y.addItems(self.df.columns)

        # Активируем кнопку для построения графика
        self.plot_button.setEnabled(True)

    def plot_graph(self):
        try:
            x_column = self.combo_x.currentText()
            y_column = self.combo_y.currentText()

            # Проверка, что данные по оси Y числовые
            if not pd.api.types.is_numeric_dtype(self.df[y_column]):
                print("Ошибка: данные по оси Y должны быть числовыми.")
                return

            # Очистка предыдущего графика
            self.figure.clear()

            # Построение графика
            ax = self.figure.add_subplot(111)
            ax.plot(self.df[x_column], self.df[y_column], label=f"{y_column} vs {x_column}")
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            ax.legend()
            ax.grid(True)

            # Форматирование оси X (если это даты)
            if pd.api.types.is_datetime64_any_dtype(self.df[x_column]):
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
                self.figure.autofmt_xdate()  # Автоматический поворот дат

            # Обновление холста
            self.canvas.draw()
        except Exception as e:
            print(f"Ошибка при построении графика: {e}")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()