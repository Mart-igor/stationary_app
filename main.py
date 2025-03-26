import sys
import os
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup
from PySide6.QtCore import  QPropertyAnimation, QUrl
from PySide6.QtGui import QIcon
from ui.ui_station_interface import Ui_MainWindow
from PySide6 import QtCore

from Function import AppFunction

# ---------------------------------------------------------------------------------------------------------------------------------------------------
from PySide6.QtWidgets import QFileDialog,QTableWidgetItem,  QMessageBox
import pandas as pd
import numpy as np

import matplotlib.dates as mdates
from matplotlib.patches import Rectangle

from sklearn.metrics import f1_score
from scipy.optimize import minimize

from PySide6.QtGui import QDesktopServices, QTextDocument, QTextCursor, QTextDocument, QTextCursor, QTextTableFormat, QTextCharFormat, QColor, QTextFrameFormat
from PySide6.QtPrintSupport import QPrintPreviewDialog, QPrinter
from PySide6.QtCore import Qt

from report import ReportPrinter

from PySide6.QtCore import QStandardPaths, QFile, QIODevice


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        self.table_result = None

        
        self.styles = self.load_styles("json/style.json")#
        
        self.apply_default_styles()
        
        self.apply_global_styles()



        self.button_group = QButtonGroup(self)
        for button_name in self.styles["QPushButtonGroup"]["Buttons"]:
            button = getattr(self.ui, button_name, None)
            if button:
                self.button_group.addButton(button)

        self.button_group.buttonClicked.connect(self.on_button_clicked)


        # сдвигам левое меню 
        self.ui.menu_btn.clicked.connect(lambda:self.slide_left_menu())
        # сдвигаем вправо лог ин
        self.ui.signin.clicked.connect(lambda:self.slide_right_menu())

        # Устанавливаем начальную страницу
        self.ui.stackedWidget.setCurrentIndex(0)
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
        # Кнопки управления
        # self.export_btn.clicked.connect(self.export_to_csv)
        # печать результатов
        self.ui.print_btn.clicked.connect(self.on_print)
        # превью печати
        # self.ui.reset_btn.clicked.connect(self.on_print_preview)
        # to pdf
        self.ui.export_pdf_btn.clicked.connect(self.export_to_pdf)
        # to csv
        self.ui.export_csv_btn.clicked.connect(self.export_to_csv)
        # to json
        self.ui.export_json_btn.clicked.connect(self.export_to_json)
        # to excel
        self.ui.pushButton_4.clicked.connect(self.export_to_excel)

        # печать
        self.printer = ReportPrinter(self)

        # Подключение событий мыши widget12
        self.ui.widget_12.connect_events(self)

        # Открытие ссылок в broweser
        self.ui.about_browser.setOpenExternalLinks(True)  # Важно!        

        # выбор алгортима
        self.ui.alg_box.addItems([
            "Одномерные конрольные карты",
            "MEWMA"
        ])
        self.ui.alg_box.setCurrentIndex(0)



        # self.ui.pushback.clicked.connect(lambda:self.slide_right_menu())

        
        # Подключаем кнопки к методам
        self.ui.home_btn.clicked.connect(self.show_home_page)
        self.ui.reports_btn.clicked.connect(self.show_report_page)
        self.ui.settings_btn.clicked.connect(self.show_settings_page)
        self.ui.algorithm_btn.clicked.connect(self.show_algorithm_page)
        self.ui.instruction_btn.clicked.connect(self.show_instruction_page)
        self.ui.account_btn.clicked.connect(self.show_account_page)
        self.ui.help_btn.clicked.connect(self.show_help_page)
        self.ui.about_btn.clicked.connect(self.show_about_page)






        dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'DB/s.db'))
        AppFunction.main(dbFolder)
        # AppFunction.displayUsers(self, AppFunction.getAllUsers(dbFolder))
        # self.ui.add_user_btn.clicked.connect(lambda: AppFunction.addUser(self, dbFolder))


    
    def display_table(self, data, table_name):
        # Отображение данных в таблице (опционально)
        table_name.setRowCount(data.shape[0])
        table_name.setColumnCount(data.shape[1])
        table_name.setHorizontalHeaderLabels(data.columns)
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                table_name.setItem(i, j, QTableWidgetItem(str(data.iat[i, j])))


    def algorith(self, data, range_max_min, start_ratio=[0.2, 0.1, 0.1]):

        l1 = start_ratio[0]
        l2 = start_ratio[1]
        l3 = start_ratio[2]

        x_st = data.iloc[:50, 0].mean()
        xf_st = data.iloc[:50, 0].mean()
        vf_st = data.iloc[:50, 0].var()
        df_st = 2 * data.iloc[:50, 0].var()

        r_list = []
        vf_list = []
        df_list = []
        xf_list = []

        for i in range(51, range_max_min):
            xf = l1 * data.iloc[i, 0] + (1 - l1) * xf_st
            vf = l2 * (data.iloc[i, 0] - xf_st) ** 2 + (1 - l2) * vf_st
            df = l3 * (data.iloc[i, 0] - x_st) ** 2 + (1 - l3) * df_st
            r = round(((2 - l1) * vf) / df, 4)

            vf_list.append(vf)
            df_list.append(df)
            r_list.append(r)
            xf_list.append(xf)

            x_st = data.iloc[i, 0]
            xf_st = xf
            vf_st = vf
            df_st = df

        rr = pd.DataFrame(data=r_list, index=data.iloc[51:range_max_min].index, columns=['R'])
        rr['stationary'] = np.where(rr['R'] > 2.3715370273232828, 0, 1)
        return rr

    def plot(self, widget_name, data_x, data_y, label, label_x, label_y):

        widget_name.figure.clear()

        ax = widget_name.figure.add_subplot(111)
        ax.plot(data_x, data_y, label=label)
        ax.set_xlabel(label_x)
        ax.set_ylabel(label_y)
        ax.legend()
        ax.grid(True)

        # Форматирование оси X (если это даты)
        if pd.api.types.is_datetime64_any_dtype(data_x):
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
            widget_name.figure.autofmt_xdate()

        widget_name.canvas.draw()

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

        # вызываем метод заполнения таблицы
        self.display_table(self.df, self.ui.table_data)

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
            self.plot(self.ui.widget_4, self.df[x_column], self.df[y_column], f"{y_column} vs {x_column}", x_column, y_column)
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
            range_max_min = x_max - x_min

            # Генерация индексов
            indexes_v3 = [i for i in range(x_min, x_max, 1)]
            self.data_v3 = data_PT.iloc[indexes_v3]

            rr = self.algorith(self.data_v3, range_max_min)
            self.data_graph = pd.concat([self.data_v3, rr], axis=1)
            self.data_graph['assessment'] = 0
            self.display_table(self.data_graph, self.ui.table_classification)            

        except Exception as e:
            print(f"Ошибка: {e}")

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
            # Получаем значения из QLineEdit
            x_min = int(self.ui.x_min.text())
            x_max = int(self.ui.x_max.text())

            # Индексы строк (ось X)
            x_data = range(x_min, x_max)
            self.plot(self.ui.widget_12, x_data, y_data, "График по первому столбцу", "Индекс строки", "Значение первого столбца")
        except Exception as e:
            print(f"Ошибка при построении графика: {e}")
            
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
        
# Обновление таблицы послед выделения участков
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
        self.display_table(self.data_graph, self.ui.table_classification)

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

    def search_ratio(self, x):
    
        x_min = int(self.ui.x_min.text())
        x_max = int(self.ui.x_max.text())
        x_range = x_max - x_min

        rr = self.algorith(self.data_v3, x_range, x)
        score = f1_score(self.y_true, rr['stationary'], average='binary')

        return -score

    def ratio_calculation(self):
        x0 = [0.5, 0.5, 0.5]
        bnds = ((0, 1), (0, 1), (0, 1))

        def callback(xk, *args, **kwargs):
            print(f'current ratio: {xk}')

        result = minimize(self.search_ratio, x0, method="Powell", bounds=bnds, callback=callback)
        self.all_ratios = result.x
        self.essential_f = result.fun
        self.ui.k_1.setText(f"K_1: {round(self.all_ratios[0], 4)}")
        self.ui.k_2.setText(f"K_2: {round(self.all_ratios[1], 4)}")
        self.ui.k_3.setText(f"K_3: {round(self.all_ratios[2], 4)}")
        self.ui.F_score.setText(f"F_score: {abs(round(self.essential_f, 4))}")

    def plot_graph_result(self):
        column_name = self.ui.box_y.currentText()
        x_min = 0
        x_max = len(self.df)
        range_max_min = x_max - x_min

        rr = self.algorith(self.df[[column_name]], range_max_min, self.all_ratios)
        self.table_result = pd.concat([self.df, rr], axis=1)

        if 'time' not in self.table_result.columns:
            print("Столбец 'time' не найден в данных")
            return

        # Очистка предыдущего графика
        self.ui.widget_12.figure.clear()

        # Построение графика
        ax = self.ui.widget_12.figure.add_subplot(111)

        ax.plot(self.table_result['time'], 
            self.table_result[column_name], 
            'g-', alpha=0.5, label=column_name)

        # ax.plot(self.table_result.iloc[51:range_max_min].index, self.table_result.iloc[51:range_max_min, 0], label='x')

        # Построение стационарных точек
        stationary_data = self.table_result[self.table_result['stationary'] == 1]
        ax.plot(stationary_data['time'], 
                stationary_data[column_name], 
                'r*', markersize=8, label='Стационарные точки')
        # stationary_data = self.table_result[self.table_result['stationary'] == 1]
        # ax.plot(stationary_data.index, stationary_data['PV-FT-15'], 'r*', markersize=4, label='steady-state')

        # Построение нестационарных точек
        non_stationary_data = self.table_result[self.table_result['stationary'] == 0]
        ax.plot(non_stationary_data['time'], 
                non_stationary_data[column_name], 
                'bo', markersize=4, label='Нестационарные точки')
        # non_stationary_data = self.table_result[self.table_result['stationary'] == 0]
        # ax.plot(non_stationary_data.index, non_stationary_data['PV-FT-15'], 'bo', markersize=4, label='not at steady-state')

        # Настройка графика
        ax.set_xlabel('Время')
        ax.set_ylabel("Значение")
        ax.legend()
        ax.grid(True)

        # Обновление холста
        self.ui.widget_12.canvas.draw()
        self.display_table(self.table_result, self.ui.report_table)

    
    # копирование крипто кошелька
    def copy_wallet_address(self):
        # Копирование адреса кошелька в буфер обмена
        clipboard = QApplication.clipboard()
        clipboard.setText(self.wallet_address.text())
        QMessageBox.information(self, "Скопировано", "Адрес кошелька скопирован в буфер обмена!") 

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
            new_width = 150
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
        """Загружает стили из JSON файла с проверкой ошибок"""
        try:
            with open(style_file, 'r', encoding='utf-8') as f:
                styles = json.load(f)
                
            # Базовая валидация структуры
            if not isinstance(styles, dict):
                raise ValueError("Style file should contain a dictionary")
                
            return styles
        except Exception as e:
            print(f"Error loading styles: {str(e)}")
            return {}  # Возвращаем пустой словарь при ошибке

    def apply_global_styles(self):
        style_string = ""
        
        # Глобальные стили
        for selector, properties in self.styles["Global"].items():
            style_string += f"{selector} {{"
            for prop, value in properties.items():
                style_string += f"{prop}: {value}; "
            style_string += "}\n"
        
        # Стили виджетов
        for category, items in self.styles.items():
            if category != "Global" and category != "ButtonGroups":
                for selector, properties in items.items():
                    if not isinstance(properties, dict):  # Пропускаем SpecialLabels
                        continue
                    style_string += f"{selector} {{"
                    for prop, value in properties.items():
                        style_string += f"{prop}: {value}; "
                    style_string += "}\n"
        
        self.setStyleSheet(style_string)

    def apply_default_styles(self):
        """Применяет специальные стили для групп виджетов"""
        if not hasattr(self, 'styles') or 'QPushButtonGroup' not in self.styles:
            return

        button_group = self.styles['QPushButtonGroup']
        not_active_style = button_group.get('Style', {}).get('NotActive', '')
        
        if not not_active_style:
            return

        # Применяем стили только к существующим кнопкам
        for button_name in button_group.get('Buttons', []):
            button = getattr(self.ui, button_name, None)
            if button:
                # Сохраняем objectName для отладки
                original_name = button.objectName()
                try:
                    button.setStyleSheet(not_active_style)
                except Exception as e:
                    print(f"Error applying style to {original_name}: {str(e)}")

    def on_button_clicked(self, button):
        active_style = self.styles["QPushButtonGroup"]["Style"]["Active"]
        not_active_style = self.styles["QPushButtonGroup"]["Style"]["NotActive"]

        for btn in self.button_group.buttons():
            btn.setStyleSheet(not_active_style)
        button.setStyleSheet(active_style)  


    def show_home_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)  

    def show_algorithm_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)  

    def show_report_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)  

    def show_settings_page(self):
        self.ui.stackedWidget.setCurrentIndex(8)  

    def show_instruction_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)  

    def show_account_page(self):
        self.ui.stackedWidget.setCurrentIndex(6)  

    def show_help_page(self):
        self.ui.stackedWidget.setCurrentIndex(7)  

    def show_about_page(self):
        self.ui.stackedWidget.setCurrentIndex(5)  

    def go_to_page_2(self):
        algorithm = self.ui.alg_box.currentText()
        if algorithm == "Одномерные конрольные карты":
            self.ui.stackedWidget.setCurrentIndex(2) 


    def on_print(self):
        """Обработка печати"""
        # Можно печатать либо таблицу, либо исходный DataFrame (если он есть)
        if hasattr(self, 'table_result'):
            self.printer.print_data(self.table_result, "DataFrame Report")
    
    def on_print_preview(self):
        """Предпросмотр печати"""
        if hasattr(self, 'table_result'):
            self.printer.print_preview(self.table_result, "DataFrame Report")

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
                    self.table_result.shape[0] + 1, 
                    self.table_result.shape[1], 
                    table_format
                )
                
                # Заголовки
                for col in range(self.table_result.shape[1]):
                    cursor.insertText(self.table_result.columns[col])
                    cursor.movePosition(QTextCursor.NextCell)
                
                # Данные
                for row in range(self.table_result.shape[0]):
                    for col in range(self.table_result.shape[1]):
                        cursor.insertText(str(self.table_result.iloc[row, col]))
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
                self.table_result.to_csv(filename, index=False, encoding='utf-8-sig', sep=';')
                QMessageBox.information(self, "Успех", "CSV успешно сохранен!")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")
    
    def export_to_json(self):
        """Экспорт в JSON"""
        filename, _ = QFileDialog.getSaveFileName(
            self, "Сохранить JSON", "", "JSON Files (*.json)")
        
        if filename:
            try:
                # Конвертируем DataFrame в словарь
                data_dict = self.table_result.to_dict(orient='records')
                
                # Сохраняем в файл с отступами
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(data_dict, f, ensure_ascii=False, indent=4)
                
                QMessageBox.information(self, "Успех", "JSON успешно сохранен!")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")
    
    def export_to_excel(self):
        """Экспорт в Excel (XLSX)"""
        try:
            import openpyxl  # Проверяем наличие модуля
        except ImportError:
            QMessageBox.critical(
                self, 
                "Ошибка", 
                "Для экспорта в Excel требуется модуль openpyxl.\n"
                "Установите его командой: pip install openpyxl"
            )
            return
        
        filename, _ = QFileDialog.getSaveFileName(
            self, "Сохранить Excel", "", "Excel Files (*.xlsx)")
        
        if filename:
            try:
                if not filename.endswith('.xlsx'):
                    filename += '.xlsx'
                
                with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                    self.table_result.to_excel(writer, index=False, sheet_name='Данные')
                
                QMessageBox.information(self, "Успех", "Excel файл успешно сохранен!")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
