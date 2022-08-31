import bpy
from bpy.types import Panel
from . float_op import FLOAT_OT_Btn, FLOAT_OT_Close_Btn

class FLOAT_PT_Panel(Panel):
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_label = "Camera to View"
  bl_category = "Camera to View"

  def draw(self, context):
    layout = self.layout

    row = layout.row()
    col = row.column()
    col.operator(FLOAT_OT_Btn.bl_idname, text="Floating", icon="WINDOW")

    col = row.column()
    col.operator(FLOAT_OT_Close_Btn.bl_idname, text="Close", icon="PANEL_CLOSE")