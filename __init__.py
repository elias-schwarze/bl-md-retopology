from . import addon_updater_ops
from . import mdr_prefs

bl_info = {
    "name": "MD Retopology",
    "author": "Elias Schwarze",
    "description": "A suite of tools for retopologizing Marvelous Designer garments in Blender",
    "blender": (3, 6, 0),
    "version": (0, 1, 0),
    "location": "3D Viewport > Properties panel (N) > MD Retopo Tab",
    "category": "Object"
}

classes = (mdr_prefs
           )


def register():

    addon_updater_ops.register(bl_info)

    for c in classes:
        c.register()


def unregister():

    for c in reversed(classes):
        c.unregister()

    addon_updater_ops.unregister()
