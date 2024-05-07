from typing import runtime_checkable, Protocol


@runtime_checkable
class ByteStream(Protocol):
    """A file-like object with a read method that returns bytes."""

    def read(self, size: int = -1) -> bytes: ...


@runtime_checkable
class AsyncByteStream(Protocol):
    """A file-like object with an async read method."""

    async def read(self, size: int = -1) -> bytes: ...