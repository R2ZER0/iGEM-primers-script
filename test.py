#!/usr/bin/python
# -*- coding: utf-8 -*-
# A simple primers generating test using sample data

# Our primers generating function
from primers import primers

# Biopython's sequence import library
from Bio import SeqIO

# Qt's stuff
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QDeclarativeView
 
# Create Qt application and the QDeclarative view
app = QApplication(sys.argv)
view = QDeclarativeView()
# Create an URL to the QML file
url = QUrl('view.qml')
# Set the QML file and show
view.setSource(url)
view.show()
# Enter Qt main loop
sys.exit(app.exec_())


