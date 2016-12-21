import bpy

def main(context):
	active_object = context.active_object
	a_key = active_object.data.shape_keys
	the_sk = bpy.data.shape_keys[a_key.name]
	basis = the_sk.reference_key
	count = len(basis.data.items())
	for kb in the_sk.key_blocks:
		if kb.name == basis.name: continue
		is_same = True
		for i in range(count):
			if kb.data[i].co != basis.data[i].co:
				is_same = False
				break
		if is_same:
			index = active_object.data.shape_keys.key_blocks.keys().index(kb.name)
			active_object.active_shape_key_index = index
			bpy.ops.object.shape_key_remove()
			print("Removing Shape Key: " + kb.name + " " + str(index))

class RESKOperator(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "object.remove_excess_shape_keys"
	bl_label = "Remove Excess Shape Keys"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		main(context)
		return {'FINISHED'}


def register():
	bpy.utils.register_class(RESKOperator)

def unregister():
	bpy.utils.unregister_class(RESKOperator)

if __name__ == "__main__":
	register()
