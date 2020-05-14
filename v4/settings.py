from rules import Rule
from conseedset import StartBoardGenerator
import json


class Settings:
    def __init__(self, fileName):
        self.settingsFN = fileName
        self.ruleFN = None
        self.seedFN = None
        self.pictureDN = None

        self.consoleMode = False
        self.iteration = 1

    
    def consInit(self):
        self.consInitSeedFN()
        self.consInitRuleFN()
        self.consInitCountOfIteration()
        self.consInitPictureDN()


    def consInitSeedFN(self):
        self.seedFN = input('Input file name for seed: ')


    def consInitRuleFN(self):
        self.ruleFN = input('Input file name for rule: ')


    def consInitCountOfIteration(self):
        self.iteration = input("Input count of iteration for simulation:")


    def consInitPictureDN(self):
        self.pictureDN = input('Input directory name for output: ')


    def saveSettings(self) -> bool:
        f = open(self.settingsFN, 'w')
        if f.closed():
            return False

        jsonDict = {
            'Settings' : {
                'Iteration' : self.iteration,
                'Console mode' : self.consoleMode,
                'Rule FN' : self.ruleFN,
                'Seed FN' : self.seedFN,
                'Picture DN' : self.pictureDN
            }
        }

        json.dump(jsonDict, f, indent=4)

        f.close()

        return True

    
    def loadSettings(self) -> bool:
        f = open(self.settingsFN, 'r')
        if f.closed():
            return False

        jsonDict = json.load(f)
        if 'Settings' not in jsonDict:
            return False

        js = jsonDict['Settings']

        self.iteration      = js['Iteration']
        self.consoleMode    = js['Console mode']
        self.ruleFN         = js['Rule FN']
        self.seedFN         = js['Seed FN'] 
        self.pictureDN      = js['Picture DN']

        f.close()

        return True