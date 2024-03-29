# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tflite/tflite_converter_calculator.proto

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
  name='mediapipe/calculators/tflite/tflite_converter_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>mediapipe/calculators/tflite/tflite_converter_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xf5\x02\n TfLiteConverterCalculatorOptions\x12\x19\n\x0bzero_center\x18\x01 \x01(\x08:\x04true\x12\'\n\x18use_custom_normalization\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x16\n\ncustom_div\x18\x07 \x01(\x02:\x02-1\x12\x16\n\ncustom_sub\x18\x08 \x01(\x02:\x02-1\x12\x1e\n\x0f\x66lip_vertically\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x10max_num_channels\x18\x03 \x01(\x05:\x01\x33\x12\x1f\n\x10row_major_matrix\x18\x04 \x01(\x08:\x05\x66\x61lse\x12$\n\x15use_quantized_tensors\x18\x05 \x01(\x08:\x05\x66\x61lse2Y\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xc5\xc3\x9bu \x01(\x0b\x32+.mediapipe.TfLiteConverterCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_TFLITECONVERTERCALCULATOROPTIONS = _descriptor.Descriptor(
  name='TfLiteConverterCalculatorOptions',
  full_name='mediapipe.TfLiteConverterCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='zero_center', full_name='mediapipe.TfLiteConverterCalculatorOptions.zero_center', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_custom_normalization', full_name='mediapipe.TfLiteConverterCalculatorOptions.use_custom_normalization', index=1,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='custom_div', full_name='mediapipe.TfLiteConverterCalculatorOptions.custom_div', index=2,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(-1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='custom_sub', full_name='mediapipe.TfLiteConverterCalculatorOptions.custom_sub', index=3,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(-1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flip_vertically', full_name='mediapipe.TfLiteConverterCalculatorOptions.flip_vertically', index=4,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_num_channels', full_name='mediapipe.TfLiteConverterCalculatorOptions.max_num_channels', index=5,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='row_major_matrix', full_name='mediapipe.TfLiteConverterCalculatorOptions.row_major_matrix', index=6,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_quantized_tensors', full_name='mediapipe.TfLiteConverterCalculatorOptions.use_quantized_tensors', index=7,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.TfLiteConverterCalculatorOptions.ext', index=0,
      number=245817797, type=11, cpp_type=10, label=1,
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
  serialized_start=116,
  serialized_end=489,
)

DESCRIPTOR.message_types_by_name['TfLiteConverterCalculatorOptions'] = _TFLITECONVERTERCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TfLiteConverterCalculatorOptions = _reflection.GeneratedProtocolMessageType('TfLiteConverterCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _TFLITECONVERTERCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.tflite.tflite_converter_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TfLiteConverterCalculatorOptions)
  })
_sym_db.RegisterMessage(TfLiteConverterCalculatorOptions)

_TFLITECONVERTERCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _TFLITECONVERTERCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TFLITECONVERTERCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
