from simulator import Simulator
from grass import Grass
from rules import Rule
from conseedset import StartBoardGenerator
import numpy as np
from collections import namedtuple
from settings import Settings
from frame import *
from menu import *


settings = Settings('settings.json')
isSuccessfullyLoadS = settings.loadSettings()
if not isSuccessfullyLoadS:
    settings.consInit()
    settings.saveSettings()


rule = Rule()
isSuccessfullyLoadS = rule.jsonToObj(settings.ruleFN)
if not isSuccessfullyLoadS:
    rule.consInit()
    rule.objToJson(settings.ruleFN)


seed = StartBoardGenerator(settings.seedFN)
isSuccessfullyLoadS = seed.fileLoad()
if not isSuccessfullyLoadS:
    seed.consInit()
    seed.fileSave()





def startSim():
    sim = Simulator(rule, seed.square_face)
    sim.setSeed(seed.board)

    print(sim.getGrowMatrix())

    frames = list()

    for iter in range(int(settings.iteration)):
        sim.simulateStep()
        frames.append(sim.getCells())

        print('#' + str(iter))
        print(sim.getGrowMatrix())

    frameToJsonFile(frames, settings.pictureDN, True)


def setSeed():
    seed.showSelf()
    seed.consInit()
    seed.fileSave()


def setRule():
    rule.showSelf()
    rule.consInit()
    rule.objToJson(settings.ruleFN)


def setFNSeed():
    print("Last: "+ settings.seedFN)
    settings.seedFN = input("Input seed file name: ")
    settings.saveSettings()


def setFNRule():
    print("Last: "+ settings.ruleFN)
    settings.ruleFN = input("Input rule file name: ")
    settings.saveSettings()



while True:
    action = askAction(mainMenu)
    if action == 1:
        startSim()
        break
    elif action == 2:
        settings.iteration = askIterations()
        settings.saveSettings()
    elif action == 3:
        setSeed()
    elif action == 4:
        setRule()
    elif action == 5:
        setFNSeed()
    elif action == 6:
        setFNRule()
