# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensorflow/tensorflow_session_from_saved_model_calculator.proto

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
  name='mediapipe/calculators/tensorflow/tensorflow_session_from_saved_model_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nUmediapipe/calculators/tensorflow/tensorflow_session_from_saved_model_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xd2\x02\n0TensorFlowSessionFromSavedModelCalculatorOptions\x12\x18\n\x10saved_model_path\x18\x01 \x01(\t\x12\'\n\x0esignature_name\x18\x02 \x01(\t:\x0fserving_default\x12\'\n\x19\x63onvert_signature_to_tags\x18\x03 \x01(\x08:\x04true\x12\x19\n\x11load_latest_model\x18\x04 \x01(\x08\x12\x13\n\x07use_tpu\x18\x05 \x01(\x08\x42\x02\x18\x01\x12\x17\n\x0fsaved_model_tag\x18\x06 \x03(\t2i\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xdb\xe8\xc6t \x01(\x0b\x32;.mediapipe.TensorFlowSessionFromSavedModelCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_TENSORFLOWSESSIONFROMSAVEDMODELCALCULATOROPTIONS = _descriptor.Descriptor(
  name='TensorFlowSessionFromSavedModelCalculatorOptions',
  full_name='mediapipe.TensorFlowSessionFromSavedModelCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='saved_model_path', full_name='mediapipe.TensorFlowSessionFromSavedModelCalculatorOptions.saved_model_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature_name', full_name='mediapipe.TensorFlowSessionFromSavedModelCalculatorOptions.signature_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"serving_default".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='convert_signature_to_tags', full_name='mediapipe.TensorFlowSessionFromSavedModelCalculatorOptions.convert_signature_to_tags', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load_latest_model', full_name='mediapipe.TensorFlowSessionFromSavedModelCalculatorOptions.load_latest_model', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_tpu', full_name='mediapipe.TensorFlowSessionFromSavedModelCalculatorOptions.use_tpu', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='saved_model_tag', full_name='mediapipe.TensorFlowSessionFromSavedModelCalculatorOptions.saved_model_tag', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.TensorFlowSessionFromSavedModelCalculatorOptions.ext', index=0,
      number=244429915, type=11, cpp_type=10, label=1,
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
  serialized_start=139,
  serialized_end=477,
)

DESCRIPTOR.message_types_by_name['TensorFlowSessionFromSavedModelCalculatorOptions'] = _TENSORFLOWSESSIONFROMSAVEDMODELCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorFlowSessionFromSavedModelCalculatorOptions = _reflection.GeneratedProtocolMessageType('TensorFlowSessionFromSavedModelCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _TENSORFLOWSESSIONFROMSAVEDMODELCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.tensorflow.tensorflow_session_from_saved_model_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TensorFlowSessionFromSavedModelCalculatorOptions)
  })
_sym_db.RegisterMessage(TensorFlowSessionFromSavedModelCalculatorOptions)

_TENSORFLOWSESSIONFROMSAVEDMODELCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _TENSORFLOWSESSIONFROMSAVEDMODELCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TENSORFLOWSESSIONFROMSAVEDMODELCALCULATOROPTIONS.extensions_by_name['ext'])

_TENSORFLOWSESSIONFROMSAVEDMODELCALCULATOROPTIONS.fields_by_name['use_tpu']._options = None
# @@protoc_insertion_point(module_scope)
