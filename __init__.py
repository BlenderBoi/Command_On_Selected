bl_info = {
    "name": "Command On Selected",
    "author": "BlenderBoi",
    "version": (1, 0, 0),
    "blender": (3, 00, 0),
    "description": "",
    "category": "Experimental",
}

import bpy
from . import Command_On_Selected_Panel
from . import Run_Command

modules = [
    Command_On_Selected_Panel,
    Run_Command
    ]

def register():

    for module in modules:
        module.register()

def unregister():

    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
