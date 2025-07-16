import os
import io
import json
import base64
import timeit
import xlsxwriter
from typing import Optional
from dotenv import load_dotenv
from loguru import logger
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult

# Importing utility functions for post-processing
from doc_model import AnalyzeOptions, AnalyzeType, ChunkingType
from doc_proc_aoai import img_desc_from_azure_openai
from doc_proc_chunk import MarkdownContentChunker, RecursiveContentChunker
from doc_proc_img import crop_image_from_pdf_page
from doc_proc_md import save_documents, update_figure_description

load_dotenv()

DOC_INTELLIGENCE_ENDPOINT = os.getenv("DOC_INTELLIGENCE_ENDPOINT")
DOC_INTELLIGENCE_API_KEY = os.getenv("DOC_INTELLIGENCE_API_KEY")
# Initialize Azure OpenAI client for vision analysis
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

input_dir_base = "data"
output_dir_base = "output"


def analyze_general_documents(
    input_file_location: str,
    analyze_type: AnalyzeType,
    output_content_format: Optional[str] = "markdown",
) -> AnalyzeResult:
    """
    Analyze a general document using Azure Document Intelligence.

    :param image_file_path: Path to the image file to be analyzed.
    """
    # Create a client
    document_intelligence_client = DocumentIntelligenceClient(
        endpoint=DOC_INTELLIGENCE_ENDPOINT,
        credential=AzureKeyCredential(DOC_INTELLIGENCE_API_KEY),
    )
    with open(input_file_location, "rb") as f:
        poller = document_intelligence_client.begin_analyze_document(
            "prebuilt-layout",
            body=f,
            content_type="application/octet-stream",
            output_content_format=(
                "markdown" if output_content_format == "markdown" else "text"
            ),
        )
    result = poller.result()

    # Invoke post-processing based on the options provided
    options = AnalyzeOptions()
    options.result = result
    options.input_file_location = input_file_location
    options.analyze_type = analyze_type

    md_content = result.content if hasattr(result, "content") else ""
    with open(
        os.path.join(output_dir_base, f"{options.file_name}_raw.md"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(md_content)

    analyze_general_documents_post_processing(options)

    return result


def analyze_general_documents_post_processing(options: AnalyzeOptions):
    """
    Post-process the analysis result based on the options provided.

    :param options: AnalyzeOptions containing the result and other settings.
    """
    if options.result is None:
        raise ValueError("No analysis result to process.")

    if len(options.analyze_type) == 0:
        raise ValueError("No analyze type specified in options.")

    analyze_type_list = options.analyze_type
    chunking_type = options.chunking_type

    for analyze_type in analyze_type_list:
        if analyze_type == AnalyzeType.IMG_DESCRIPTION:
            # Process image description analysis
            logger.info("Processing image description analysis...")
            markdown_content = analyze_general_documents_to_image_description(
                options.result, options.input_file_location, options.file_name
            )

            # Process content chunking based on the specified type
            logger.info("Processing content chunking...")
            if chunking_type == ChunkingType.MARKDOWN_CHUNKING:
                chunker = MarkdownContentChunker(content=markdown_content)
            elif chunking_type == ChunkingType.RECURSIVE_CHUNKING:
                chunker = RecursiveContentChunker(content=markdown_content)
            else:
                raise ValueError("Unsupported chunking type specified.")

            chunks = chunker.chunk()
            # Save the chunks to a file
            chunk_file_path = os.path.join(
                output_dir_base, f"{options.file_name}_chunks.json"
            )
            save_documents(chunks, chunk_file_path)

            logger.info(f"Chunks saved to {chunk_file_path}")
            logger.info(f"Generated {len(chunks)} chunks from the document.")
        elif analyze_type == AnalyzeType.TABLE_PARSE:
            logger.info("Processing table parsing analysis...")
            # Invoke table parsing analysis
            analyze_general_documents_table_data_to_excel(
                options.result, options.file_name
            )
        else:
            logger.warning(f"Unknown analyze type: {analyze_type}")


def analyze_general_documents_to_image_description(
    result: AnalyzeResult, input_file_location: str, file_name: str
):
    # check file extension
    file_extension = os.path.splitext(input_file_location)[1].lower()
    if file_extension not in [".pdf"]:
        logger.warning(f"Unsupported file extension: {file_extension}")
        return

    logger.info("Analyzing image description...")
    client = AzureOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
    )

    descriptions_output = []
    md_content = result.content if hasattr(result, "content") else ""

    # Check if figures exist at result level
    if hasattr(result, "figures") and result.figures:
        logger.info(f"Found {len(result.figures)} figures in document")

        for figure_idx, figure in enumerate(result.figures):
            try:
                logger.info(f"--------Analysis of Figure #{figure_idx + 1}--------")

                # Extract caption information
                caption_content = ""
                caption_polygons = []

                if hasattr(figure, "caption") and figure.caption:
                    caption_content = figure.caption.get("content", "")
                    if caption_content:
                        logger.info(f"Caption: {caption_content}")

                    # Get caption bounding regions to exclude from figure regions
                    caption_bounding_regions = figure.caption.get("boundingRegions", [])
                    for caption_region in caption_bounding_regions:
                        caption_polygons.append(caption_region.get("polygon", []))

                # Process bounding regions (excluding caption regions)
                bounding_regions = figure.get("boundingRegions", [])
                if not bounding_regions:
                    logger.warning(
                        f"No bounding regions found for figure {figure_idx + 1}"
                    )
                    continue

                for region_idx, region in enumerate(bounding_regions):
                    polygon = region.get("polygon", [])
                    page_number = (
                        region.get("pageNumber", 1) - 1
                    )  # Convert to 0-indexed

                    # Skip if this polygon matches a caption polygon
                    if polygon in caption_polygons:
                        logger.info(
                            f"Skipping caption region for figure {figure_idx + 1}"
                        )
                        continue

                    if not polygon:
                        logger.warning(
                            f"Empty polygon for figure {figure_idx + 1}, region {region_idx}"
                        )
                        continue

                    # To learn more about bounding regions, see https://aka.ms/bounding-region
                    bounding_box = (
                        region.polygon[0],  # x0 (left)
                        region.polygon[1],  # y0 (top)
                        region.polygon[4],  # x1 (right)
                        region.polygon[5],  # y1 (bottom)
                    )

                    # Crop the figure from the PDF page
                    cropped_image = crop_image_from_pdf_page(
                        input_file_location, page_number, bounding_box
                    )

                    # Convert image to base64 for Azure OpenAI
                    buffered = io.BytesIO()
                    cropped_image.save(buffered, format="PNG")
                    img_base64 = base64.b64encode(buffered.getvalue()).decode()

                    # Generate description using Azure OpenAI Vision
                    description = img_desc_from_azure_openai(client, img_base64)

                    # Save the cropped image
                    image_filename = f"{file_name}_figure_{figure_idx + 1}_region_{region_idx + 1}.png"
                    image_path = os.path.join(output_dir_base, image_filename)
                    cropped_image.save(image_path)

                    # Store description data
                    figure_data = {
                        "figure_index": figure_idx + 1,
                        "region_index": region_idx + 1,
                        "page_number": page_number
                        + 1,  # Convert back to 1-indexed for output
                        "image_path": image_path,
                        "bounding_box": bounding_box,
                        "polygon": polygon,
                        "description": description,
                        "caption": caption_content,
                        "elements": (
                            figure.get("elements", [])
                            if hasattr(figure, "elements")
                            else []
                        ),
                    }
                    descriptions_output.append(figure_data)

                    logger.info(
                        f"Generated description for figure {figure_idx + 1}, region {region_idx + 1}"
                    )

                    # Update markdown file with figure descriptions
                    figure_idx = figure_idx + 1
                    md_content = update_figure_description(
                        md_content, description, figure_idx
                    )

            except Exception as e:
                logger.error(f"Error processing figure {figure_idx + 1}: {str(e)}")
                continue
    else:
        logger.info("No figures found in document")

    # Save descriptions to JSON file
    descriptions_file = os.path.join(
        output_dir_base, f"{file_name}_figure_descriptions.json"
    )
    with open(descriptions_file, "w", encoding="utf-8") as f:
        json.dump(descriptions_output, f, indent=2, ensure_ascii=False)

    # Save the updated Markdown content to a file
    with open(
        os.path.join(output_dir_base, f"{file_name}_updated.md"), "w", encoding="utf-8"
    ) as f:
        f.write(md_content)

    logger.info(
        f"Saved {len(descriptions_output)} figure descriptions to {descriptions_file}"
    )

    return md_content


def analyze_general_documents_table_data_to_excel(
    result: AnalyzeResult, file_name: str
):
    # replace the file extension with .xlsx
    output_dir_path = "output"
    # create the output file name with .xlsx extension
    excel_output_file_name = f"{file_name}_tables.xlsx"

    if not hasattr(result, "tables"):
        logger.warning("No tables found in the document.")
        return

    workbook = xlsxwriter.Workbook(
        os.path.join(output_dir_path, excel_output_file_name)
    )

    for table_idx, table in enumerate(result.tables):
        adj_row_idx = 0
        adj_col_idx = 0
        tbl_worksheet = workbook.add_worksheet(name=f"{file_name}_{table_idx + 1}")

        logger.info(
            "Table # {} has {} rows and {} columns".format(
                table_idx, table.row_count, table.column_count
            )
        )

        cell_content = ""
        for cell in table.cells:
            cell_content = cell.content
            cell_content = str(cell_content).replace(":unselected:", "")
            cell_content = str(cell_content).replace(":selected:", "")
            cell_content = cell_content.strip()

            row_idx = adj_row_idx + cell.row_index

            if cell.column_index > adj_col_idx:
                adj_col_idx = cell.column_index

            tbl_worksheet.write(row_idx, cell.column_index, cell_content)

        adj_row_idx = adj_row_idx + table.row_count + 1

    logger.info(
        os.path.join(output_dir_path, excel_output_file_name),
        ": Excel has been created.",
    )
    workbook.close()


if __name__ == "__main__":
    # Measure the time taken for the analysis
    logger.info("Starting document analysis...")
    timeit_start = timeit.default_timer()

    input_dir_base = "data"
    input_sample_file = "contoso.pdf"
    input_file_path = os.path.join(input_dir_base, input_sample_file)

    output_dir_base = "output"
    os.makedirs(output_dir_base, exist_ok=True)
    file_name = os.path.splitext(os.path.basename(input_file_path))[0]

    output_file_name = f"{file_name}_output.json"
    output_file_path = os.path.join(output_dir_base, output_file_name)

    result = analyze_general_documents(
        input_file_path,
        analyze_type=[AnalyzeType.TABLE_PARSE, AnalyzeType.IMG_DESCRIPTION],
    )

    timeit_end = timeit.default_timer()
    logger.info(
        f"Finished processing {input_file_path} in {timeit_end - timeit_start:.2f} seconds."
    )

    json_string = json.dumps(result.as_dict(), indent=4)
    # Save result as json to file
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(json_string)
    logger.info(f"Result saved to {output_file_path}")
