import json
import uuid


class MarkdownProcessor:
    @staticmethod
    def save_documents(docs: list, file_path: str, formatting=True):
        """
        ドキュメントをJSONファイルとして保存する。
        """
        if not docs:
            raise ValueError("ドキュメントがありません。")

        # Markdownチャンクを使った場合、アウトプットが異なるため、標準化する処理を入れる。
        if formatting:
            first = docs[0]
            if hasattr(first, "page_content"):
                # Type: from langchain_core.documents import Document
                docs_as_dicts = [{"id": str(uuid.uuid4()), "content": doc.page_content} for doc in docs]
            else:
                docs_as_dicts = [{"id": str(uuid.uuid4()), "content": doc} for doc in docs]
        else:
            raise TypeError(f"サポートされていないドキュメントタイプ: {type(first)}")

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(docs_as_dicts, f, ensure_ascii=False, indent=4)
