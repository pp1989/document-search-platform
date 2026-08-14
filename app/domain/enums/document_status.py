from enum import Enum


class DocumentStatus(str, Enum):
    """
    Represents the lifecycle state of a document.
    """

    UPLOADED = "UPLOADED"

    PROCESSING = "PROCESSING"

    CHUNKED = "CHUNKED"

    EMBEDDED = "EMBEDDED"

    INDEXED = "INDEXED"

    FAILED = "FAILED"
