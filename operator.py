import bpy
import os

class OBJECT_OT_add_projector_light(bpy.types.Operator):
    bl_idname = "object.add_projector_light"
    bl_label = "Add Projector Light"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        # Path to the blend file
        addon_directory = os.path.dirname(__file__)
        blend_file_path = os.path.join(addon_directory, "Projector.blend")
        
        # Name of the collection to append
        collection_name = "Projector"
        
        # Append the collection from the blend file
        with bpy.data.libraries.load(blend_file_path, link=False) as (data_from, data_to):
            if collection_name in data_from.collections:
                data_to.collections.append(collection_name)
            else:
                self.report({'ERROR'}, f"Collection '{collection_name}' not found in '{blend_file_path}'")
                return {'CANCELLED'}
        
        # Add the collection to the current scene
        for collection in data_to.collections:
            if collection is not None:
                # Ensure the collection is not linked and thus editable
                bpy.context.scene.collection.children.link(collection)
        
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_add_projector_light)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_projector_light)

if __name__ == "__main__":
    register()
