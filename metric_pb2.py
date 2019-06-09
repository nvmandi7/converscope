# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metric.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='metric.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0cmetric.proto\"\x86\x01\n\x0cMetricFilter\x12\x17\n\x0f\x63onversation_id\x18\x01 \x01(\x03\x12\x17\n\x0fstart_timestamp\x18\x02 \x01(\x03\x12\x15\n\rend_timestamp\x18\x03 \x01(\x03\x12\x13\n\x0bsender_name\x18\x04 \x01(\t\x12\x18\n\x10max_participants\x18\x05 \x01(\x03\"`\n\rMetricRequest\x12\x1b\n\x06metric\x18\x01 \x01(\x0e\x32\x0b.MetricName\x12\x1d\n\x06\x66ilter\x18\x02 \x01(\x0b\x32\r.MetricFilter\x12\x13\n\x0btime_chunks\x18\x03 \x01(\x03\"U\n\x0eMetricResponse\x12\x1f\n\x07request\x18\x01 \x01(\x0b\x32\x0e.MetricRequest\x12\"\n\nint_metric\x18\x02 \x03(\x0b\x32\x0e.IntegerMetric\"=\n\rIntegerMetric\x12\r\n\x05value\x18\x01 \x01(\x03\x12\x1d\n\x06\x66ilter\x18\x02 \x01(\x0b\x32\r.MetricFilter*2\n\nMetricName\x12\x0e\n\nMN_UNKNOWN\x10\x00\x12\x14\n\x10MN_MESSAGE_COUNT\x10\x01\x62\x06proto3')
)

_METRICNAME = _descriptor.EnumDescriptor(
  name='MetricName',
  full_name='MetricName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MN_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MN_MESSAGE_COUNT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=401,
  serialized_end=451,
)
_sym_db.RegisterEnumDescriptor(_METRICNAME)

MetricName = enum_type_wrapper.EnumTypeWrapper(_METRICNAME)
MN_UNKNOWN = 0
MN_MESSAGE_COUNT = 1



_METRICFILTER = _descriptor.Descriptor(
  name='MetricFilter',
  full_name='MetricFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conversation_id', full_name='MetricFilter.conversation_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='MetricFilter.start_timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='MetricFilter.end_timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_name', full_name='MetricFilter.sender_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_participants', full_name='MetricFilter.max_participants', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=151,
)


_METRICREQUEST = _descriptor.Descriptor(
  name='MetricRequest',
  full_name='MetricRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric', full_name='MetricRequest.metric', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='MetricRequest.filter', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_chunks', full_name='MetricRequest.time_chunks', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=249,
)


_METRICRESPONSE = _descriptor.Descriptor(
  name='MetricResponse',
  full_name='MetricResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='MetricResponse.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_metric', full_name='MetricResponse.int_metric', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=336,
)


_INTEGERMETRIC = _descriptor.Descriptor(
  name='IntegerMetric',
  full_name='IntegerMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='IntegerMetric.value', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='IntegerMetric.filter', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=399,
)

_METRICREQUEST.fields_by_name['metric'].enum_type = _METRICNAME
_METRICREQUEST.fields_by_name['filter'].message_type = _METRICFILTER
_METRICRESPONSE.fields_by_name['request'].message_type = _METRICREQUEST
_METRICRESPONSE.fields_by_name['int_metric'].message_type = _INTEGERMETRIC
_INTEGERMETRIC.fields_by_name['filter'].message_type = _METRICFILTER
DESCRIPTOR.message_types_by_name['MetricFilter'] = _METRICFILTER
DESCRIPTOR.message_types_by_name['MetricRequest'] = _METRICREQUEST
DESCRIPTOR.message_types_by_name['MetricResponse'] = _METRICRESPONSE
DESCRIPTOR.message_types_by_name['IntegerMetric'] = _INTEGERMETRIC
DESCRIPTOR.enum_types_by_name['MetricName'] = _METRICNAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetricFilter = _reflection.GeneratedProtocolMessageType('MetricFilter', (_message.Message,), dict(
  DESCRIPTOR = _METRICFILTER,
  __module__ = 'metric_pb2'
  # @@protoc_insertion_point(class_scope:MetricFilter)
  ))
_sym_db.RegisterMessage(MetricFilter)

MetricRequest = _reflection.GeneratedProtocolMessageType('MetricRequest', (_message.Message,), dict(
  DESCRIPTOR = _METRICREQUEST,
  __module__ = 'metric_pb2'
  # @@protoc_insertion_point(class_scope:MetricRequest)
  ))
_sym_db.RegisterMessage(MetricRequest)

MetricResponse = _reflection.GeneratedProtocolMessageType('MetricResponse', (_message.Message,), dict(
  DESCRIPTOR = _METRICRESPONSE,
  __module__ = 'metric_pb2'
  # @@protoc_insertion_point(class_scope:MetricResponse)
  ))
_sym_db.RegisterMessage(MetricResponse)

IntegerMetric = _reflection.GeneratedProtocolMessageType('IntegerMetric', (_message.Message,), dict(
  DESCRIPTOR = _INTEGERMETRIC,
  __module__ = 'metric_pb2'
  # @@protoc_insertion_point(class_scope:IntegerMetric)
  ))
_sym_db.RegisterMessage(IntegerMetric)


# @@protoc_insertion_point(module_scope)
