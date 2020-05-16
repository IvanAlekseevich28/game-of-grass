from frame import *
from printer import BlenderPrinter
import json


f = open('C:\\Users\\Ivan\\gitProj\\game-of-grass\\v5\\Printers\\blenderPrinter\\outputDir.json', 'r')
jsonDict = json.load(f)
f.close()
outputDir = str()
if 'output directory' not in jsonDict:
    outputDir = 'C:\\Users\\Ivan\\Videos'
    jsonDict.update({'output directory' : outputDir})

dataFN = str()
if 'data file name' not in jsonDict:
    dataFN = "C:\\Users\\Ivan\\gitProj\\game-of-grass\\v5\\Printers\\consolePrinter\\out.json"
    jsonDict.update({'data file name' : dataFN})

f = open('outputDir.json', 'w')
json.dump(jsonDict, f, indent=4)
f.close()

frames = JsonFileToFrames("C:\\Users\\Ivan\\gitProj\\game-of-grass\\v5\\Printers\\consolePrinter\\out.json")
print('Frames count = '+str(len(frames)))

printer = BlenderPrinter(len(frames), 'C:\\Users\\Ivan\\Videos')
#print(sim.getGrowMatrix())


iter = 0
for frame in frames:
    printer.printFrame(frame, iter + 1)
    iter += 1
    
    #print('#' + str(iter))
    #print(sim.getGrowMatrix())