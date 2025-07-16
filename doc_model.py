from enum import Enum
import os
from typing import Optional, List
from azure.ai.documentintelligence.models import AnalyzeResult


class ChunkingType(Enum):
    MARKDOWN_CHUNKING: int = 1
    RECURSIVE_CHUNKING: int = 2
    SEMANTIC_CHUNKING: int = 3


class AnalyzeType(Enum):
    TABLE_PARSE: int = 1
    IMG_DESCRIPTION: int = 2


class AnalyzeOptions:
    def __init__(self):
        self.result: AnalyzeResult = None
        self.input_file_location: str = ""
        self.analyze_type: List[AnalyzeType] = []
        self.chunking_type: ChunkingType = ChunkingType.MARKDOWN_CHUNKING
    
    @property
    def file_name(self) -> str:
        # file_name will be updated based on the input_file_location
        return os.path.splitext(os.path.basename(self.input_file_location))[0] if self.input_file_location else ""