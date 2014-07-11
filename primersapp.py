import sys
import re
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, IUPAC, _verify_alphabet
from primers import primers2
from StringIO import StringIO

class PrimersApp:
    def __init__(self):
        # Display our main window (using pure QML!)
        self.engine = QDeclarativeEngine()
        self.windowComponent = QDeclarativeComponent(self.engine, QUrl.fromLocalFile("view.qml"))
        
        self.currentSequence = Seq("", generic_dna)
        self.currentPrimers = {
            'UF': Seq("", generic_dna),
            'UR': Seq("", generic_dna),
            'DF': Seq("", generic_dna),
            'DR': Seq("", generic_dna)
        }
        
        if self.windowComponent.isError():
            print('QML ERROR:')
            print(self.windowComponent.errors())
            sys.exit(-1)

        else:
            self.window = self.windowComponent.create()
            self.window.show()
            
            # Connect up the signals
            self.engine.quit.connect(self.quit_slot)
            self.window.setSequenceFromClipFasta.connect(self.setSequenceFromClipFasta_slot)
            self.window.setSequenceFromClipRaw.connect(self.setSequenceFromClipRaw_slot)
            self.window.setSequenceRaw.connect(self.setSequenceRaw_slot)
            self.window.getPrimers.connect(self.getPrimers_slot)
            self.window.copyPrimer.connect(self.copyPrimer_slot)
            

    @Slot()
    def quit_slot(self):
        """When the application quits."""
        print("Ahh nooo I'm quitting!!")
        sys.exit()

    @Slot()
    def setSequenceFromClipFasta_slot(self):
        """When we want to use FASTA from the clipboard."""
        print("setSequenceFromClipFasta")
        clipboard = QClipboard()
        rawseq = clipboard.text()
        try:
            seq = SeqIO.read(StringIO(rawseq), "fasta").seq
            self.setSequenceRaw_slot(str(seq))
        except ValueError:
            self.errorMessage("This doesn't look like FASTA!\n\n" + str(rawseq[0:64]) + "...\n")

    @Slot()
    def setSequenceFromClipRaw_slot(self):
        """When using a raw sequence from the clipboard."""
        print("setSequenceFromClipRaw")
        clipboard = QClipboard()
        rawseq = clipboard.text()
        self.setSequenceRaw_slot(rawseq)

    @Slot(str)
    def setSequenceRaw_slot(self, rawseq):
        """Set the current sequence to the given one"""
        rawseq = re.compile('[\s]').sub('', rawseq.upper())
        try:
            seq = Seq(rawseq, IUPAC.unambiguous_dna)
            if not _verify_alphabet(seq):
                raise ValueError("Alphabet Verification Failed!")
            self.currentSequence = seq
            self.window.gotSequence.emit(str(self.currentSequence))
        except ValueError:
            self.errorMessage("This doesn't look like DNA!\n\n" + str(rawseq[0:64]) + "...\n")

    @Slot()
    def getPrimers_slot(self):
        """Generate the primers"""
        primers = primers2(self.currentSequence)
        self.currentPrimers = primers
        self.window.gotPrimers.emit(str(primers['UF']), str(primers['UR']), str(primers['DF']), str(primers['DR']))

    @Slot(str)
    def copyPrimer_slot(self, which):
        """Copy a given primer to the clipboard"""
        print("copyPrimer")
        QClipboard().setText(str(self.currentPrimers[which]))
        
    def errorMessage(self, message):
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()
