# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/game/gameanticheat/game_anticheat_action_request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.networking.requests.game.gameanticheat import game_anticheat_action_pb2 as pogoprotos_dot_networking_dot_requests_dot_game_dot_gameanticheat_dot_game__anticheat__action__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/game/gameanticheat/game_anticheat_action_request.proto',
  package='pogoprotos.networking.requests.game.gameanticheat',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nUpogoprotos/networking/requests/game/gameanticheat/game_anticheat_action_request.proto\x12\x31pogoprotos.networking.requests.game.gameanticheat\x1aMpogoprotos/networking/requests/game/gameanticheat/game_anticheat_action.proto\"\x93\x01\n\x1aGameAnticheatActionRequest\x12\\\n\x0crequest_type\x18\x01 \x01(\x0e\x32\x46.pogoprotos.networking.requests.game.gameanticheat.GameAnticheatAction\x12\x17\n\x0frequest_message\x18\x02 \x01(\x0c\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_networking_dot_requests_dot_game_dot_gameanticheat_dot_game__anticheat__action__pb2.DESCRIPTOR,])




_GAMEANTICHEATACTIONREQUEST = _descriptor.Descriptor(
  name='GameAnticheatActionRequest',
  full_name='pogoprotos.networking.requests.game.gameanticheat.GameAnticheatActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_type', full_name='pogoprotos.networking.requests.game.gameanticheat.GameAnticheatActionRequest.request_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_message', full_name='pogoprotos.networking.requests.game.gameanticheat.GameAnticheatActionRequest.request_message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=220,
  serialized_end=367,
)

_GAMEANTICHEATACTIONREQUEST.fields_by_name['request_type'].enum_type = pogoprotos_dot_networking_dot_requests_dot_game_dot_gameanticheat_dot_game__anticheat__action__pb2._GAMEANTICHEATACTION
DESCRIPTOR.message_types_by_name['GameAnticheatActionRequest'] = _GAMEANTICHEATACTIONREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameAnticheatActionRequest = _reflection.GeneratedProtocolMessageType('GameAnticheatActionRequest', (_message.Message,), dict(
  DESCRIPTOR = _GAMEANTICHEATACTIONREQUEST,
  __module__ = 'pogoprotos.networking.requests.game.gameanticheat.game_anticheat_action_request_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.game.gameanticheat.GameAnticheatActionRequest)
  ))
_sym_db.RegisterMessage(GameAnticheatActionRequest)


# @@protoc_insertion_point(module_scope)
