bl_info = {
    "name" : "Floating Camera to View",
    "author" : "Claromes",
    "description" : "Fast access to Camera to View",
    "blender" : (3, 2, 2),
    "version" : (0, 1, 0),
    "location" : "View3D",
    "category" : "3D View",
    "doc_url": "https://github.com/claromes/floating_camera_to_view",
    "tracker_url": "https://github.com/claromes/floating_camera_to_view/issues"
}

import bpy
from . float_op import FLOAT_Popup_Settings, FLOAT_OT_Popup
from . float_pnl import FLOAT_PT_Panel

classes = (
    FLOAT_Popup_Settings,
    FLOAT_OT_Popup,
    FLOAT_PT_Panel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.float_set = bpy.props.PointerProperty(type=FLOAT_Popup_Settings)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.float_set