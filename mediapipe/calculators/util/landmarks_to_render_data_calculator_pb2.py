# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/util/landmarks_to_render_data_calculator.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2
from mediapipe.util import color_pb2 as mediapipe_dot_util_dot_color__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/util/landmarks_to_render_data_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nDmediapipe/calculators/util/landmarks_to_render_data_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a\x1amediapipe/util/color.proto\"\xff\x02\n&LandmarksToRenderDataCalculatorOptions\x12\x1c\n\x14landmark_connections\x18\x01 \x03(\x05\x12(\n\x0elandmark_color\x18\x02 \x01(\x0b\x32\x10.mediapipe.Color\x12*\n\x10\x63onnection_color\x18\x03 \x01(\x0b\x32\x10.mediapipe.Color\x12\x14\n\tthickness\x18\x04 \x01(\x01:\x01\x31\x12&\n\x18visualize_landmark_depth\x18\x05 \x01(\x08:\x04true\x12!\n\x12utilize_visibility\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x14visibility_threshold\x18\x07 \x01(\x01:\x01\x30\x32_\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xbd\xd2\x9d{ \x01(\x0b\x32\x31.mediapipe.LandmarksToRenderDataCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_util_dot_color__pb2.DESCRIPTOR,])




_LANDMARKSTORENDERDATACALCULATOROPTIONS = _descriptor.Descriptor(
  name='LandmarksToRenderDataCalculatorOptions',
  full_name='mediapipe.LandmarksToRenderDataCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='landmark_connections', full_name='mediapipe.LandmarksToRenderDataCalculatorOptions.landmark_connections', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='landmark_color', full_name='mediapipe.LandmarksToRenderDataCalculatorOptions.landmark_color', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection_color', full_name='mediapipe.LandmarksToRenderDataCalculatorOptions.connection_color', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='thickness', full_name='mediapipe.LandmarksToRenderDataCalculatorOptions.thickness', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visualize_landmark_depth', full_name='mediapipe.LandmarksToRenderDataCalculatorOptions.visualize_landmark_depth', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='utilize_visibility', full_name='mediapipe.LandmarksToRenderDataCalculatorOptions.utilize_visibility', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visibility_threshold', full_name='mediapipe.LandmarksToRenderDataCalculatorOptions.visibility_threshold', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.LandmarksToRenderDataCalculatorOptions.ext', index=0,
      number=258435389, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=150,
  serialized_end=533,
)

_LANDMARKSTORENDERDATACALCULATOROPTIONS.fields_by_name['landmark_color'].message_type = mediapipe_dot_util_dot_color__pb2._COLOR
_LANDMARKSTORENDERDATACALCULATOROPTIONS.fields_by_name['connection_color'].message_type = mediapipe_dot_util_dot_color__pb2._COLOR
DESCRIPTOR.message_types_by_name['LandmarksToRenderDataCalculatorOptions'] = _LANDMARKSTORENDERDATACALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LandmarksToRenderDataCalculatorOptions = _reflection.GeneratedProtocolMessageType('LandmarksToRenderDataCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _LANDMARKSTORENDERDATACALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.util.landmarks_to_render_data_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.LandmarksToRenderDataCalculatorOptions)
  })
_sym_db.RegisterMessage(LandmarksToRenderDataCalculatorOptions)

_LANDMARKSTORENDERDATACALCULATOROPTIONS.extensions_by_name['ext'].message_type = _LANDMARKSTORENDERDATACALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_LANDMARKSTORENDERDATACALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
