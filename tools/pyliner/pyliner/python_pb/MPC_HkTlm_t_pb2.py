# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_MPC_HkTlm_t.proto

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
  name='_py_MPC_HkTlm_t.proto',
  package='',
  serialized_pb=_b('\n\x15_py_MPC_HkTlm_t.proto\"\xdd\x03\n\x0eMPC_HkTlm_t_pb\x12\x10\n\x08VelMaxXy\x18\x01 \x02(\x02\x12 \n\x18\x41\x63\x63\x65lerationStateLimitXY\x18\x02 \x02(\x02\x12\x11\n\tInTakeoff\x18\x03 \x02(\x08\x12\x1b\n\x13\x41ltitudeHoldEngaged\x18\x04 \x02(\x08\x12\x1b\n\x13TripletLatLonFinite\x18\x05 \x02(\x08\x12\x12\n\nYawTakeoff\x18\x06 \x02(\x02\x12\x15\n\rRunAltControl\x18\x07 \x02(\x08\x12\x19\n\x11ManualJerkLimitXY\x18\x08 \x02(\x02\x12\x0b\n\x03Yaw\x18\t \x02(\x02\x12\x15\n\rRunPosControl\x18\n \x02(\x08\x12\x10\n\x08WasArmed\x18\x0b \x02(\x08\x12\x10\n\x08usCmdCnt\x18\x0c \x02(\r\x12\x11\n\tWasLanded\x18\r \x02(\x08\x12\x17\n\x0fTakeoffVelLimit\x18\x0e \x02(\x02\x12\x10\n\x08ModeAuto\x18\x0f \x02(\x08\x12\x11\n\tTlmHeader\x18\x10 \x03(\r\x12\x1f\n\x17\x41\x63\x63\x65lerationStateLimitZ\x18\x11 \x02(\x02\x12\x18\n\x10ManualJerkLimitZ\x18\x12 \x02(\x02\x12\x1b\n\x13PositionHoldEngaged\x18\x13 \x02(\x08\x12\x13\n\x0busCmdErrCnt\x18\x14 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MPC_HKTLM_T_PB = _descriptor.Descriptor(
  name='MPC_HkTlm_t_pb',
  full_name='MPC_HkTlm_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='VelMaxXy', full_name='MPC_HkTlm_t_pb.VelMaxXy', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccelerationStateLimitXY', full_name='MPC_HkTlm_t_pb.AccelerationStateLimitXY', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='InTakeoff', full_name='MPC_HkTlm_t_pb.InTakeoff', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AltitudeHoldEngaged', full_name='MPC_HkTlm_t_pb.AltitudeHoldEngaged', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TripletLatLonFinite', full_name='MPC_HkTlm_t_pb.TripletLatLonFinite', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YawTakeoff', full_name='MPC_HkTlm_t_pb.YawTakeoff', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RunAltControl', full_name='MPC_HkTlm_t_pb.RunAltControl', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ManualJerkLimitXY', full_name='MPC_HkTlm_t_pb.ManualJerkLimitXY', index=7,
      number=8, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Yaw', full_name='MPC_HkTlm_t_pb.Yaw', index=8,
      number=9, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RunPosControl', full_name='MPC_HkTlm_t_pb.RunPosControl', index=9,
      number=10, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WasArmed', full_name='MPC_HkTlm_t_pb.WasArmed', index=10,
      number=11, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usCmdCnt', full_name='MPC_HkTlm_t_pb.usCmdCnt', index=11,
      number=12, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WasLanded', full_name='MPC_HkTlm_t_pb.WasLanded', index=12,
      number=13, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TakeoffVelLimit', full_name='MPC_HkTlm_t_pb.TakeoffVelLimit', index=13,
      number=14, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ModeAuto', full_name='MPC_HkTlm_t_pb.ModeAuto', index=14,
      number=15, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='MPC_HkTlm_t_pb.TlmHeader', index=15,
      number=16, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccelerationStateLimitZ', full_name='MPC_HkTlm_t_pb.AccelerationStateLimitZ', index=16,
      number=17, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ManualJerkLimitZ', full_name='MPC_HkTlm_t_pb.ManualJerkLimitZ', index=17,
      number=18, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PositionHoldEngaged', full_name='MPC_HkTlm_t_pb.PositionHoldEngaged', index=18,
      number=19, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usCmdErrCnt', full_name='MPC_HkTlm_t_pb.usCmdErrCnt', index=19,
      number=20, type=13, cpp_type=3, label=2,
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
  serialized_start=26,
  serialized_end=503,
)

DESCRIPTOR.message_types_by_name['MPC_HkTlm_t_pb'] = _MPC_HKTLM_T_PB

MPC_HkTlm_t_pb = _reflection.GeneratedProtocolMessageType('MPC_HkTlm_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _MPC_HKTLM_T_PB,
  __module__ = '_py_MPC_HkTlm_t_pb2'
  # @@protoc_insertion_point(class_scope:MPC_HkTlm_t_pb)
  ))
_sym_db.RegisterMessage(MPC_HkTlm_t_pb)


# @@protoc_insertion_point(module_scope)
