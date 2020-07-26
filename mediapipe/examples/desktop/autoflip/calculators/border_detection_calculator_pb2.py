# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/examples/desktop/autoflip/calculators/border_detection_calculator.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/examples/desktop/autoflip/calculators/border_detection_calculator.proto',
  package='mediapipe.autoflip',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nQmediapipe/examples/desktop/autoflip/calculators/border_detection_calculator.proto\x12\x12mediapipe.autoflip\x1a$mediapipe/framework/calculator.proto\"\xde\x02\n BorderDetectionCalculatorOptions\x12\x1a\n\x0f\x63olor_tolerance\x18\x01 \x01(\x05:\x01\x36\x12#\n\x18\x62order_object_padding_px\x18\x02 \x01(\x05:\x01\x35\x12%\n\x18vertical_search_distance\x18\x03 \x01(\x02:\x03\x30.2\x12&\n\x17\x62order_color_pixel_perc\x18\x04 \x01(\x02:\x05\x30.995\x12&\n\x19solid_background_tol_perc\x18\x05 \x01(\x02:\x03\x30.5\x12\x1d\n\x12\x64\x65\x66\x61ult_padding_px\x18\x06 \x01(\x05:\x01\x30\x32\x63\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x87\xa8\xf2\x83\x01 \x01(\x0b\x32\x34.mediapipe.autoflip.BorderDetectionCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_BORDERDETECTIONCALCULATOROPTIONS = _descriptor.Descriptor(
  name='BorderDetectionCalculatorOptions',
  full_name='mediapipe.autoflip.BorderDetectionCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='color_tolerance', full_name='mediapipe.autoflip.BorderDetectionCalculatorOptions.color_tolerance', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=6,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='border_object_padding_px', full_name='mediapipe.autoflip.BorderDetectionCalculatorOptions.border_object_padding_px', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vertical_search_distance', full_name='mediapipe.autoflip.BorderDetectionCalculatorOptions.vertical_search_distance', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.2),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='border_color_pixel_perc', full_name='mediapipe.autoflip.BorderDetectionCalculatorOptions.border_color_pixel_perc', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.995),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='solid_background_tol_perc', full_name='mediapipe.autoflip.BorderDetectionCalculatorOptions.solid_background_tol_perc', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_padding_px', full_name='mediapipe.autoflip.BorderDetectionCalculatorOptions.default_padding_px', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.autoflip.BorderDetectionCalculatorOptions.ext', index=0,
      number=276599815, type=11, cpp_type=10, label=1,
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
  serialized_start=144,
  serialized_end=494,
)

DESCRIPTOR.message_types_by_name['BorderDetectionCalculatorOptions'] = _BORDERDETECTIONCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BorderDetectionCalculatorOptions = _reflection.GeneratedProtocolMessageType('BorderDetectionCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _BORDERDETECTIONCALCULATOROPTIONS,
  '__module__' : 'mediapipe.examples.desktop.autoflip.calculators.border_detection_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.autoflip.BorderDetectionCalculatorOptions)
  })
_sym_db.RegisterMessage(BorderDetectionCalculatorOptions)

_BORDERDETECTIONCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _BORDERDETECTIONCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_BORDERDETECTIONCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)