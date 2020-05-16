import bpy
def changeGrow(x, y, newGrow, grasses):
    newGrasses = []
    for el in grasses:
        if el[1] == x and el[2] == y :
            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.object.select_pattern(pattern=el[0].name)
            el[0].scale = (1,1, newGrow)
            #el[4] = newGrow
            bpy.ops.anim.keyframe_insert_menu(type='Scaling')
            newGrasses.append( (el[0], el[1], el[2], el[3], newGrow) )
        else:
            newGrasses.append(el)
    return newGrasses