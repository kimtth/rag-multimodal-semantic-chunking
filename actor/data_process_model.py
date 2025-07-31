from dataclasses import dataclass, field
from enum import Enum
from azure.ai.documentintelligence.models import AnalyzeResult


class AnalyzeType(str, Enum):
    TABLE_PARSE = "table_parse"
    IMG_DESCRIPTION = "img_description"


class ChunkingType(str, Enum):
    MARKDOWN_CHUNKING = "markdown_chunking"
    RECURSIVE_CHUNKING = "recursive_chunking"


@dataclass
class AnalyzeOptions:
    input_file_location: str = ""
    file_name: str = ""
    analyze_type: list[AnalyzeType] = field(default_factory=list)
    chunking_type: ChunkingType = ChunkingType.MARKDOWN_CHUNKING
    output_content_format: str = "markdown"
    result: AnalyzeResult | None = None
