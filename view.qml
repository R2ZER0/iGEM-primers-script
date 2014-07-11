import QtQuick 1.1
import QtDesktop 0.1

Window {
    id: window
    //width: 640
    //height: 480
    visible: true
    title: "EdiGEM2014: Clips Primers Generator"
    
    signal setSequenceFromClipFasta()
    signal setSequenceFromClipRaw()
    signal setSequenceRaw(string seq)
    
    signal gotSequence(string seq)
    
    signal getPrimers()
    signal gotPrimers(string uf, string ur, string df, string dr)
    
    signal copyPrimer(string which)
    
    
    onGotSequence: {
        sequenceTextArea.text = seq
        window.getPrimers()
    }
    
    onGotPrimers: {
        console.log("onGotPrimers")
        ufTextField.text = uf
        urTextField.text = ur
        dfTextField.text = df
        drTextField.text = dr
    }
    
    MenuBar {
        Menu {
            text: "File"
            MenuItem {
                text: "Quit"
                shortcut: "Ctrl+Q"
                onTriggered: Qt.quit()
            }
        }
    }
    
    Row {
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.topMargin: 5
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        height: parent.height
        width: parent.width
        
        Column {
            width: window.width*0.5
            
            Row {
                id: pasteButtonsRow
                Button {
                    text: "Paste FASTA"
                    onClicked: window.setSequenceFromClipFasta()
                }
                Button {
                    text: "Paste Sequence"
                    onClicked: window.setSequenceFromClipRaw()
                }
                Button {
                    text: "Get Primers"
                    onClicked: window.setSequenceRaw(sequenceTextArea.text)
                }
            }
            
            Label { text: "Part Sequence:"; id: partSequenceLabel }
            
            TextArea {
                id: sequenceTextArea
                text: ""
                width: parent.width
                height: window.height - (pasteButtonsRow.height + partSequenceLabel.height + 24)
                wrapMode: Text.WrapAnywhere
            }
        }
        
        Column {
            width: window.width*0.5
            spacing: 5
            
            Row {
                Text { text: "Clips Primers:" }
            }
            
            Row {
                Label { text: "UF"; id: ufLabel; font.pointSize: 14 }
                TextField {
                    id: ufTextField
                    readOnly: true
                    width: window.width*0.5 - (ufCopyButton.width + ufLabel.width)
                }
                Button {
                    text: "Copy UF"
                    id: ufCopyButton
                    onClicked: window.copyPrimer("UF")
                    height: parent.height
                }
            }
            
            Row {
                Label { text: "UR"; id: urLabel; font.pointSize: 14 }
                TextField {
                    id: urTextField
                    objectName: "urTextField"
                    width: window.width*0.5 - (urCopyButton.width + urLabel.width)
                }
                Button {
                    text: "Copy UR"
                    id: urCopyButton
                    onClicked: window.copyPrimer("UR")
                    height: parent.height
                }
            }
            
            Row {
                Label { text: "DF"; id: dfLabel; font.pointSize: 14 }
                TextField {
                    id: dfTextField
                    objectName: "dfTextField"
                    width: window.width*0.5 - (dfCopyButton.width + dfLabel.width)
                }
                Button {
                    text: "Copy DF"
                    id: dfCopyButton
                    onClicked: window.copyPrimer("DF")
                    height: parent.height
                }
            }
            
            Row {
                Label { text: "DR"; id: drLabel; font.pointSize: 14 }
                TextField {
                    id: drTextField
                    objectName: "drTextField"
                    width: window.width*0.5 - (drCopyButton.width + drLabel.width)
                }
                Button {
                    text: "Copy DR"
                    id: drCopyButton
                    onClicked: window.copyPrimer("DR")
                    height: parent.height
                }
            }
        }
        
    }
}

