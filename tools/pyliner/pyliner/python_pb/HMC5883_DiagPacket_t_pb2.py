# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_HMC5883_DiagPacket_t.proto

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
  name='_py_HMC5883_DiagPacket_t.proto',
  package='',
  serialized_pb=_b('\n\x1e_py_HMC5883_DiagPacket_t.proto\"\xe6\x01\n\x1bHMC5883_CalibrationMsg_t_pb\x12\x0f\n\x07z_scale\x18\x01 \x02(\x02\x12\x0f\n\x07y_scale\x18\x02 \x02(\x02\x12\x10\n\x08y_offset\x18\x03 \x02(\x02\x12\x10\n\x08x_offset\x18\x04 \x02(\x02\x12\x18\n\x10z_scale_internal\x18\x05 \x02(\x02\x12\x10\n\x08z_offset\x18\x06 \x02(\x02\x12\x10\n\x08Rotation\x18\x07 \x02(\r\x12\x0f\n\x07x_scale\x18\x08 \x02(\x02\x12\x18\n\x10x_scale_internal\x18\t \x02(\x02\x12\x18\n\x10y_scale_internal\x18\n \x02(\x02\"}\n\x1aHMC5883_ConversionMsg_t_pb\x12\x0f\n\x07\x43onfigA\x18\x01 \x02(\r\x12\x0f\n\x07\x43onfigB\x18\x02 \x02(\r\x12\x0f\n\x07Scaling\x18\x03 \x02(\x02\x12\r\n\x05Range\x18\x04 \x02(\x02\x12\x0f\n\x07\x44ivider\x18\x05 \x02(\x02\x12\x0c\n\x04Unit\x18\x06 \x02(\x02\"\x90\x01\n\x17HMC5883_DiagPacket_t_pb\x12/\n\nConversion\x18\x01 \x02(\x0b\x32\x1b.HMC5883_ConversionMsg_t_pb\x12\x11\n\tTlmHeader\x18\x02 \x03(\r\x12\x31\n\x0b\x43\x61libration\x18\x03 \x02(\x0b\x32\x1c.HMC5883_CalibrationMsg_t_pb')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HMC5883_CALIBRATIONMSG_T_PB = _descriptor.Descriptor(
  name='HMC5883_CalibrationMsg_t_pb',
  full_name='HMC5883_CalibrationMsg_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='z_scale', full_name='HMC5883_CalibrationMsg_t_pb.z_scale', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y_scale', full_name='HMC5883_CalibrationMsg_t_pb.y_scale', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y_offset', full_name='HMC5883_CalibrationMsg_t_pb.y_offset', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x_offset', full_name='HMC5883_CalibrationMsg_t_pb.x_offset', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z_scale_internal', full_name='HMC5883_CalibrationMsg_t_pb.z_scale_internal', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z_offset', full_name='HMC5883_CalibrationMsg_t_pb.z_offset', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Rotation', full_name='HMC5883_CalibrationMsg_t_pb.Rotation', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x_scale', full_name='HMC5883_CalibrationMsg_t_pb.x_scale', index=7,
      number=8, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x_scale_internal', full_name='HMC5883_CalibrationMsg_t_pb.x_scale_internal', index=8,
      number=9, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y_scale_internal', full_name='HMC5883_CalibrationMsg_t_pb.y_scale_internal', index=9,
      number=10, type=2, cpp_type=6, label=2,
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
  serialized_end=265,
)


_HMC5883_CONVERSIONMSG_T_PB = _descriptor.Descriptor(
  name='HMC5883_ConversionMsg_t_pb',
  full_name='HMC5883_ConversionMsg_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ConfigA', full_name='HMC5883_ConversionMsg_t_pb.ConfigA', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ConfigB', full_name='HMC5883_ConversionMsg_t_pb.ConfigB', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Scaling', full_name='HMC5883_ConversionMsg_t_pb.Scaling', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Range', full_name='HMC5883_ConversionMsg_t_pb.Range', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Divider', full_name='HMC5883_ConversionMsg_t_pb.Divider', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Unit', full_name='HMC5883_ConversionMsg_t_pb.Unit', index=5,
      number=6, type=2, cpp_type=6, label=2,
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
  serialized_start=267,
  serialized_end=392,
)


_HMC5883_DIAGPACKET_T_PB = _descriptor.Descriptor(
  name='HMC5883_DiagPacket_t_pb',
  full_name='HMC5883_DiagPacket_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Conversion', full_name='HMC5883_DiagPacket_t_pb.Conversion', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='HMC5883_DiagPacket_t_pb.TlmHeader', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Calibration', full_name='HMC5883_DiagPacket_t_pb.Calibration', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=395,
  serialized_end=539,
)

_HMC5883_DIAGPACKET_T_PB.fields_by_name['Conversion'].message_type = _HMC5883_CONVERSIONMSG_T_PB
_HMC5883_DIAGPACKET_T_PB.fields_by_name['Calibration'].message_type = _HMC5883_CALIBRATIONMSG_T_PB
DESCRIPTOR.message_types_by_name['HMC5883_CalibrationMsg_t_pb'] = _HMC5883_CALIBRATIONMSG_T_PB
DESCRIPTOR.message_types_by_name['HMC5883_ConversionMsg_t_pb'] = _HMC5883_CONVERSIONMSG_T_PB
DESCRIPTOR.message_types_by_name['HMC5883_DiagPacket_t_pb'] = _HMC5883_DIAGPACKET_T_PB

HMC5883_CalibrationMsg_t_pb = _reflection.GeneratedProtocolMessageType('HMC5883_CalibrationMsg_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _HMC5883_CALIBRATIONMSG_T_PB,
  __module__ = '_py_HMC5883_DiagPacket_t_pb2'
  # @@protoc_insertion_point(class_scope:HMC5883_CalibrationMsg_t_pb)
  ))
_sym_db.RegisterMessage(HMC5883_CalibrationMsg_t_pb)

HMC5883_ConversionMsg_t_pb = _reflection.GeneratedProtocolMessageType('HMC5883_ConversionMsg_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _HMC5883_CONVERSIONMSG_T_PB,
  __module__ = '_py_HMC5883_DiagPacket_t_pb2'
  # @@protoc_insertion_point(class_scope:HMC5883_ConversionMsg_t_pb)
  ))
_sym_db.RegisterMessage(HMC5883_ConversionMsg_t_pb)

HMC5883_DiagPacket_t_pb = _reflection.GeneratedProtocolMessageType('HMC5883_DiagPacket_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _HMC5883_DIAGPACKET_T_PB,
  __module__ = '_py_HMC5883_DiagPacket_t_pb2'
  # @@protoc_insertion_point(class_scope:HMC5883_DiagPacket_t_pb)
  ))
_sym_db.RegisterMessage(HMC5883_DiagPacket_t_pb)


# @@protoc_insertion_point(module_scope)
