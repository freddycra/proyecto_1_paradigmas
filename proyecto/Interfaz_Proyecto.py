# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 12:46:59 2018

@author: krist
"""

# PyQt5 text area
# pythonprogramminglanguage.com

import sys
from PyQt5.Qt import QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QAction, QPlainTextEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QSize
import xml.etree.cElementTree as ET
from xml.dom import minidom


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
 
 
        abrir = QAction(QIcon('exit24.png'), 'Abrir TXT', self)
        abrir.triggered.connect(self.leerArchivo)
        fileMenu.addAction(abrir)
        
        abrir2 = QAction(QIcon('exit24.png'), 'Abrir XML', self)
        abrir2.triggered.connect(self.leerArchivo2)
        fileMenu.addAction(abrir2)
        
        guardar = QAction(QIcon('exit24.png'), 'Guardar TXT', self)
        guardar.triggered.connect(self.guardarArchivo)
        fileMenu.addAction(guardar)
        
        guardar2 = QAction(QIcon('exit24.png'), 'Guardar XML', self)
        guardar2.triggered.connect(self.guardarArchivo2)
        fileMenu.addAction(guardar2)
        
        cargar = QAction(QIcon('exit24.png'), 'Cargar Hileras', self)
        cargar.triggered.connect(self.cargarHileras)
        fileMenu.addAction(cargar)
        
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
        self.b.insertPlainText('α')
        
        
    @pyqtSlot()
    def on_click2(self):
        print('Botón de beta')
        self.b.insertPlainText('β')
        
    @pyqtSlot()
    def on_click3(self):
        print('Botón de gamma')
        self.b.insertPlainText('γ')

    @pyqtSlot()
    def on_click4(self):
        print('Botón de delta')
        self.b.insertPlainText('δ')
        
    @pyqtSlot()
    def on_click5(self):
        print('Botón de epsilon')
        self.b.insertPlainText('ε')
        
    @pyqtSlot()
    def on_click6(self):
        print('Botón de dzeta')
        self.b.insertPlainText('ζ')
    
    @pyqtSlot()
    def on_click7(self):
        print('Botón de eta')
        self.b.insertPlainText('η')

    @pyqtSlot()
    def on_click8(self):
        print('Botón de theta')
        self.b.insertPlainText('θ')
        
    @pyqtSlot()
    def on_click9(self):
        print('Botón de lambda')
        self.b.insertPlainText('λ')
        
    @pyqtSlot()
    def on_click10(self):
        print('Botón de mi')
        self.b.insertPlainText('μ')
        
    @pyqtSlot()
    def on_click11(self):
        print('Botón de xi')
        self.b.insertPlainText('ξ')
        
    @pyqtSlot()
    def on_click12(self):
        print('Botón de pi')
        self.b.insertPlainText('π')
        
    @pyqtSlot()
    def on_click13(self):
        print('Botón de phi')
        self.b.insertPlainText('φ')
        
    @pyqtSlot()
    def on_click14(self):
        print('Botón de omega')
        self.b.insertPlainText('Ω')
        
        
    def guardarArchivo(self):
        print('Guardando TXT')
        texto = self.b.toPlainText()
        direccion = self.saveFileDialog()
        if (not(direccion is 'nulo')):
            direccion = direccion+'.txt'
            f = open (direccion,'w')
            f.write(texto)
            f.close()
        else:
            print('El usuario canceló la operación')
            
            
    def guardarArchivo2(self):
        print('Guardando XML')
        texto = self.b.toPlainText()
        direccion = self.saveFileDialog()
        if (not(direccion is 'nulo')):
            root = ET.Element("root")
            doc = ET.SubElement(root, "doc")
            nodo1 = ET.SubElement(doc, "nodo1", name="nodo")
            nodo1.text = texto
            arbol = ET.ElementTree(root)
            direccion = direccion+'.xml'
            arbol.write(direccion)
        else:
            print('El usuario canceló la operación')
        
        
    def leerArchivo(self):
        print('Leyendo TXT')
        direccion = self.openFileNameDialogTXT()
        if (not(direccion is 'nulo')):
            f = open (direccion,'r')
            mensaje = f.read()
            self.b.clear()
            self.b.insertPlainText(mensaje)
            f.close()
        else:
            print('El usuario canceló la operación')

        
    def leerArchivo2(self):
        print('Leyendo XML')
        direccion = self.openFileNameDialogXML()
        if (not(direccion is 'nulo')):
            mydoc = minidom.parse(direccion)
            items = mydoc.getElementsByTagName('nodo1')
            print('Item 1 attribute:')  
            print(items[0].attributes['name'].value)
            print(items[0].firstChild.data)  
            self.b.clear()
            mensaje = items[0].firstChild.data
            self.b.insertPlainText(mensaje)
        else:
            print('El usuario canceló la operación')
        
    
    def cargarHileras(self):
        print('Cargando Hileras')
        direccion = self.openFileNameDialogTXT()
        if (not(direccion is 'nulo')):
            f = open (direccion,'r')
            mensaje = f.read()
            self.c.clear()
            self.c.insertPlainText(mensaje)
            f.close()
        else:
            print('El usuario canceló la operación')
        
    def openFileNameDialogTXT(self):   
        textoAuxiliar = 'nulo'
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Text Files (*.txt)", options=options)
        if fileName:
            #print(fileName)
            textoAuxiliar = fileName
        print(textoAuxiliar)
        return textoAuxiliar
        
    
    def openFileNameDialogXML(self):   
        textoAuxiliar = 'nulo'
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","XML Files (*.xml)", options=options)
        if fileName:
            #print(fileName)
            textoAuxiliar = fileName
        print(textoAuxiliar)
        return textoAuxiliar
 
    def saveFileDialog(self):    
        textoAuxiliar = 'nulo'
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            #print(fileName)
            textoAuxiliar = fileName
        print(textoAuxiliar)
        return textoAuxiliar
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit( app.exec_() )