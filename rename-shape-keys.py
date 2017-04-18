import bpy

active_object = bpy.context.active_object
a_key = active_object.data.shape_keys
the_sk = bpy.data.shape_keys[a_key.name]
basis = the_sk.reference_key
count = len(basis.data.items())
for kb in the_sk.key_blocks:
	# kb.name = kb.name.replace("", "")
