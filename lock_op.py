import bpy
from bpy.types import Operator

# poll_message_set
# report

# LOCK CAMERA OP
class LOCK_OT_Camera_View_On_Op(Operator):
  bl_idname = "space_data.lock_camera_on"
  bl_label = "Lock"
  bl_description = "Lock the Camera to View"

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

  @classmethod
  def poll(cls, context):
    if context.space_data.lock_camera == False:
      return False
    else:
      return True

  def execute(self, context):
    context.space_data.lock_camera = False

    return {"FINISHED"}