# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_CFE_TBL_TblRegPacket_Payload_t.proto

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
  name='_py_CFE_TBL_TblRegPacket_Payload_t.proto',
  package='',
  serialized_pb=_b('\n(_py_CFE_TBL_TblRegPacket_Payload_t.proto\"<\n\x15\x43\x46\x45_TIME_SysTime_t_pb\x12\x0f\n\x07Seconds\x18\x01 \x02(\r\x12\x12\n\nSubseconds\x18\x02 \x02(\r\"\xb3\x03\n!CFE_TBL_TblRegPacket_Payload_t_pb\x12\x1a\n\x12InactiveBufferAddr\x18\x01 \x02(\r\x12\x16\n\x0eLastFileLoaded\x18\x02 \x02(\t\x12\x0c\n\x04Name\x18\x03 \x02(\t\x12\x10\n\x08\x44umpOnly\x18\x04 \x02(\x08\x12\x19\n\x11ValidationFuncPtr\x18\x05 \x02(\r\x12\x17\n\x0fTableLoadedOnce\x18\x06 \x02(\x08\x12\x0c\n\x04Size\x18\x07 \x02(\r\x12\x0b\n\x03\x43rc\x18\x08 \x02(\r\x12\x12\n\nByteAlign4\x18\t \x02(\r\x12\x10\n\x08\x43ritical\x18\n \x02(\x08\x12\x13\n\x0b\x44\x62lBuffered\x18\x0b \x02(\x08\x12\x1d\n\x15\x46ileCreateTimeSubSecs\x18\x0c \x02(\r\x12\x13\n\x0bLoadPending\x18\r \x02(\x08\x12\x1a\n\x12\x46ileCreateTimeSecs\x18\x0e \x02(\r\x12\x30\n\x10TimeOfLastUpdate\x18\x0f \x02(\x0b\x32\x16.CFE_TIME_SysTime_t_pb\x12\x18\n\x10\x41\x63tiveBufferAddr\x18\x10 \x02(\r\x12\x14\n\x0cOwnerAppName\x18\x11 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CFE_TIME_SYSTIME_T_PB = _descriptor.Descriptor(
  name='CFE_TIME_SysTime_t_pb',
  full_name='CFE_TIME_SysTime_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Seconds', full_name='CFE_TIME_SysTime_t_pb.Seconds', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Subseconds', full_name='CFE_TIME_SysTime_t_pb.Subseconds', index=1,
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
  serialized_start=44,
  serialized_end=104,
)


_CFE_TBL_TBLREGPACKET_PAYLOAD_T_PB = _descriptor.Descriptor(
  name='CFE_TBL_TblRegPacket_Payload_t_pb',
  full_name='CFE_TBL_TblRegPacket_Payload_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='InactiveBufferAddr', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.InactiveBufferAddr', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LastFileLoaded', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.LastFileLoaded', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Name', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.Name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DumpOnly', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.DumpOnly', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ValidationFuncPtr', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.ValidationFuncPtr', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TableLoadedOnce', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.TableLoadedOnce', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Size', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.Size', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Crc', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.Crc', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ByteAlign4', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.ByteAlign4', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Critical', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.Critical', index=9,
      number=10, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DblBuffered', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.DblBuffered', index=10,
      number=11, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FileCreateTimeSubSecs', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.FileCreateTimeSubSecs', index=11,
      number=12, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LoadPending', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.LoadPending', index=12,
      number=13, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FileCreateTimeSecs', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.FileCreateTimeSecs', index=13,
      number=14, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeOfLastUpdate', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.TimeOfLastUpdate', index=14,
      number=15, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ActiveBufferAddr', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.ActiveBufferAddr', index=15,
      number=16, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OwnerAppName', full_name='CFE_TBL_TblRegPacket_Payload_t_pb.OwnerAppName', index=16,
      number=17, type=9, cpp_type=9, label=2,
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
  serialized_start=107,
  serialized_end=542,
)

_CFE_TBL_TBLREGPACKET_PAYLOAD_T_PB.fields_by_name['TimeOfLastUpdate'].message_type = _CFE_TIME_SYSTIME_T_PB
DESCRIPTOR.message_types_by_name['CFE_TIME_SysTime_t_pb'] = _CFE_TIME_SYSTIME_T_PB
DESCRIPTOR.message_types_by_name['CFE_TBL_TblRegPacket_Payload_t_pb'] = _CFE_TBL_TBLREGPACKET_PAYLOAD_T_PB

CFE_TIME_SysTime_t_pb = _reflection.GeneratedProtocolMessageType('CFE_TIME_SysTime_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CFE_TIME_SYSTIME_T_PB,
  __module__ = '_py_CFE_TBL_TblRegPacket_Payload_t_pb2'
  # @@protoc_insertion_point(class_scope:CFE_TIME_SysTime_t_pb)
  ))
_sym_db.RegisterMessage(CFE_TIME_SysTime_t_pb)

CFE_TBL_TblRegPacket_Payload_t_pb = _reflection.GeneratedProtocolMessageType('CFE_TBL_TblRegPacket_Payload_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CFE_TBL_TBLREGPACKET_PAYLOAD_T_PB,
  __module__ = '_py_CFE_TBL_TblRegPacket_Payload_t_pb2'
  # @@protoc_insertion_point(class_scope:CFE_TBL_TblRegPacket_Payload_t_pb)
  ))
_sym_db.RegisterMessage(CFE_TBL_TblRegPacket_Payload_t_pb)


# @@protoc_insertion_point(module_scope)
