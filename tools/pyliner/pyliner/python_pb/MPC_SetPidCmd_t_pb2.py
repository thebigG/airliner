# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_MPC_SetPidCmd_t.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='_py_MPC_SetPidCmd_t.proto',
  package='',
  serialized_pb=_b('\n\x19_py_MPC_SetPidCmd_t.proto\"m\n\x12MPC_SetPidCmd_t_pb\x12\x13\n\x0bucCmdHeader\x18\x01 \x03(\r\x12\x0f\n\x07PidVelD\x18\x02 \x02(\x02\x12\x0f\n\x07PidGain\x18\x03 \x02(\x02\x12\x0f\n\x07PidVelI\x18\x04 \x02(\x02\x12\x0f\n\x07PidVelP\x18\x05 \x02(\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MPC_SETPIDCMD_T_PB = _descriptor.Descriptor(
  name='MPC_SetPidCmd_t_pb',
  full_name='MPC_SetPidCmd_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ucCmdHeader', full_name='MPC_SetPidCmd_t_pb.ucCmdHeader', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PidVelD', full_name='MPC_SetPidCmd_t_pb.PidVelD', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PidGain', full_name='MPC_SetPidCmd_t_pb.PidGain', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PidVelI', full_name='MPC_SetPidCmd_t_pb.PidVelI', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PidVelP', full_name='MPC_SetPidCmd_t_pb.PidVelP', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['MPC_SetPidCmd_t_pb'] = _MPC_SETPIDCMD_T_PB

MPC_SetPidCmd_t_pb = _reflection.GeneratedProtocolMessageType('MPC_SetPidCmd_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _MPC_SETPIDCMD_T_PB,
  __module__ = '_py_MPC_SetPidCmd_t_pb2'
  # @@protoc_insertion_point(class_scope:MPC_SetPidCmd_t_pb)
  ))
_sym_db.RegisterMessage(MPC_SetPidCmd_t_pb)


# @@protoc_insertion_point(module_scope)
