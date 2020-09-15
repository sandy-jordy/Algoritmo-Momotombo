from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox

Ui_MainWindow, UiBaseClass = uic.loadUiType('./view/mainwindow.ui')

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

#nuevos importes
from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn.tree import DecisionTreeClassifier 
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import *
from sklearn.discriminant_analysis import *
from sklearn.neighbors import *
from sklearn.tree import *
from sklearn.naive_bayes import *
from sklearn.svm import *
from sklearn.model_selection import *
from sklearn.metrics import *

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error
from matplotlib.colors import ListedColormap
import statsmodels.api as sm

import sys
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
#aqui terminan

class MainController(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # getting data set
        self.btnCargar.clicked.connect(self.browseSlot)
        self.btnCompare.clicked.connect(self.compareMethods)
        self.btnPredecir.clicked.connect(self.GuardarModelo)
       

    def browseSlot(self):
        ''' Called when the user presses the Browse button'''
        
        #self.debugPrint( "Browse button pressed" )
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "Abrir Archivo",
                        "",
                        "Todos los Archivos (*);;Archivos CSV (*.csv)",
                        options=options)
        if fileName:
            
            self.gettingDataSet(fileName)
            
            self.DataSetPage.setData(self.dataset)
            self.DataSetDescription.setData(self.dataset.describe())
            self.DataSetBox.setData(self.dataset)
            self.DataSetHist.setData(self.dataset)
            self.DataSetGraficador.setData(self.dataset)
            self.DataSetPrediccion.setDatos(self.dataset)
            
    def gettingDataSet(self, direccion):
        url = direccion
        names = ['mes','nacion_cod','GastoPublicidad','IngresoMensual']
        self.dataset:pd.DataFrame = pd.read_csv(url, sep=';', encoding='utf-8', names=names)
        
        
    def clean_dataset(self, df:pd.DataFrame):
        assert isinstance(df,pd.DataFrame), "df needs to be a pd.DataFrame"
        df.dropna(inplace=True)
        indices_to_keep=~df.isin([np.nan,np.inf,-np.inf]).any(1)
        return df[indices_to_keep].astype(np.float64)

    
    def compareMethods(self):
        self.clean_dataset(self.dataset)
        self.array=self.dataset.values
        #se pone el numero de columnas
        X=self.array[:,0:3]
        Y=self.array[:,3]
        validation_size=0.1
        seed=50
        X_e,X_t,Y_e,Y_t=train_test_split(X,Y,test_size=validation_size,random_state=seed)
        
        res = sm.OLS(Y,X).fit()
        
        self.DataSetDetails.setData("{}".format(res.summary()))
        self.DataSetDetails.setData("Parámetros: {}".format(res.params))

        self.DataSetDetails.setData("\n")

    
    def GuardarModelo(self):
        self.clean_dataset(self.dataset)
        self.array=self.dataset.values

        #se pone el numero de columnas
        X=self.array[:,0:3]
        Y=self.array[:,3]
        validation_size=0.1
        seed=50
        X_e,X_t,Y_e,Y_t=train_test_split(X,Y,test_size=validation_size,random_state=seed)
       
        reg=LinearRegression()
        reg.fit(X_e,Y_e)
        '''print(reg.score(X_t,Y_t))'''
        
        from sklearn.externals import joblib
        joblib.dump(reg,'modelo_entrenado.pkl')
        
    
       


        