# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_LC_SetLCState_t.proto

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
  name='_py_LC_SetLCState_t.proto',
  package='',
  serialized_pb=_b('\n\x19_py_LC_SetLCState_t.proto\"L\n\x12LC_SetLCState_t_pb\x12\x0f\n\x07Padding\x18\x01 \x02(\r\x12\x12\n\nNewLCState\x18\x02 \x02(\r\x12\x11\n\tCmdHeader\x18\x03 \x03(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LC_SETLCSTATE_T_PB = _descriptor.Descriptor(
  name='LC_SetLCState_t_pb',
  full_name='LC_SetLCState_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Padding', full_name='LC_SetLCState_t_pb.Padding', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NewLCState', full_name='LC_SetLCState_t_pb.NewLCState', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdHeader', full_name='LC_SetLCState_t_pb.CmdHeader', index=2,
      number=3, type=13, cpp_type=3, label=3,
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
  serialized_start=29,
  serialized_end=105,
)

DESCRIPTOR.message_types_by_name['LC_SetLCState_t_pb'] = _LC_SETLCSTATE_T_PB

LC_SetLCState_t_pb = _reflection.GeneratedProtocolMessageType('LC_SetLCState_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _LC_SETLCSTATE_T_PB,
  __module__ = '_py_LC_SetLCState_t_pb2'
  # @@protoc_insertion_point(class_scope:LC_SetLCState_t_pb)
  ))
_sym_db.RegisterMessage(LC_SetLCState_t_pb)


# @@protoc_insertion_point(module_scope)
