# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plane.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bplane.proto\"B\n\x05Plane\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\t\n\x01x\x18\x03 \x01(\x05\x12\t\n\x01y\x18\x04 \x01(\x05\x12\t\n\x01z\x18\x05 \x01(\x05\":\n\tPlaneNoId\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\x12\t\n\x01z\x18\x04 \x01(\x05\" \n\x06Planes\x12\x16\n\x06planes\x18\x01 \x03(\x0b\x32\x06.Plane\"\x12\n\x10GetPlanesRequest\"\x18\n\x16GetPlanesStreamRequest2\x8e\x01\n\x0cPlaneService\x12!\n\x0b\x43reatePlane\x12\n.PlaneNoId\x1a\x06.Plane\x12\'\n\tGetPlanes\x12\x11.GetPlanesRequest\x1a\x07.Planes\x12\x32\n\x0cStreamPlanes\x12\x17.GetPlanesStreamRequest\x1a\x07.Planes0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plane_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_PLANE']._serialized_start=15
  _globals['_PLANE']._serialized_end=81
  _globals['_PLANENOID']._serialized_start=83
  _globals['_PLANENOID']._serialized_end=141
  _globals['_PLANES']._serialized_start=143
  _globals['_PLANES']._serialized_end=175
  _globals['_GETPLANESREQUEST']._serialized_start=177
  _globals['_GETPLANESREQUEST']._serialized_end=195
  _globals['_GETPLANESSTREAMREQUEST']._serialized_start=197
  _globals['_GETPLANESSTREAMREQUEST']._serialized_end=221
  _globals['_PLANESERVICE']._serialized_start=224
  _globals['_PLANESERVICE']._serialized_end=366
# @@protoc_insertion_point(module_scope)