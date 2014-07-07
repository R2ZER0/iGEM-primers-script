#!/usr/bin/python
# -*- coding: utf-8 -*-
# A simple primers generating test using sample data

# Our primers generating function
from primers import primers

# Biopython's sequence import library
from Bio import SeqIO

# Qt's GUI stuff
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *

class MainWindow(QDeclarativeView):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("EdiGEM 2014: Primers")
        self.setSource(QUrl.fromLocalFile("view.qml"))
        self.setResizeMode(QDeclarativeView.SizeRootObjectToView)
    
if __name__ == '__main__':
    
    # Create a new GUI application
    application = QApplication(sys.argv)
    
    # Display our main window
    window = MainWindow()
    window.show()
    
    # Run, be free!
    sys.exit(application.exec_())
 