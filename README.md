# 📄 Multi-modal Preprocessing for Search Indexing with Azure Document Intelligence

## ✨ Features

1. 🖼️ Extract figures from documents and save them as PNG images.
2. 🤖 Generate figure descriptions using Azure OpenAI Multimodal.
3. 📝 Update markdown outputs with generated descriptions.
4. 📊 Extract tables and convert them into Excel files.
5. 📖 Text Chunking to markdown ouputs using `MarkdownHeaderTextSplitter`, `RecursiveContentChunker`, and `SemanticContentChunker (TBD)`

## 🚀 Usage

```
python doc_intelli.py
```

## 📚 Learn More

- [📘 Document Intelligence Official Samples](https://github.com/Azure-Samples/document-intelligence-code-samples): Python (v4.0) / RAG samples / Figure understanding.
- [Build Intelligent RAG for Multimodality and Complex Document Structures](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/build-intelligent-rag-for-multimodality-and-complex-document-structure/4118184)
- [nohanaga: Document Intelligence Samples](https://github.com/nohanaga/document-intelligence-samples) | [🔗 Output](https://qiita.com/nohanaga/items/1263f4a6bc909b6524c8): Article in Japanese
- [📖 7 Chunking Strategies for Langchain](https://medium.com/@anixlynch/7-chunking-strategies-for-langchain-b50dac194813#6da7)
- [MarkdownHeaderTextSplitter](https://python.langchain.com/docs/how_to/markdown_header_metadata_splitter/)
- [⚡ Azure Functions vs. Indexers: AI Data Ingestion](https://devblogs.microsoft.com/ise/unlock-ai-search-potential-the-case-for-azure-functions-in-data-ingestion/)
- [RAG Time: Mastering RAG](https://github.com/microsoft/rag-time)