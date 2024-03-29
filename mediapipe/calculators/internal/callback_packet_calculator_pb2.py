# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/internal/callback_packet_calculator.proto

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
  name='mediapipe/calculators/internal/callback_packet_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n?mediapipe/calculators/internal/callback_packet_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\x99\x02\n\x1f\x43\x61llbackPacketCalculatorOptions\x12\x44\n\x04type\x18\x01 \x01(\x0e\x32\x36.mediapipe.CallbackPacketCalculatorOptions.PointerType\x12\x0f\n\x07pointer\x18\x02 \x01(\x0c\"E\n\x0bPointerType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rVECTOR_PACKET\x10\x01\x12\x16\n\x12POST_STREAM_PACKET\x10\x02\x32X\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xeb\xc7\xa4u \x01(\x0b\x32*.mediapipe.CallbackPacketCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])



_CALLBACKPACKETCALCULATOROPTIONS_POINTERTYPE = _descriptor.EnumDescriptor(
  name='PointerType',
  full_name='mediapipe.CallbackPacketCalculatorOptions.PointerType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VECTOR_PACKET', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POST_STREAM_PACKET', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=239,
  serialized_end=308,
)
_sym_db.RegisterEnumDescriptor(_CALLBACKPACKETCALCULATOROPTIONS_POINTERTYPE)


_CALLBACKPACKETCALCULATOROPTIONS = _descriptor.Descriptor(
  name='CallbackPacketCalculatorOptions',
  full_name='mediapipe.CallbackPacketCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='mediapipe.CallbackPacketCalculatorOptions.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pointer', full_name='mediapipe.CallbackPacketCalculatorOptions.pointer', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.CallbackPacketCalculatorOptions.ext', index=0,
      number=245965803, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  nested_types=[],
  enum_types=[
    _CALLBACKPACKETCALCULATOROPTIONS_POINTERTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=398,
)

_CALLBACKPACKETCALCULATOROPTIONS.fields_by_name['type'].enum_type = _CALLBACKPACKETCALCULATOROPTIONS_POINTERTYPE
_CALLBACKPACKETCALCULATOROPTIONS_POINTERTYPE.containing_type = _CALLBACKPACKETCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['CallbackPacketCalculatorOptions'] = _CALLBACKPACKETCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CallbackPacketCalculatorOptions = _reflection.GeneratedProtocolMessageType('CallbackPacketCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _CALLBACKPACKETCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.internal.callback_packet_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.CallbackPacketCalculatorOptions)
  })
_sym_db.RegisterMessage(CallbackPacketCalculatorOptions)

_CALLBACKPACKETCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _CALLBACKPACKETCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_CALLBACKPACKETCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
