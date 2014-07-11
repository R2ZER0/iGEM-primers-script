# Qt's GUI stuff
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *
from primersapp import PrimersApp

    
# Create a new GUI application
application = QApplication(sys.argv)

window = PrimersApp()

# Run, be free!
sys.exit(application.exec_())