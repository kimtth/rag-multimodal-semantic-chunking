import os
import io
import json
import base64
from typing import Optional
from loguru import logger
from openai import AzureOpenAI
from azure.ai.documentintelligence.models import AnalyzeResult
from actor.markdown_processor import MarkdownProcessor


class ImageDescriptionProcessor:
    """Handles image description generation using Azure OpenAI Vision."""

    def __init__(self, aoai_client: AzureOpenAI, pdf_processor, output_dir: str):
        self.aoai_client = aoai_client
        self.pdf_processor = pdf_processor
        self.output_dir = output_dir
        self.md_processor = MarkdownProcessor()

    def process_figures(
        self, result: AnalyzeResult, input_file_path: str, file_name: str
    ) -> Optional[str]:
        """
        Process all figures in the document and generate descriptions.

        Args:
            result: Document Intelligence analysis result
            input_file_path: Path to the input PDF file
            file_name: Base filename for output files

        Returns:
            Updated markdown content with figure descriptions
        """
        # Check file extension
        file_extension = os.path.splitext(input_file_path)[1].lower()
        if file_extension not in [".pdf"]:
            logger.warning(f"Unsupported file extension: {file_extension}")
            return None

        logger.info("Processing figure descriptions...")

        descriptions_output = []
        md_content = getattr(result, "content", "")

        if not (hasattr(result, "figures") and result.figures):
            logger.info("No figures found in document")
            return md_content

        logger.info(f"Found {len(result.figures)} figures in document")

        for figure_idx, figure in enumerate(result.figures):
            try:
                logger.info(f"Processing Figure #{figure_idx + 1}")

                # Extract caption information
                caption_content, caption_polygons = self._extract_caption_info(figure)

                # Process bounding regions
                figure_data_list = self._process_figure_regions(
                    figure,
                    figure_idx,
                    input_file_path,
                    file_name,
                    caption_content,
                    caption_polygons,
                )

                descriptions_output.extend(figure_data_list)

                # Update markdown with descriptions
                for figure_data in figure_data_list:
                    md_content = self.md_processor.update_figure_description(
                        md_content, figure_data["description"], figure_idx + 1
                    )

            except Exception as e:
                logger.error(f"Error processing figure {figure_idx + 1}: {str(e)}")
                continue

        # Save outputs
        self._save_descriptions(descriptions_output, file_name)
        self._save_updated_markdown(md_content, file_name)

        logger.info(f"Processed {len(descriptions_output)} figure descriptions")
        return md_content

    def _extract_caption_info(self, figure) -> tuple[str, list]:
        """Extract caption content and polygons from figure."""
        caption_content = ""
        caption_polygons = []

        if hasattr(figure, "caption") and figure.caption:
            caption_content = figure.caption.get("content", "")
            if caption_content:
                logger.info(f"Caption: {caption_content}")

            caption_bounding_regions = figure.caption.get("boundingRegions", [])
            for caption_region in caption_bounding_regions:
                caption_polygons.append(caption_region.get("polygon", []))

        return caption_content, caption_polygons

    def _process_figure_regions(
        self,
        figure,
        figure_idx: int,
        input_file_path: str,
        file_name: str,
        caption_content: str,
        caption_polygons: list,
    ) -> list:
        """Process all regions of a figure."""
        figure_data_list = []
        bounding_regions = figure.get("boundingRegions", [])

        if not bounding_regions:
            logger.warning(f"No bounding regions found for figure {figure_idx + 1}")
            return figure_data_list

        for region_idx, region in enumerate(bounding_regions):
            polygon = region.get("polygon", [])

            # Skip caption regions and empty polygons
            if polygon in caption_polygons or not polygon:
                continue

            try:
                figure_data = self._process_single_region(
                    region,
                    figure_idx,
                    region_idx,
                    input_file_path,
                    file_name,
                    caption_content,
                    figure,
                )
                if figure_data:
                    figure_data_list.append(figure_data)

            except Exception as e:
                logger.error(f"Error processing region {region_idx}: {str(e)}")
                continue

        return figure_data_list

    def _process_single_region(
        self,
        region,
        figure_idx: int,
        region_idx: int,
        input_file_path: str,
        file_name: str,
        caption_content: str,
        figure,
    ) -> Optional[dict]:
        """Process a single figure region."""
        polygon = region.get("polygon", [])
        page_number = region.get("pageNumber", 1) - 1  # Convert to 0-indexed

        # Create bounding box
        bounding_box = (
            polygon[0],  # x0 (left)
            polygon[1],  # y0 (top)
            polygon[4],  # x1 (right)
            polygon[5],  # y1 (bottom)
        )

        # Crop image
        cropped_image = self.pdf_processor.crop_image_from_pdf_page(
            input_file_path, page_number, bounding_box
        )

        # Convert to base64
        buffered = io.BytesIO()
        cropped_image.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode()

        # Generate description
        description = self.generate_description(img_base64, caption_content)

        # Save cropped image
        image_filename = (
            f"{file_name}_figure_{figure_idx + 1}_region_{region_idx + 1}.png"
        )
        image_path = os.path.join(self.output_dir, image_filename)
        cropped_image.save(image_path)

        # Create figure data
        return {
            "figure_index": figure_idx + 1,
            "region_index": region_idx + 1,
            "page_number": page_number + 1,
            "image_path": image_path,
            "bounding_box": bounding_box,
            "polygon": polygon,
            "description": description,
            "caption": caption_content,
            "elements": (
                figure.get("elements", []) if hasattr(figure, "elements") else []
            ),
        }

    def generate_description(self, img_base64: str, caption: str = "") -> str:
        """Generate description for an image using Azure OpenAI Vision."""
        try:
            response = self.aoai_client.chat.completions.create(
                model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                # "text": "Analyze this figure/image from a document and provide a detailed description. Focus on key elements, any text or labels visible in the image.",
                                "text": (
                                    f"Describe this image (note: it has image caption: {caption}):"
                                    if caption
                                    else "Describe this image:"
                                ),
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{img_base64}"
                                },
                            },
                        ],
                    }
                ],
            )
            description = response.choices[0].message.content.strip()
            logger.info(f"Generated description: {description}")

            return description
        except Exception as e:
            logger.error(f"Error generating image description: {str(e)}")
            return ""

    def _save_descriptions(self, descriptions: list, file_name: str):
        """Save figure descriptions to JSON file."""
        descriptions_file = os.path.join(
            self.output_dir, f"{file_name}_figure_descriptions.json"
        )
        with open(descriptions_file, "w", encoding="utf-8") as f:
            json.dump(descriptions, f, indent=2, ensure_ascii=False)
        logger.info(f"Descriptions saved to {descriptions_file}")

    def _save_updated_markdown(self, md_content: str, file_name: str):
        """Save updated markdown with figure descriptions."""
        md_file = os.path.join(self.output_dir, f"{file_name}_updated.md")
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(md_content)
        logger.info(f"Updated markdown saved to {md_file}")
