# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_CFE_ES_CDSPool_t.proto

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
  name='_py_CFE_ES_CDSPool_t.proto',
  package='',
  serialized_pb=_b('\n\x1a_py_CFE_ES_CDSPool_t.proto\"P\n\x1c\x43\x46\x45_ES_CDSBlockSizeDesc_t_pb\x12\x12\n\nNumCreated\x18\x01 \x02(\r\x12\x0b\n\x03Top\x18\x02 \x02(\r\x12\x0f\n\x07MaxSize\x18\x03 \x02(\r\"\xe6\x01\n\x13\x43\x46\x45_ES_CDSPool_t_pb\x12\x0b\n\x03\x45nd\x18\x01 \x02(\r\x12\x14\n\x0c\x43heckErrCntr\x18\x02 \x02(\r\x12\x0f\n\x07MutexId\x18\x03 \x02(\r\x12\x0f\n\x07\x43urrent\x18\x04 \x02(\r\x12\r\n\x05Start\x18\x05 \x02(\r\x12\x14\n\x0cMinBlockSize\x18\x06 \x02(\r\x12\x11\n\tSizeIndex\x18\x07 \x02(\x05\x12/\n\x08SizeDesc\x18\x08 \x03(\x0b\x32\x1d.CFE_ES_CDSBlockSizeDesc_t_pb\x12\x13\n\x0bRequestCntr\x18\t \x02(\r\x12\x0c\n\x04Size\x18\n \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CFE_ES_CDSBLOCKSIZEDESC_T_PB = _descriptor.Descriptor(
  name='CFE_ES_CDSBlockSizeDesc_t_pb',
  full_name='CFE_ES_CDSBlockSizeDesc_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='NumCreated', full_name='CFE_ES_CDSBlockSizeDesc_t_pb.NumCreated', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Top', full_name='CFE_ES_CDSBlockSizeDesc_t_pb.Top', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MaxSize', full_name='CFE_ES_CDSBlockSizeDesc_t_pb.MaxSize', index=2,
      number=3, type=13, cpp_type=3, label=2,
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
  serialized_start=30,
  serialized_end=110,
)


_CFE_ES_CDSPOOL_T_PB = _descriptor.Descriptor(
  name='CFE_ES_CDSPool_t_pb',
  full_name='CFE_ES_CDSPool_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='End', full_name='CFE_ES_CDSPool_t_pb.End', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CheckErrCntr', full_name='CFE_ES_CDSPool_t_pb.CheckErrCntr', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MutexId', full_name='CFE_ES_CDSPool_t_pb.MutexId', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Current', full_name='CFE_ES_CDSPool_t_pb.Current', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Start', full_name='CFE_ES_CDSPool_t_pb.Start', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MinBlockSize', full_name='CFE_ES_CDSPool_t_pb.MinBlockSize', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SizeIndex', full_name='CFE_ES_CDSPool_t_pb.SizeIndex', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SizeDesc', full_name='CFE_ES_CDSPool_t_pb.SizeDesc', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RequestCntr', full_name='CFE_ES_CDSPool_t_pb.RequestCntr', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Size', full_name='CFE_ES_CDSPool_t_pb.Size', index=9,
      number=10, type=13, cpp_type=3, label=2,
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
  serialized_start=113,
  serialized_end=343,
)

_CFE_ES_CDSPOOL_T_PB.fields_by_name['SizeDesc'].message_type = _CFE_ES_CDSBLOCKSIZEDESC_T_PB
DESCRIPTOR.message_types_by_name['CFE_ES_CDSBlockSizeDesc_t_pb'] = _CFE_ES_CDSBLOCKSIZEDESC_T_PB
DESCRIPTOR.message_types_by_name['CFE_ES_CDSPool_t_pb'] = _CFE_ES_CDSPOOL_T_PB

CFE_ES_CDSBlockSizeDesc_t_pb = _reflection.GeneratedProtocolMessageType('CFE_ES_CDSBlockSizeDesc_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CFE_ES_CDSBLOCKSIZEDESC_T_PB,
  __module__ = '_py_CFE_ES_CDSPool_t_pb2'
  # @@protoc_insertion_point(class_scope:CFE_ES_CDSBlockSizeDesc_t_pb)
  ))
_sym_db.RegisterMessage(CFE_ES_CDSBlockSizeDesc_t_pb)

CFE_ES_CDSPool_t_pb = _reflection.GeneratedProtocolMessageType('CFE_ES_CDSPool_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CFE_ES_CDSPOOL_T_PB,
  __module__ = '_py_CFE_ES_CDSPool_t_pb2'
  # @@protoc_insertion_point(class_scope:CFE_ES_CDSPool_t_pb)
  ))
_sym_db.RegisterMessage(CFE_ES_CDSPool_t_pb)


# @@protoc_insertion_point(module_scope)
