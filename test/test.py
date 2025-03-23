import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle


class MplWidgetOptimize(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Создаем фигуру и холст Matplotlib
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Добавляем холст в layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # Переменные для хранения координат выделения
        self.selection_start = None
        self.selection_end = None

    def connect_events(self, callback):
        """Подключение событий мыши"""
        self.canvas.mpl_connect('button_press_event', callback.on_press)
        self.canvas.mpl_connect('button_release_event', callback.on_release)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Инициализация интерфейса
        self.ui = self.setup_ui()

        # Подключение событий мыши
        self.mpl_widget = MplWidgetOptimize()
        self.mpl_widget.connect_events(self)

        # Пример данных
        self.df = pd.DataFrame({
            'Data': np.random.rand(100),  # Пример данных для графика
            'Selection': np.zeros(100)   # Столбец для выделения
        })

        # Список для хранения выделенных участков
        self.selected_regions = []

        # Отображение данных в таблице
        self.display_data_in_table(self.df)

        # Построение графика
        self.plot_data()

    def setup_ui(self):
        """Инициализация интерфейса"""
        layout = QVBoxLayout()

        # Добавляем виджет для графика
        layout.addWidget(self.mpl_widget)

        # Кнопка для добавления стационарных участков
        self.add_stationary_button = QPushButton("Add Stationary")
        self.add_stationary_button.clicked.connect(self.on_add_stationary_clicked)
        layout.addWidget(self.add_stationary_button)

        # Таблица для отображения данных
        self.table_data = QTableWidget()
        layout.addWidget(self.table_data)

        self.setLayout(layout)

    def on_press(self, event):
        """Обработка нажатия мыши"""
        if event.inaxes is not None:
            self.selection_start = event.xdata  # Сохраняем начало выделения

    def on_release(self, event):
        """Обработка отпускания мыши"""
        if event.inaxes is not None and self.selection_start is not None:
            self.selection_end = event.xdata  # Сохраняем конец выделения

            # Добавляем выделенный участок в список
            self.selected_regions.append((self.selection_start, self.selection_end))

            # Перекрашиваем выделенный участок на графике
            self.highlight_selected_region(self.selection_start, self.selection_end)

            # Сбрасываем выделение
            self.selection_start = None
            self.selection_end = None

    def highlight_selected_region(self, start, end):
        """Перекрашивание выделенного участка на графике"""
        ax = self.mpl_widget.figure.axes[0]
        height = ax.get_ylim()[1] - ax.get_ylim()[0]  # Высота графика
        rect = Rectangle((start, ax.get_ylim()[0]), end - start, height,
                         color='yellow', alpha=0.3)  # Прямоугольник для выделения
        ax.add_patch(rect)
        self.mpl_widget.canvas.draw()

    def on_add_stationary_clicked(self):
        """Обработка нажатия кнопки 'add_stationary'"""
        for start, end in self.selected_regions:
            # Определяем диапазон индексов
            start_index = int(np.floor(start))
            end_index = int(np.ceil(end))

            # Убедимся, что индексы находятся в пределах данных
            start_index = max(0, min(start_index, len(self.df) - 1))
            end_index = max(0, min(end_index, len(self.df) - 1))

            # Обновляем столбец 'Selection' в выделенном диапазоне
            self.df.loc[start_index:end_index, 'Selection'] = 1

        # Обновляем таблицу QTableWidget
        self.display_data_in_table(self.df)

        # Очищаем список выделенных участков
        self.selected_regions.clear()

        # Очищаем выделения на графике
        self.clear_highlights()

    def clear_highlights(self):
        """Очистка всех выделений на графике"""
        ax = self.mpl_widget.figure.axes[0]
        for patch in ax.patches:
            patch.remove()
        self.mpl_widget.canvas.draw()

    def display_data_in_table(self, data):
        """Отображение данных в QTableWidget"""
        self.table_data.setRowCount(data.shape[0])
        self.table_data.setColumnCount(data.shape[1])
        self.table_data.setHorizontalHeaderLabels(data.columns)

        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                item = QTableWidgetItem(str(data.iat[i, j]))
                self.table_data.setItem(i, j, item)

    def plot_data(self):
        """Построение графика"""
        self.mpl_widget.figure.clear()
        ax = self.mpl_widget.figure.add_subplot(111)
        ax.plot(self.df.index, self.df['Data'], label="Данные")
        ax.set_xlabel("Индекс строки")
        ax.set_ylabel("Значение")
        ax.legend()
        ax.grid(True)
        self.mpl_widget.canvas.draw()