from langchain_core.documents import Document
from typing import List
import os
import json
import uuid


def update_figure_description(md_content: str, img_description: str, idx: int) -> str:
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
        if start == -1:
            return md_content  # not enough figures
        pos = start + len(start_tag)

    # Find the corresponding </figure>
    end = md_content.find(end_tag, pos)
    if end == -1:
        return md_content

    # Inject the description comment immediately after the <figure> tag
    before = md_content[:pos]
    after = md_content[end:]
    return before + insert + after


def save_documents_with_as_dict(docs: List[Document], file_path: str):
    # Convert all documents to dicts using the built-in method
    docs_as_dicts = [doc.model_dump() for doc in docs]

    # Save to JSON file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(docs_as_dicts, f, ensure_ascii=False, indent=4)


def save_documents_with_texts(docs: List[str], file_path: str):
    docs_as_dicts = [{"id": str(uuid.uuid4()), "content": doc} for doc in docs]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(docs_as_dicts, f, ensure_ascii=False, indent=4)


def save_documents(docs: List, file_path: str):
    # Type check to items in List
    if all(isinstance(doc, Document) for doc in docs):
        save_documents_with_as_dict(docs, file_path)
    if all(isinstance(doc, str) for doc in docs):
        save_documents_with_texts(docs, file_path)
