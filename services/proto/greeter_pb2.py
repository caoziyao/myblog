# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/greeter.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/greeter.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x13proto/greeter.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\rHelloResponse\x12\x10\n\x08greeting\x18\x02 \x01(\t23\n\x07Greeter\x12(\n\x05Hello\x12\r.HelloRequest\x1a\x0e.HelloResponse\"\x00\x62\x06proto3')
)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='HelloRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=23,
  serialized_end=51,
)


_HELLORESPONSE = _descriptor.Descriptor(
  name='HelloResponse',
  full_name='HelloResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='HelloResponse.greeting', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=53,
  serialized_end=86,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloResponse'] = _HELLORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREQUEST,
  __module__ = 'proto.greeter_pb2'
  # @@protoc_insertion_point(class_scope:HelloRequest)
  ))
_sym_db.RegisterMessage(HelloRequest)

HelloResponse = _reflection.GeneratedProtocolMessageType('HelloResponse', (_message.Message,), dict(
  DESCRIPTOR = _HELLORESPONSE,
  __module__ = 'proto.greeter_pb2'
  # @@protoc_insertion_point(class_scope:HelloResponse)
  ))
_sym_db.RegisterMessage(HelloResponse)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='Greeter',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=88,
  serialized_end=139,
  methods=[
  _descriptor.MethodDescriptor(
    name='Hello',
    full_name='Greeter.Hello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLORESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)