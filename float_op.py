import bpy
from bpy.types import Operator, PropertyGroup

# POPUP BOOL SETTINGS
class FLOAT_Popup_Settings(PropertyGroup):
  float_set: bpy.props.BoolProperty()

# POPUP OP
class FLOAT_OT_Popup(Operator):
  bl_idname = "wm.popup"
  bl_label = "Camera to View"
  bl_description = "Floating Camera to View"
  bl_options = {"REGISTER"}

  float_set: bpy.props.BoolProperty(name="float_set")

  @classmethod
  def poll(cls, context):
    return True

  def execute(self, context):
    return {"FINISHED"}

  def invoke(self, context, event):
    return context.window_manager.invoke_popup(self, width=82)

  def draw(self, context):
    layout = self.layout
    scene = context.scene
    float_popup = scene.float_set

    layout.label(text="Camera to View")

    if (float_popup.float_set == True):
      layout.prop(float_popup, "float_set", text="", icon="LOCKED")
      context.space_data.lock_camera = True

    else:
      layout.prop(float_popup, "float_set", text="", icon="UNLOCKED")
      context.space_data.lock_camera = False