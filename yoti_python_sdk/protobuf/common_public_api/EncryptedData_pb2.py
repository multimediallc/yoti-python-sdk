# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EncryptedData.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='EncryptedData.proto',
  package='compubapi_v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x45ncryptedData.proto\x12\x0c\x63ompubapi_v1\"0\n\rEncryptedData\x12\n\n\x02iv\x18\x01 \x01(\x0c\x12\x13\n\x0b\x63ipher_text\x18\x02 \x01(\x0c\x62\x06proto3'
)




_ENCRYPTEDDATA = _descriptor.Descriptor(
  name='EncryptedData',
  full_name='compubapi_v1.EncryptedData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='iv', full_name='compubapi_v1.EncryptedData.iv', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cipher_text', full_name='compubapi_v1.EncryptedData.cipher_text', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=85,
)

DESCRIPTOR.message_types_by_name['EncryptedData'] = _ENCRYPTEDDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EncryptedData = _reflection.GeneratedProtocolMessageType('EncryptedData', (_message.Message,), {
  'DESCRIPTOR' : _ENCRYPTEDDATA,
  '__module__' : 'EncryptedData_pb2'
  # @@protoc_insertion_point(class_scope:compubapi_v1.EncryptedData)
  })
_sym_db.RegisterMessage(EncryptedData)


# @@protoc_insertion_point(module_scope)
