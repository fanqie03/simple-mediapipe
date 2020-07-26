# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/examples/desktop/autoflip/quality/focus_point.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/examples/desktop/autoflip/quality/focus_point.proto',
  package='mediapipe.autoflip',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=mediapipe/examples/desktop/autoflip/quality/focus_point.proto\x12\x12mediapipe.autoflip\"\xca\x02\n\nFocusPoint\x12\x17\n\x0cnorm_point_x\x18\x01 \x01(\x02:\x01\x30\x12\x17\n\x0cnorm_point_y\x18\x02 \x01(\x02:\x01\x30\x12I\n\x04type\x18\x0b \x01(\x0e\x32-.mediapipe.autoflip.FocusPoint.FocusPointType:\x0cTYPE_INCLUDE\x12\x11\n\x04left\x18\x03 \x01(\x02:\x03\x30.3\x12\x13\n\x06\x62ottom\x18\x04 \x01(\x02:\x03\x30.3\x12\x12\n\x05right\x18\t \x01(\x02:\x03\x30.3\x12\x10\n\x03top\x18\n \x01(\x02:\x03\x30.3\x12\x12\n\x06weight\x18\x05 \x01(\x02:\x02\x31\x35\"Q\n\x0e\x46ocusPointType\x12\x10\n\x0cTYPE_INCLUDE\x10\x01\x12\x15\n\x11TYPE_EXCLUDE_LEFT\x10\x02\x12\x16\n\x12TYPE_EXCLUDE_RIGHT\x10\x03*\n\x08\xa0\x9c\x01\x10\x80\x80\x80\x80\x02\"L\n\x0f\x46ocusPointFrame\x12-\n\x05point\x18\x01 \x03(\x0b\x32\x1e.mediapipe.autoflip.FocusPoint*\n\x08\xa0\x9c\x01\x10\x80\x80\x80\x80\x02'
)



_FOCUSPOINT_FOCUSPOINTTYPE = _descriptor.EnumDescriptor(
  name='FocusPointType',
  full_name='mediapipe.autoflip.FocusPoint.FocusPointType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_INCLUDE', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TYPE_EXCLUDE_LEFT', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TYPE_EXCLUDE_RIGHT', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=323,
  serialized_end=404,
)
_sym_db.RegisterEnumDescriptor(_FOCUSPOINT_FOCUSPOINTTYPE)


_FOCUSPOINT = _descriptor.Descriptor(
  name='FocusPoint',
  full_name='mediapipe.autoflip.FocusPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='norm_point_x', full_name='mediapipe.autoflip.FocusPoint.norm_point_x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='norm_point_y', full_name='mediapipe.autoflip.FocusPoint.norm_point_y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='mediapipe.autoflip.FocusPoint.type', index=2,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='left', full_name='mediapipe.autoflip.FocusPoint.left', index=3,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.3),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bottom', full_name='mediapipe.autoflip.FocusPoint.bottom', index=4,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.3),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right', full_name='mediapipe.autoflip.FocusPoint.right', index=5,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.3),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='top', full_name='mediapipe.autoflip.FocusPoint.top', index=6,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.3),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weight', full_name='mediapipe.autoflip.FocusPoint.weight', index=7,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(15),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FOCUSPOINT_FOCUSPOINTTYPE,
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(20000, 536870912), ],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=416,
)


_FOCUSPOINTFRAME = _descriptor.Descriptor(
  name='FocusPointFrame',
  full_name='mediapipe.autoflip.FocusPointFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='mediapipe.autoflip.FocusPointFrame.point', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(20000, 536870912), ],
  oneofs=[
  ],
  serialized_start=418,
  serialized_end=494,
)

_FOCUSPOINT.fields_by_name['type'].enum_type = _FOCUSPOINT_FOCUSPOINTTYPE
_FOCUSPOINT_FOCUSPOINTTYPE.containing_type = _FOCUSPOINT
_FOCUSPOINTFRAME.fields_by_name['point'].message_type = _FOCUSPOINT
DESCRIPTOR.message_types_by_name['FocusPoint'] = _FOCUSPOINT
DESCRIPTOR.message_types_by_name['FocusPointFrame'] = _FOCUSPOINTFRAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FocusPoint = _reflection.GeneratedProtocolMessageType('FocusPoint', (_message.Message,), {
  'DESCRIPTOR' : _FOCUSPOINT,
  '__module__' : 'mediapipe.examples.desktop.autoflip.quality.focus_point_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.autoflip.FocusPoint)
  })
_sym_db.RegisterMessage(FocusPoint)

FocusPointFrame = _reflection.GeneratedProtocolMessageType('FocusPointFrame', (_message.Message,), {
  'DESCRIPTOR' : _FOCUSPOINTFRAME,
  '__module__' : 'mediapipe.examples.desktop.autoflip.quality.focus_point_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.autoflip.FocusPointFrame)
  })
_sym_db.RegisterMessage(FocusPointFrame)


# @@protoc_insertion_point(module_scope)