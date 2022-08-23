import bpy
from bpy.types import Panel

class LOCK_PT_Panel(Panel):
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_label = "Camera to View"
  bl_category = "Camera"

  def draw(self, context):

    layout = self.layout

    row = layout.row()
    col = row.column()
    col.operator("space_data.lock_camera_on", text="Lock")

    col = row.column()
    col.operator("space_data.lock_camera_off", text="Unlock")