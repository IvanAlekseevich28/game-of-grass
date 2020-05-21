from frame import *
from printer import BlenderPrinter
import json
from setup import Setup

def appRun():
    s = Setup()
    if s.load():
        s.showSelf()
    else:
        s.consInit()
        s.save()

    frames = JsonFileToFrames(s.inputFile)
    print('Frames count = '+str(len(frames)))

    printer = BlenderPrinter(len(frames), s.outputDir, s.FPS)


    iter = 0
    for frame in frames:
        printer.printFrame(frame, iter + 1)
        iter += 1
    