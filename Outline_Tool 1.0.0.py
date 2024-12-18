bl_info = {
    "name": "Nami's Toolbox",
    "author": "Naminiuk (Ivan Dylov)",
    "version": (1, 0, 0),
    "blender": (4, 3, 0),
    "location": "3D Viewport > Sidebar > Nami's Toolbox",
    "description": "Automatic outline creation",
    "category": "Development",
}

import bpy

def update_outline(self, context):
    """Update outline in real-time when properties are changed"""
    for so in context.selected_objects:
        if so.type == 'MESH':
            for mod in so.modifiers:
                if mod.type == 'SOLIDIFY':
                    mod.thickness = context.scene.outline_thickness
            for mat_slot in so.material_slots:
                mat = mat_slot.material
                if mat and "Outline" in mat.name:
                    nodes = mat.node_tree.nodes
                    emission_node = next((n for n in nodes if n.type == 'EMISSION'), None)
                    if emission_node:
                        emission_node.inputs[0].default_value = (*context.scene.outline_color, 1.0)

def register_properties():
    bpy.types.Scene.outline_thickness = bpy.props.FloatProperty(
        name="Outline Thickness",
        description="Thickness of the solidify modifier",
        default=0.1,
        min=-1.0,
        max=1.0,
        update=update_outline
    )

    bpy.types.Scene.outline_color = bpy.props.FloatVectorProperty(
        name="Outline Color",
        description="Color of the outline material",
        subtype='COLOR',
        default=(0.0, 0.0, 0.0),
        min=0.0, max=1.0,
        update=update_outline 
    )

class MESH_OT_outline_creation(bpy.types.Operator):
    """Apply outline to the selected objects"""
    bl_idname = "mesh.outline_creation"
    bl_label = "Apply Outline"
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context):
        for so in context.selected_objects:
            if so.type == 'MESH':
                
                outline_mat_name = f"Outline_{so.name}"
                existing_mat = bpy.data.materials.get(outline_mat_name)
                if not existing_mat:
                    new_mat = bpy.data.materials.new(name=outline_mat_name)
                    new_mat.use_nodes = True
                    nodes = new_mat.node_tree.nodes
                    links = new_mat.node_tree.links
                    
                    for node in nodes:
                        nodes.remove(node)
                    
                    output_node = nodes.new(type='ShaderNodeOutputMaterial')
                    emission_node = nodes.new(type='ShaderNodeEmission')
                    
                    output_node.location = (200, 0)
                    emission_node.location = (0, 0)
                    
                    links.new(emission_node.outputs[0], output_node.inputs[0])
                    emission_node.inputs[0].default_value = (*context.scene.outline_color, 1.0)
                    
                    new_mat.diffuse_color = (*context.scene.outline_color, 1.0) 
                else:
                    new_mat = existing_mat
                
                if not any(mat_slot.material == new_mat for mat_slot in so.material_slots):
                    so.data.materials.append(new_mat)
                
                solidify_mod = next((mod for mod in so.modifiers if mod.type == 'SOLIDIFY'), None)
                if not solidify_mod:
                    solidify_mod = so.modifiers.new(name="Solidify", type='SOLIDIFY')
                solidify_mod.thickness = context.scene.outline_thickness
                solidify_mod.offset = 1.0
        return {'FINISHED'}

class OBJECT_PT_outline_panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Outline Tool"
    bl_idname = "OBJECT_PT_outline_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Outline Tool'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "outline_thickness")
        layout.prop(context.scene, "outline_color")
        layout.operator("mesh.outline_creation", text="Apply Outline", icon='MOD_SOLIDIFY')

def register():
    bpy.utils.register_class(MESH_OT_outline_creation)
    bpy.utils.register_class(OBJECT_PT_outline_panel)
    register_properties()

def unregister():
    bpy.utils.unregister_class(MESH_OT_outline_creation)
    bpy.utils.unregister_class(OBJECT_PT_outline_panel)
    
    del bpy.types.Scene.outline_thickness
    del bpy.types.Scene.outline_color

if __name__ == "__main__":
    register()
