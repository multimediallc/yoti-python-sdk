# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Attribute.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ContentType_pb2 as ContentType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x41ttribute.proto\x12\rattrpubapi_v1\x1a\x11\x43ontentType.proto\"\xf7\x01\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x30\n\x0c\x63ontent_type\x18\x03 \x01(\x0e\x32\x1a.attrpubapi_v1.ContentType\x12&\n\x07\x61nchors\x18\x04 \x03(\x0b\x32\x15.attrpubapi_v1.Anchor\x12\x32\n\ruser_metadata\x18\x05 \x03(\x0b\x32\x1b.attrpubapi_v1.UserMetadata\x12)\n\x08metadata\x18\x06 \x01(\x0b\x32\x17.attrpubapi_v1.Metadata\x12\x14\n\x0c\x65phemeral_id\x18\x07 \x01(\t\"q\n\x08Metadata\x12\x1d\n\x15superseded_time_stamp\x18\x01 \x01(\t\x12\x11\n\tdeletable\x18\x02 \x01(\x08\x12\x12\n\nreceipt_id\x18\x03 \x01(\x0c\x12\x0f\n\x07revoked\x18\x04 \x01(\x08\x12\x0e\n\x06locked\x18\x05 \x01(\x08\"\xb3\x01\n\x06\x41nchor\x12\x15\n\rartifact_link\x18\x01 \x01(\x0c\x12\x1b\n\x13origin_server_certs\x18\x02 \x03(\x0c\x12\x1a\n\x12\x61rtifact_signature\x18\x03 \x01(\x0c\x12\x10\n\x08sub_type\x18\x04 \x01(\t\x12\x11\n\tsignature\x18\x05 \x01(\x0c\x12\x19\n\x11signed_time_stamp\x18\x06 \x01(\x0c\x12\x19\n\x11\x61ssociated_source\x18\x07 \x01(\t\"*\n\x0cUserMetadata\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x86\x01\n\nMultiValue\x12/\n\x06values\x18\x01 \x03(\x0b\x32\x1f.attrpubapi_v1.MultiValue.Value\x1aG\n\x05Value\x12\x30\n\x0c\x63ontent_type\x18\x01 \x01(\x0e\x32\x1a.attrpubapi_v1.ContentType\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Attribute_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ATTRIBUTE']._serialized_start=54
  _globals['_ATTRIBUTE']._serialized_end=301
  _globals['_METADATA']._serialized_start=303
  _globals['_METADATA']._serialized_end=416
  _globals['_ANCHOR']._serialized_start=419
  _globals['_ANCHOR']._serialized_end=598
  _globals['_USERMETADATA']._serialized_start=600
  _globals['_USERMETADATA']._serialized_end=642
  _globals['_MULTIVALUE']._serialized_start=645
  _globals['_MULTIVALUE']._serialized_end=779
  _globals['_MULTIVALUE_VALUE']._serialized_start=708
  _globals['_MULTIVALUE_VALUE']._serialized_end=779
# @@protoc_insertion_point(module_scope)
