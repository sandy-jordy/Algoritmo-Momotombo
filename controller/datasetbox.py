from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout

Ui_DataSetBox, UiBaseClass = uic.loadUiType('./view/datasetbox.ui')

from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
from matplotlib.figure import Figure

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib as plt
from statsmodels.sandbox.regression.predstd import wls_prediction_std

from matplotlib.colors import ListedColormap
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')


class DataSetBox(QMainWindow, Ui_DataSetBox):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_DataSetBox.__init__(self)        
        self.setupUi(self)
                     

        # set graphCanvas
        self.canvas = FigureCanvas(Figure())
        vLayout = QVBoxLayout()
        vLayout.addWidget(self.canvas)
        self.graphCanvas.setLayout(vLayout)

        # Matplotlib Toolbar
        self.addToolBar(NavigationToolbar2QT(self.canvas, self))

    def setData(self, data:pd.DataFrame):
        self.data = data
        self.updatePlot()    

    def addSubplot(self, dRows, dColumns, position):
        return self.canvas.figure.add_subplot(dRows, dColumns, position)

    def toGraph(self):
        self.canvas.figure.tight_layout()
        self.canvas.draw()

    def updatePlot(self):
        if not self.data.empty:
            axes = self.addSubplot(1, 1, 1)
            self.data.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False, ax=axes)
            self.toGraph()
        else:
            QMessageBox.warning(self, 'No Connection', 'No Connection for DataFrame')