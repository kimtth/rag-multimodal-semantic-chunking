import os
import json
import timeit
from dotenv import load_dotenv
from loguru import logger
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult

from actor.data_process_model import AnalyzeOptions, AnalyzeType, ChunkingType
from actor.aoai_img_desc_processor import ImageDescriptionProcessor
from actor.content_chunker import ContentChunkerFactory
from actor.pdf_img_processor import PDFImageProcessor
from actor.markdown_processor import MarkdownProcessor
from actor.table_processor import TableProcessor

load_dotenv()


class DocumentAnalyzer:
    """Main class for analyzing documents using Azure Document Intelligence."""

    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        self._ensure_output_dir()

        # Initialize Azure clients
        self.doc_client = self._create_document_client()
        self.aoai_client = self._create_aoai_client()

        # Initialize processors
        self.pdf_processor = PDFImageProcessor()
        self.image_processor = ImageDescriptionProcessor(
            self.aoai_client, self.pdf_processor, self.output_dir
        )
        self.md_processor = MarkdownProcessor()

    def _create_document_client(self) -> DocumentIntelligenceClient:
        """Create Azure Document Intelligence client."""
        return DocumentIntelligenceClient(
            endpoint=os.getenv("DOC_INTELLIGENCE_ENDPOINT"),
            credential=AzureKeyCredential(os.getenv("DOC_INTELLIGENCE_API_KEY")),
        )

    def _create_aoai_client(self) -> AzureOpenAI:
        """Create Azure OpenAI client."""
        return AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        )

    def _ensure_output_dir(self):
        """Ensure output directory exists."""
        os.makedirs(self.output_dir, exist_ok=True)

    def analyze(self, options: AnalyzeOptions) -> AnalyzeResult:
        """
        Analyze a document based on the provided options.

        Args:
            options: Analysis configuration options

        Returns:
            AnalyzeResult from Azure Document Intelligence
        """
        logger.info(f"Starting analysis of {options.input_file_location}")

        # Run document analysis
        result = self._run_document_analysis(options)
        options.result = result

        # Save raw markdown
        self._save_raw_markdown(result, options.file_name)

        # Run post-processing
        self._post_process(options)

        return result

    def _run_document_analysis(self, options: AnalyzeOptions) -> AnalyzeResult:
        """Run the actual document analysis."""
        with open(options.input_file_location, "rb") as f:
            poller = self.doc_client.begin_analyze_document(
                "prebuilt-layout",
                body=f,
                content_type="application/octet-stream",
                output_content_format=options.output_content_format,
            )
        return poller.result()

    def _save_raw_markdown(self, result: AnalyzeResult, file_name: str):
        """Save the raw markdown content."""
        md_content = getattr(result, "content", "")
        raw_path = os.path.join(self.output_dir, f"{file_name}_raw.md")

        with open(raw_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        logger.info(f"Raw markdown saved to {raw_path}")

    def _post_process(self, options: AnalyzeOptions):
        """Run post-processing based on analysis types."""
        if not options.result:
            raise ValueError("No analysis result to process.")

        if not options.analyze_type:
            raise ValueError("No analyze type specified in options.")

        for analyze_type in options.analyze_type:
            if analyze_type == AnalyzeType.IMG_DESCRIPTION:
                self._process_image_descriptions(options)
            elif analyze_type == AnalyzeType.TABLE_PARSE:
                self._process_tables(options)
            else:
                logger.warning(f"Unknown analyze type: {analyze_type}")

    def _process_image_descriptions(self, options: AnalyzeOptions):
        """Process image descriptions and chunking."""
        logger.info("Processing image description analysis...")

        # Generate image descriptions
        markdown_content = self.image_processor.process_figures(
            options.result, options.input_file_location, options.file_name
        )

        if not markdown_content:
            logger.warning("No markdown content generated from image processing")
            return

        # Process content chunking
        logger.info("Processing content chunking...")
        chunker = ContentChunkerFactory.create(options.chunking_type, markdown_content)
        chunks = chunker.chunk()

        # Save chunks
        chunk_file_path = os.path.join(
            self.output_dir, f"{options.file_name}_chunks.json"
        )
        self.md_processor.save_documents(chunks, chunk_file_path)

        logger.info(f"Generated {len(chunks)} chunks saved to {chunk_file_path}")

    def _process_tables(self, options: AnalyzeOptions):
        """Process table parsing to Excel."""
        logger.info("Processing table parsing analysis...")

        if not hasattr(options.result, "tables") or not options.result.tables:
            logger.warning("No tables found in the document.")
            return

        table_processor = TableProcessor(self.output_dir)
        table_processor.export_to_excel(options.result, options.file_name)


def run_workflow():
    """Main execution function."""
    logger.info("Starting document analysis...")
    start_time = timeit.default_timer()

    # Setup
    input_dir_base = "data"
    input_sample_file = "contoso.pdf"
    input_file_path = os.path.join(input_dir_base, input_sample_file)
    output_dir_base = "output"
    file_name = os.path.splitext(os.path.basename(input_file_path))[0]

    # Create analyzer and options
    analyzer = DocumentAnalyzer(output_dir_base)
    options = AnalyzeOptions(
        input_file_location=input_file_path,
        file_name=file_name,
        analyze_type=[AnalyzeType.TABLE_PARSE, AnalyzeType.IMG_DESCRIPTION],
        chunking_type=ChunkingType.MARKDOWN_CHUNKING,
    )

    # Run analysis
    result = analyzer.analyze(options)

    # Save result
    output_file_path = os.path.join(output_dir_base, f"{file_name}_output.json")
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(result.as_dict(), f, indent=4)

    end_time = timeit.default_timer()
    logger.info(f"Analysis completed in {end_time - start_time:.2f} seconds")
    logger.info(f"Result saved to {output_file_path}")


if __name__ == "__main__":
    run_workflow()
