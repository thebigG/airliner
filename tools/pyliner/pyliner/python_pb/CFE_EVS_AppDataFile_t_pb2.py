# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_CFE_EVS_AppDataFile_t.proto

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
  name='_py_CFE_EVS_AppDataFile_t.proto',
  package='',
  serialized_pb=_b('\n\x1f_py_CFE_EVS_AppDataFile_t.proto\"S\n\x12\x45VS_BinFilter_t_pb\x12\x0f\n\x07\x45ventID\x18\x01 \x02(\x05\x12\x0f\n\x07Padding\x18\x02 \x02(\r\x12\x0c\n\x04Mask\x18\x03 \x02(\r\x12\r\n\x05\x43ount\x18\x04 \x02(\r\"\x97\x01\n\x18\x43\x46\x45_EVS_AppDataFile_t_pb\x12\x1c\n\x14\x45ventTypesActiveFlag\x18\x01 \x02(\r\x12\x12\n\nEventCount\x18\x02 \x02(\r\x12$\n\x07\x46ilters\x18\x03 \x03(\x0b\x32\x13.EVS_BinFilter_t_pb\x12\x12\n\nActiveFlag\x18\x04 \x02(\r\x12\x0f\n\x07\x41ppName\x18\x05 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EVS_BINFILTER_T_PB = _descriptor.Descriptor(
  name='EVS_BinFilter_t_pb',
  full_name='EVS_BinFilter_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='EventID', full_name='EVS_BinFilter_t_pb.EventID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Padding', full_name='EVS_BinFilter_t_pb.Padding', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Mask', full_name='EVS_BinFilter_t_pb.Mask', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Count', full_name='EVS_BinFilter_t_pb.Count', index=3,
      number=4, type=13, cpp_type=3, label=2,
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
  serialized_start=35,
  serialized_end=118,
)


_CFE_EVS_APPDATAFILE_T_PB = _descriptor.Descriptor(
  name='CFE_EVS_AppDataFile_t_pb',
  full_name='CFE_EVS_AppDataFile_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='EventTypesActiveFlag', full_name='CFE_EVS_AppDataFile_t_pb.EventTypesActiveFlag', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EventCount', full_name='CFE_EVS_AppDataFile_t_pb.EventCount', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Filters', full_name='CFE_EVS_AppDataFile_t_pb.Filters', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ActiveFlag', full_name='CFE_EVS_AppDataFile_t_pb.ActiveFlag', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AppName', full_name='CFE_EVS_AppDataFile_t_pb.AppName', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=121,
  serialized_end=272,
)

_CFE_EVS_APPDATAFILE_T_PB.fields_by_name['Filters'].message_type = _EVS_BINFILTER_T_PB
DESCRIPTOR.message_types_by_name['EVS_BinFilter_t_pb'] = _EVS_BINFILTER_T_PB
DESCRIPTOR.message_types_by_name['CFE_EVS_AppDataFile_t_pb'] = _CFE_EVS_APPDATAFILE_T_PB

EVS_BinFilter_t_pb = _reflection.GeneratedProtocolMessageType('EVS_BinFilter_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _EVS_BINFILTER_T_PB,
  __module__ = '_py_CFE_EVS_AppDataFile_t_pb2'
  # @@protoc_insertion_point(class_scope:EVS_BinFilter_t_pb)
  ))
_sym_db.RegisterMessage(EVS_BinFilter_t_pb)

CFE_EVS_AppDataFile_t_pb = _reflection.GeneratedProtocolMessageType('CFE_EVS_AppDataFile_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CFE_EVS_APPDATAFILE_T_PB,
  __module__ = '_py_CFE_EVS_AppDataFile_t_pb2'
  # @@protoc_insertion_point(class_scope:CFE_EVS_AppDataFile_t_pb)
  ))
_sym_db.RegisterMessage(CFE_EVS_AppDataFile_t_pb)


# @@protoc_insertion_point(module_scope)
