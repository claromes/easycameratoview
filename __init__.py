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
from . lock_op import LOCK_Popup_Settings, LOCK_OT_Popup
from . lock_pnl import LOCK_PT_Panel

classes = (
    LOCK_Popup_Settings,
    LOCK_OT_Popup,
    LOCK_PT_Panel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.lock_set = bpy.props.PointerProperty(type=LOCK_Popup_Settings)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.lock_set