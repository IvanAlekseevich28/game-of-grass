from simulator import Simulator
from grass import Grass
from rules import Rule
from conseedset import StartBoardGenerator
import numpy as np
from collections import namedtuple
from printer import *


loadORInit = 'y'
seed = StartBoardGenerator(20, 'startPoints.txt')
if loadORInit == 'y':
    seed.fileLoad()
    seed.printPoints()
else:
    seed.consInit()

sim = Simulator(Rule(), seed.square_face)
sim.setSeed(seed.board)
printer = BlenderPrinter('C:\\Users\\FedEx\\Pictures\\Gol\\')
printer.printFrame(sim.getCells(), 0)
#print(sim.getGrowMatrix())



for iter in range(2):
    sim.simulateStep()
    printer.printFrame(sim.getCells(), iter + 1)
    #print('#' + str(iter))
    #print(sim.getGrowMatrix())