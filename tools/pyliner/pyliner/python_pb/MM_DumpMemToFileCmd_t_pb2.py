# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_MM_DumpMemToFileCmd_t.proto

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
  name='_py_MM_DumpMemToFileCmd_t.proto',
  package='',
  serialized_pb=_b('\n\x1f_py_MM_DumpMemToFileCmd_t.proto\"3\n\x10\x43\x46S_SymAddr_t_pb\x12\x0f\n\x07SymName\x18\x01 \x03(\t\x12\x0e\n\x06Offset\x18\x02 \x02(\r\"\x9f\x01\n\x18MM_DumpMemToFileCmd_t_pb\x12(\n\rSrcSymAddress\x18\x01 \x02(\x0b\x32\x11.CFS_SymAddr_t_pb\x12\x11\n\tCmdHeader\x18\x02 \x03(\r\x12\x10\n\x08\x46ileName\x18\x03 \x03(\t\x12\x0f\n\x07Padding\x18\x04 \x03(\r\x12\x12\n\nNumOfBytes\x18\x05 \x02(\r\x12\x0f\n\x07MemType\x18\x06 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




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
  serialized_start=35,
  serialized_end=86,
)


_MM_DUMPMEMTOFILECMD_T_PB = _descriptor.Descriptor(
  name='MM_DumpMemToFileCmd_t_pb',
  full_name='MM_DumpMemToFileCmd_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SrcSymAddress', full_name='MM_DumpMemToFileCmd_t_pb.SrcSymAddress', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdHeader', full_name='MM_DumpMemToFileCmd_t_pb.CmdHeader', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FileName', full_name='MM_DumpMemToFileCmd_t_pb.FileName', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Padding', full_name='MM_DumpMemToFileCmd_t_pb.Padding', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NumOfBytes', full_name='MM_DumpMemToFileCmd_t_pb.NumOfBytes', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MemType', full_name='MM_DumpMemToFileCmd_t_pb.MemType', index=5,
      number=6, type=13, cpp_type=3, label=2,
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
  serialized_start=89,
  serialized_end=248,
)

_MM_DUMPMEMTOFILECMD_T_PB.fields_by_name['SrcSymAddress'].message_type = _CFS_SYMADDR_T_PB
DESCRIPTOR.message_types_by_name['CFS_SymAddr_t_pb'] = _CFS_SYMADDR_T_PB
DESCRIPTOR.message_types_by_name['MM_DumpMemToFileCmd_t_pb'] = _MM_DUMPMEMTOFILECMD_T_PB

CFS_SymAddr_t_pb = _reflection.GeneratedProtocolMessageType('CFS_SymAddr_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CFS_SYMADDR_T_PB,
  __module__ = '_py_MM_DumpMemToFileCmd_t_pb2'
  # @@protoc_insertion_point(class_scope:CFS_SymAddr_t_pb)
  ))
_sym_db.RegisterMessage(CFS_SymAddr_t_pb)

MM_DumpMemToFileCmd_t_pb = _reflection.GeneratedProtocolMessageType('MM_DumpMemToFileCmd_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _MM_DUMPMEMTOFILECMD_T_PB,
  __module__ = '_py_MM_DumpMemToFileCmd_t_pb2'
  # @@protoc_insertion_point(class_scope:MM_DumpMemToFileCmd_t_pb)
  ))
_sym_db.RegisterMessage(MM_DumpMemToFileCmd_t_pb)


# @@protoc_insertion_point(module_scope)
