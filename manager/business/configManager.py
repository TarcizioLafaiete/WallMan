import os
import json

from .utils import envorimentVariables

class configManager:

    def __init__(self):
        self.permanentFile = envorimentVariables.settings_json.value[0]
        self.currentFile = envorimentVariables.current_settings_json.value[0]

    def addfolderInImageList(self,folder:str):
        files = []
        for root,dirs,file_walks in os.walk(folder):
            files += [os.path.join(root,file) for file in file_walks if file.endswith('.jpg') | file.endswith('.png') | file.endswith('.jpeg')]

        self.addImagesInImageList(files)

    def addImagesInImageList(self,images:list):
        settings  = {}
        with open(self.currentFile,'r') as file:
            settings = json.load(file)

        for image in images:
            settings['images_list'].append(image)

        with open(self.currentFile,'w') as file:
            json.dump(settings,file,indent=4)

    def removeImageInImageList(self,images:list):
        settings = {}
        with open(self.currentFile,'r') as file:
            settings = json.load(file)
        
        new_list = list(set(settings['images_list']) - set(images))
        settings['images_list'] = new_list

        with open(self.currentFile,'w') as file:
            json.dump(settings,file,indent=4)

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
