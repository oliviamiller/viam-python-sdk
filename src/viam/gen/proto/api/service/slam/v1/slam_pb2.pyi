"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
from ...... import proto
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetPositionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of slam service'

    def __init__(self, *, name: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetPositionRequest = GetPositionRequest

class GetPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POSE_FIELD_NUMBER: builtins.int

    @property
    def pose(self) -> proto.api.common.v1.common_pb2.PoseInFrame:
        """Current position of the robot within the World frame."""
        pass

    def __init__(self, *, pose: typing.Optional[proto.api.common.v1.common_pb2.PoseInFrame]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> None:
        ...
global___GetPositionResponse = GetPositionResponse

class GetMapRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    CAMERA_POSITION_FIELD_NUMBER: builtins.int
    INCLUDE_ROBOT_MARKER_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of slam service'
    mime_type: typing.Text
    'Requested MIME type of response (image/jpeg or image/pcd)'

    @property
    def camera_position(self) -> proto.api.common.v1.common_pb2.Pose:
        """Optional parameter for image/jpeg mime_type, used to project point
        cloud into a 2D image.
        """
        pass
    include_robot_marker: builtins.bool
    'Optional parameter for image/jpeg mime_type, defaults to false.\n    Tells us whether to include the robot position on the 2D image.\n    '

    def __init__(self, *, name: typing.Text=..., mime_type: typing.Text=..., camera_position: typing.Optional[proto.api.common.v1.common_pb2.Pose]=..., include_robot_marker: builtins.bool=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['camera_position', b'camera_position']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['camera_position', b'camera_position', 'include_robot_marker', b'include_robot_marker', 'mime_type', b'mime_type', 'name', b'name']) -> None:
        ...
global___GetMapRequest = GetMapRequest

class GetMapResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POINT_CLOUD_FIELD_NUMBER: builtins.int
    IMAGE_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int

    @property
    def point_cloud(self) -> proto.api.common.v1.common_pb2.PointCloudObject:
        ...
    image: builtins.bytes
    mime_type: typing.Text
    'Actual MIME type of response (image/jpeg or image/pcd)'

    def __init__(self, *, point_cloud: typing.Optional[proto.api.common.v1.common_pb2.PointCloudObject]=..., image: builtins.bytes=..., mime_type: typing.Text=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['image', b'image', 'map', b'map', 'point_cloud', b'point_cloud']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['image', b'image', 'map', b'map', 'mime_type', b'mime_type', 'point_cloud', b'point_cloud']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['map', b'map']) -> typing.Optional[typing_extensions.Literal['point_cloud', 'image']]:
        ...
global___GetMapResponse = GetMapResponse