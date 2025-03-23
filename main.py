import sys
import os
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup
from PySide6.QtCore import QRect, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon
from ui.ui_station_graph_click import Ui_MainWindow
from PySide6 import QtCore

from Function import AppFunction

# ---------------------------------------------------------------------------------------------------------------------------------------------------
from PySide6.QtWidgets import QFileDialog,QTableWidgetItem,  QTableWidget, QPushButton, QWidget, QLabel
import pandas as pd
import numpy as np
from PySide6.QtCore import QThread, Signal
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle

from sklearn.metrics import f1_score
from scipy.optimize import minimize
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

# ************************************************************************************
        self.df = None
        self.selection_start = None
        self.selection_end = None

        self.data_graph = None
        
        # Список для хранения выделенных участков
        self.selected_regions = []
        # estimation personal
        self.y_true = None
        # frame для текущей даты
        self.data_v3 = None
        # retrive
        self.all_ratios = None
# ************************************************************************************

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




        # Устанавливаем начальную страницу
        # self.stacked_widget.setCurrentIndex(0)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
        self.ui.load_btn.clicked.connect(self.load_csv)
        self.ui.data_graph_btn.clicked.connect(self.plot_graph)
        self.ui.data_graph_btn.setEnabled(False)  # Изначально кнопка неактивна
        self.ui.optimize.clicked.connect(self.calculate_stationary)
        # перейти на вторую страницу
        self.ui.next_page_1.clicked.connect(self.go_to_page_2)
        # построение графика оптимизации
        self.ui.graph_opt.clicked.connect(self.plot_graph_optimize)
        # Отображение данных в таблице
        self.ui.add_stationar.clicked.connect(self.on_add_stationary_clicked)
        # Расчет коэффициентов
        self.ui.search_k.clicked.connect(self.ratio_calculation)
        # Вывод итогового результата
        self.ui.graph_result.clicked.connect(self.plot_graph_result)
# ---------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
# РАБОТА С ГРАФИКОМ И ВЫДЕЛЕНИЕМ УЧАСТКОВ
        # Подключение событий мыши widget12
        self.ui.widget_12.connect_events(self)

#--------------------------------------------------------------------------------------------------



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


    def calculate_stationary(self):
        try:
            # Получаем значения из QLineEdit
            x_min = int(self.ui.x_min.text())
            x_max = int(self.ui.x_max.text())

            # Получаем название столбца из QComboBox
            column_name = self.ui.box_y.currentText()

            # Проверяем, что столбец существует в DataFrame
            if column_name not in self.df.columns:
                raise ValueError(f"Столбец '{column_name}' не найден в DataFrame")

            # Выбираем данные из DataFrame
            data_PT = self.df[[column_name]]

            # Вычисляем диапазон
            range_max_min = x_max - x_min

            # Генерация индексов
            indexes_v3 = [i for i in range(x_min, x_max, 1)]
            self.data_v3 = data_PT.iloc[indexes_v3]

            # Параметры алгоритма
            l1 = 0.2
            l2 = 0.1
            l3 = 0.1

            # Начальные значения
            x_st = self.data_v3.iloc[:50, 0].mean()
            xf_st = self.data_v3.iloc[:50, 0].mean()
            vf_st = self.data_v3.iloc[:50, 0].var()
            df_st = 2 * self.data_v3.iloc[:50, 0].var()

            # Списки для хранения результатов
            r_list = []
            vf_list = []
            df_list = []
            xf_list = []

            # Основной цикл алгоритма
            for i in range(51, range_max_min):
                xf = l1 * self.data_v3.iloc[i, 0] + (1 - l1) * xf_st
                vf = l2 * (self.data_v3.iloc[i, 0] - xf_st) ** 2 + (1 - l2) * vf_st
                df = l3 * (self.data_v3.iloc[i, 0] - x_st) ** 2 + (1 - l3) * df_st
                r = round(((2 - l1) * vf) / df, 4)

                vf_list.append(vf)
                df_list.append(df)
                r_list.append(r)
                xf_list.append(xf)

                x_st = self.data_v3.iloc[i, 0]
                xf_st = xf
                vf_st = vf
                df_st = df

            # Создание DataFrame с результатами
            rr = pd.DataFrame(data=r_list, index=self.data_v3.iloc[51:range_max_min].index, columns=['R'])
            # vff = pd.DataFrame(data=vf_list, index=self.data_v3.iloc[51:range_max_min].index, columns=['Vf'])
            # dff = pd.DataFrame(data=df_list, index=self.data_v3.iloc[51:range_max_min].index, columns=['Df'])
            # xff = pd.DataFrame(data=xf_list, index=self.data_v3.iloc[51:range_max_min].index, columns=['Xf'])

            # Добавление столбца stationary
            rr['stationary'] = np.where(rr['R'] > 2.3715370273232828, 0, 1)

            # Объединение результатов
            self.data_graph = pd.concat([self.data_v3, rr], axis=1)

            self.data_graph['assessment'] = 0
            # Вывод результата в QTableWidget
            self.ui.table_classification.setRowCount(self.data_graph.shape[0])
            self.ui.table_classification.setColumnCount(self.data_graph.shape[1])
            self.ui.table_classification.setHorizontalHeaderLabels(self.data_graph.columns)
            
            for i in range(self.data_graph.shape[0]):
                for j in range(self.data_graph.shape[1]):
                    self.ui.table_classification.setItem(i, j, QTableWidgetItem(str(self.data_graph.iat[i, j])))
            

        except Exception as e:
            print(f"Ошибка: {e}")
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Построение грфика для оптимизации
    def plot_graph_optimize(self):
        try:
            # Получаем данные из QTableWidget
            table = self.ui.table_classification  # Замените на ваш QTableWidget
            row_count = table.rowCount()
            column_count = table.columnCount()

            # Проверяем, что таблица не пустая
            if row_count == 0 or column_count == 0:
                print("Ошибка: таблица пуста.")
                return
            
            # Извлекаем данные из первого столбца (ось Y)
            y_data = []
            for i in range(row_count):
                item = table.item(i, 0)  # Первый столбец (индекс 0)
                if item is not None:
                    try:
                        y_value = float(item.text())  # Преобразуем текст в число
                        y_data.append(y_value)
                    except ValueError:
                        print(f"Ошибка: значение в строке {i} не является числом.")
                        return

            # Проверяем, что данные по оси Y не пустые
            if not y_data:
                print("Ошибка: нет данных для построения графика.")
                return

            # Получаем значения из QLineEdit
            x_min = int(self.ui.x_min.text())
            x_max = int(self.ui.x_max.text())

            # Индексы строк (ось X)
            x_data = range(x_min, x_max)

            # Очистка предыдущего графика
            self.ui.widget_12.figure.clear()

            # Построение графика
            ax = self.ui.widget_12.figure.add_subplot(111)
            ax.plot(x_data, y_data, label="График по первому столбцу")
            ax.set_xlabel("Индекс строки")  # Подпись оси X
            ax.set_ylabel("Значение первого столбца")  # Подпись оси Y
            ax.legend()
            ax.grid(True)

            # Обновление холста
            self.ui.widget_12.canvas.draw()
        except Exception as e:
            print(f"Ошибка при построении графика: {e}")
# ---------------------------------------------------------------------------------------------------------------------------------------------------


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Ваимодействие с графиком через мышьку
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
        ax = self.ui.widget_12.figure.axes[0]
        height = ax.get_ylim()[1] - ax.get_ylim()[0]  # Высота графика
        rect = Rectangle((start, ax.get_ylim()[0]), end - start, height,
                         color='yellow', alpha=0.3)  # Прямоугольник для выделения
        ax.add_patch(rect)
        self.ui.widget_12.canvas.draw()
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Обновление таблицы послед выделения участков
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def on_add_stationary_clicked(self):
        """Обработка нажатия кнопки 'add_stationary'"""
        for start, end in self.selected_regions:
            # Определяем диапазон индексов
            start_index = int(np.floor(start))
            end_index = int(np.ceil(end))

            # Убедимся, что индексы находятся в пределах данных
            start_index = max(0, min(start_index, len(self.df) - 1))
            end_index = max(0, min(end_index, len(self.df) - 1))

            # Обновляем столбец 'assessment' в выделенном диапазоне
            self.data_graph.loc[start_index:end_index, 'assessment'] = 1

        # Обновляем таблицу QTableWidget
        self.display_data_in_table(self.data_graph)

        #Получаем переменную с личной оценкой
        self.y_true = np.array(self.data_graph['assessment'].iloc[51:])

        # Очищаем список выделенных участков
        self.selected_regions.clear()

        # Очищаем выделения на графике
        self.clear_highlights()

    def clear_highlights(self):
        """Очистка всех выделений на графике"""
        ax = self.ui.widget_12.figure.axes[0]
        for patch in ax.patches:
            patch.remove()
        self.ui.widget_12.canvas.draw()

    def display_data_in_table(self, data):
        """Отображение данных в QTableWidget"""
        self.ui.table_classification.setRowCount(data.shape[0])
        self.ui.table_classification.setColumnCount(data.shape[1])
        self.ui.table_classification.setHorizontalHeaderLabels(data.columns)

        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                item = QTableWidgetItem(str(data.iat[i, j]))
                self.ui.table_classification.setItem(i, j, item)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    def search_ratio(self, x):
    
        x_min = int(self.ui.x_min.text())
        x_max = int(self.ui.x_max.text())
        x_range = x_max - x_min

        l1 = x[0]
        l2 = x[1]
        l3 = x[2]

        x_st = self.data_v3.iloc[:50, 0].mean()
        xf_st = self.data_v3.iloc[:50, 0].mean()
        vf_st = self.data_v3.iloc[:50, 0].var()
        df_st = 2 * self.data_v3.iloc[:50, 0].var()
        r_list = []

        for i in range(51, x_range):
            xf = l1 * self.data_v3.iloc[i, 0] + (1 - l1) * xf_st
            vf = l2 * (self.data_v3.iloc[i, 0] - xf_st) ** 2 + (1 - l2) * vf_st
            df = l3 * (self.data_v3.iloc[i, 0] - x_st) ** 2 + (1 - l3) * df_st
            r = ((2 - l1) * vf) / df
            r_list.append(r)
            x_st = self.data_v3.iloc[i, 0]
            xf_st = xf
            vf_st = vf
            df_st = df

        r_np = np.array(r_list)

        self.y_pred = np.where(r_np > 2.3715370273232828, 0, 1)
        score = f1_score(self.y_true, self.y_pred, average='binary')

        return -score

    def ratio_calculation(self):
        x0 = [0.5, 0.5, 0.5]
        bnds = ((0, 1), (0, 1), (0, 1))

        def callback(xk, *args, **kwargs):
            self.ui.k_1.setText(f"K_1: {round(xk[0], 4)}")
            self.ui.k_2.setText(f"K_2: {round(xk[1], 4)}")
            self.ui.k_3.setText(f"K_3: {round(xk[2], 4)}")

        result = minimize(self.search_ratio, x0, method="Powell", bounds=bnds, callback=callback)
        self.all_ratios = result.x
        self.essential_f = result.fun
        self.ui.k_1.setText(f"K_1: {round(self.all_ratios[0], 4)}")
        self.ui.k_2.setText(f"K_2: {round(self.all_ratios[1], 4)}")
        self.ui.k_3.setText(f"K_3: {round(self.all_ratios[2], 4)}")
        self.ui.F_score.setText(f"F_score: {round(self.essential_f, 4)}")
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    def plot_graph_result(self):

        x_min = int(self.ui.x_min.text())
        x_max = int(self.ui.x_max.text())
        range_max_min = x_max - x_min

    # Параметры алгоритма
        l1 = self.all_ratios[0]
        l2 = self.all_ratios[1]
        l3 = self.all_ratios[2]

        # Начальные значения
        x_st = self.data_v3.iloc[:50, 0].mean()
        xf_st = self.data_v3.iloc[:50, 0].mean()
        vf_st = self.data_v3.iloc[:50, 0].var()
        df_st = 2 * self.data_v3.iloc[:50, 0].var()

        # Списки для хранения результатов
        r_list = []
        vf_list = []
        df_list = []
        xf_list = []

        # Основной цикл алгоритма
        for i in range(51, range_max_min):
            xf = l1 * self.data_v3.iloc[i, 0] + (1 - l1) * xf_st
            vf = l2 * (self.data_v3.iloc[i, 0] - xf_st) ** 2 + (1 - l2) * vf_st
            df = l3 * (self.data_v3.iloc[i, 0] - x_st) ** 2 + (1 - l3) * df_st
            r = round(((2 - l1) * vf) / df, 4)

            vf_list.append(vf)
            df_list.append(df)
            r_list.append(r)
            xf_list.append(xf)

            x_st = self.data_v3.iloc[i, 0]
            xf_st = xf
            vf_st = vf
            df_st = df

        # Создание DataFrame с результатами
        rr = pd.DataFrame(data=r_list, index=self.data_v3.iloc[51:range_max_min].index, columns=['R'])
        # vff = pd.DataFrame(data=vf_list, index=self.data_v3.iloc[51:range_max_min].index, columns=['Vf'])
        # dff = pd.DataFrame(data=df_list, index=self.data_v3.iloc[51:range_max_min].index, columns=['Df'])
        # xff = pd.DataFrame(data=xf_list, index=self.data_v3.iloc[51:range_max_min].index, columns=['Xf'])

        # Добавление столбца stationary
        rr['stationary'] = np.where(rr['R'] > 2.3715370273232828, 0, 1)
        data_graph = pd.concat([self.data_v3, rr], axis=1)

        # Очистка предыдущего графика
        self.ui.widget_12.figure.clear()

        # Построение графика
        ax = self.ui.widget_12.figure.add_subplot(111)
        ax.plot(data_graph.iloc[51:range_max_min].index, data_graph.iloc[51:range_max_min, 0], label='x')

        # Построение стационарных точек
        stationary_data = data_graph[data_graph['stationary'] == 1]
        ax.plot(stationary_data.index, stationary_data['PV-FT-15'], 'r*', markersize=4, label='steady-state')

        # Построение нестационарных точек
        non_stationary_data = data_graph[data_graph['stationary'] == 0]
        ax.plot(non_stationary_data.index, non_stationary_data['PV-FT-15'], 'bo', markersize=4, label='not at steady-state')

        # Настройка графика
        ax.set_xlabel("Индекс")
        ax.set_ylabel("Значение")
        ax.legend()
        ax.grid(True)

        # Обновление холста
        self.ui.widget_12.canvas.draw()

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&



# ##############################################################################################
    def go_to_page_2(self):
        """Переход на вторую страницу"""
        self.ui.stackedWidget.setCurrentIndex(1) 
# ##############################################################################################

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
