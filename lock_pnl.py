import bpy, bgl, blf
from bpy.types import Gizmo, GizmoGroup, Region

font_info = {
    "font_id": 0,
    "handler": None,
}

# Testing 3D view draw
class LOCK_GT_View3D(Gizmo):
  bl_idname = "LOCK_GT_VIEW3D"

  def init():
    font_info["handler"] = bpy.types.SpaceView3D.draw_handler_add(
      draw, (None, None), "WINDOW", "POST_PIXEL")

  if __name__ == "__main__":
      init()

  def draw(self, context):
    x = bpy.context.region.width - 100
    y = bpy.context.region.height - 500

    bgl.glEnable(bgl.GL_BLEND)

    font_id = font_info["font_id"]

    blf.position(font_id, x, y, 0)
    blf.size(font_id, 20, 96)
    blf.color(font_id, 1, 1, 1, 1)
    blf.draw(font_id, "LOCK")

    bgl.glDisable(bgl.GL_BLEND)

class LOCK_GT_OVERLAY(GizmoGroup):
    bl_idname = "LOCK_GGT_OVERLAY"
    bl_label = "Camera to View"
    bl_space_type = "VIEW_3D"
    bl_region_type = "WINDOW"
    bl_options = {"SELECT", "PERSISTENT"}

    def setup(self, context):
      self.gizmos.new(LOCK_GT_View3D.bl_idname)