import bpy

bl_info = {
    "name": "Enhance Plugin",
    "blender": (2, 80, 0),
    "category": "Object",
}

class OBJECT_OT_EnhanceBlur(bpy.types.Operator):
    bl_idname = "object.enhance_blur"
    bl_label = "Enhance Blur"
    bl_options = {'REGISTER', 'UNDO'}

    blur_factor: bpy.props.FloatProperty(
        name="Blur Factor",
        default=0.5,
        min=0.0,
        max=10.0
    )

    def execute(self, context):
        obj = context.object
        if obj and obj.type == 'MESH':
            modifier = obj.modifiers.new(name="Blur", type='SMOOTH')
            modifier.factor = self.blur_factor
            bpy.ops.object.modifier_apply(modifier="Blur")
            self.report({'INFO'}, "Blur applied to the object")
        else:
            self.report({'ERROR'}, "No mesh object selected")
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(OBJECT_OT_EnhanceBlur.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_EnhanceBlur)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_EnhanceBlur)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()
