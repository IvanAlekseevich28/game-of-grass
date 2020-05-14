from simulator import Simulator
from grass import Grass
from rules import Rule
from conseedset import StartBoardGenerator
import numpy as np
from collections import namedtuple
from printer import *
from menu import *
from settings import Settings


menu = Menu(True)


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


seed = StartBoardGenerator(settings.settingsFN)
isSuccessfullyLoadS = seed.fileLoad()
if not isSuccessfullyLoadS:
    seed.consInit()
    seed.fileSave()



sim = Simulator(Rule(), seed.square_face)
sim.setSeed(seed.board)
printer = BlenderPrinter(settings.pictureDN)
printer.printFrame(sim.getCells(), 0)
#print(sim.getGrowMatrix())



for iter in range(settings.iteration):
    sim.simulateStep()
    printer.printFrame(sim.getCells(), iter + 1)
    #print('#' + str(iter))
    #print(sim.getGrowMatrix())