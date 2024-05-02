"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PackageFormat:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PackageFormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PackageFormat.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PACKAGE_FORMAT_UNSPECIFIED: _PackageFormat.ValueType
    'unknown/unset (autodetection may be attempted)'
    PACKAGE_FORMAT_RAW: _PackageFormat.ValueType
    'do nothing'
    PACKAGE_FORMAT_XZ: _PackageFormat.ValueType
    'decompress .xz file'
    PACKAGE_FORMAT_EXECUTABLE: _PackageFormat.ValueType
    'set executable permissions'
    PACKAGE_FORMAT_XZ_EXECUTABLE: _PackageFormat.ValueType
    'decompress and set executable'

class PackageFormat(_PackageFormat, metaclass=_PackageFormatEnumTypeWrapper):
    ...
PACKAGE_FORMAT_UNSPECIFIED: PackageFormat.ValueType
'unknown/unset (autodetection may be attempted)'
PACKAGE_FORMAT_RAW: PackageFormat.ValueType
'do nothing'
PACKAGE_FORMAT_XZ: PackageFormat.ValueType
'decompress .xz file'
PACKAGE_FORMAT_EXECUTABLE: PackageFormat.ValueType
'set executable permissions'
PACKAGE_FORMAT_XZ_EXECUTABLE: PackageFormat.ValueType
'decompress and set executable'
global___PackageFormat = PackageFormat

@typing.final
class DeviceAgentConfigRequest(google.protobuf.message.Message):
    """Device side"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class SubsystemVersionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str

        def __init__(self, *, key: builtins.str=..., value: builtins.str=...) -> None:
            ...

        def ClearField(self, field_name: typing.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    ID_FIELD_NUMBER: builtins.int
    HOST_INFO_FIELD_NUMBER: builtins.int
    SUBSYSTEM_VERSIONS_FIELD_NUMBER: builtins.int
    id: builtins.str
    'robot partID'

    @property
    def host_info(self) -> global___HostInfo:
        """info about the host system"""

    @property
    def subsystem_versions(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """current subsystems and versions"""

    def __init__(self, *, id: builtins.str=..., host_info: global___HostInfo | None=..., subsystem_versions: collections.abc.Mapping[builtins.str, builtins.str] | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['host_info', b'host_info']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['host_info', b'host_info', 'id', b'id', 'subsystem_versions', b'subsystem_versions']) -> None:
        ...
global___DeviceAgentConfigRequest = DeviceAgentConfigRequest

@typing.final
class DeviceAgentConfigResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class SubsystemConfigsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> global___DeviceSubsystemConfig:
            ...

        def __init__(self, *, key: builtins.str=..., value: global___DeviceSubsystemConfig | None=...) -> None:
            ...

        def HasField(self, field_name: typing.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    SUBSYSTEM_CONFIGS_FIELD_NUMBER: builtins.int
    CHECK_INTERVAL_FIELD_NUMBER: builtins.int

    @property
    def subsystem_configs(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___DeviceSubsystemConfig]:
        """subsystems to be installed/configured/updated
        note: previously installed subsystems will be removed from the system if removed from this list
        """

    @property
    def check_interval(self) -> google.protobuf.duration_pb2.Duration:
        """how often this request should be repeated"""

    def __init__(self, *, subsystem_configs: collections.abc.Mapping[builtins.str, global___DeviceSubsystemConfig] | None=..., check_interval: google.protobuf.duration_pb2.Duration | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['check_interval', b'check_interval']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['check_interval', b'check_interval', 'subsystem_configs', b'subsystem_configs']) -> None:
        ...
global___DeviceAgentConfigResponse = DeviceAgentConfigResponse

@typing.final
class DeviceSubsystemConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UPDATE_INFO_FIELD_NUMBER: builtins.int
    DISABLE_FIELD_NUMBER: builtins.int
    FORCE_RESTART_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    disable: builtins.bool
    'if this subsystem is disabled and should not be started by the agent'
    force_restart: builtins.bool
    'force_restart will restart the subsystem, even if no updates are available'

    @property
    def update_info(self) -> global___SubsystemUpdateInfo:
        """data needed to download/validate the subsystem"""

    @property
    def attributes(self) -> google.protobuf.struct_pb2.Struct:
        """arbitrary config sections"""

    def __init__(self, *, update_info: global___SubsystemUpdateInfo | None=..., disable: builtins.bool=..., force_restart: builtins.bool=..., attributes: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['attributes', b'attributes', 'update_info', b'update_info']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['attributes', b'attributes', 'disable', b'disable', 'force_restart', b'force_restart', 'update_info', b'update_info']) -> None:
        ...
global___DeviceSubsystemConfig = DeviceSubsystemConfig

@typing.final
class HostInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PLATFORM_FIELD_NUMBER: builtins.int
    DISTRO_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    platform: builtins.str
    'platform is the docker styled combination of kernel and architecture. Ex: linux/amd64, darwin/arm64'
    distro: builtins.str
    'ID and VERSION_ID fields from /etc/os-release, colon seperated. Ex: ubuntu:22.04, debian:11'

    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """additional tags for specific hardware or software that's present and may affect software selection
        ex: "jetson", "rpi4", "systemd", etc.
        """

    def __init__(self, *, platform: builtins.str=..., distro: builtins.str=..., tags: collections.abc.Iterable[builtins.str] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['distro', b'distro', 'platform', b'platform', 'tags', b'tags']) -> None:
        ...
global___HostInfo = HostInfo

@typing.final
class SubsystemUpdateInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FILENAME_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    SHA256_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    filename: builtins.str
    'unpacked filename as it is expected on disk (regardless of url)'
    url: builtins.str
    'url to download from'
    version: builtins.str
    'version expected at the url'
    sha256: builtins.bytes
    'sha256 sum of file as downloaded'
    format: global___PackageFormat.ValueType
    'determines if decompression or executable permissions are needed'

    def __init__(self, *, filename: builtins.str=..., url: builtins.str=..., version: builtins.str=..., sha256: builtins.bytes=..., format: global___PackageFormat.ValueType=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['filename', b'filename', 'format', b'format', 'sha256', b'sha256', 'url', b'url', 'version', b'version']) -> None:
        ...
global___SubsystemUpdateInfo = SubsystemUpdateInfo