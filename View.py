import sys
from Control import Control
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.control = Control()

        self.setMinimumSize(QSize(500, 240))
        self.setWindowTitle('Markov\'s Algorithm')

        self.b = QPlainTextEdit(self)
        self.b.move(10,10)
        self.b.resize(400, 200)

        button = QPushButton('Enter', self)
        button.clicked.connect(self.enterPressed)
        button.resize(50, 32)
        button.move(420,180)

    def enterPressed(self):
        self.control.addRules(self.b.toPlainText())
        self.control.printInfo()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
