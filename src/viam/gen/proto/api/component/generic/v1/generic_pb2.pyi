"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.struct_pb2
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class DoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    COMMAND_FIELD_NUMBER: builtins.int
    name: typing.Text

    @property
    def command(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, name: typing.Text=..., command: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['command', b'command']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['command', b'command', 'name', b'name']) -> None:
        ...
global___DoRequest = DoRequest

class DoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESULT_FIELD_NUMBER: builtins.int

    @property
    def result(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, result: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['result', b'result']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['result', b'result']) -> None:
        ...
global___DoResponse = DoResponse