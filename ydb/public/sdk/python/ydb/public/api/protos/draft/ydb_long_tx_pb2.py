# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ydb/public/api/protos/draft/ydb_long_tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb.public.api.protos import ydb_operation_pb2 as ydb_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ydb/public/api/protos/draft/ydb_long_tx.proto',
  package='Ydb.LongTx',
  syntax='proto3',
  serialized_options=b'\n\026com.yandex.ydb.long_txB\014LongTxProtos\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-ydb/public/api/protos/draft/ydb_long_tx.proto\x12\nYdb.LongTx\x1a)ydb/public/api/protos/ydb_operation.proto\"\x7f\n\x04\x44\x61ta\x12\'\n\x06\x66ormat\x18\x01 \x01(\x0e\x32\x17.Ydb.LongTx.Data.Format\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"@\n\x06\x46ormat\x12\x16\n\x12\x46ORMAT_UNSPECIFIED\x10\x00\x12\x0c\n\x08YDB_ROWS\x10\x01\x12\x10\n\x0c\x41PACHE_ARROW\x10\x03\"\xd0\x01\n\x17\x42\x65ginTransactionRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12=\n\x07tx_type\x18\x02 \x01(\x0e\x32,.Ydb.LongTx.BeginTransactionRequest.TxTypeId\";\n\x08TxTypeId\x12\x1a\n\x16TX_TYPE_ID_UNSPECIFIED\x10\x00\x12\t\n\x05WRITE\x10\x01\x12\x08\n\x04READ\x10\x02\"\'\n\x16\x42\x65ginTransactionResult\x12\r\n\x05tx_id\x18\x01 \x01(\t\"H\n\x18\x42\x65ginTransactionResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"d\n\x18\x43ommitTransactionRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\r\n\x05tx_id\x18\x02 \x01(\t\"(\n\x17\x43ommitTransactionResult\x12\r\n\x05tx_id\x18\x01 \x01(\t\"I\n\x19\x43ommitTransactionResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"f\n\x1aRollbackTransactionRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\r\n\x05tx_id\x18\x02 \x01(\t\"*\n\x19RollbackTransactionResult\x12\r\n\x05tx_id\x18\x01 \x01(\t\"K\n\x1bRollbackTransactionResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\x98\x01\n\x0cWriteRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\r\n\x05tx_id\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x10\n\x08\x64\x65\x64up_id\x18\x04 \x01(\t\x12\x1e\n\x04\x64\x61ta\x18\x05 \x01(\x0b\x32\x10.Ydb.LongTx.Data\"<\n\x0bWriteResult\x12\r\n\x05tx_id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65\x64up_id\x18\x03 \x01(\t\"=\n\rWriteResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"}\n\x0bReadRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\r\n\x05tx_id\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\r\n\x03sql\x18\x0b \x01(\tH\x00\x42\x07\n\x05query\"j\n\nReadResult\x12\r\n\x05tx_id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\r\n\x05\x63hunk\x18\x03 \x01(\x04\x12\x10\n\x08\x66inished\x18\x04 \x01(\x08\x12\x1e\n\x04\x64\x61ta\x18\x05 \x01(\x0b\x32\x10.Ydb.LongTx.Data\"<\n\x0cReadResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.OperationB)\n\x16\x63om.yandex.ydb.long_txB\x0cLongTxProtos\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[ydb_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2.DESCRIPTOR,])



_DATA_FORMAT = _descriptor.EnumDescriptor(
  name='Format',
  full_name='Ydb.LongTx.Data.Format',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FORMAT_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='YDB_ROWS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APACHE_ARROW', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=167,
  serialized_end=231,
)
_sym_db.RegisterEnumDescriptor(_DATA_FORMAT)

_BEGINTRANSACTIONREQUEST_TXTYPEID = _descriptor.EnumDescriptor(
  name='TxTypeId',
  full_name='Ydb.LongTx.BeginTransactionRequest.TxTypeId',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TX_TYPE_ID_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WRITE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='READ', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=383,
  serialized_end=442,
)
_sym_db.RegisterEnumDescriptor(_BEGINTRANSACTIONREQUEST_TXTYPEID)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='Ydb.LongTx.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='format', full_name='Ydb.LongTx.Data.format', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='Ydb.LongTx.Data.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATA_FORMAT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=231,
)


_BEGINTRANSACTIONREQUEST = _descriptor.Descriptor(
  name='BeginTransactionRequest',
  full_name='Ydb.LongTx.BeginTransactionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.LongTx.BeginTransactionRequest.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_type', full_name='Ydb.LongTx.BeginTransactionRequest.tx_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BEGINTRANSACTIONREQUEST_TXTYPEID,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=442,
)


_BEGINTRANSACTIONRESULT = _descriptor.Descriptor(
  name='BeginTransactionResult',
  full_name='Ydb.LongTx.BeginTransactionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_id', full_name='Ydb.LongTx.BeginTransactionResult.tx_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=444,
  serialized_end=483,
)


_BEGINTRANSACTIONRESPONSE = _descriptor.Descriptor(
  name='BeginTransactionResponse',
  full_name='Ydb.LongTx.BeginTransactionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.LongTx.BeginTransactionResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=485,
  serialized_end=557,
)


_COMMITTRANSACTIONREQUEST = _descriptor.Descriptor(
  name='CommitTransactionRequest',
  full_name='Ydb.LongTx.CommitTransactionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.LongTx.CommitTransactionRequest.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_id', full_name='Ydb.LongTx.CommitTransactionRequest.tx_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=659,
)


_COMMITTRANSACTIONRESULT = _descriptor.Descriptor(
  name='CommitTransactionResult',
  full_name='Ydb.LongTx.CommitTransactionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_id', full_name='Ydb.LongTx.CommitTransactionResult.tx_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=661,
  serialized_end=701,
)


_COMMITTRANSACTIONRESPONSE = _descriptor.Descriptor(
  name='CommitTransactionResponse',
  full_name='Ydb.LongTx.CommitTransactionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.LongTx.CommitTransactionResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=703,
  serialized_end=776,
)


_ROLLBACKTRANSACTIONREQUEST = _descriptor.Descriptor(
  name='RollbackTransactionRequest',
  full_name='Ydb.LongTx.RollbackTransactionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.LongTx.RollbackTransactionRequest.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_id', full_name='Ydb.LongTx.RollbackTransactionRequest.tx_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=778,
  serialized_end=880,
)


_ROLLBACKTRANSACTIONRESULT = _descriptor.Descriptor(
  name='RollbackTransactionResult',
  full_name='Ydb.LongTx.RollbackTransactionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_id', full_name='Ydb.LongTx.RollbackTransactionResult.tx_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=882,
  serialized_end=924,
)


_ROLLBACKTRANSACTIONRESPONSE = _descriptor.Descriptor(
  name='RollbackTransactionResponse',
  full_name='Ydb.LongTx.RollbackTransactionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.LongTx.RollbackTransactionResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=926,
  serialized_end=1001,
)


_WRITEREQUEST = _descriptor.Descriptor(
  name='WriteRequest',
  full_name='Ydb.LongTx.WriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.LongTx.WriteRequest.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_id', full_name='Ydb.LongTx.WriteRequest.tx_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='Ydb.LongTx.WriteRequest.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dedup_id', full_name='Ydb.LongTx.WriteRequest.dedup_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='Ydb.LongTx.WriteRequest.data', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1004,
  serialized_end=1156,
)


_WRITERESULT = _descriptor.Descriptor(
  name='WriteResult',
  full_name='Ydb.LongTx.WriteResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_id', full_name='Ydb.LongTx.WriteResult.tx_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='Ydb.LongTx.WriteResult.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dedup_id', full_name='Ydb.LongTx.WriteResult.dedup_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1158,
  serialized_end=1218,
)


_WRITERESPONSE = _descriptor.Descriptor(
  name='WriteResponse',
  full_name='Ydb.LongTx.WriteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.LongTx.WriteResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1220,
  serialized_end=1281,
)


_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='Ydb.LongTx.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.LongTx.ReadRequest.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_id', full_name='Ydb.LongTx.ReadRequest.tx_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='Ydb.LongTx.ReadRequest.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sql', full_name='Ydb.LongTx.ReadRequest.sql', index=3,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='query', full_name='Ydb.LongTx.ReadRequest.query',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1283,
  serialized_end=1408,
)


_READRESULT = _descriptor.Descriptor(
  name='ReadResult',
  full_name='Ydb.LongTx.ReadResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_id', full_name='Ydb.LongTx.ReadResult.tx_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='Ydb.LongTx.ReadResult.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk', full_name='Ydb.LongTx.ReadResult.chunk', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='finished', full_name='Ydb.LongTx.ReadResult.finished', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='Ydb.LongTx.ReadResult.data', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1410,
  serialized_end=1516,
)


_READRESPONSE = _descriptor.Descriptor(
  name='ReadResponse',
  full_name='Ydb.LongTx.ReadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.LongTx.ReadResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1518,
  serialized_end=1578,
)

_DATA.fields_by_name['format'].enum_type = _DATA_FORMAT
_DATA_FORMAT.containing_type = _DATA
_BEGINTRANSACTIONREQUEST.fields_by_name['operation_params'].message_type = ydb_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_BEGINTRANSACTIONREQUEST.fields_by_name['tx_type'].enum_type = _BEGINTRANSACTIONREQUEST_TXTYPEID
_BEGINTRANSACTIONREQUEST_TXTYPEID.containing_type = _BEGINTRANSACTIONREQUEST
_BEGINTRANSACTIONRESPONSE.fields_by_name['operation'].message_type = ydb_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_COMMITTRANSACTIONREQUEST.fields_by_name['operation_params'].message_type = ydb_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_COMMITTRANSACTIONRESPONSE.fields_by_name['operation'].message_type = ydb_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_ROLLBACKTRANSACTIONREQUEST.fields_by_name['operation_params'].message_type = ydb_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_ROLLBACKTRANSACTIONRESPONSE.fields_by_name['operation'].message_type = ydb_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_WRITEREQUEST.fields_by_name['operation_params'].message_type = ydb_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_WRITEREQUEST.fields_by_name['data'].message_type = _DATA
_WRITERESPONSE.fields_by_name['operation'].message_type = ydb_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_READREQUEST.fields_by_name['operation_params'].message_type = ydb_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_READREQUEST.oneofs_by_name['query'].fields.append(
  _READREQUEST.fields_by_name['sql'])
_READREQUEST.fields_by_name['sql'].containing_oneof = _READREQUEST.oneofs_by_name['query']
_READRESULT.fields_by_name['data'].message_type = _DATA
_READRESPONSE.fields_by_name['operation'].message_type = ydb_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['BeginTransactionRequest'] = _BEGINTRANSACTIONREQUEST
DESCRIPTOR.message_types_by_name['BeginTransactionResult'] = _BEGINTRANSACTIONRESULT
DESCRIPTOR.message_types_by_name['BeginTransactionResponse'] = _BEGINTRANSACTIONRESPONSE
DESCRIPTOR.message_types_by_name['CommitTransactionRequest'] = _COMMITTRANSACTIONREQUEST
DESCRIPTOR.message_types_by_name['CommitTransactionResult'] = _COMMITTRANSACTIONRESULT
DESCRIPTOR.message_types_by_name['CommitTransactionResponse'] = _COMMITTRANSACTIONRESPONSE
DESCRIPTOR.message_types_by_name['RollbackTransactionRequest'] = _ROLLBACKTRANSACTIONREQUEST
DESCRIPTOR.message_types_by_name['RollbackTransactionResult'] = _ROLLBACKTRANSACTIONRESULT
DESCRIPTOR.message_types_by_name['RollbackTransactionResponse'] = _ROLLBACKTRANSACTIONRESPONSE
DESCRIPTOR.message_types_by_name['WriteRequest'] = _WRITEREQUEST
DESCRIPTOR.message_types_by_name['WriteResult'] = _WRITERESULT
DESCRIPTOR.message_types_by_name['WriteResponse'] = _WRITERESPONSE
DESCRIPTOR.message_types_by_name['ReadRequest'] = _READREQUEST
DESCRIPTOR.message_types_by_name['ReadResult'] = _READRESULT
DESCRIPTOR.message_types_by_name['ReadResponse'] = _READRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.Data)
  })
_sym_db.RegisterMessage(Data)

BeginTransactionRequest = _reflection.GeneratedProtocolMessageType('BeginTransactionRequest', (_message.Message,), {
  'DESCRIPTOR' : _BEGINTRANSACTIONREQUEST,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.BeginTransactionRequest)
  })
_sym_db.RegisterMessage(BeginTransactionRequest)

BeginTransactionResult = _reflection.GeneratedProtocolMessageType('BeginTransactionResult', (_message.Message,), {
  'DESCRIPTOR' : _BEGINTRANSACTIONRESULT,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.BeginTransactionResult)
  })
_sym_db.RegisterMessage(BeginTransactionResult)

BeginTransactionResponse = _reflection.GeneratedProtocolMessageType('BeginTransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _BEGINTRANSACTIONRESPONSE,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.BeginTransactionResponse)
  })
_sym_db.RegisterMessage(BeginTransactionResponse)

CommitTransactionRequest = _reflection.GeneratedProtocolMessageType('CommitTransactionRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMMITTRANSACTIONREQUEST,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.CommitTransactionRequest)
  })
_sym_db.RegisterMessage(CommitTransactionRequest)

CommitTransactionResult = _reflection.GeneratedProtocolMessageType('CommitTransactionResult', (_message.Message,), {
  'DESCRIPTOR' : _COMMITTRANSACTIONRESULT,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.CommitTransactionResult)
  })
_sym_db.RegisterMessage(CommitTransactionResult)

CommitTransactionResponse = _reflection.GeneratedProtocolMessageType('CommitTransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMMITTRANSACTIONRESPONSE,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.CommitTransactionResponse)
  })
_sym_db.RegisterMessage(CommitTransactionResponse)

RollbackTransactionRequest = _reflection.GeneratedProtocolMessageType('RollbackTransactionRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLLBACKTRANSACTIONREQUEST,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.RollbackTransactionRequest)
  })
_sym_db.RegisterMessage(RollbackTransactionRequest)

RollbackTransactionResult = _reflection.GeneratedProtocolMessageType('RollbackTransactionResult', (_message.Message,), {
  'DESCRIPTOR' : _ROLLBACKTRANSACTIONRESULT,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.RollbackTransactionResult)
  })
_sym_db.RegisterMessage(RollbackTransactionResult)

RollbackTransactionResponse = _reflection.GeneratedProtocolMessageType('RollbackTransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLLBACKTRANSACTIONRESPONSE,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.RollbackTransactionResponse)
  })
_sym_db.RegisterMessage(RollbackTransactionResponse)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITEREQUEST,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.WriteRequest)
  })
_sym_db.RegisterMessage(WriteRequest)

WriteResult = _reflection.GeneratedProtocolMessageType('WriteResult', (_message.Message,), {
  'DESCRIPTOR' : _WRITERESULT,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.WriteResult)
  })
_sym_db.RegisterMessage(WriteResult)

WriteResponse = _reflection.GeneratedProtocolMessageType('WriteResponse', (_message.Message,), {
  'DESCRIPTOR' : _WRITERESPONSE,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.WriteResponse)
  })
_sym_db.RegisterMessage(WriteResponse)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), {
  'DESCRIPTOR' : _READREQUEST,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.ReadRequest)
  })
_sym_db.RegisterMessage(ReadRequest)

ReadResult = _reflection.GeneratedProtocolMessageType('ReadResult', (_message.Message,), {
  'DESCRIPTOR' : _READRESULT,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.ReadResult)
  })
_sym_db.RegisterMessage(ReadResult)

ReadResponse = _reflection.GeneratedProtocolMessageType('ReadResponse', (_message.Message,), {
  'DESCRIPTOR' : _READRESPONSE,
  '__module__' : 'ydb.public.api.protos.draft.ydb_long_tx_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.LongTx.ReadResponse)
  })
_sym_db.RegisterMessage(ReadResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
