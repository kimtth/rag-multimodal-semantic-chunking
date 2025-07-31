from enum import Enum


class ChunkingType(str, Enum):
    MARKDOWN_CHUNKING = "markdown_chunking"
    RECURSIVE_CHUNKING = "recursive_chunking"


