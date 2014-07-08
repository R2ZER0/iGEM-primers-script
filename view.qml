import QtQuick 1.1
import QtDesktop 0.1

Window {
    id: window
    width: 640
    height: 480
    visible: true
    
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
    

    Button {
        text: "Quit"
        onClicked: Qt.quit()
    }
}

