# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_TO_HkTlm_t.proto

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
  name='_py_TO_HkTlm_t.proto',
  package='',
  serialized_pb=_b('\n\x14_py_TO_HkTlm_t.proto\"\xd2\x01\n\rTO_HkTlm_t_pb\x12\x1d\n\x15QueuedInOutputChannel\x18\x01 \x03(\r\x12\x10\n\x08usCmdCnt\x18\x02 \x02(\r\x12\x10\n\x08MemInUse\x18\x03 \x02(\r\x12\x11\n\tTlmHeader\x18\x04 \x03(\r\x12\x19\n\x11usTotalMsgDropped\x18\x05 \x02(\r\x12\x13\n\x0busCmdErrCnt\x18\x06 \x02(\r\x12\x15\n\rMemPoolHandle\x18\x07 \x02(\r\x12\x14\n\x0cPeakMemInUse\x18\x08 \x02(\r\x12\x0e\n\x06MaxMem\x18\t \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TO_HKTLM_T_PB = _descriptor.Descriptor(
  name='TO_HkTlm_t_pb',
  full_name='TO_HkTlm_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='QueuedInOutputChannel', full_name='TO_HkTlm_t_pb.QueuedInOutputChannel', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usCmdCnt', full_name='TO_HkTlm_t_pb.usCmdCnt', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MemInUse', full_name='TO_HkTlm_t_pb.MemInUse', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='TO_HkTlm_t_pb.TlmHeader', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usTotalMsgDropped', full_name='TO_HkTlm_t_pb.usTotalMsgDropped', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usCmdErrCnt', full_name='TO_HkTlm_t_pb.usCmdErrCnt', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MemPoolHandle', full_name='TO_HkTlm_t_pb.MemPoolHandle', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PeakMemInUse', full_name='TO_HkTlm_t_pb.PeakMemInUse', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MaxMem', full_name='TO_HkTlm_t_pb.MaxMem', index=8,
      number=9, type=13, cpp_type=3, label=2,
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
  serialized_start=25,
  serialized_end=235,
)

DESCRIPTOR.message_types_by_name['TO_HkTlm_t_pb'] = _TO_HKTLM_T_PB

TO_HkTlm_t_pb = _reflection.GeneratedProtocolMessageType('TO_HkTlm_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _TO_HKTLM_T_PB,
  __module__ = '_py_TO_HkTlm_t_pb2'
  # @@protoc_insertion_point(class_scope:TO_HkTlm_t_pb)
  ))
_sym_db.RegisterMessage(TO_HkTlm_t_pb)


# @@protoc_insertion_point(module_scope)
