# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_MD_DwellTableLoad_t.proto

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
  name='_py_MD_DwellTableLoad_t.proto',
  package='',
  serialized_pb=_b('\n\x1d_py_MD_DwellTableLoad_t.proto\"`\n\x16MD_TableLoadEntry_t_pb\x12\r\n\x05\x44\x65lay\x18\x01 \x02(\r\x12\'\n\x0c\x44wellAddress\x18\x02 \x02(\x0b\x32\x11.CFS_SymAddr_t_pb\x12\x0e\n\x06Length\x18\x03 \x02(\r\"3\n\x10\x43\x46S_SymAddr_t_pb\x12\x0f\n\x07SymName\x18\x01 \x03(\t\x12\x0e\n\x06Offset\x18\x02 \x02(\r\"d\n\x16MD_DwellTableLoad_t_pb\x12&\n\x05\x45ntry\x18\x01 \x03(\x0b\x32\x17.MD_TableLoadEntry_t_pb\x12\x0f\n\x07\x45nabled\x18\x02 \x02(\r\x12\x11\n\tSignature\x18\x03 \x03(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MD_TABLELOADENTRY_T_PB = _descriptor.Descriptor(
  name='MD_TableLoadEntry_t_pb',
  full_name='MD_TableLoadEntry_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Delay', full_name='MD_TableLoadEntry_t_pb.Delay', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DwellAddress', full_name='MD_TableLoadEntry_t_pb.DwellAddress', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Length', full_name='MD_TableLoadEntry_t_pb.Length', index=2,
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
  serialized_start=33,
  serialized_end=129,
)


_CFS_SYMADDR_T_PB = _descriptor.Descriptor(
  name='CFS_SymAddr_t_pb',
  full_name='CFS_SymAddr_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SymName', full_name='CFS_SymAddr_t_pb.SymName', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Offset', full_name='CFS_SymAddr_t_pb.Offset', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=131,
  serialized_end=182,
)


_MD_DWELLTABLELOAD_T_PB = _descriptor.Descriptor(
  name='MD_DwellTableLoad_t_pb',
  full_name='MD_DwellTableLoad_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Entry', full_name='MD_DwellTableLoad_t_pb.Entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Enabled', full_name='MD_DwellTableLoad_t_pb.Enabled', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Signature', full_name='MD_DwellTableLoad_t_pb.Signature', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=184,
  serialized_end=284,
)

_MD_TABLELOADENTRY_T_PB.fields_by_name['DwellAddress'].message_type = _CFS_SYMADDR_T_PB
_MD_DWELLTABLELOAD_T_PB.fields_by_name['Entry'].message_type = _MD_TABLELOADENTRY_T_PB
DESCRIPTOR.message_types_by_name['MD_TableLoadEntry_t_pb'] = _MD_TABLELOADENTRY_T_PB
DESCRIPTOR.message_types_by_name['CFS_SymAddr_t_pb'] = _CFS_SYMADDR_T_PB
DESCRIPTOR.message_types_by_name['MD_DwellTableLoad_t_pb'] = _MD_DWELLTABLELOAD_T_PB

MD_TableLoadEntry_t_pb = _reflection.GeneratedProtocolMessageType('MD_TableLoadEntry_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _MD_TABLELOADENTRY_T_PB,
  __module__ = '_py_MD_DwellTableLoad_t_pb2'
  # @@protoc_insertion_point(class_scope:MD_TableLoadEntry_t_pb)
  ))
_sym_db.RegisterMessage(MD_TableLoadEntry_t_pb)

CFS_SymAddr_t_pb = _reflection.GeneratedProtocolMessageType('CFS_SymAddr_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CFS_SYMADDR_T_PB,
  __module__ = '_py_MD_DwellTableLoad_t_pb2'
  # @@protoc_insertion_point(class_scope:CFS_SymAddr_t_pb)
  ))
_sym_db.RegisterMessage(CFS_SymAddr_t_pb)

MD_DwellTableLoad_t_pb = _reflection.GeneratedProtocolMessageType('MD_DwellTableLoad_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _MD_DWELLTABLELOAD_T_PB,
  __module__ = '_py_MD_DwellTableLoad_t_pb2'
  # @@protoc_insertion_point(class_scope:MD_DwellTableLoad_t_pb)
  ))
_sym_db.RegisterMessage(MD_DwellTableLoad_t_pb)


# @@protoc_insertion_point(module_scope)
