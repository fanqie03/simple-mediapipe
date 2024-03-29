# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/examples/desktop/autoflip/calculators/content_zooming_calculator.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.examples.desktop.autoflip.quality import kinematic_path_solver_pb2 as mediapipe_dot_examples_dot_desktop_dot_autoflip_dot_quality_dot_kinematic__path__solver__pb2
from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/examples/desktop/autoflip/calculators/content_zooming_calculator.proto',
  package='mediapipe.autoflip',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nPmediapipe/examples/desktop/autoflip/calculators/content_zooming_calculator.proto\x12\x12mediapipe.autoflip\x1aGmediapipe/examples/desktop/autoflip/quality/kinematic_path_solver.proto\x1a$mediapipe/framework/calculator.proto\"\xf7\x04\n\x1f\x43ontentZoomingCalculatorOptions\x12\x19\n\x0cscale_factor\x18\x01 \x01(\x02:\x03\x30.9\x12\x44\n\x16kinematic_options_zoom\x18\x06 \x01(\x0b\x32$.mediapipe.autoflip.KinematicOptions\x12\x44\n\x16kinematic_options_tilt\x18\x07 \x01(\x0b\x32$.mediapipe.autoflip.KinematicOptions\x12\"\n\x11us_before_zoomout\x18\t \x01(\x03:\x07\x31\x30\x30\x30\x30\x30\x30\x12M\n\x0btarget_size\x18\x08 \x01(\x0b\x32\x38.mediapipe.autoflip.ContentZoomingCalculatorOptions.Size\x12\x43\n\x11kinematic_options\x18\x02 \x01(\x0b\x32$.mediapipe.autoflip.KinematicOptionsB\x02\x18\x01\x12!\n\x15min_motion_to_reframe\x18\x04 \x01(\x03\x42\x02\x18\x01\x12 \n\x11min_vertical_zoom\x18\x05 \x01(\x02:\x01\x31\x42\x02\x18\x01\x12%\n\x15\x66rames_before_zoomout\x18\x03 \x01(\x03:\x02\x33\x30\x42\x02\x18\x01\x1a%\n\x04Size\x12\r\n\x05width\x18\x01 \x01(\x03\x12\x0e\n\x06height\x18\x02 \x01(\x03\x32\x62\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x98\xcf\xa5\x95\x01 \x01(\x0b\x32\x33.mediapipe.autoflip.ContentZoomingCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_examples_dot_desktop_dot_autoflip_dot_quality_dot_kinematic__path__solver__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_CONTENTZOOMINGCALCULATOROPTIONS_SIZE = _descriptor.Descriptor(
  name='Size',
  full_name='mediapipe.autoflip.ContentZoomingCalculatorOptions.Size',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='mediapipe.autoflip.ContentZoomingCalculatorOptions.Size.width', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='mediapipe.autoflip.ContentZoomingCalculatorOptions.Size.height', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=710,
  serialized_end=747,
)

_CONTENTZOOMINGCALCULATOROPTIONS = _descriptor.Descriptor(
  name='ContentZoomingCalculatorOptions',
  full_name='mediapipe.autoflip.ContentZoomingCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scale_factor', full_name='mediapipe.autoflip.ContentZoomingCalculatorOptions.scale_factor', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.9),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kinematic_options_zoom', full_name='mediapipe.autoflip.ContentZoomingCalculatorOptions.kinematic_options_zoom', index=1,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kinematic_options_tilt', full_name='mediapipe.autoflip.ContentZoomingCalculatorOptions.kinematic_options_tilt', index=2,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='us_before_zoomout', full_name='mediapipe.autoflip.ContentZoomingCalculatorOptions.us_before_zoomout', index=3,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=1000000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_size', full_name='mediapipe.autoflip.ContentZoomingCalculatorOptions.target_size', index=4,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kinematic_options', full_name='mediapipe.autoflip.ContentZoomingCalculatorOptions.kinematic_options', index=5,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_motion_to_reframe', full_name='mediapipe.autoflip.ContentZoomingCalculatorOptions.min_motion_to_reframe', index=6,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_vertical_zoom', full_name='mediapipe.autoflip.ContentZoomingCalculatorOptions.min_vertical_zoom', index=7,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frames_before_zoomout', full_name='mediapipe.autoflip.ContentZoomingCalculatorOptions.frames_before_zoomout', index=8,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=30,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.autoflip.ContentZoomingCalculatorOptions.ext', index=0,
      number=313091992, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  nested_types=[_CONTENTZOOMINGCALCULATOROPTIONS_SIZE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=847,
)

_CONTENTZOOMINGCALCULATOROPTIONS_SIZE.containing_type = _CONTENTZOOMINGCALCULATOROPTIONS
_CONTENTZOOMINGCALCULATOROPTIONS.fields_by_name['kinematic_options_zoom'].message_type = mediapipe_dot_examples_dot_desktop_dot_autoflip_dot_quality_dot_kinematic__path__solver__pb2._KINEMATICOPTIONS
_CONTENTZOOMINGCALCULATOROPTIONS.fields_by_name['kinematic_options_tilt'].message_type = mediapipe_dot_examples_dot_desktop_dot_autoflip_dot_quality_dot_kinematic__path__solver__pb2._KINEMATICOPTIONS
_CONTENTZOOMINGCALCULATOROPTIONS.fields_by_name['target_size'].message_type = _CONTENTZOOMINGCALCULATOROPTIONS_SIZE
_CONTENTZOOMINGCALCULATOROPTIONS.fields_by_name['kinematic_options'].message_type = mediapipe_dot_examples_dot_desktop_dot_autoflip_dot_quality_dot_kinematic__path__solver__pb2._KINEMATICOPTIONS
DESCRIPTOR.message_types_by_name['ContentZoomingCalculatorOptions'] = _CONTENTZOOMINGCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContentZoomingCalculatorOptions = _reflection.GeneratedProtocolMessageType('ContentZoomingCalculatorOptions', (_message.Message,), {

  'Size' : _reflection.GeneratedProtocolMessageType('Size', (_message.Message,), {
    'DESCRIPTOR' : _CONTENTZOOMINGCALCULATOROPTIONS_SIZE,
    '__module__' : 'mediapipe.examples.desktop.autoflip.calculators.content_zooming_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.autoflip.ContentZoomingCalculatorOptions.Size)
    })
  ,
  'DESCRIPTOR' : _CONTENTZOOMINGCALCULATOROPTIONS,
  '__module__' : 'mediapipe.examples.desktop.autoflip.calculators.content_zooming_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.autoflip.ContentZoomingCalculatorOptions)
  })
_sym_db.RegisterMessage(ContentZoomingCalculatorOptions)
_sym_db.RegisterMessage(ContentZoomingCalculatorOptions.Size)

_CONTENTZOOMINGCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _CONTENTZOOMINGCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_CONTENTZOOMINGCALCULATOROPTIONS.extensions_by_name['ext'])

_CONTENTZOOMINGCALCULATOROPTIONS.fields_by_name['kinematic_options']._options = None
_CONTENTZOOMINGCALCULATOROPTIONS.fields_by_name['min_motion_to_reframe']._options = None
_CONTENTZOOMINGCALCULATOROPTIONS.fields_by_name['min_vertical_zoom']._options = None
_CONTENTZOOMINGCALCULATOROPTIONS.fields_by_name['frames_before_zoomout']._options = None
# @@protoc_insertion_point(module_scope)
