import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFileDialog, QGridLayout, QLabel
from PyQt5.QtWebEngineWidgets import *

class addWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def createText(self):
        filePath = os.path.realpath("profiles/"+self.nameTextBox.text()+".txt")
        print(os.path.exists(filePath))
        file = open(filePath, "r+")
        file.write(self.nameTextBox.text())

    def initUI(self):
        self.setFixedSize(400,400)
        self.setWindowTitle("Add Student")

        self.WindowGrid = QGridLayout()

        self.nameLabel = QLabel("Name:")
        self.nameTextBox = QLineEdit()
        self.addButton = QPushButton("Add", self)
        self.cancelButton = QPushButton("Cancel",self)

        self.WindowGrid.addWidget(self.nameLabel,1,0)
        self.WindowGrid.addWidget(self.nameTextBox,1,2)
        self.WindowGrid.addWidget(self.addButton,3,1)
        self.WindowGrid.addWidget(self.cancelButton,3,2)

        self.cancelButton.clicked.connect(self.close)
        self.addButton.clicked.connect(self.createText)

        self.setLayout(self.WindowGrid)
        self.show()

class controllerWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def getFile(self):
        self.fileName = QFileDialog.getOpenFileName(self,"Open File")
        self.path.setText(self.fileName[0])

    def preview(self):
        self.web.show()
        self.web.load(QUrl(self.path.text()))
    def createAddWindow(self):
        addStudent = addWindow()
        addStudent.__init__()
    def initUI(self):

        self.setFixedSize(800,800)

        self.upload = QPushButton("Upload", self)
        self.upload.setToolTip("Upload student work")
        self.upload.resize(self.upload.sizeHint())

        self.path = QLineEdit()

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.upload,1,0)
        self.grid.addWidget(self.path,1,1,1,4)

        self.previewButton = QPushButton("Preview",self)
        self.previewButton.setToolTip("Preview selected PDF")
        self.add = QPushButton("Add", self)
        self.add.setToolTip("Add student profiles")
        self.select = QPushButton("Select",self)
        self.select.setToolTip("Select student profiles")
        self.check = QPushButton("Check",self)
        self.check.setToolTip("Check work against past work")

        self.web = QWebEngineView()
        self.web.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

        self.grid.addWidget(self.add,8,1.5)
        self.grid.addWidget(self.select,8,2.5)
        self.grid.addWidget(self.check,8,3.5)
        self.grid.addWidget(self.web,2,0,4,0)
        self.grid.addWidget(self.previewButton,1,5)

        self.upload.clicked.connect(self.getFile)
        self.previewButton.clicked.connect(self.preview)
        self.add.clicked.connect(self.createAddWindow)

        self.setLayout(self.grid)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("Checkr")
    window = controllerWindow()
    sys.exit(app.exec_())

