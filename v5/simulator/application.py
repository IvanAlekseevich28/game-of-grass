from simulator import Simulator
from grass import Grass
from rules import Rule
from conseedset import StartBoardGenerator
import numpy as np
from collections import namedtuple
from settings import Settings
from frame import *


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



sim = Simulator(Rule(), seed.square_face)
sim.setSeed(seed.board)

print(sim.getGrowMatrix())

frames = list()

for iter in range(int(settings.iteration)):
    sim.simulateStep()
    frames.append(sim.getCells())

    print('#' + str(iter))
    print(sim.getGrowMatrix())

frameToJsonFile(frames, settings.pictureDN, True)
