bl_info = {
    "name" : "Floating Camera to View",
    "author" : "Claromes",
    "description" : "Fast access to Camera to View",
    "blender" : (3, 2, 2),
    "version" : (0, 0, 5),
    "location" : "View3D",
    "category" : "3D View",
    "doc_url": "https://github.com/claromes/floating_camera_to_view",
    "tracker_url": "https://github.com/claromes/floating_camera_to_view/issues"
}

import bpy
from . float_op import FLOAT_OT_Btn, FLOAT_OT_Close_Btn
from . float_pnl import FLOAT_PT_Panel

classes = (
    FLOAT_OT_Btn,
    FLOAT_OT_Close_Btn,
    FLOAT_PT_Panel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)