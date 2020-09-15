from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox

Ui_DataSetDescription, UiBaseClass = uic.loadUiType('./view/datasetdescription.ui')

import pandas as pd

from controller.dataframetablemodel import DataFrameTableModel

class DataSetDescription(QMainWindow, Ui_DataSetDescription):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_DataSetDescription.__init__(self)
        self.setupUi(self)

    def setData(self, data:pd.DataFrame):
        self.data = data
        self.updateTable()

    def updateTable(self):
        if not self.data.empty:
            self.tableView.setModel(DataFrameTableModel(self.data))
        else:
            QMessageBox.warning(self, 'No Connection', 'No Connection for DataFrame')