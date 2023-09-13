from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Plane(_message.Message):
    __slots__ = ["id", "name", "x", "y", "z"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    x: int
    y: int
    z: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., z: _Optional[int] = ...) -> None: ...

class PlaneNoId(_message.Message):
    __slots__ = ["name", "x", "y", "z"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    name: str
    x: int
    y: int
    z: int
    def __init__(self, name: _Optional[str] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., z: _Optional[int] = ...) -> None: ...

class Planes(_message.Message):
    __slots__ = ["planes"]
    PLANES_FIELD_NUMBER: _ClassVar[int]
    planes: _containers.RepeatedCompositeFieldContainer[Plane]
    def __init__(self, planes: _Optional[_Iterable[_Union[Plane, _Mapping]]] = ...) -> None: ...

class GetPlanesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPlanesStreamRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
