# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_PX4_ControlStateMsg_t.proto

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
  name='_py_PX4_ControlStateMsg_t.proto',
  package='',
  serialized_pb=_b('\n\x1f_py_PX4_ControlStateMsg_t.proto\"\xd7\x03\n\x18PX4_ControlStateMsg_t_pb\x12\x0c\n\x04PosY\x18\x01 \x02(\x02\x12\x10\n\x08\x41irspeed\x18\x02 \x02(\x02\x12\x0c\n\x04PosZ\x18\x03 \x02(\x02\x12\x0c\n\x04PosX\x18\x04 \x02(\x02\x12\x13\n\x0bVelVariance\x18\x05 \x03(\x02\x12\x13\n\x0b\x44\x65ltaQReset\x18\x06 \x03(\x02\x12\x13\n\x0bPosVariance\x18\x07 \x03(\x02\x12\x11\n\tTimestamp\x18\x08 \x02(\x04\x12\x14\n\x0cRollRateBias\x18\t \x02(\x02\x12\x11\n\tTlmHeader\x18\n \x03(\r\x12\x15\n\rPitchRateBias\x18\x0b \x02(\x02\x12\x0c\n\x04VelX\x18\x0c \x02(\x02\x12\t\n\x01Q\x18\r \x03(\x02\x12\x0c\n\x04\x41\x63\x63Y\x18\x0e \x02(\x02\x12\x0c\n\x04\x41\x63\x63X\x18\x0f \x02(\x02\x12\x0c\n\x04VelY\x18\x10 \x02(\x02\x12\x0c\n\x04\x41\x63\x63Z\x18\x11 \x02(\x02\x12\x0f\n\x07YawRate\x18\x12 \x02(\x02\x12\x18\n\x10QuatResetCounter\x18\x13 \x02(\r\x12\x10\n\x08RollRate\x18\x14 \x02(\x02\x12\x15\n\rAirspeedValid\x18\x15 \x02(\x08\x12\x11\n\tPitchRate\x18\x16 \x02(\x02\x12\x12\n\nHorzAccMag\x18\x17 \x02(\x02\x12\x13\n\x0bYawRateBias\x18\x18 \x02(\x02\x12\x0c\n\x04VelZ\x18\x19 \x02(\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PX4_CONTROLSTATEMSG_T_PB = _descriptor.Descriptor(
  name='PX4_ControlStateMsg_t_pb',
  full_name='PX4_ControlStateMsg_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PosY', full_name='PX4_ControlStateMsg_t_pb.PosY', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Airspeed', full_name='PX4_ControlStateMsg_t_pb.Airspeed', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PosZ', full_name='PX4_ControlStateMsg_t_pb.PosZ', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PosX', full_name='PX4_ControlStateMsg_t_pb.PosX', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='VelVariance', full_name='PX4_ControlStateMsg_t_pb.VelVariance', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DeltaQReset', full_name='PX4_ControlStateMsg_t_pb.DeltaQReset', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PosVariance', full_name='PX4_ControlStateMsg_t_pb.PosVariance', index=6,
      number=7, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Timestamp', full_name='PX4_ControlStateMsg_t_pb.Timestamp', index=7,
      number=8, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RollRateBias', full_name='PX4_ControlStateMsg_t_pb.RollRateBias', index=8,
      number=9, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='PX4_ControlStateMsg_t_pb.TlmHeader', index=9,
      number=10, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PitchRateBias', full_name='PX4_ControlStateMsg_t_pb.PitchRateBias', index=10,
      number=11, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='VelX', full_name='PX4_ControlStateMsg_t_pb.VelX', index=11,
      number=12, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Q', full_name='PX4_ControlStateMsg_t_pb.Q', index=12,
      number=13, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccY', full_name='PX4_ControlStateMsg_t_pb.AccY', index=13,
      number=14, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccX', full_name='PX4_ControlStateMsg_t_pb.AccX', index=14,
      number=15, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='VelY', full_name='PX4_ControlStateMsg_t_pb.VelY', index=15,
      number=16, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccZ', full_name='PX4_ControlStateMsg_t_pb.AccZ', index=16,
      number=17, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YawRate', full_name='PX4_ControlStateMsg_t_pb.YawRate', index=17,
      number=18, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='QuatResetCounter', full_name='PX4_ControlStateMsg_t_pb.QuatResetCounter', index=18,
      number=19, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RollRate', full_name='PX4_ControlStateMsg_t_pb.RollRate', index=19,
      number=20, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AirspeedValid', full_name='PX4_ControlStateMsg_t_pb.AirspeedValid', index=20,
      number=21, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PitchRate', full_name='PX4_ControlStateMsg_t_pb.PitchRate', index=21,
      number=22, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HorzAccMag', full_name='PX4_ControlStateMsg_t_pb.HorzAccMag', index=22,
      number=23, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YawRateBias', full_name='PX4_ControlStateMsg_t_pb.YawRateBias', index=23,
      number=24, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='VelZ', full_name='PX4_ControlStateMsg_t_pb.VelZ', index=24,
      number=25, type=2, cpp_type=6, label=2,
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
  serialized_start=36,
  serialized_end=507,
)

DESCRIPTOR.message_types_by_name['PX4_ControlStateMsg_t_pb'] = _PX4_CONTROLSTATEMSG_T_PB

PX4_ControlStateMsg_t_pb = _reflection.GeneratedProtocolMessageType('PX4_ControlStateMsg_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _PX4_CONTROLSTATEMSG_T_PB,
  __module__ = '_py_PX4_ControlStateMsg_t_pb2'
  # @@protoc_insertion_point(class_scope:PX4_ControlStateMsg_t_pb)
  ))
_sym_db.RegisterMessage(PX4_ControlStateMsg_t_pb)


# @@protoc_insertion_point(module_scope)
