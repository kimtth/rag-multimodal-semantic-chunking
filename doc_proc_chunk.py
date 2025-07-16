from langchain_core.documents import Document
from typing import List
from doc_proc_md import save_documents


class BaseChunker:
    def __init__(self, content: str = ""):
        self.content = content

    def chunk(self) -> List[Document]:
        raise NotImplementedError("This method should be overridden by subclasses.")


class RecursiveContentChunker(BaseChunker):
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


class MarkdownContentChunker(BaseChunker):
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


class SemanticContentChunker(BaseChunker):
    def __init__(self, content: str = ""):
        super().__init__(content)

    def chunk(self) -> List[Document]:
        raise NotImplementedError("Under construction, not implemented yet.")
    

if __name__ == "__main__":
    # Example usage
    import os
    input_file_path = os.path.join("output", "contoso_updated.md")

    with open(input_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    chunker = MarkdownContentChunker(content=content)
    chunks = chunker.chunk()

    output_dir_base = "output"
    file_path = os.path.join(output_dir_base, "chunks_contents.json")
    save_documents(chunks, file_path)

    chunker = RecursiveContentChunker(content=content)
    chunks = chunker.chunk()

    file_path = os.path.join(output_dir_base, "chunks_recursive.json")
    save_documents(chunks, file_path)
