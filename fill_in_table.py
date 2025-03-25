def fill_in_the_table(self, table):
    self.ui.table_classification.setRowCount(self.data_graph.shape[0])
    self.ui.table_classification.setColumnCount(self.data_graph.shape[1])
    self.ui.table_classification.setHorizontalHeaderLabels(self.data_graph.columns)
    
    for i in range(self.data_graph.shape[0]):
        for j in range(self.data_graph.shape[1]):
            self.ui.table_classification.setItem(i, j, QTableWidgetItem(str(self.data_graph.iat[i, j])))