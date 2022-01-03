import bpy



class COS_OT_Run_Command_On_Selected(bpy.types.Operator):
    """Command on Selected,
    NOTE: This is Prone to Error so Don't get Surprised"""
    bl_idname = "cos.run_command_on_selected"
    bl_label = "Run Command On Selected"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if context.mode == "OBJECT":
            return True

    def execute(self, context):
        scn = context.scene

        selected_objects = [object for object in context.selected_objects]
        active_object = context.active_object

        if len(selected_objects) > 0:

            # try:

            for object in context.view_layer.objects:
                object.select_set(False)

            for object in selected_objects:
                object.select_set(True)
                context.view_layer.objects.active = object


                try:
                    exec(scn.COS_Commands)

                except Exception as e:
                    self.report({"ERROR"}, scn.COS_Commands + " Failed To Run on " + object.name)
                    print(e)

                object.select_set(False)



            for object in selected_objects:
                object.select_set(True)

            context.view_layer.objects.active = active_object


        return {'FINISHED'}




classes = [COS_OT_Run_Command_On_Selected]

def register():


    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():


    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
