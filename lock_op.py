import bpy
from bpy.types import Operator, PropertyGroup

# POPUP BOOL SETTINGS
class LOCK_Popup_Settings(PropertyGroup):
  lock_set: bpy.props.BoolProperty()

# POPUP OP
class LOCK_OT_Popup(Operator):
  bl_idname = "wm.popup"
  bl_label = "Camera to View"
  bl_description = "Un/Lock the Camera to View"
  bl_options = {"REGISTER"}

  lock: bpy.props.BoolProperty(name="Lock")

  @classmethod
  def poll(cls, context):
    return True

  def execute(self, context):
    return {"FINISHED"}

  def invoke(self, context, event):
    return context.window_manager.invoke_popup(self, width=40)

  def draw(self, context):
    layout = self.layout
    scene = context.scene
    lock = scene.lock

    #layout.label(text="Lock")

    if (lock.lock == True):
      layout.prop(lock_set, "lock", text="", icon="LOCKED")
      context.space_data.lock_camera = True
    else:
      layout.prop(lock_set, "lock", text="", icon="UNLOCKED")
      context.space_data.lock_camera = False