# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: antispam/safetynet/v1/safetynet_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import kik_unofficial.protobuf.common_rpc_pb2 as common__rpc__pb2
import kik_unofficial.protobuf.protobuf_validation_pb2 as protobuf__validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='antispam/safetynet/v1/safetynet_service.proto',
  package='mobile.antispam.safetynet.v1',
  syntax='proto3',
  serialized_pb=_b('\n-antispam/safetynet/v1/safetynet_service.proto\x12\x1cmobile.antispam.safetynet.v1\x1a\x10\x63ommon_rpc.proto\x1a\x19protobuf_validation.proto\"\x84\x01\n\x10GetNonceResponse\x12\x45\n\x06result\x18\x01 \x01(\x0e\x32\x35.mobile.antispam.safetynet.v1.GetNonceResponse.Result\x12\x17\n\x05nonce\x18\x02 \x01(\tB\x08\xca\x9d%\x04\x08\x01(\x10\"\x10\n\x06Result\x12\x06\n\x02OK\x10\x00\";\n\x1eVerifyAttestationResultRequest\x12\x19\n\x03jws\x18\x01 \x01(\tB\x0c\xca\x9d%\x08\x08\x01(\x01\x30\xa8\xc3\x01\"\xb3\x01\n\x1fVerifyAttestationResultResponse\x12T\n\x06result\x18\x01 \x01(\x0e\x32\x44.mobile.antispam.safetynet.v1.VerifyAttestationResultResponse.Result\":\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x11\n\rINVALID_NONCE\x10\x01\x12\x15\n\x11MALFORMED_REQUEST\x10\x02\x32\xf9\x01\n\tSafetyNet\x12Q\n\x08GetNonce\x12\x13.common.VoidRequest\x1a..mobile.antispam.safetynet.v1.GetNonceResponse\"\x00\x12\x98\x01\n\x17VerifyAttestationResult\x12<.mobile.antispam.safetynet.v1.VerifyAttestationResultRequest\x1a=.mobile.antispam.safetynet.v1.VerifyAttestationResultResponse\"\x00\x42{\n\x1e\x63om.kik.antispam.safetynet.rpcZYgithub.com/kikinteractive/xiphias-api-mobile/generated/go/antispam/safetynet/v1;safetynetb\x06proto3')
  ,
  dependencies=[common__rpc__pb2.DESCRIPTOR,protobuf__validation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETNONCERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.antispam.safetynet.v1.GetNonceResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=241,
  serialized_end=257,
)
_sym_db.RegisterEnumDescriptor(_GETNONCERESPONSE_RESULT)

_VERIFYATTESTATIONRESULTRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.antispam.safetynet.v1.VerifyAttestationResultResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_NONCE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MALFORMED_REQUEST', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=442,
  serialized_end=500,
)
_sym_db.RegisterEnumDescriptor(_VERIFYATTESTATIONRESULTRESPONSE_RESULT)


_GETNONCERESPONSE = _descriptor.Descriptor(
  name='GetNonceResponse',
  full_name='mobile.antispam.safetynet.v1.GetNonceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.antispam.safetynet.v1.GetNonceResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='mobile.antispam.safetynet.v1.GetNonceResponse.nonce', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\004\010\001(\020'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETNONCERESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=257,
)


_VERIFYATTESTATIONRESULTREQUEST = _descriptor.Descriptor(
  name='VerifyAttestationResultRequest',
  full_name='mobile.antispam.safetynet.v1.VerifyAttestationResultRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jws', full_name='mobile.antispam.safetynet.v1.VerifyAttestationResultRequest.jws', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\010\010\001(\0010\250\303\001'))),
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
  serialized_start=259,
  serialized_end=318,
)


_VERIFYATTESTATIONRESULTRESPONSE = _descriptor.Descriptor(
  name='VerifyAttestationResultResponse',
  full_name='mobile.antispam.safetynet.v1.VerifyAttestationResultResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.antispam.safetynet.v1.VerifyAttestationResultResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VERIFYATTESTATIONRESULTRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=500,
)

_GETNONCERESPONSE.fields_by_name['result'].enum_type = _GETNONCERESPONSE_RESULT
_GETNONCERESPONSE_RESULT.containing_type = _GETNONCERESPONSE
_VERIFYATTESTATIONRESULTRESPONSE.fields_by_name['result'].enum_type = _VERIFYATTESTATIONRESULTRESPONSE_RESULT
_VERIFYATTESTATIONRESULTRESPONSE_RESULT.containing_type = _VERIFYATTESTATIONRESULTRESPONSE
DESCRIPTOR.message_types_by_name['GetNonceResponse'] = _GETNONCERESPONSE
DESCRIPTOR.message_types_by_name['VerifyAttestationResultRequest'] = _VERIFYATTESTATIONRESULTREQUEST
DESCRIPTOR.message_types_by_name['VerifyAttestationResultResponse'] = _VERIFYATTESTATIONRESULTRESPONSE

GetNonceResponse = _reflection.GeneratedProtocolMessageType('GetNonceResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETNONCERESPONSE,
  __module__ = 'antispam.safetynet.v1.safetynet_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.antispam.safetynet.v1.GetNonceResponse)
  ))
_sym_db.RegisterMessage(GetNonceResponse)

VerifyAttestationResultRequest = _reflection.GeneratedProtocolMessageType('VerifyAttestationResultRequest', (_message.Message,), dict(
  DESCRIPTOR = _VERIFYATTESTATIONRESULTREQUEST,
  __module__ = 'antispam.safetynet.v1.safetynet_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.antispam.safetynet.v1.VerifyAttestationResultRequest)
  ))
_sym_db.RegisterMessage(VerifyAttestationResultRequest)

VerifyAttestationResultResponse = _reflection.GeneratedProtocolMessageType('VerifyAttestationResultResponse', (_message.Message,), dict(
  DESCRIPTOR = _VERIFYATTESTATIONRESULTRESPONSE,
  __module__ = 'antispam.safetynet.v1.safetynet_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.antispam.safetynet.v1.VerifyAttestationResultResponse)
  ))
_sym_db.RegisterMessage(VerifyAttestationResultResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036com.kik.antispam.safetynet.rpcZYgithub.com/kikinteractive/xiphias-api-mobile/generated/go/antispam/safetynet/v1;safetynet'))
_GETNONCERESPONSE.fields_by_name['nonce'].has_options = True
_GETNONCERESPONSE.fields_by_name['nonce']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\004\010\001(\020'))
_VERIFYATTESTATIONRESULTREQUEST.fields_by_name['jws'].has_options = True
_VERIFYATTESTATIONRESULTREQUEST.fields_by_name['jws']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\010\010\001(\0010\250\303\001'))
# @@protoc_insertion_point(module_scope)