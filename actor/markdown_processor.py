import os
import json
import uuid
from langchain_core.documents import Document
from typing import List


class MarkdownProcessor:
    """Handles markdown processing operations."""

    @staticmethod
    def update_figure_description(
        md_content: str, img_description: str, idx: int
    ) -> str:
        """
        Updates the idx-th <figure>…</figure> block in the Markdown with a comment containing the image description.
        """
        start_tag = "<figure>"
        end_tag = "</figure>"
        insert = f'{os.linesep}{os.linesep} #### FigureContent {os.linesep}{os.linesep} "{img_description}"'

        # Find the start of the idx-th <figure>
        pos = 0
        for _ in range(idx + 1):
            start = md_content.find(start_tag, pos)
            if start == -1:  # Return -1 on failure.
                return md_content
            pos = start + len(start_tag)

        # Find the corresponding </figure>
        end = md_content.find(end_tag, pos)
        if end == -1:
            return md_content

        # Inject the description comment immediately after the <figure> tag
        before = md_content[:pos]
        after = md_content[end:]
        return before + insert + after

    @staticmethod
    def save_documents(docs: list, file_path: str):
        """
        Save a list of Documents, raw strings, or dicts as a JSON file.
        """
        if not docs:
            raise ValueError("No documents to save")

        first = docs[0]
        # Documents → use model_dump()
        if isinstance(first, Document):
            docs_as_dicts = [doc.model_dump() for doc in docs]
        # Plain text → wrap with id & content
        elif isinstance(first, str):
            docs_as_dicts = [{"id": str(uuid.uuid4()), "content": doc} for doc in docs]
        # Already dicts → assume ready to dump
        elif isinstance(first, dict):
            docs_as_dicts = docs
        else:
            raise TypeError(f"Unsupported document type: {type(first)}")

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(docs_as_dicts, f, ensure_ascii=False, indent=4)
