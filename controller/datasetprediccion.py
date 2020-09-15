from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets

Ui_DataSetBox, UiBaseClass = uic.loadUiType('./view/datasetprediccion.ui')

from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
from matplotlib.figure import Figure

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import *
from sklearn.discriminant_analysis import *
from sklearn.neighbors import *
from sklearn.tree import *
from sklearn.naive_bayes import *
from sklearn.svm import *
from sklearn.model_selection import *

class DataSetPrediccion(QMainWindow, Ui_DataSetBox):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_DataSetBox.__init__(self)        
        self.setupUi(self)
        self.CargarM.clicked.connect(self.cargarModelo)
        self.btnPVentas.clicked.connect(self.prediceValor)
        
    def setData(self, text):
        self.textEdit.append(text)  

    def cargarModelo(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "Abrir Archivo",
                        "",
                        "Todos los Archivos (*);;Archivos CSV (*.csv)",
                        options=options)
        if fileName:
            self.CargarModelo(fileName)
        
    def CargarModelo(self,filename):
        from sklearn.externals import joblib
        self.reg=joblib.load(str(filename))
        print(self.reg)
        
    def setDatos(self,data:pd.DataFrame):
        self.data = data  
        
    def prediceValor(self):
        self.array=self.data.values

        #se pone el numero de columnas
        X=self.array[:,0:3]
        Y=self.array[:,3]
        
        
        y_pred=self.reg.predict(X)
        error=np.sqrt(mean_squared_error(Y,y_pred))  
        r2=self.reg.score(X,Y)
        self.e1.setText('El valor del error es: '+str(error))
        self.e2.setText('El valor del r2 es: '+str(r2))   
        self.e3.setText('los coeficientes son: '+str(self.reg.coef_))
      
        #print('Los ingresos para el mes',mes,' en la nacion: ',nacion_cod,' con gasto de publicidad de: ',GastoPublicidad,' es: ',reg.predict([[mes,nacion_cod,GastoPublicidad]]))
        d1=int(self.meses.currentIndex()+1)
        d2=int(self.paises.currentIndex()+1)
        d3=int(self.txtpublicidad.toPlainText())
        self.textEdit.setText(str(int(self.reg.predict([[d1,d2,d3]]))))

