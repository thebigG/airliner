# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_PX4_EstimatorStatusMsg_t.proto

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
  name='_py_PX4_EstimatorStatusMsg_t.proto',
  package='',
  serialized_pb=_b('\n\"_py_PX4_EstimatorStatusMsg_t.proto\"\x95\x02\n\x1bPX4_EstimatorStatusMsg_t_pb\x12\x13\n\x0bHealthFlags\x18\x01 \x02(\r\x12\x10\n\x08NanFlags\x18\x02 \x02(\r\x12\x0c\n\x04Vibe\x18\x03 \x03(\x02\x12\x11\n\tTimestamp\x18\x04 \x02(\x04\x12\x13\n\x0b\x43ovariances\x18\x05 \x03(\x02\x12\x18\n\x10\x43ontrolModeFlags\x18\x06 \x02(\r\x12\x0e\n\x06States\x18\x07 \x03(\x02\x12\x19\n\x11GpsCheckFailFlags\x18\x08 \x02(\r\x12\x14\n\x0cTimeoutFlags\x18\t \x02(\r\x12\x18\n\x10\x46ilterFaultFlags\x18\n \x02(\r\x12\x11\n\tNumStates\x18\x0b \x02(\r\x12\x11\n\tTlmHeader\x18\x0c \x03(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PX4_ESTIMATORSTATUSMSG_T_PB = _descriptor.Descriptor(
  name='PX4_EstimatorStatusMsg_t_pb',
  full_name='PX4_EstimatorStatusMsg_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='HealthFlags', full_name='PX4_EstimatorStatusMsg_t_pb.HealthFlags', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NanFlags', full_name='PX4_EstimatorStatusMsg_t_pb.NanFlags', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Vibe', full_name='PX4_EstimatorStatusMsg_t_pb.Vibe', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Timestamp', full_name='PX4_EstimatorStatusMsg_t_pb.Timestamp', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Covariances', full_name='PX4_EstimatorStatusMsg_t_pb.Covariances', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlModeFlags', full_name='PX4_EstimatorStatusMsg_t_pb.ControlModeFlags', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='States', full_name='PX4_EstimatorStatusMsg_t_pb.States', index=6,
      number=7, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GpsCheckFailFlags', full_name='PX4_EstimatorStatusMsg_t_pb.GpsCheckFailFlags', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeoutFlags', full_name='PX4_EstimatorStatusMsg_t_pb.TimeoutFlags', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FilterFaultFlags', full_name='PX4_EstimatorStatusMsg_t_pb.FilterFaultFlags', index=9,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NumStates', full_name='PX4_EstimatorStatusMsg_t_pb.NumStates', index=10,
      number=11, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='PX4_EstimatorStatusMsg_t_pb.TlmHeader', index=11,
      number=12, type=13, cpp_type=3, label=3,
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
  serialized_end=316,
)

DESCRIPTOR.message_types_by_name['PX4_EstimatorStatusMsg_t_pb'] = _PX4_ESTIMATORSTATUSMSG_T_PB

PX4_EstimatorStatusMsg_t_pb = _reflection.GeneratedProtocolMessageType('PX4_EstimatorStatusMsg_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _PX4_ESTIMATORSTATUSMSG_T_PB,
  __module__ = '_py_PX4_EstimatorStatusMsg_t_pb2'
  # @@protoc_insertion_point(class_scope:PX4_EstimatorStatusMsg_t_pb)
  ))
_sym_db.RegisterMessage(PX4_EstimatorStatusMsg_t_pb)


# @@protoc_insertion_point(module_scope)
