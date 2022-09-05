import bpy
from bpy.types import Operator

class LOCK_OT_Camera_View(Operator):
    bl_idname = "space_data.lock_camera"
    bl_label = "Lock"
    bl_description = "Lock Camera to View"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        if context.space_data.lock_camera == False:
            return True
        else:
            return False

    def execute(self, context):
        context.space_data.lock_camera = True

        return {'FINISHED'}

class UNLOCK_OT_Camera_View(Operator):
    bl_idname = "space_data.unlock_camera"
    bl_label = "Unlock"
    bl_description = "Unlock Camera to View"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        if context.space_data.lock_camera == False:
            return False
        else:
            return True

    def execute(self, context):
        context.space_data.lock_camera = False

        return {'FINISHED'}