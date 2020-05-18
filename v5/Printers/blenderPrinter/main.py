from frame import *
from printer import BlenderPrinter
import json
from setup import Setup


setup = Setup()
setup.load()

frames = JsonFileToFrames(setup.inputFile)
print('Frames count = '+str(len(frames)))

printer = BlenderPrinter(len(frames), setup.outputDir, setup.FPS)
#print(sim.getGrowMatrix())


iter = 0
for frame in frames:
    printer.printFrame(frame, iter + 1)
    iter += 1
    
    #print('#' + str(iter))
    #print(sim.getGrowMatrix())