import bpy

#bpy.ops.object.select_all(action='TOGGLE')
#grassExample = bpy.data.objects[1]
#grassExample.select = True

#plane = bpy.data.objects['Plane']
#plane.select = False

def drawGrass(x, y, grow, color):
	selectedObj = bpy.context.selected_objects[0]
	bpy.ops.object.duplicate()
	selectedObj.location = (x,y,0)
	selectedObj.scale = (1,1,grow)

#drawGrass(1,1,1,0)
#drawGrass(2,2,2,0)
#drawGrass(3,3,3,0)
#grassExample.hide = True
#grassExample.hide_render = True
#grassExample.hide_select = True