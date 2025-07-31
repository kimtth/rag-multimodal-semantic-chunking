from langchain_core.documents import Document
from typing import List, Any
from abc import ABC, abstractmethod
from actor_basic.data_process_model import ChunkingType
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import MarkdownHeaderTextSplitter


class ContentChunker(ABC):
    """インターフェースを定義する"""

    def __init__(self, content: str):
        self.content = content

    @abstractmethod
    def chunk(self) -> List[Any]:
        """インターフェースのメソッド"""
        raise NotImplementedError("必ず実装する必要があります。")


class MarkdownContentChunker(ContentChunker):
    """
    セマンティックなマークダウンのコンテンツのチャンクを作成する。
    """

    def __init__(self, content: str = ""):
        super().__init__(content)
        self.headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]

    def chunk(self) -> List[Document]:
        # Markdown Splits
        markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=self.headers_to_split_on, strip_headers=False
        )
        md_header_splits = markdown_splitter.split_text(self.content)
        return md_header_splits


class RecursiveContentChunker(ContentChunker):
    """指定したサイズとオーバーラップでコンテンツをチャンクする"""

    def __init__(self, content: str = ""):
        super().__init__(content)

    def chunk(self) -> List[Document]:
        chunk_size = 200
        chunk_overlap = 50
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
        splits = text_splitter.split_text(self.content)
        return splits


class ContentChunkerFactory:
    """コンテンツチャンクのファクトリー"""

    @staticmethod
    def create(chunking_type: ChunkingType, content: str) -> ContentChunker:
        if chunking_type == ChunkingType.MARKDOWN_CHUNKING:
            return MarkdownContentChunker(content)
        elif chunking_type == ChunkingType.RECURSIVE_CHUNKING:
            return RecursiveContentChunker(content)
        else:
            raise ValueError(f"サポートされていないチャンクタイプ: {chunking_type}")
