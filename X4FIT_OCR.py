import logging
import os
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from scan import scan


class UiScanform(object):
    def __init__(self):
        self.inputFolder = ""
        self.outputFolder = ""
        self.numberOfImages = 0
        self.scannedImages = 0
        self.progress = ""
        self.done = False

    def setupUi(self, frmScan):
        frmScan.setObjectName("frmScan")
        frmScan.setWindowModality(QtCore.Qt.ApplicationModal)
        frmScan.setEnabled(True)
        frmScan.resize(450, 338)

        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setBold(True)
        font.setWeight(75)
        frmScan.setFont(font)

        frmScan.setMouseTracking(False)
        frmScan.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmScan.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(frmScan)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 941, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 220, 401, 61))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.btnInput = QtWidgets.QPushButton(self.groupBox)
        self.btnInput.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.btnInput.setAutoRepeat(True)
        self.btnInput.setAutoExclusive(True)
        self.btnInput.setAutoDefault(True)
        self.btnInput.setDefault(False)
        self.btnInput.setFlat(False)
        self.btnInput.setObjectName("btnInput")

        self.btnOutput = QtWidgets.QPushButton(self.groupBox)
        self.btnOutput.setGeometry(QtCore.QRect(150, 10, 101, 41))
        self.btnOutput.setAutoRepeat(True)
        self.btnOutput.setAutoExclusive(True)
        self.btnOutput.setAutoDefault(True)
        self.btnOutput.setDefault(False)
        self.btnOutput.setFlat(False)
        self.btnOutput.setObjectName("btnOutput")

        self.btnStart = QtWidgets.QPushButton(self.groupBox)
        self.btnStart.setGeometry(QtCore.QRect(290, 10, 101, 41))
        self.btnStart.setAutoRepeat(True)
        self.btnStart.setAutoExclusive(True)
        self.btnStart.setAutoDefault(True)
        self.btnStart.setDefault(False)
        self.btnStart.setFlat(False)
        self.btnStart.setEnabled(False)
        self.btnStart.setObjectName("btnStart")

        self.lblInput = QtWidgets.QLabel(self.centralwidget)
        self.lblInput.setGeometry(QtCore.QRect(30, 80, 81, 16))
        self.lblInput.setObjectName("lblInput")

        self.lblOutput = QtWidgets.QLabel(self.centralwidget)
        self.lblOutput.setGeometry(QtCore.QRect(30, 150, 81, 16))
        self.lblOutput.setObjectName("lblOutput")

        self.lblLinkInput = QtWidgets.QLabel(self.centralwidget)
        self.lblLinkInput.setGeometry(QtCore.QRect(100, 80, 300, 16))
        self.lblLinkInput.setObjectName("lblLinkInput")

        self.lblLinkOutput = QtWidgets.QLabel(self.centralwidget)
        self.lblLinkOutput.setGeometry(QtCore.QRect(100, 150, 300, 16))
        self.lblLinkOutput.setObjectName("lblLinkOutput")

        self.lblProgress = QtWidgets.QLabel(self.centralwidget)
        self.lblProgress.setGeometry(QtCore.QRect(30, 200, 300, 16))
        self.lblProgress.setObjectName("lblProgress")

        self.lblEllipsis = QtWidgets.QLabel(self.centralwidget)
        self.lblEllipsis.setGeometry(QtCore.QRect(100, 200, 300, 16))
        self.lblEllipsis.setObjectName("lblEllipsis")

        frmScan.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(frmScan)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 21))
        self.menubar.setObjectName("menubar")
        frmScan.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(frmScan)
        self.statusbar.setObjectName("statusbar")
        frmScan.setStatusBar(self.statusbar)

        self.retranslateUi(frmScan)
        QtCore.QMetaObject.connectSlotsByName(frmScan)

        # Events:
        self.btnInput.clicked.connect(self.loadInputFolder)
        self.btnOutput.clicked.connect(self.loadOutputFolder)
        self.btnStart.clicked.connect(self.scan)

    def loadInputFolder(self):
        if self.outputFolder == "":
            defaultPath = 'C:/'
        else:
            defaultPath = self.outputFolder
        self.inputFolder = QFileDialog.getExistingDirectory(None, 'Select a folder:', defaultPath,
                                                            QFileDialog.ShowDirsOnly)
        if self.inputFolder != "":
            self.lblLinkInput.setText(self.inputFolder)
            if self.outputFolder != "":
                self.btnStart.setEnabled(True)

    def loadOutputFolder(self):
        if self.inputFolder == "":
            defaultPath = 'C:/'
        else:
            defaultPath = self.inputFolder
        self.outputFolder = QFileDialog.getExistingDirectory(None, 'Select a folder:', defaultPath,
                                                             QFileDialog.ShowDirsOnly)
        if self.outputFolder != "":
            self.lblLinkOutput.setText(self.outputFolder)
            if self.inputFolder != "":
                self.btnStart.setEnabled(True)

    def scan(self):
        images = os.listdir(self.inputFolder)
        filenames = [(filename.split("."))[0] for filename in images]
        self.numberOfImages = len(filenames)
        dot = "."
        self.progress = "Progress: " + str(self.scannedImages) + "/" + str(self.numberOfImages)
        self.lblProgress.setText(self.progress)
        self.scanLoop(images, filenames)

        '''
        thread1 = threading.Thread(target=self.scanLoop(images, filenames))
        thread1.start()
        thread2 = threading.Thread(target=self.waitingLoop(dot))
        thread2.start()
        '''

    def scanLoop(self, images, filenames):
        for i, image in enumerate(images):
            try:

                scan(self.inputFolder, self.outputFolder, filenames, i, image)
                self.scannedImages += 1
                self.progress = "Progress: " + str(self.scannedImages) + "/" + str(self.numberOfImages)
                self.lblProgress.setText(self.progress)
            except Exception as e:
                logging.exception(e)

        self.done = True

        msg = QtWidgets.QMessageBox()
        if self.scannedImages == self.numberOfImages:
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("All images are scanned successfully!")
        else:
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Cannot scan all images in your chosen folder!")
        msg.setWindowTitle("Message")
        msg.exec_()

    def waitingLoop(self, dot):
        while not self.done:
            dot += "."
            if len(dot) == 6:
                dot = "."
            self.lblEllipsis.setText(dot)
            time.sleep(1)

    def retranslateUi(self, frmScan):
        _translate = QtCore.QCoreApplication.translate
        frmScan.setWindowTitle(_translate("frmScan", "SCANNING"))
        self.label.setText(_translate("frmScan", "X4FIT OCR"))
        self.btnInput.setText(_translate("frmScan", "Input Folder"))
        self.btnOutput.setText(_translate("frmScan", "Output Folder"))
        self.btnStart.setText(_translate("frmScan", "Start"))
        self.lblInput.setText(_translate("frmScan", "Input Link:"))
        self.lblOutput.setText(_translate("frmScan", "Output Link:"))
        self.lblLinkInput.setText(_translate("frmScan", "Choose Input Folder!"))
        self.lblLinkOutput.setText(_translate("frmScan", "Choose Output Folder!"))
        self.lblProgress.setText("")
        self.lblEllipsis.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = UiScanform()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
