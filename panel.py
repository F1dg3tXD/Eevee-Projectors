import bpy

class PROJECTOR_PT_main_panel(bpy.types.Panel):
    bl_label = "Eevee Projector Light"
    bl_idname = "PROJECTOR_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Create'
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.add_projector_light", text="Add Projector Light")

def register():
    bpy.utils.register_class(PROJECTOR_PT_main_panel)

def unregister():
    bpy.utils.unregister_class(PROJECTOR_PT_main_panel)
