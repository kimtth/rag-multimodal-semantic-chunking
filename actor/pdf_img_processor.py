import fitz
from PIL import Image
from typing import Tuple


class PDFImageProcessor:
    """
    A class to process images from PDF files.
    """

    def crop_image_from_pdf_page(
        self,
        pdf_path: str,
        page_number: int,
        bounding_box: Tuple[float, float, float, float],
    ) -> Image.Image:
        """
        Crop an image from a specific PDF page using bounding box coordinates.

        Args:
            pdf_path: Path to the PDF file
            page_number: Page number (0-indexed)
            bounding_box: Tuple of (x0, y0, x1, y1) coordinates

        Returns:
            PIL Image of the cropped region
        """
        doc = fitz.open(pdf_path)
        page = doc.load_page(page_number)

        # Cropping the page. The rect requires the coordinates in the format (x0, y0, x1, y1).
        bbx = [x * 72 for x in bounding_box]
        rect = fitz.Rect(bbx)
        pix = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72), clip=rect)

        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        doc.close()

        return img
