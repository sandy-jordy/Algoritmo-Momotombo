from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox

Ui_DataSetPage, UiBaseClass = uic.loadUiType('./view/datasetpage.ui')
from controller.dataframetablemodel import DataFrameTableModel

import pandas as pd

class DataSetPage(QMainWindow, Ui_DataSetPage):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_DataSetPage.__init__(self)
        self.setupUi(self)

    def setData(self, data:pd.DataFrame):
        self.data = data
        self.updateTable()

    def updateTable(self):
        if not self.data.empty:
            self.tableView.setModel(DataFrameTableModel(self.data))
        else:
            QMessageBox.warning(self, 'No Connection', 'No Connection for DataFrame')