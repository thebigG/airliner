# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_GPS_DeviceMessage_t.proto

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
  name='_py_GPS_DeviceMessage_t.proto',
  package='',
  serialized_pb=_b('\n\x1d_py_GPS_DeviceMessage_t.proto\"<\n\x16GPS_DeviceMessage_t_pb\x12\x11\n\tTlmHeader\x18\x01 \x03(\r\x12\x0f\n\x07Payload\x18\x02 \x03(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GPS_DEVICEMESSAGE_T_PB = _descriptor.Descriptor(
  name='GPS_DeviceMessage_t_pb',
  full_name='GPS_DeviceMessage_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='GPS_DeviceMessage_t_pb.TlmHeader', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Payload', full_name='GPS_DeviceMessage_t_pb.Payload', index=1,
      number=2, type=13, cpp_type=3, label=3,
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
  serialized_start=33,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['GPS_DeviceMessage_t_pb'] = _GPS_DEVICEMESSAGE_T_PB

GPS_DeviceMessage_t_pb = _reflection.GeneratedProtocolMessageType('GPS_DeviceMessage_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _GPS_DEVICEMESSAGE_T_PB,
  __module__ = '_py_GPS_DeviceMessage_t_pb2'
  # @@protoc_insertion_point(class_scope:GPS_DeviceMessage_t_pb)
  ))
_sym_db.RegisterMessage(GPS_DeviceMessage_t_pb)


# @@protoc_insertion_point(module_scope)
