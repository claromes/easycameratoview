import bpy
from bpy.types import Operator, PropertyGroup

# DIALOG BOOL SETTINGS
class LOCK_Dialog_Settings(PropertyGroup):
  lock: bpy.props.BoolProperty()

# DIALOG OP
class LOCK_OT_Dialog(Operator):
  bl_idname = "wm.dialog"
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
      layout.prop(lock, "lock", text="", icon="LOCKED")
      context.space_data.lock_camera = True
    else:
      layout.prop(lock, "lock", text="", icon="UNLOCKED")
      context.space_data.lock_camera = False