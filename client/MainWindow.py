import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QFileDialog

class initGUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def getFile(self):
        self.fileName = QFileDialog.getOpenFileName(self,"Open File")
        self.path.setText(self.fileName[0])

    def initUI(self):
        self.upload = QPushButton("Upload", self)
        self.upload.setToolTip("Upload student work")
        self.upload.resize(self.upload.sizeHint())

        self.path = QLineEdit()

        hboxUpload = QHBoxLayout()
        hboxUpload.addWidget(self.upload)
        hboxUpload.addStretch()
        hboxUpload.addWidget(self.path)

        vbox = QVBoxLayout()
        vbox.addLayout(hboxUpload)
        vbox.addStretch()

        add = QPushButton("Add", self)

        hboxPreview = QHBoxLayout()
        hboxPreview.addWidget(add)

        vbox.addLayout(hboxPreview)

        self.upload.clicked.connect(self.getFile)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("Checkr")
    window = initGUI()
    window.show()
    sys.exit(app.exec_())

