import os
import json
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from actor_basic.content_chunker import ContentChunkerFactory
from actor_basic.data_process_model import ChunkingType
from actor_basic.markdown_processor import MarkdownProcessor

load_dotenv()


def doc_intelli_main():
    endpoint = os.getenv("DOC_INTELLIGENCE_ENDPOINT")
    api_key = os.getenv("DOC_INTELLIGENCE_API_KEY")
    input_file = "data/contoso-p.pdf"
    output_dir = "output_basic"
    os.makedirs(output_dir, exist_ok=True)

    # 1. Document Intelligenceクライエントを初期化する
    client = DocumentIntelligenceClient(
        endpoint, credential=AzureKeyCredential(api_key)
    )
    with open(input_file, "rb") as f:
        poller = client.begin_analyze_document(
            "prebuilt-layout",
            body=f,
            content_type="application/pdf",
            output_content_format="markdown",
        )
        result = poller.result()
    content = getattr(result, "content", "")

    # 2. コンテンツをチャンクする
    # Markdownチャンクによるチャンク
    chunker_md = ContentChunkerFactory.create(ChunkingType.MARKDOWN_CHUNKING, content)
    docs_md = chunker_md.chunk()

    # Recursiveチャンクによるチャンク
    chunker_rc = ContentChunkerFactory.create(ChunkingType.RECURSIVE_CHUNKING, content)
    docs_rc = chunker_rc.chunk()

    # 3. チャンクされた結果をJSONに保存する
    MarkdownProcessor.save_documents(docs_md, os.path.join(output_dir, "docs_md.json"))
    MarkdownProcessor.save_documents(docs_rc, os.path.join(output_dir, "docs_rc.json"))

    output_file_path = os.path.join(output_dir, f"content_output.json")
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(result.as_dict(), f, indent=4)


def local_result_main():
    # テスト用の関数：ローカルに保存したDocument Intelligenceの結果を使う
    input_file = "output_basic/content_output.json"
    output_dir = "output_basic"
    with open(input_file, "r") as f:
        result_json = f.read()
        content = json.loads(result_json).get("content", "")
    chunker = ContentChunkerFactory.create(ChunkingType.RECURSIVE_CHUNKING, content)
    docs_rc = chunker.chunk()
    MarkdownProcessor.save_documents(docs_rc, os.path.join(output_dir, "docs_rc_normalized.json"))
    
    chunker = ContentChunkerFactory.create(ChunkingType.MARKDOWN_CHUNKING, content)
    docs_md = chunker.chunk()
    MarkdownProcessor.save_documents(docs_md, os.path.join(output_dir, "docs_md_normalized.json"))


if __name__ == "__main__":
    doc_intelli_main()
    # local_result_main()
