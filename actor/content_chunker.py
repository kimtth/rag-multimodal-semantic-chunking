from langchain_core.documents import Document
from typing import List, Dict, Any
from abc import ABC, abstractmethod
from actor.data_process_model import ChunkingType


class ContentChunker(ABC):
    """Abstract base class for content chunkers."""

    def __init__(self, content: str):
        self.content = content

    @abstractmethod
    def chunk(self) -> List[Dict[str, Any]]:
        """Chunk the content and return list of chunks."""
        raise NotImplementedError("Subclasses must implement this method.")


class RecursiveContentChunker(ContentChunker):
    """Recursive text chunker."""

    def __init__(self, content: str = ""):
        super().__init__(content)

    def chunk(self) -> List[Document]:
        from langchain_text_splitters import RecursiveCharacterTextSplitter

        chunk_size = 250
        chunk_overlap = 30
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
        splits = text_splitter.split_text(self.content)
        return splits


class MarkdownContentChunker(ContentChunker):
    """
    Content-Aware Splitting for Markdown Documents
    """

    def __init__(self, content: str = ""):
        super().__init__(content)
        self.headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]

    def chunk(self) -> List[Document]:
        from langchain_text_splitters import MarkdownHeaderTextSplitter

        # Markdown Splits
        markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=self.headers_to_split_on, strip_headers=False
        )
        md_header_splits = markdown_splitter.split_text(self.content)
        return md_header_splits


class SemanticContentChunker(ContentChunker):
    def __init__(self, content: str = ""):
        super().__init__(content)

    def chunk(self) -> List[Document]:
        raise NotImplementedError("Not implemented yet.")


class ContentChunkerFactory:
    """Factory for creating content chunkers."""

    @staticmethod
    def create(chunking_type: ChunkingType, content: str) -> ContentChunker:
        """
        Create a content chunker based on the specified type.

        Args:
            chunking_type: Type of chunking to perform
            content: Content to chunk

        Returns:
            ContentChunker instance
        """
        if chunking_type == ChunkingType.MARKDOWN_CHUNKING:
            return MarkdownContentChunker(content)
        elif chunking_type == ChunkingType.RECURSIVE_CHUNKING:
            return RecursiveContentChunker(content)
        else:
            raise ValueError(f"Unsupported chunking type: {chunking_type}")

