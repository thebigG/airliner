# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_LC_MListTag.proto

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
  name='_py_LC_MListTag.proto',
  package='',
  serialized_pb=_b('\n\x15_py_LC_MListTag.proto\"U\n\x0eLC_MListTag_pb\x12\x11\n\tMessageID\x18\x01 \x02(\r\x12\r\n\x05Spare\x18\x02 \x02(\r\x12\x13\n\x0bWatchPtList\x18\x03 \x02(\r\x12\x0c\n\x04Next\x18\x04 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LC_MLISTTAG_PB = _descriptor.Descriptor(
  name='LC_MListTag_pb',
  full_name='LC_MListTag_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MessageID', full_name='LC_MListTag_pb.MessageID', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Spare', full_name='LC_MListTag_pb.Spare', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WatchPtList', full_name='LC_MListTag_pb.WatchPtList', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Next', full_name='LC_MListTag_pb.Next', index=3,
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
  serialized_start=25,
  serialized_end=110,
)

DESCRIPTOR.message_types_by_name['LC_MListTag_pb'] = _LC_MLISTTAG_PB

LC_MListTag_pb = _reflection.GeneratedProtocolMessageType('LC_MListTag_pb', (_message.Message,), dict(
  DESCRIPTOR = _LC_MLISTTAG_PB,
  __module__ = '_py_LC_MListTag_pb2'
  # @@protoc_insertion_point(class_scope:LC_MListTag_pb)
  ))
_sym_db.RegisterMessage(LC_MListTag_pb)


# @@protoc_insertion_point(module_scope)
