# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_CF_QueueDirFiles_t.proto

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
  name='_py_CF_QueueDirFiles_t.proto',
  package='',
  serialized_pb=_b('\n\x1c_py_CF_QueueDirFiles_t.proto\"\xa3\x01\n\x15\x43\x46_QueueDirFiles_t_pb\x12\x10\n\x08Preserve\x18\x01 \x02(\r\x12\x0c\n\x04\x43han\x18\x02 \x02(\r\x12\x10\n\x08Priority\x18\x03 \x02(\r\x12\x11\n\tCmdOrPoll\x18\x04 \x02(\r\x12\x0f\n\x07\x44stPath\x18\x05 \x03(\t\x12\x0f\n\x07SrcPath\x18\x06 \x03(\t\x12\x14\n\x0cPeerEntityId\x18\x07 \x03(\t\x12\r\n\x05\x43lass\x18\x08 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CF_QUEUEDIRFILES_T_PB = _descriptor.Descriptor(
  name='CF_QueueDirFiles_t_pb',
  full_name='CF_QueueDirFiles_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Preserve', full_name='CF_QueueDirFiles_t_pb.Preserve', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Chan', full_name='CF_QueueDirFiles_t_pb.Chan', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Priority', full_name='CF_QueueDirFiles_t_pb.Priority', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdOrPoll', full_name='CF_QueueDirFiles_t_pb.CmdOrPoll', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DstPath', full_name='CF_QueueDirFiles_t_pb.DstPath', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SrcPath', full_name='CF_QueueDirFiles_t_pb.SrcPath', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PeerEntityId', full_name='CF_QueueDirFiles_t_pb.PeerEntityId', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Class', full_name='CF_QueueDirFiles_t_pb.Class', index=7,
      number=8, type=13, cpp_type=3, label=2,
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
  serialized_start=33,
  serialized_end=196,
)

DESCRIPTOR.message_types_by_name['CF_QueueDirFiles_t_pb'] = _CF_QUEUEDIRFILES_T_PB

CF_QueueDirFiles_t_pb = _reflection.GeneratedProtocolMessageType('CF_QueueDirFiles_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CF_QUEUEDIRFILES_T_PB,
  __module__ = '_py_CF_QueueDirFiles_t_pb2'
  # @@protoc_insertion_point(class_scope:CF_QueueDirFiles_t_pb)
  ))
_sym_db.RegisterMessage(CF_QueueDirFiles_t_pb)


# @@protoc_insertion_point(module_scope)
