import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFileDialog, QGridLayout, QLabel, QComboBox
from PyQt5.QtWebEngineWidgets import *

def CreateControllerWindow():
    global cw
    cw = controllerWindow()
    cw.show()

def CreateAddWindow():
    global a
    a = addWindow()
    a.show()

def CreateSelectWindow():
    global sw
    sw = selectWindow()
    sw.show()

class selectWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initAddUI()

    def generate_list(self):
        with open("profiles/all_profiles.txt", "r") as f:
            self.list_of_names = [line.strip() for line  in f]
        for e in self.list_of_names:
            self.dropDown.addItem(e)

    def getSelectedStudent(self):
        self.selectedStudent = self.dropDown.currentText()
        self.close()

    def initAddUI(self):
        self.setFixedSize(250,200)
        self.setWindowTitle("Select Student")
        self.selectedStudent = ""

        self.windowGrid = QGridLayout()

        #List that contains student names
        self.list_of_names = []

        self.dropDown = QComboBox();
        self.select = QPushButton("Select",self)
        self.cancel = QPushButton("Cancel",self)

        self.windowGrid.addWidget(self.dropDown,1,0,1,2)
        self.windowGrid.addWidget(self.select,2,0)
        self.windowGrid.addWidget(self.cancel,2,1)

        self.generate_list()

        self.cancel.clicked.connect(self.close)
        self.select.clicked.connect(self.getSelectedStudent)

        self.setLayout(self.windowGrid)

class addWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initAddUI()

    def createText(self):
        self.filePath = os.path.realpath("profiles/"+self.nameTextBox.text()+".txt")
        self.file = open(self.filePath, "a")
        self.file.write(self.nameTextBox.text()+"\n[]\n[]")
        self.file = open(os.path.realpath("profiles/all_profiles.txt"), "a")
        self.file.write(self.nameTextBox.text()+"\n")
        self.file.close()
        self.close()

    def initAddUI(self):
        self.setFixedSize(250,200)
        self.setWindowTitle("Add Student")

        self.WindowGrid = QGridLayout()

        self.nameLabel = QLabel("Name:")
        self.nameTextBox = QLineEdit()
        self.addButton = QPushButton("Add", self)
        self.cancelButton = QPushButton("Cancel",self)

        self.WindowGrid.addWidget(self.nameLabel,1,1)
        self.WindowGrid.addWidget(self.nameTextBox,1,2,1,3)
        self.WindowGrid.addWidget(self.addButton,3,2)
        self.WindowGrid.addWidget(self.cancelButton,3,3)

        self.cancelButton.clicked.connect(self.close)
        self.addButton.clicked.connect(self.createText)

        self.setLayout(self.WindowGrid)

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

    def initUI(self):

        self.setFixedSize(800,800)

        self.upload = QPushButton("Upload", self)
        self.upload.setToolTip("Upload student work")
        self.upload.resize(self.upload.sizeHint())

        self.path = QLineEdit()

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.upload,1,0)
        self.grid.addWidget(self.path,1,1,1,5)

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
        self.web.settings = QWebEngineView

        self.grid.addWidget(self.add,8,2)
        self.grid.addWidget(self.select,8,3)
        self.grid.addWidget(self.check,8,4)
        self.grid.addWidget(self.web,2,0,4,0)
        self.grid.addWidget(self.previewButton,1,6)

        self.upload.clicked.connect(self.getFile)
        self.previewButton.clicked.connect(self.preview)
        self.add.clicked.connect(CreateAddWindow)
        self.select.clicked.connect(CreateSelectWindow)

        self.setLayout(self.grid)

if __name__ == '__main__':
    open("profiles/all_profiles.txt","w").close()
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("Checkr")
    window = CreateControllerWindow()
    sys.exit(app.exec_())

