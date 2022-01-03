import bpy



class COS_PT_Command_On_Selected_Panel(bpy.types.Panel):
    """Command On Selected"""
    bl_label = "Command On Selected"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Command On Selected"

    @classmethod
    def poll(cls, context):
        if context.mode == "OBJECT":
            return True

    def draw(self, context):
        layout = self.layout
        scn = context.scene
        layout.label(text="Command on Selected:")
        layout.prop(scn, "COS_Commands", text="")
        layout.operator("cos.run_command_on_selected", text="Command On Selected")

classes = [COS_PT_Command_On_Selected_Panel]

def register():


    bpy.types.Scene.COS_Commands = bpy.props.StringProperty(default="bpy.ops.object.modifier_add(type='SUBSURF')")


    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():

    del bpy.types.Scene.COS_Commands


    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
