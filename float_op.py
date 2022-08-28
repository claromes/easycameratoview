import bpy, gpu
from bpy.types import Operator, PropertyGroup, Region
from gpu_extras.batch import batch_for_shader

class FLOAT_Btn_Settings(PropertyGroup):
  float_set: bpy.props.BoolProperty()

class FLOAT_OT_Btn(Operator):
  bl_idname = "wm.btn"
  bl_label = "Camera to View"
  bl_description = "Floating Camera to View"
  bl_options = {"REGISTER"}

  float_set: bpy.props.BoolProperty(name="float_set")

  @classmethod
  def poll(cls, context):
    return True

  def execute(self, context):
    return {"FINISHED"}

  def modal(self, context, event):
    context.area.tag_redraw()

    if event.type in {'ESC'}: #TODO: create close button
      bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
      bpy.data.images.remove(self.image)
      return {'CANCELLED'}

    if event.type in {'LEFTMOUSE'}:
      if event.value in {'CLICK'} and context.space_data.lock_camera == False:
        context.space_data.lock_camera = True
      elif event.value in {'CLICK'} and context.space_data.lock_camera == True:
        context.space_data.lock_camera = False

        return {'PASS_THROUGH'}

    return {'PASS_THROUGH'}

  def invoke(self, context, event):
    self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback, (self, context), 'WINDOW', 'POST_PIXEL')
    context.window_manager.modal_handler_add(self)

    return {'RUNNING_MODAL'}

def draw_callback(self, context):
  x = bpy.context.region.width
  y = bpy.context.region.height

  shader = gpu.shader.from_builtin('2D_IMAGE')

  batch = batch_for_shader(
      shader, 'TRI_FAN',
      {
          "pos": ((x - 230, y - 264), (x - 255, y - 264), (x - 255, y - 238), (x - 230, y - 238)), #TODO: dynamic position
          "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
      },
  )

  if context.space_data.lock_camera == True:
    self.image = bpy.data.images.load("//lock.png")
    self.texture = gpu.texture.from_image(self.image)
  elif context.space_data.lock_camera == False:
    self.image = bpy.data.images.load("//unlock.png")
    self.texture = gpu.texture.from_image(self.image)

  image = self.image
  texture = self.texture #TODO: fix alpha

  shader.bind()
  shader.uniform_sampler("image", texture)
  batch.draw(shader)