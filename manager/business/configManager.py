import os
import json

from .utils import envorimentVariables

class configManager:

    def __init__(self):
        self.permanentFile = envorimentVariables.settings_json.value[0]
        self.currentFile = envorimentVariables.current_settings_json.value[0]

    def addfolderInImageList(self,folder:str,carouselName:str):
        files = []
        for root,dirs,file_walks in os.walk(folder):
            files += [os.path.join(root,file) for file in file_walks if file.endswith('.jpg') | file.endswith('.png') | file.endswith('.jpeg')]

        self.addImagesInImageList(files,carouselName)

    def addImagesInImageList(self,images:list,carouselName:str):
        settings  = {}
        with open(self.currentFile,'r') as file:
            settings = json.load(file)
            
        current_carousel = carouselName

        for image in images:
            settings[current_carousel].append(image)

        set_images = set(settings[current_carousel])
        settings[current_carousel] = list(set_images)

        with open(self.currentFile,'w') as file:
            json.dump(settings,file,indent=4)

    def removeImageInImageList(self,images:list,carouselName:str):
        settings = {}
        with open(self.currentFile,'r') as file:
            settings = json.load(file)
        
        current_carousel = carouselName

        new_list = list(set(settings[current_carousel]) - set(images))
        settings[current_carousel] = new_list

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
