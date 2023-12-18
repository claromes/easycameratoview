bl_info = {
    "name" : "Easy Camera to View",
    "description" : "Easy access to Camera to View",
    "author" : "Claromes",
    "version" : (0, 2, 0),
    "blender" : (4, 0, 2),
    "location" : "Header",
    "doc_url": "https://github.com/claromes/easy_camera_to_view",
    "tracker_url": "https://github.com/claromes/easy_camera_to_view/issues",
    "category": "Camera"
}

import bpy
from . header_ops import LOCK_OT_Camera_View, UNLOCK_OT_Camera_View
from . header_pnl import HEADER_MT_Panel

classes = (
    LOCK_OT_Camera_View,
    UNLOCK_OT_Camera_View,
    HEADER_MT_Panel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.VIEW3D_HT_header.append(header_pnl.HEADER_MT_Panel.draw)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.VIEW3D_HT_header.remove(header_pnl.HEADER_MT_Panel.draw)