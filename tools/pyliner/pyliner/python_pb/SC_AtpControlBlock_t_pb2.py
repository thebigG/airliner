# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_SC_AtpControlBlock_t.proto

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
  name='_py_SC_AtpControlBlock_t.proto',
  package='',
  serialized_pb=_b('\n\x1e_py_SC_AtpControlBlock_t.proto\"\x7f\n\x17SC_AtpControlBlock_t_pb\x12\x10\n\x08\x41tpState\x18\x01 \x02(\r\x12\x11\n\tCmdNumber\x18\x02 \x02(\r\x12\x11\n\tAtsNumber\x18\x03 \x02(\r\x12\x14\n\x0cTimeIndexPtr\x18\x04 \x02(\r\x12\x16\n\x0eSwitchPendFlag\x18\x05 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SC_ATPCONTROLBLOCK_T_PB = _descriptor.Descriptor(
  name='SC_AtpControlBlock_t_pb',
  full_name='SC_AtpControlBlock_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='AtpState', full_name='SC_AtpControlBlock_t_pb.AtpState', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdNumber', full_name='SC_AtpControlBlock_t_pb.CmdNumber', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AtsNumber', full_name='SC_AtpControlBlock_t_pb.AtsNumber', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeIndexPtr', full_name='SC_AtpControlBlock_t_pb.TimeIndexPtr', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SwitchPendFlag', full_name='SC_AtpControlBlock_t_pb.SwitchPendFlag', index=4,
      number=5, type=13, cpp_type=3, label=2,
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
  serialized_start=34,
  serialized_end=161,
)

DESCRIPTOR.message_types_by_name['SC_AtpControlBlock_t_pb'] = _SC_ATPCONTROLBLOCK_T_PB

SC_AtpControlBlock_t_pb = _reflection.GeneratedProtocolMessageType('SC_AtpControlBlock_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _SC_ATPCONTROLBLOCK_T_PB,
  __module__ = '_py_SC_AtpControlBlock_t_pb2'
  # @@protoc_insertion_point(class_scope:SC_AtpControlBlock_t_pb)
  ))
_sym_db.RegisterMessage(SC_AtpControlBlock_t_pb)


# @@protoc_insertion_point(module_scope)
