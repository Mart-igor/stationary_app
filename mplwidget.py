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