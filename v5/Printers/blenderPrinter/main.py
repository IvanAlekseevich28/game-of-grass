from frame import *
from printer import BlenderPrinter
import json


f = open('outputDir.json', 'r')
jsonDict = json.load(f)
f.close()
outputDir = str()
if 'output directory' not in jsonDict:
    outputDir = input('Input output dir: ')
    jsonDict.update({'output directory' : outputDir})

dataFN = str()
if 'data file name' not in jsonDict:
    dataFN = input('Input data file name: ')
    jsonDict.update({'data file name' : dataFN})

f = open('outputDir.json', 'w')
json.dump(jsonDict, f, indent=4)
f.close()

frames = JsonFileToFrames(dataFN)
print('Frames count = '+str(len(frames)))

printer = BlenderPrinter(outputDir)
#print(sim.getGrowMatrix())


iter = 0
for frame in range():
    printer.printFrame(frame, iter + 1)
    iter += 1
    
    #print('#' + str(iter))
    #print(sim.getGrowMatrix())