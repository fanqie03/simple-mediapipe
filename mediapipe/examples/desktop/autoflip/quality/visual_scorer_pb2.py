# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/examples/desktop/autoflip/quality/visual_scorer.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/examples/desktop/autoflip/quality/visual_scorer.proto',
  package='mediapipe.autoflip',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n?mediapipe/examples/desktop/autoflip/quality/visual_scorer.proto\x12\x12mediapipe.autoflip\"j\n\x13VisualScorerOptions\x12\x16\n\x0b\x61rea_weight\x18\x01 \x01(\x02:\x01\x31\x12\x1b\n\x10sharpness_weight\x18\x02 \x01(\x02:\x01\x30\x12\x1e\n\x13\x63olorfulness_weight\x18\x03 \x01(\x02:\x01\x30'
)




_VISUALSCOREROPTIONS = _descriptor.Descriptor(
  name='VisualScorerOptions',
  full_name='mediapipe.autoflip.VisualScorerOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='area_weight', full_name='mediapipe.autoflip.VisualScorerOptions.area_weight', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sharpness_weight', full_name='mediapipe.autoflip.VisualScorerOptions.sharpness_weight', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='colorfulness_weight', full_name='mediapipe.autoflip.VisualScorerOptions.colorfulness_weight', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=193,
)

DESCRIPTOR.message_types_by_name['VisualScorerOptions'] = _VISUALSCOREROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VisualScorerOptions = _reflection.GeneratedProtocolMessageType('VisualScorerOptions', (_message.Message,), {
  'DESCRIPTOR' : _VISUALSCOREROPTIONS,
  '__module__' : 'mediapipe.examples.desktop.autoflip.quality.visual_scorer_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.autoflip.VisualScorerOptions)
  })
_sym_db.RegisterMessage(VisualScorerOptions)


# @@protoc_insertion_point(module_scope)