from game_of_life import generateBoard, advanceBoard
import time
import bpy
import os
from createGrass import *
from changeGrow import *
bpy.app.debug = True


if __name__ == '__main__':
    f = generateBoard("......X.\nXX......\n.X...XXX")
    oldf = []
    out = ""
    grass = bpy.context.selected_objects[0]
    grasses = []
    steps = 5
    fps = 5
    secPerStep = 4 #constant
    bpy.context.scene.render.fps = fps
    framesPerStep = secPerStep*fps
    bpy.data.scenes['Scene'].frame_end = (steps-1)*framesPerStep
    for i in range(steps):
        for el in f:
            changed = False
            for g in grasses:
                if el.x == g[1] and el.y == g[2]:
                    grasses = changeGrow(el.x,el.y,el.grow,grasses)
                    changed = True
            if changed == False:
                grasses = createGrass(el.x, el.y, 0, el.grow, grass, grasses)
        oldf = f
        f = advanceBoard(f)
        bpy.data.scenes['Scene'].frame_current += framesPerStep
        print("out:\n" + out)