import bpy, gpu
from bpy.types import Operator, Region
from gpu_extras.batch import batch_for_shader

close = False

class FLOAT_OT_Btn(Operator):
  bl_idname = "region_data.floating_button_camera"
  bl_label = "Camera to View"
  bl_description = "Floating Camera to View button"
  bl_options = {"REGISTER"}

  @classmethod
  def poll(cls, context):
    return True

  def execute(self, context):
    return {"FINISHED"}

  def modal(self, context, event):
    #bpy.data.images

    context.area.tag_redraw()

    if close == True:
      bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
      return {'CANCELLED'}

    if event.type in {'LEFTMOUSE'}: #TODO: get image position
      if event.value in {'CLICK'} and context.space_data.lock_camera == False:
        context.space_data.lock_camera = True
      elif event.value in {'CLICK'} and context.space_data.lock_camera == True:
        context.space_data.lock_camera = False

    return {'PASS_THROUGH'}

  def invoke(self, context, event):
    global close
    self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback, (self, context), 'WINDOW', 'POST_PIXEL')
    context.window_manager.modal_handler_add(self)

    close = False

    return {'RUNNING_MODAL'}

class FLOAT_OT_Close_Btn(Operator):
  bl_idname = "region_data.close_button_camera"
  bl_label = "Camera to View"
  bl_description = "Close Camera to View button"
  bl_options = {"REGISTER"}

  @classmethod
  def poll(cls, context):
    return True

  def execute(self, context):
    global close
    close = True

    return {"FINISHED"}

def draw_callback(self, context):
  x = bpy.context.region.width
  y = bpy.context.region.height

  shader = gpu.shader.from_builtin('2D_IMAGE')

  batch = batch_for_shader(
      shader, 'TRI_FAN',
      {
          "pos": ((x - 220, y - 267), (x - 255, y - 267), (x - 255, y - 238), (x - 220, y - 238)),
          "texCoord": ((1, 0), (0, 0), (0, 1), (1, 1)),
      },
  )

  if context.space_data.lock_camera == True:
    self.image = bpy.data.images.load("//lock.jpg")
    self.texture = gpu.texture.from_image(self.image)
  elif context.space_data.lock_camera == False:
    self.image = bpy.data.images.load("//unlock.jpg")
    self.texture = gpu.texture.from_image(self.image)

  image = self.image
  texture = self.texture

  shader.bind()
  shader.uniform_sampler("image", texture)
  batch.draw(shader)