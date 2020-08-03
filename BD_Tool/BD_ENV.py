import os
import json
import sys
import maya.cmds as cmds

def envSetup():
    directory = cmds.internalVar(userAppDir=True)
    configFile = os.path.join(directory, 'BD_Config.json')
    with open(configFile, 'r') as f:
        path = json.load(f)
    sys.path.append(path)

