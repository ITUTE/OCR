from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from scan import ScanImage


class UiScanform(object):
    def __init__(self):
        self.outputFolder = ""
        self.inputFolder = ""

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
        font.setPointSize(18)
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
        self.lblLinkInput.setGeometry(QtCore.QRect(100, 80, 200, 16))
        self.lblLinkInput.setObjectName("lblLinkInput")

        self.lblLinkOutput = QtWidgets.QLabel(self.centralwidget)
        self.lblLinkOutput.setGeometry(QtCore.QRect(100, 150, 200, 16))
        self.lblLinkOutput.setObjectName("lblLinkOutput")

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
        self.inputFolder = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        if self.inputFolder != "":
            self.lblLinkInput.setText(self.inputFolder)
            if self.outputFolder != "":
                self.btnStart.setEnabled(True)

    def loadOutputFolder(self):
        self.outputFolder = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        if self.outputFolder != "":
            self.lblLinkOutput.setText(self.outputFolder)
            if self.inputFolder != "":
                self.btnStart.setEnabled(True)

    def scan(self):
        scanImage = ScanImage(self.inputFolder, self.outputFolder)
        scanImage.scan()
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("All images are scanned successfully!")
        msg.setWindowTitle("Message")
        msg.exec_()

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = UiScanform()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
