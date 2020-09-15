from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout

Ui_DataSetBox, UiBaseClass = uic.loadUiType('./view/grafico.ui')

from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
from matplotlib.figure import Figure

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from matplotlib.colors import ListedColormap
import statsmodels.api as sm
from sklearn.linear_model import *
from sklearn.discriminant_analysis import *
from sklearn.neighbors import *
from sklearn.tree import *
from sklearn.naive_bayes import *
from sklearn.svm import *
from sklearn.model_selection import *
from sklearn.metrics import *
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

class DataSetGraficador(QMainWindow, Ui_DataSetBox):
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

    def addSubplot(self):
        return self.canvas.figure.add_subplot(111,projection='3d')

    def toGraph(self):
        self.canvas.figure.tight_layout()
        self.canvas.draw()

    def updatePlot(self):
        if not self.data.empty:
       
            ax=self.addSubplot()
            
            ax.clear()
          
            ax.set_title('Gráfica de ingreso según el mes, país y publicidad.')
            ax.set_xlabel('mes')
            ax.set_ylabel('pais')
            ax.set_zlabel('publicidad')
            
            array=self.data.values
            a1=array[:,0]
            a2=array[:,1]
            a3=array[:,2]
            a4=array[:,3]
            
            m=ax.scatter(a1,a2,a3,c=a4,cmap=plt.hot())
            ax.figure.colorbar(m)
            
            self.toGraph()
        else:
            QMessageBox.warning(self, 'No Connection', 'No Connection for DataFrame')
        
        


