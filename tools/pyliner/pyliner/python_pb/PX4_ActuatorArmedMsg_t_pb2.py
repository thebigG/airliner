# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_PX4_ActuatorArmedMsg_t.proto

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
  name='_py_PX4_ActuatorArmedMsg_t.proto',
  package='',
  serialized_pb=_b('\n _py_PX4_ActuatorArmedMsg_t.proto\"\xd5\x01\n\x19PX4_ActuatorArmedMsg_t_pb\x12\x15\n\rForceFailsafe\x18\x01 \x02(\x08\x12\x12\n\nReadyToArm\x18\x02 \x02(\x08\x12\x11\n\tTimestamp\x18\x03 \x02(\x04\x12\x1c\n\x14InEscCalibrationMode\x18\x04 \x02(\x08\x12\x11\n\tTlmHeader\x18\x05 \x03(\r\x12\x10\n\x08Lockdown\x18\x06 \x02(\x08\x12\x10\n\x08Prearmed\x18\x07 \x02(\x08\x12\r\n\x05\x41rmed\x18\x08 \x02(\x08\x12\x16\n\x0eManualLockdown\x18\t \x02(\x08')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PX4_ACTUATORARMEDMSG_T_PB = _descriptor.Descriptor(
  name='PX4_ActuatorArmedMsg_t_pb',
  full_name='PX4_ActuatorArmedMsg_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ForceFailsafe', full_name='PX4_ActuatorArmedMsg_t_pb.ForceFailsafe', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ReadyToArm', full_name='PX4_ActuatorArmedMsg_t_pb.ReadyToArm', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Timestamp', full_name='PX4_ActuatorArmedMsg_t_pb.Timestamp', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='InEscCalibrationMode', full_name='PX4_ActuatorArmedMsg_t_pb.InEscCalibrationMode', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='PX4_ActuatorArmedMsg_t_pb.TlmHeader', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Lockdown', full_name='PX4_ActuatorArmedMsg_t_pb.Lockdown', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Prearmed', full_name='PX4_ActuatorArmedMsg_t_pb.Prearmed', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Armed', full_name='PX4_ActuatorArmedMsg_t_pb.Armed', index=7,
      number=8, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ManualLockdown', full_name='PX4_ActuatorArmedMsg_t_pb.ManualLockdown', index=8,
      number=9, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=37,
  serialized_end=250,
)

DESCRIPTOR.message_types_by_name['PX4_ActuatorArmedMsg_t_pb'] = _PX4_ACTUATORARMEDMSG_T_PB

PX4_ActuatorArmedMsg_t_pb = _reflection.GeneratedProtocolMessageType('PX4_ActuatorArmedMsg_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _PX4_ACTUATORARMEDMSG_T_PB,
  __module__ = '_py_PX4_ActuatorArmedMsg_t_pb2'
  # @@protoc_insertion_point(class_scope:PX4_ActuatorArmedMsg_t_pb)
  ))
_sym_db.RegisterMessage(PX4_ActuatorArmedMsg_t_pb)


# @@protoc_insertion_point(module_scope)
