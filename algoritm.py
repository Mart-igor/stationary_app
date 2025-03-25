import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


def calculate_stationary(self, start, end, x, ):
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