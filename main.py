import bpy
from . import operator, panel

def register():
    operator.register()
    panel.register()

def unregister():
    operator.unregister()
    panel.unregister()
