import sys
import json

class configManager:

    def __init__(self):
        self.permanentFile = '../settings.json'
        self.currentFile = '../currentSettings.json'

    def fillCurrentFile(self,newConfigs:dict):
        currentConfigs = {}
        with open(self.currentFile,'r') as file:
            currentConfigs = json.load(file)
            currentConfigs.update(newConfigs)

        with open(self.currentFile,'w') as file:
            json.dump(currentConfigs,file,indent=4)

    def saveSettingsFile(self):

        settings = {}

        with open(self.currentFile,'r') as file:
            settings = json.load(file)
        
        with open(self.permanentFile,'w') as file:
            json.dump(settings,file,indent=4)
