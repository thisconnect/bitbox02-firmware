# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: system.proto

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
  name='system.proto',
  package='shiftcrypto.bitbox02',
  syntax='proto3',
  serialized_pb=_b('\n\x0csystem.proto\x12\x14shiftcrypto.bitbox02\"\x0f\n\rRebootRequestb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REBOOTREQUEST = _descriptor.Descriptor(
  name='RebootRequest',
  full_name='shiftcrypto.bitbox02.RebootRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=53,
)

DESCRIPTOR.message_types_by_name['RebootRequest'] = _REBOOTREQUEST

RebootRequest = _reflection.GeneratedProtocolMessageType('RebootRequest', (_message.Message,), dict(
  DESCRIPTOR = _REBOOTREQUEST,
  __module__ = 'system_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.RebootRequest)
  ))
_sym_db.RegisterMessage(RebootRequest)


# @@protoc_insertion_point(module_scope)
