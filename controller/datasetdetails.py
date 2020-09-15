from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout

Ui_DataSetBox, UiBaseClass = uic.loadUiType('./view/datasetdetails.ui')

from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
from matplotlib.figure import Figure

import pandas as pd

class DataSetDetails(QMainWindow, Ui_DataSetBox):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_DataSetBox.__init__(self)        
        self.setupUi(self)
                     
    def setData(self, text):
        self.textEdit.append(text)  
    