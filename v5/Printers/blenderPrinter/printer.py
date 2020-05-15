from simulator import Cell
import time
import bpy
import os
from drawGrass import *
bpy.app.debug = True


class BlenderPrinter:
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.lastFrame = set()
        
        
    def printFrame(self, frame:set, i):
        newEls = []
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