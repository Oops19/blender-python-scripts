# Add the Move Rig
armature_name = 'rig'  # The rig  'rig.Largedog'

o19_Root_Bone = 'b__ROOT__'  # The root bone of the rig
o19_Move_Bone = 'b__MoveBone'

o19_R_Front__IK = 'b__R_Front__IK'
o19_L_Front__IK = 'b__L_Front__IK'
o19_R_Hind__IK = 'b__R_Hind__IK'
o19_L_Hind__IK = 'b__L_Hind__IK'

o19_R_Front__Pole = 'b__R_Front__Pole'
o19_L_Front__Pole = 'b__L_Front__Pole'
o19_R_Hind__Pole = 'b__R_Hind__Pole'
o19_L_Hind__Pole = 'b__L_Hind__Pole'

o19_Root_Bind_Bone = 'b__ROOT_bind__'
o19_R_Front_Paw = 'b__R_Mid1__'
o19_L_Front_Paw = 'b__L_Mid1__'
o19_R_Hind_Paw = 'b__R_Toe1__'
o19_L_Hind_Paw = 'b__L_Toe1__'

o19_R_Front_Hip = 'b__R_ArmExportPole__'  # b__R__UpperArm__  # b__R__ArmExportPole__
o19_L_Front_Hip = 'b__L_ArmExportPole__'
o19_R_Hind_Hip = 'b__R_LegExportPole__'  # b__R_Thigh__
o19_L_Hind_Hip = 'b__L_LegExportPole__'



body_height = 1.6 # llama=1.6 - dog=0.8 # .8 = 80 cm = 8 dm
body_width = 0.5  # .4 = 40 cm = 4 dm
body_front_y = 0.1  # .2 = 20 cm = 2 dm
body_hind_y = 0.6  # .6 = 60 cm = 6 dm

hind_bone_z = body_height / 2  # .4 = 4 dm
bone_x = body_width / 2   # 0.2 = 2 dm
move_bones_1 = {
    o19_Move_Bone: {
        'parent': o19_Root_Bone,
        'head': [0.0, 0.0, body_height],  # 0/0/.8 - 0.8m above center
        'tail': [0.0, 0.0, 0.1],  # 0/0/.1 - 1dm length
    },
}
move_bones_2 = {
    o19_R_Front__IK: {
        'parent': o19_Move_Bone,
        'pos': o19_R_Front_Paw,
        'offset': [0, 0, 0],
        'tail': [0.0, 0.0, 0.1],  # 0/0/.01 - 1dm length
    },
    o19_L_Front__IK: {
        'parent': o19_Move_Bone,
        'pos': o19_L_Front_Paw,
        'offset': [0, 0, 0],
        'tail': [0.0, 0.0, 0.1],  # 0/0/.01 - 1dm length
    },
    o19_R_Hind__IK: {
        'parent': o19_Move_Bone,
        'pos': o19_R_Hind_Paw,
        'offset': [0, 0, 0],
        'tail': [0.0, 0.0, 0.1],  # 0/0/.01 - 1dm length
    },
    o19_L_Hind__IK: {
        'parent': o19_Move_Bone,
        'pos': o19_L_Hind_Paw,
        'offset': [0, 0, 0],
        'tail': [0.0, 0.0, 0.1],  # 0/0/.01 - 1dm length
    },

    o19_R_Front__Pole: {
        'parent': o19_Move_Bone,
        'pos': o19_R_Hind_Paw,  # Hind Pole above Back
        'offset': [-0.2, -0.4, hind_bone_z],  # -.2/-.3/.4 - 2dm to the left, 3dm to the front, 4dm up
        'tail': [0.0, 0.0, 0.1],  # 0/0/.01 - 1dm length
    },
    o19_L_Front__Pole: {
        'parent': o19_Move_Bone,
        'pos': o19_L_Hind_Paw,  # Hind Pole above Back
        'offset': [0.2, -0.4, hind_bone_z],  # +.2/-.3/0 - 2dm to the right, 3dm to the front
        'tail': [0.0, 0.0, 0.1],  # 0/0/.1 - 1dm length
    },
    o19_R_Hind__Pole: {
        'parent': o19_Move_Bone,
        'pos': o19_R_Front_Paw,  # Hind Pole above Front
        'offset': [-0.2, 0.4, hind_bone_z],  # -.2/+.3/.8 - 2dm to the left, 3dm to the back
        'tail': [0.0, 0.0, 0.1],  # 0/0/.1 - 1dm length
    },
    o19_L_Hind__Pole: {
        'parent': o19_Move_Bone,
        'pos': o19_L_Front_Paw,  # Hind Pole above Front
        'offset': [0.2, 0.4, hind_bone_z],
        'tail': [0.0, 0.0, 0.1],  # 0/0/.1 - 1dm length
    },
}

bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.mode_set(mode='EDIT', toggle=False)
bpy.ops.object.mode_set(mode='EDIT')
arm = bpy.data.objects[armature_name]
bpy.context.scene.objects.active = arm

# TODO select the rig properly


for bone_name, bone_definition in move_bones_1.items():
    print(bone_name)
    bone = arm.data.edit_bones.new(bone_name)
    parent_bone = bone_definition.get('parent')
    setattr(bone, 'parent', arm.data.edit_bones[parent_bone])
    setattr(bone, 'head', bone_definition.get('head'))
    x, y, z = bone_definition.get('head')
    xx, yy, zz = bone_definition.get('tail')
    print(x, y, z)
    print(xx, yy, zz)
    setattr(bone, 'tail', [x+xx, y+yy, z+zz])

for bone_name, bone_definition in move_bones_2.items():
    print(bone_name)
    bone = arm.data.edit_bones.new(bone_name)
    pos_name = bone_definition.get('pos')
    pos_bone = arm.data.edit_bones[pos_name]
    x, y, z = pos_bone.head
    xd, yd, zd = bone_definition.get('offset')
    x += xd
    #y += yd
    z += zd
    xt, yt, zt = bone_definition.get('tail')
    xt += x
    yt += y
    zt += z
    parent_bone = bone_definition.get('parent')
    setattr(bone, 'parent', arm.data.edit_bones[parent_bone])
    setattr(bone, 'head', [x, y, z])
    setattr(bone, 'tail', [xt, yt, zt])



############################




bpy.ops.object.mode_set(mode='POSE', toggle=False)
arm = bpy.data.objects[armature_name]
pole_bones = {
    o19_Root_Bind_Bone: {
        'CHILD_OF':
            [('influence', 1.0), ('is_proxy_local', False), ('mute', False), ('name', 'Child Of'), ('owner_space', 'POSE'),
             ('show_expanded', True), ('subtarget', o19_Move_Bone), ('target_space', 'WORLD'),
             ('use_location_x', True), ('use_location_y', True), ('use_location_z', True),
             ('use_rotation_x', True), ('use_rotation_y', True), ('use_rotation_z', True),
             ('use_scale_x', True), ('use_scale_y', True), ('use_scale_z', True)]
    },
    o19_R_Front_Hip: {
        'COPY_LOCATION':
            [('head_tail', 0.0), ('influence', 1.0), ('invert_x', False), ('invert_y', False), ('invert_z', False), ('is_proxy_local', False), ('mute', False), ('name', 'Copy Location'), ('owner_space', 'WORLD'), ('show_expanded', True), ('subtarget', o19_R_Front__Pole), ('target', arm),
             ('target_space', 'WORLD'), ('use_bbone_shape', False), ('use_offset', False), ('use_x', True), ('use_y', True), ('use_z', True)]
    },
    o19_L_Front_Hip: {
        'COPY_LOCATION':
            [('head_tail', 0.0), ('influence', 1.0), ('invert_x', False), ('invert_y', False), ('invert_z', False), ('is_proxy_local', False), ('mute', False), ('name', 'Copy Location'), ('owner_space', 'WORLD'), ('show_expanded', True), ('subtarget', o19_L_Front__Pole), ('target', arm),
             ('target_space', 'WORLD'), ('use_bbone_shape', False), ('use_offset', False), ('use_x', True), ('use_y', True), ('use_z', True)]
    },
    o19_R_Hind_Hip: {
        'COPY_LOCATION':
            [('head_tail', 0.0), ('influence', 1.0), ('invert_x', False), ('invert_y', False), ('invert_z', False), ('is_proxy_local', False), ('mute', False), ('name', 'Copy Location'), ('owner_space', 'WORLD'), ('show_expanded', True), ('subtarget', o19_R_Hind__Pole), ('target', arm),
             ('target_space', 'WORLD'), ('use_bbone_shape', False), ('use_offset', False), ('use_x', True), ('use_y', True), ('use_z', True)]
    },
    o19_L_Hind_Hip: {
        'COPY_LOCATION':
            [('head_tail', 0.0), ('influence', 1.0), ('invert_x', False), ('invert_y', False), ('invert_z', False), ('is_proxy_local', False), ('mute', False), ('name', 'Copy Location'), ('owner_space', 'WORLD'), ('show_expanded', True), ('subtarget', o19_L_Hind__Pole), ('target', arm),
             ('target_space', 'WORLD'), ('use_bbone_shape', False), ('use_offset', False), ('use_x', True), ('use_y', True), ('use_z', True)]
    },

}
ik_bones = {
    o19_R_Front_Paw: {
        'IK':
            [('active', True), ('chain_count', 4), ('distance', 1.0), ('ik_type', 'COPY_POSE'), ('influence', 1.0), ('is_proxy_local', False), ('iterations', 500),
             ('limit_mode', 'LIMITDIST_INSIDE'), ('lock_location_x', True), ('lock_location_y', True), ('lock_location_z', True), ('lock_rotation_x', True), ('lock_rotation_y', True), ('lock_rotation_z', True), ('mute', False), ('name', 'IK'), ('orient_weight', 1.0), ('owner_space', 'WORLD'),
             ('pole_angle', 0.0), ('pole_subtarget', o19_R_Front__Pole), ('pole_target', arm), ('reference_axis', 'BONE'), ('show_expanded', True), ('subtarget', o19_R_Front__IK), ('target', arm), ('target_space', 'WORLD'), ('use_location', True), ('use_rotation', True),
             ('use_stretch', True), ('use_tail', True), ('weight', 1.0)]
    },
    o19_L_Front_Paw: {
        'IK':
            [('active', True), ('chain_count', 4), ('distance', 1.0), ('ik_type', 'COPY_POSE'), ('influence', 1.0), ('is_proxy_local', False), ('iterations', 500),
             ('limit_mode', 'LIMITDIST_INSIDE'), ('lock_location_x', True), ('lock_location_y', True), ('lock_location_z', True), ('lock_rotation_x', True), ('lock_rotation_y', True), ('lock_rotation_z', True), ('mute', False), ('name', 'IK'), ('orient_weight', 1.0), ('owner_space', 'WORLD'),
             ('pole_angle', 0.0), ('pole_subtarget', o19_L_Front__Pole), ('pole_target', arm), ('reference_axis', 'BONE'), ('show_expanded', True), ('subtarget', o19_L_Front__IK), ('target', arm), ('target_space', 'WORLD'), ('use_location', True), ('use_rotation', True),
             ('use_stretch', True), ('use_tail', True), ('weight', 1.0)]
    },
    o19_R_Hind_Paw: {
        'IK':
            [('active', True), ('chain_count', 4), ('distance', 1.0), ('ik_type', 'COPY_POSE'), ('influence', 1.0), ('is_proxy_local', False), ('iterations', 500),
             ('limit_mode', 'LIMITDIST_INSIDE'), ('lock_location_x', True), ('lock_location_y', True), ('lock_location_z', True), ('lock_rotation_x', True), ('lock_rotation_y', True), ('lock_rotation_z', True), ('mute', False), ('name', 'IK'), ('orient_weight', 1.0), ('owner_space', 'WORLD'),
             ('pole_angle', 0.0), ('pole_subtarget', o19_R_Hind__Pole), ('pole_target', arm), ('reference_axis', 'BONE'), ('show_expanded', True), ('subtarget', o19_R_Hind__IK), ('target', arm), ('target_space', 'WORLD'), ('use_location', True), ('use_rotation', True),
             ('use_stretch', True), ('use_tail', True), ('weight', 1.0)]
    },
    o19_L_Hind_Paw: {
        'IK':
            [('active', True), ('chain_count', 4), ('distance', 1.0), ('ik_type', 'COPY_POSE'), ('influence', 1.0), ('is_proxy_local', False), ('iterations', 500),
             ('limit_mode', 'LIMITDIST_INSIDE'), ('lock_location_x', True), ('lock_location_y', True), ('lock_location_z', True), ('lock_rotation_x', True), ('lock_rotation_y', True), ('lock_rotation_z', True), ('mute', False), ('name', 'IK'), ('orient_weight', 1.0), ('owner_space', 'WORLD'),
             ('pole_angle', 0.0), ('pole_subtarget', o19_L_Hind__Pole), ('pole_target', arm), ('reference_axis', 'BONE'), ('show_expanded', True), ('subtarget', o19_L_Hind__IK), ('target', arm), ('target_space', 'WORLD'), ('use_location', True), ('use_rotation', True),
             ('use_stretch', True), ('use_tail', True), ('weight', 1.0)]
    },
}


for bone_name, add_constraints in pole_bones.items():
    p_bone = arm.pose.bones[bone_name]
    for _type, constraints in add_constraints.items():
        crc = p_bone.constraints.new(_type)
        for constraint in constraints:
            try:
                setattr(crc, constraint[0], constraint[1])
            except Exception as e:
                print("Error: " + str(e))

for bone_name, add_constraints in ik_bones.items():
    p_bone = arm.pose.bones[bone_name]
    for _type, constraints in add_constraints.items():
        crc = p_bone.constraints.new(_type)
        for constraint in constraints:
            try:
                setattr(crc, constraint[0], constraint[1])
            except Exception as e:
                print("Error: " + str(e))


