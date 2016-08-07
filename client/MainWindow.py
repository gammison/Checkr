import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFileDialog, QGridLayout
from PyQt5.QtWebEngineWidgets import *

class initGUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def getFile(self):
        self.fileName = QFileDialog.getOpenFileName(self,"Open File")
        self.path.setText(self.fileName[0])
        self.web.load(QUrl(self.path.text()))

    def initUI(self):

        self.setFixedSize(800,800)

        self.upload = QPushButton("Upload", self)
        self.upload.setToolTip("Upload student work")
        self.upload.resize(self.upload.sizeHint())

        self.path = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.upload,1,0)
        grid.addWidget(self.path,1,1,1,4)

        add = QPushButton("Add", self)
        add.setToolTip("Add student profiles")
        select = QPushButton("Select",self)
        select.setToolTip("Select student profiles")
        check = QPushButton("Check",self)
        check.setToolTip("Check work against past work")

        self.web = QWebEngineView()
        self.web.settings().setAttribute(QWebEngineSettings.PluginsEnabled,True)

        grid.addWidget(add,8,1)
        grid.addWidget(select,8,2)
        grid.addWidget(check,8,3)

        grid.addWidget(self.web,2,0,5,0)

        self.upload.clicked.connect(self.getFile)

        self.setLayout(grid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("Checkr")
    window = initGUI()
    window.show()
    sys.exit(app.exec_())

