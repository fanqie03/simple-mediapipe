# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensorflow/object_detection_tensors_to_detections_calculator.proto

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
  name='mediapipe/calculators/tensorflow/object_detection_tensors_to_detections_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nXmediapipe/calculators/tensorflow/object_detection_tensors_to_detections_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xdd\x01\n3ObjectDetectionsTensorToDetectionsCalculatorOptions\x12\x19\n\x0emask_threshold\x18\x01 \x01(\x02:\x01\x30\x12\x1d\n\x15tensor_dim_to_squeeze\x18\x02 \x03(\x05\x32l\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x88\x83\xf0[ \x01(\x0b\x32>.mediapipe.ObjectDetectionsTensorToDetectionsCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_OBJECTDETECTIONSTENSORTODETECTIONSCALCULATOROPTIONS = _descriptor.Descriptor(
  name='ObjectDetectionsTensorToDetectionsCalculatorOptions',
  full_name='mediapipe.ObjectDetectionsTensorToDetectionsCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mask_threshold', full_name='mediapipe.ObjectDetectionsTensorToDetectionsCalculatorOptions.mask_threshold', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tensor_dim_to_squeeze', full_name='mediapipe.ObjectDetectionsTensorToDetectionsCalculatorOptions.tensor_dim_to_squeeze', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.ObjectDetectionsTensorToDetectionsCalculatorOptions.ext', index=0,
      number=192676232, type=11, cpp_type=10, label=1,
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
  serialized_start=142,
  serialized_end=363,
)

DESCRIPTOR.message_types_by_name['ObjectDetectionsTensorToDetectionsCalculatorOptions'] = _OBJECTDETECTIONSTENSORTODETECTIONSCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectDetectionsTensorToDetectionsCalculatorOptions = _reflection.GeneratedProtocolMessageType('ObjectDetectionsTensorToDetectionsCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTDETECTIONSTENSORTODETECTIONSCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.tensorflow.object_detection_tensors_to_detections_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.ObjectDetectionsTensorToDetectionsCalculatorOptions)
  })
_sym_db.RegisterMessage(ObjectDetectionsTensorToDetectionsCalculatorOptions)

_OBJECTDETECTIONSTENSORTODETECTIONSCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _OBJECTDETECTIONSTENSORTODETECTIONSCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_OBJECTDETECTIONSTENSORTODETECTIONSCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
