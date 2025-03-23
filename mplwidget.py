from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QWidget, QVBoxLayout





class MplWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Создаем фигуру и холст Matplotlib
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Добавляем холст в layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)


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