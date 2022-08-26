import bpy
from bpy.types import Operator

# poll_message_set
# report

# LOCK CAMERA OP
class LOCK_OT_Camera_View_On_Op(Operator):
  bl_idname = "space_data.lock_camera_on"
  bl_label = "Lock"
  bl_description = "Lock the Camera to View"
  bl_options = {"REGISTER"}

  @classmethod
  def poll(cls, context):
    if context.space_data.lock_camera == False:
      return True
    else:
      return False

  def execute(self, context):
    context.space_data.lock_camera = True

    return {"FINISHED"}

# UNLOCK CAMERA OP
class LOCK_OT_Camera_View_Off_Op(Operator):
  bl_idname = "space_data.lock_camera_off"
  bl_label = "Unlock"
  bl_description = "Unlock the Camera to View"
  bl_options = {"REGISTER"}

  @classmethod
  def poll(cls, context):
    if context.space_data.lock_camera == False:
      return False
    else:
      return True

  def execute(self, context):
    context.space_data.lock_camera = False

    return {"FINISHED"}

# DIALOG OP
class LOCK_OT_Dialog(Operator):
  bl_idname = "wm.dialog"
  bl_label = "C2V"
  bl_options = {"REGISTER"}

  my_bool: bpy.props.BoolProperty(name="Lock")

  def execute(self, context):

    return {"FINISHED"}

  def invoke(self, context, event):
    return context.window_manager.invoke_props_dialog(self, width=100)
