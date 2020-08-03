from Qt import QtWidgets, QtCore, QtGui
import maya.cmds as cmds
import os
import json
import shutil


class InstallationUI(QtWidgets.QDialog):

    def __init__(self):
        super(InstallationUI, self).__init__()
        self.setWindowTitle('BD_Tool_Installation')
        self.buildUI()

    def getMayaScriptFolder(self):
        USERAPPDIR = cmds.internalVar(userAppDir=True)
        DIRECTORY = os.path.join(USERAPPDIR, '2020/scripts')
        self.createDir(DIRECTORY)

    def getCustomFolder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, './', './');
        self.fileSource = os.path.join(directory, 'BD_ENV.py')
        self.createDir(directory)

    def createDir(self, dir):
        directory = cmds.internalVar(userAppDir=True)
        configFile = os.path.join(directory, 'BD_Config.json')



        with open(configFile, 'w') as f:
            json.dump(dir, f, indent=4)

        fileDestination = os.path.join(directory, 'scripts')
        print self.fileSource
        print fileDestination
        shutil.copy2(self.fileSource, fileDestination)



    def buildUI(self):
        layout = QtWidgets.QGridLayout(self)

        defualtBtw = QtWidgets.QPushButton('Defualt')
        defualtBtw.clicked.connect(self.close)
        layout.addWidget(defualtBtw, 0, 0)


        customBtw = QtWidgets.QPushButton('Custom')
        customBtw.clicked.connect(self.getCustomFolder)
        customBtw.clicked.connect(self.close)
        layout.addWidget(customBtw, 0, 1)

    def showUI(self):
        ui = InstallationUI()
        ui.show()
        return ui


InstallationCall = InstallationUI()
InstallationCallUI = InstallationUI().showUI()