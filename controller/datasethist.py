from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout

Ui_DataSetHist, UiBaseClass = uic.loadUiType('./view/datasethist.ui')

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

class DataSetHist(QMainWindow, Ui_DataSetHist):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_DataSetHist.__init__(self)
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
            self.data.hist(ax=axes)
            self.toGraph()
            
    def mostrar3D(self):
        
        fig = plt.figure()
        ax = Axes3D(fig)
         
        # Creamos una malla, sobre la cual graficaremos el plano
        xx, yy = np.meshgrid(np.linspace(0, 3500, num=10), np.linspace(0, 60, num=10))
         
        # calculamos los valores del plano para los puntos x e y
        nuevoX = (regr2.coef_[0] * xx)
        nuevoY = (regr2.coef_[1] * yy) 
         
        # calculamos los correspondientes valores para z. Debemos sumar el punto de intercepción
        z = (nuevoX + nuevoY + regr2.intercept_)
         
        # Graficamos el plano
        ax.plot_surface(xx, yy, z, alpha=0.2, cmap='hot')
         
        # Graficamos en azul los puntos en 3D
        ax.scatter(XY_train[:, 0], XY_train[:, 1], z_train, c='blue',s=30)
         
        # Graficamos en rojo, los puntos que 
        ax.scatter(XY_train[:, 0], XY_train[:, 1], z_pred, c='red',s=40)
         
        # con esto situamos la "camara" con la que visualizamos
        ax.view_init(elev=30., azim=65)
                
        ax.set_xlabel('Cantidad de Palabras')
        ax.set_ylabel('Cantidad de Enlaces,Comentarios e Imagenes')
        ax.set_zlabel('Compartido en Redes')
        ax.set_title('Regresión Lineal con Múltiples Variables')
        
              
            
    