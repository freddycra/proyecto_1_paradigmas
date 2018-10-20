# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 12:46:59 2018

@author: krist
"""

# PyQt5 text area
# pythonprogramminglanguage.com

import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QSize

class ExampleWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Proyecto Paradigmas'
        self.initUI()
        
        
    def initUI(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(1310, 800))    
        self.setWindowTitle("Proyecto Paradigmas") 

        # Add text field
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("Definiciones y Reglas\n")
        self.b.move(10,30)
        self.b.resize(900,360)
        
        self.b.setStyleSheet(
        """QPlainTextEdit {background-color: #333;
                           color: #00FF00;
                           font-size: 20px;
                           font-family: Courier;}""")
        
        self.c = QPlainTextEdit(self)
        self.c.insertPlainText("Pruebas y Testeo.\n")
        self.c.move(10,400)
        self.c.resize(640,390)
        
        self.c.setStyleSheet(
        """QPlainTextEdit {background-color: #333;
                           color: #00FF00;
                           font-size: 20px;
                           font-family: Courier;}""")

        self.d = QPlainTextEdit(self)
        self.d.insertPlainText("Resultado de la ejecución.\n")
        self.d.move(660,400)
        self.d.resize(640,390)
        self.d.setReadOnly(True)
        
        self.d.setStyleSheet(
        """QPlainTextEdit {background-color: #333;
                           color: #00FF00;
                           font-size: 20px;
                           font-family: Courier;}""")
        
        
        #Menu bar
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu('Archivo')
        ejecutar = mainMenu.addMenu('Ejecutar')
        helpMenu = mainMenu.addMenu('Help')
 
 
        abrir = QAction(QIcon('exit24.png'), 'Abrir', self)
        abrir.triggered.connect(self.leerArchivo)
        fileMenu.addAction(abrir)
        
        guardar = QAction(QIcon('exit24.png'), 'Guardar', self)
        guardar.triggered.connect(self.guardarArchivo)
        fileMenu.addAction(guardar)
        
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        
        paso = QAction(QIcon('exit24.png'), 'Paso a Paso', self)
        ejecutar.addAction(paso)
        
        correr = QAction(QIcon('exit24.png'), 'Correr', self)
        ejecutar.addAction(correr)

    
        button = QPushButton('α', self)
        button.setToolTip('Este es el botón de alpha')
        button.move(910,30) 
        button.resize(190,50)
        button.clicked.connect(self.on_click)
        
        button2 = QPushButton('β', self)
        button2.setToolTip('Este es el botón de beta')
        button2.move(1110,30) 
        button2.resize(190,50)
        button2.clicked.connect(self.on_click2)
 
        button3 = QPushButton('γ', self)
        button3.setToolTip('Este es el botón de gamma')
        button3.move(910,80) 
        button3.resize(190,50)
        button3.clicked.connect(self.on_click3)
        
        button4 = QPushButton('δ', self)
        button4.setToolTip('Este es el botón de delta')
        button4.move(1110,80) 
        button4.resize(190,50)
        button4.clicked.connect(self.on_click4)
        
        button5 = QPushButton('ε', self)
        button5.setToolTip('Este es el botón de epsilon')
        button5.move(910,130) 
        button5.resize(190,50)
        button5.clicked.connect(self.on_click5)
        
        button6 = QPushButton('ζ', self)
        button6.setToolTip('Este es el botón de dzeta')
        button6.move(1110,130) 
        button6.resize(190,50)
        button6.clicked.connect(self.on_click6)
        
        button7 = QPushButton('η', self)
        button7.setToolTip('Este es el botón de eta')
        button7.move(910,180) 
        button7.resize(190,50)
        button7.clicked.connect(self.on_click7)
        
        button8 = QPushButton('θ', self)
        button8.setToolTip('Este es el botón de theta')
        button8.move(1110,180) 
        button8.resize(190,50)
        button8.clicked.connect(self.on_click8)
        
        button9 = QPushButton('λ', self)
        button9.setToolTip('Este es el botón de lambda')
        button9.move(910,230) 
        button9.resize(190,50)
        button9.clicked.connect(self.on_click9)
        
        button10 = QPushButton('μ', self)
        button10.setToolTip('Este es el botón de mi')
        button10.move(1110,230) 
        button10.resize(190,50)
        button10.clicked.connect(self.on_click10)
        
        button11 = QPushButton('ξ', self)
        button11.setToolTip('Este es el botón de xi')
        button11.move(910,280) 
        button11.resize(190,50)
        button11.clicked.connect(self.on_click11)
        
        button12 = QPushButton('π', self)
        button12.setToolTip('Este es el botón de pi')
        button12.move(1110,280) 
        button12.resize(190,50)
        button12.clicked.connect(self.on_click12)
        
        button13 = QPushButton('φ', self)
        button13.setToolTip('Este es el botón de phi')
        button13.move(910,330) 
        button13.resize(190,60)
        button13.clicked.connect(self.on_click13)
        
        button14 = QPushButton('Ω', self)
        button14.setToolTip('Este es el botón de omega')
        button14.move(1110,330) 
        button14.resize(190,60)
        button14.clicked.connect(self.on_click14)
    
        stl = """QPushButton {
        background-color: #333;
        border-width: 2px;
        border-color: #00FF00;
        color: #00FF00;
        font-size: 30px;
        font-family: Courier;
        border-style: solid;
        }"""

        QApplication.instance().setStyleSheet(stl)
    
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        print('Botón de alpha')
        
    @pyqtSlot()
    def on_click2(self):
        print('Botón de beta')
        
    @pyqtSlot()
    def on_click3(self):
        print('Botón de gamma')

    @pyqtSlot()
    def on_click4(self):
        print('Botón de delta')
        
    @pyqtSlot()
    def on_click5(self):
        print('Botón de epsilon')
        
    @pyqtSlot()
    def on_click6(self):
        print('Botón de dzeta')
    
    @pyqtSlot()
    def on_click7(self):
        print('Botón de eta')

    @pyqtSlot()
    def on_click8(self):
        print('Botón de theta')
        
    @pyqtSlot()
    def on_click9(self):
        print('Botón de lambda')
        
    @pyqtSlot()
    def on_click10(self):
        print('Botón de mi')
        
    @pyqtSlot()
    def on_click11(self):
        print('Botón de xi')
        
    @pyqtSlot()
    def on_click12(self):
        print('Botón de pi')
        
    @pyqtSlot()
    def on_click13(self):
        print('Botón de phi')
        
    @pyqtSlot()
    def on_click14(self):
        print('Botón de omega')
        
        
    def guardarArchivo(self):
        print('Guardando')
        texto = self.b.toPlainText()
        f = open ('archivoSalida.txt','w')
        f.write(texto)
        f.close()
        
    def leerArchivo(self):
        print('Leyendo')
        f = open ('archivoSalida.txt','r')
        mensaje = f.read()
        self.b.clear()
        self.b.insertPlainText(mensaje)
        f.close()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit( app.exec_() )