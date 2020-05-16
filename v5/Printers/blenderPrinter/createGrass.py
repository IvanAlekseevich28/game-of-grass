import bpy

def createGrass(x, y, color, grow, grass, grasses):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_pattern(pattern=grass.name)
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
    grassCopy = bpy.context.selected_objects[0]
    grassCopy.location = (x, y, 0)
    grassCopy.scale = (1,1,grow)
    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
    grasses.append( (grassCopy, x, y, color, 1) )
    return grasses
    
