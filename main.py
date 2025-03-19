import sys
import os
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup
from PySide6.QtCore import QRect, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon
from ui.ui_station_rash import Ui_MainWindow
from PySide6 import QtCore

from Function import AppFunction

# ---------------------------------------------------------------------------------------------------------------------------------------------------
from PySide6.QtWidgets import QFileDialog,QTableWidgetItem,  QTableWidget, QVBoxLayout, QWidget, QLabel
import pandas as pd
from PySide6.QtCore import QThread, Signal
import matplotlib.dates as mdates

# ---------------------------------------------------------------------------------------------------------------------------------------------------





# ---------------------------------------------------------------------------------------------------------------------------------------------------



# class FileLoaderThread(QThread):
#     finished = Signal(pd.DataFrame)  # Сигнал, который передаёт загруженный DataFrame

#     def __init__(self, file_name):
#         super().__init__()
#         self.file_name = file_name

#     def run(self):
#         try:
#             # Загрузка CSV-файла
#             df = pd.read_csv(self.file_name)
#             self.finished.emit(df)  # Отправляем результат в основной поток
#         except Exception as e:
#             print(f"Ошибка при загрузке файла: {e}")
#             self.finished.emit(pd.DataFrame())

# ---------------------------------------------------------------------------------------------------------------------------------------------------







class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.styles = self.load_styles("json/style.json")#

        self.apply_global_styles()

        self.button_group = QButtonGroup(self)
        for button_name in self.styles["QPushButtonGroup"]["Buttons"]:
            button = getattr(self.ui, button_name, None)
            if button:
                self.button_group.addButton(button)

        self.button_group.buttonClicked.connect(self.on_button_clicked)

        self.apply_default_styles()


        self.ui.menu_btn.clicked.connect(lambda:self.slide_left_menu())





# ---------------------------------------------------------------------------------------------------------------------------------------------------
        self.ui.load_btn.clicked.connect(self.load_csv)
        self.ui.data_graph_btn.clicked.connect(self.plot_graph)
        self.ui.data_graph_btn.setEnabled(False)  # Изначально кнопка неактивна
# ---------------------------------------------------------------------------------------------------------------------------------------------------






        # self.ui.pushback.clicked.connect(lambda:self.slide_right_menu())

        
        self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page)
        # Подключаем кнопки к методам
        self.ui.home_btn.clicked.connect(self.show_home_page)
        self.ui.reports_btn.clicked.connect(self.show_report_page)
        self.ui.settings_btn.clicked.connect(self.show_settings_page)


        dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'DB/s.db'))
        AppFunction.main(dbFolder)
        # AppFunction.displayUsers(self, AppFunction.getAllUsers(dbFolder))
        # self.ui.add_user_btn.clicked.connect(lambda: AppFunction.addUser(self, dbFolder))





# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # def open_file_dialog(self):
    #     file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")
    #     if file_name:
    #         self.ui.name_file_label.setText(f"Selected file: {file_name}")

    #     # Чтение CSV-файла с помощью pandas
    #     df = pd.read_csv(file_name)

    #     # Отображение данных в таблице
    #     self.ui.table_data.setRowCount(df.shape[0])  # Количество строк
    #     self.ui.table_data.setColumnCount(df.shape[1])  # Количество столбцов
    #     self.ui.table_data.setHorizontalHeaderLabels(df.columns)  # Заголовки столбцов

    #     # Заполнение таблицы данными
    #     for i in range(df.shape[0]):
    #         for j in range(df.shape[1]):
    #             self.ui.table_data.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# МНОГОПОТОЧНОСТЬ

    # def start_loading(self):
    #     # Открываем диалог выбора файла
    #     file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")
    #     if not file_name:
    #         return

    #     # Отключаем кнопку загрузки, чтобы избежать повторного нажатия
    #     self.ui.load_btn.setEnabled(False)
    #     self.ui.load_btn.setText("Загрузка...")

    #     # Создаем и запускаем поток для загрузки файла
    #     self.loader_thread = FileLoaderThread(file_name)
    #     self.loader_thread.finished.connect(self.on_loading_finished)
    #     self.loader_thread.start()

    # def on_loading_finished(self, df):
    #     # Восстанавливаем кнопку загрузки
    #     self.ui.load_btn.setEnabled(True)
    #     self.ui.load_btn.setText("Load CSV")

    #     # Если файл успешно загружен
    #     if not df.empty:
    #         self.df = df

    #         # Преобразование столбца с датами (если он есть)
    #         for col in self.df.columns:
    #             if pd.api.types.is_string_dtype(self.df[col]):
    #                 try:
    #                     self.df[col] = pd.to_datetime(self.df[col])
    #                 except:
    #                     pass

    #         # Отображение данных в таблице (опционально)
    #         self.ui.table_data.setRowCount(self.df.shape[0])
    #         self.ui.table_data.setColumnCount(self.df.shape[1])
    #         self.ui.table_data.setHorizontalHeaderLabels(self.df.columns)
    #         for i in range(self.df.shape[0]):
    #             for j in range(self.df.shape[1]):
    #                 self.ui.table_data.setItem(i, j, QTableWidgetItem(str(self.df.iat[i, j])))

    #         # Заполнение выпадающих списков названиями столбцов
    #         self.ui.box_x.clear()
    #         self.ui.box_y.clear()
    #         self.ui.box_x.addItems(self.df.columns)
    #         self.ui.box_y.addItems(self.df.columns)

    #         # Активируем кнопку для построения графика
    #         self.ui.data_graph_btn.setEnabled(True)
    #     else:
    #         print("Ошибка: файл не был загружен.")

    def load_csv(self):
        # Открываем диалог выбора файла
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")
        if not file_name:
            return

        self.ui.name_file_label.setText(f"Selected file: {file_name}")
        # Чтение CSV-файла с помощью pandas
        self.df = pd.read_csv(file_name)

        # Преобразование столбца с датами (если он есть)
        for col in self.df.columns:
            if pd.api.types.is_string_dtype(self.df[col]):
                try:
                    self.df[col] = pd.to_datetime(self.df[col])
                except:
                    pass

        if len(self.df.columns) > 0:  # Проверка, что в DataFrame есть столбцы
            current_first_column = self.df.columns[0]  # Имя первого столбца
            self.df.rename(columns={current_first_column: "index"}, inplace=True)

            
        # Округление числовых столбцов до десятитысячных
        for col in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[col]):
                self.df[col] = self.df[col].round(4)  # Округление до 4 знаков после запятой

        # Отображение данных в таблице (опционально)
        self.ui.table_data.setRowCount(self.df.shape[0])
        self.ui.table_data.setColumnCount(self.df.shape[1])
        self.ui.table_data.setHorizontalHeaderLabels(self.df.columns)
        for i in range(self.df.shape[0]):
            for j in range(self.df.shape[1]):
                self.ui.table_data.setItem(i, j, QTableWidgetItem(str(self.df.iat[i, j])))

        # Заполнение выпадающих списков названиями столбцов
        self.ui.box_x.clear()
        self.ui.box_y.clear()
        self.ui.box_x.addItems(self.df.columns)
        self.ui.box_y.addItems(self.df.columns)

        # Активируем кнопку для построения графика
        self.ui.data_graph_btn.setEnabled(True)

    def plot_graph(self):
        try:
            x_column = self.ui.box_x.currentText()
            y_column = self.ui.box_y.currentText()

            # Проверка, что данные по оси Y числовые
            if not pd.api.types.is_numeric_dtype(self.df[y_column]):
                print("Ошибка: данные по оси Y должны быть числовыми.")
                return

            # Очистка предыдущего графика
            self.ui.widget_4.figure.clear()

            # Построение графика
            ax = self.ui.widget_4.figure.add_subplot(111)
            ax.plot(self.df[x_column], self.df[y_column], label=f"{y_column} vs {x_column}")
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            ax.legend()
            ax.grid(True)

            # Форматирование оси X (если это даты)
            if pd.api.types.is_datetime64_any_dtype(self.df[x_column]):
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
                self.ui.widget_4.figure.autofmt_xdate()  # Автоматический поворот дат

            # Обновление холста
            self.ui.widget_4.canvas.draw()
        except Exception as e:
            print(f"Ошибка при построении графика: {e}")
# ---------------------------------------------------------------------------------------------------------------------------------------------------




    def slide_left_menu(self):
        width = self.ui.left_menu.width()
        if width == 0:
            new_width = 200
        else:
            new_width = 0

        # Создаем анимацию для minimumWidth
        self.animation_min = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation_min.setDuration(250)
        self.animation_min.setStartValue(width)
        self.animation_min.setEndValue(new_width)
        self.animation_min.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        # Создаем анимацию для maximumWidth
        self.animation_max = QPropertyAnimation(self.ui.left_menu, b"maximumWidth")
        self.animation_max.setDuration(250)
        self.animation_max.setStartValue(width)
        self.animation_max.setEndValue(new_width)
        self.animation_max.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        # Запускаем анимации последовательно
        self.animation_min.start()
        self.animation_max.start()

        
    def slide_right_menu(self):
        width = self.ui.right_menu.width()
        if width == 0:
            new_width = 200
        else:
            new_width = 0

        # Создаем анимацию для minimumWidth
        self.animation_min = QPropertyAnimation(self.ui.right_menu, b"minimumWidth")
        self.animation_min.setDuration(250)
        self.animation_min.setStartValue(width)
        self.animation_min.setEndValue(new_width)
        self.animation_min.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        # Создаем анимацию для maximumWidth
        self.animation_max = QPropertyAnimation(self.ui.right_menu, b"maximumWidth")
        self.animation_max.setDuration(250)
        self.animation_max.setStartValue(width)
        self.animation_max.setEndValue(new_width)
        self.animation_max.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        # Запускаем анимации последовательно
        self.animation_min.start()
        self.animation_max.start()

        
    def load_styles(self, style_file):
        with open(style_file, 'r') as f:
            return json.load(f)
        
    def apply_global_styles(self):
        style_string = ""
        for widget, properties in self.styles.items():
            if widget != "QPushButtonGroup":
                style_string += f"{widget} {{"
                for property, value in properties.items():
                    style_string += f"{property}: {value}; "
                style_string += "}"
        self.setStyleSheet(style_string)

    def apply_default_styles(self):
        not_active_style = self.styles["QPushButtonGroup"]["Style"]["NotActive"]
        for button_name in self.styles["QPushButtonGroup"]["Buttons"]:
            button = getattr(self.ui, button_name, None)
            if button:
                button.setStyleSheet(not_active_style)

    def on_button_clicked(self, button):
        active_style = self.styles["QPushButtonGroup"]["Style"]["Active"]
        not_active_style = self.styles["QPushButtonGroup"]["Style"]["NotActive"]

        for btn in self.button_group.buttons():
            btn.setStyleSheet(not_active_style)
        button.setStyleSheet(active_style)  


    def show_home_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)  # Показать первую страницу

    def show_report_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)  # Показать вторую страницу

    def show_settings_page(self):
        self.ui.stackedWidget.setCurrentIndex(5)  # Показать страницу настроек


  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
