# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuffers/user_proto/user.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"protobuffers/user_proto/user.proto\x12\x04user\"\x07\n\x05\x45mpty\"\x10\n\x02Id\x12\n\n\x02id\x18\x01 \x01(\x05\"\x17\n\x07\x45lement\x12\x0c\n\x04text\x18\x01 \x01(\t\"\xc0\x01\n\x08msg_user\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0f\n\x07surname\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x03\x64ob\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06gender\x18\x05 \x01(\tH\x02\x88\x01\x01\x12\x10\n\x08username\x18\x06 \x01(\t\x12\r\n\x05\x65mail\x18\x07 \x01(\t\x12\x15\n\x08password\x18\x08 \x01(\tH\x03\x88\x01\x01\x42\x05\n\x03_idB\x06\n\x04_dobB\t\n\x07_genderB\x0b\n\t_password\"\x19\n\x08msg_list\x12\r\n\x05limit\x18\x01 \x01(\x05\"x\n\rresponse_user\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07surname\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0b\n\x03\x64ob\x18\x04 \x01(\t\x12\x0e\n\x06gender\x18\x05 \x01(\t\x12\x10\n\x08username\x18\x06 \x01(\t\x12\r\n\x05\x65mail\x18\x07 \x01(\t\"8\n\x12response_user_list\x12\"\n\x05users\x18\x01 \x03(\x0b\x32\x13.user.response_user2\xaa\x01\n\x04User\x12(\n\x0c\x43reateUpdate\x12\x0e.user.msg_user\x1a\x08.user.Id\x12$\n\x03Get\x12\x08.user.Id\x1a\x13.user.response_user\x12\x1f\n\x06\x44\x65lete\x12\x08.user.Id\x1a\x0b.user.Empty\x12\x31\n\x06Search\x12\r.user.Element\x1a\x18.user.response_user_listb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuffers.user_proto.user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTY']._serialized_start=44
  _globals['_EMPTY']._serialized_end=51
  _globals['_ID']._serialized_start=53
  _globals['_ID']._serialized_end=69
  _globals['_ELEMENT']._serialized_start=71
  _globals['_ELEMENT']._serialized_end=94
  _globals['_MSG_USER']._serialized_start=97
  _globals['_MSG_USER']._serialized_end=289
  _globals['_MSG_LIST']._serialized_start=291
  _globals['_MSG_LIST']._serialized_end=316
  _globals['_RESPONSE_USER']._serialized_start=318
  _globals['_RESPONSE_USER']._serialized_end=438
  _globals['_RESPONSE_USER_LIST']._serialized_start=440
  _globals['_RESPONSE_USER_LIST']._serialized_end=496
  _globals['_USER']._serialized_start=499
  _globals['_USER']._serialized_end=669
# @@protoc_insertion_point(module_scope)
