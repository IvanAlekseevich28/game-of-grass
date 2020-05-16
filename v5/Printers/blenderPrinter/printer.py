import time
import bpy
import os
from changeGrow import *
from createGrass import *
bpy.app.debug = True


class BlenderPrinter:
    def __init__(self, countOfFrames, dir_name):
        print(countOfFrames)
        self.dir_name = dir_name
        self.grass = bpy.context.selected_objects[0]
        self.grasses = []
        fps = 5
        secPerStep = 4 #constant
        bpy.context.scene.render.fps = fps
        self.framesPerStep = secPerStep*fps
        bpy.data.scenes['Scene'].frame_end = (countOfFrames-1)*self.framesPerStep
        
        
    def printFrame(self, frame:set, i):
        for el in frame:
            changed = False
            for g in self.grasses:
                if el.x == g[1] and el.y == g[2]:
                    self.grasses = changeGrow(el.x, el.y, el.grow,self.grasses)
                    changed = True
            if changed == False:
                self.grasses = createGrass(el.x, el.y, 0, el.grow, self.grass, self.grasses)
        bpy.data.scenes['Scene'].frame_current += self.framesPerStep

        """newEls = []
        for el in frame:
            new = True
            for oldel in self.lastFrame:
                if ( oldel.x == el.x and oldel.y == el.y ):
                    new = False
            if ( new ):
                newEls.append( (el.x, el.y) )
        delta = []
        for el in frame:
            for oldel in self.lastFrame:
                if (el.x == oldel.x and el.y == oldel.y):
                    change = el.grow - oldel.grow
                    if ( change!=0 ):
                        delta.append( (el.x, el.y, oldel.grow, el.grow) )
        for el in frame:
            drawGrass(el.x,el.y,el.grow,el.color)
        bpy.context.scene.render.filepath = self.dir_name + str(i) +'.jpg'
        bpy.ops.render.render(write_still = True)
        self.lastFrame = frame
        print('out:\n' + 'newEls: ' + str(newEls) + '\n' + ' delta: ' + str(delta) + '\n'  )
        """
        """
    out = ""
    
    for i in range(steps):
        for el in frame:
            changed = False
            for g in grasses:
                if el.x == g[1] and el.y == g[2]:
                    grasses = changeGrow(el.x,el.y,el.grow,grasses)
                    changed = True
            if changed == False:
                grasses = createGrass(el.x, el.y, 0, el.grow, grass, grasses)
        f = advanceBoard(f)
        bpy.data.scenes['Scene'].frame_current += framesPerStep
        print("out:\n" + out)"""