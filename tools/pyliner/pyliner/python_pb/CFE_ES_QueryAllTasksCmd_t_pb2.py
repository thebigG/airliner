# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_CFE_ES_QueryAllTasksCmd_t.proto

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
  name='_py_CFE_ES_QueryAllTasksCmd_t.proto',
  package='',
  serialized_pb=_b('\n#_py_CFE_ES_QueryAllTasksCmd_t.proto\"@\n$CFE_ES_QueryAllTasksCmd_Payload_t_pb\x12\x18\n\x10QueryAllFileName\x18\x01 \x03(\t\"i\n\x1c\x43\x46\x45_ES_QueryAllTasksCmd_t_pb\x12\x36\n\x07Payload\x18\x01 \x02(\x0b\x32%.CFE_ES_QueryAllTasksCmd_Payload_t_pb\x12\x11\n\tCmdHeader\x18\x02 \x03(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CFE_ES_QUERYALLTASKSCMD_PAYLOAD_T_PB = _descriptor.Descriptor(
  name='CFE_ES_QueryAllTasksCmd_Payload_t_pb',
  full_name='CFE_ES_QueryAllTasksCmd_Payload_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='QueryAllFileName', full_name='CFE_ES_QueryAllTasksCmd_Payload_t_pb.QueryAllFileName', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=39,
  serialized_end=103,
)


_CFE_ES_QUERYALLTASKSCMD_T_PB = _descriptor.Descriptor(
  name='CFE_ES_QueryAllTasksCmd_t_pb',
  full_name='CFE_ES_QueryAllTasksCmd_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Payload', full_name='CFE_ES_QueryAllTasksCmd_t_pb.Payload', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdHeader', full_name='CFE_ES_QueryAllTasksCmd_t_pb.CmdHeader', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=105,
  serialized_end=210,
)

_CFE_ES_QUERYALLTASKSCMD_T_PB.fields_by_name['Payload'].message_type = _CFE_ES_QUERYALLTASKSCMD_PAYLOAD_T_PB
DESCRIPTOR.message_types_by_name['CFE_ES_QueryAllTasksCmd_Payload_t_pb'] = _CFE_ES_QUERYALLTASKSCMD_PAYLOAD_T_PB
DESCRIPTOR.message_types_by_name['CFE_ES_QueryAllTasksCmd_t_pb'] = _CFE_ES_QUERYALLTASKSCMD_T_PB

CFE_ES_QueryAllTasksCmd_Payload_t_pb = _reflection.GeneratedProtocolMessageType('CFE_ES_QueryAllTasksCmd_Payload_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CFE_ES_QUERYALLTASKSCMD_PAYLOAD_T_PB,
  __module__ = '_py_CFE_ES_QueryAllTasksCmd_t_pb2'
  # @@protoc_insertion_point(class_scope:CFE_ES_QueryAllTasksCmd_Payload_t_pb)
  ))
_sym_db.RegisterMessage(CFE_ES_QueryAllTasksCmd_Payload_t_pb)

CFE_ES_QueryAllTasksCmd_t_pb = _reflection.GeneratedProtocolMessageType('CFE_ES_QueryAllTasksCmd_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CFE_ES_QUERYALLTASKSCMD_T_PB,
  __module__ = '_py_CFE_ES_QueryAllTasksCmd_t_pb2'
  # @@protoc_insertion_point(class_scope:CFE_ES_QueryAllTasksCmd_t_pb)
  ))
_sym_db.RegisterMessage(CFE_ES_QueryAllTasksCmd_t_pb)


# @@protoc_insertion_point(module_scope)
