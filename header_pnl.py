import bpy
from bpy.types import Menu
from . header_ops import LOCK_OT_Camera_View, UNLOCK_OT_Camera_View

class HEADER_MT_Panel(Menu):
    bl_label = 'Camera to View'
    bl_idname = 'HEADER_MT_Panel'

    def draw(self, context):
        layout = self.layout
        row = layout.row()

        lock = context.space_data.lock_camera

        if lock is not False:
            row.operator(UNLOCK_OT_Camera_View.bl_idname, text='Camera to View', icon='LOCKED', depress=True)
        else:
            row.operator(LOCK_OT_Camera_View.bl_idname, text='Camera to View', icon='UNLOCKED', depress=False)