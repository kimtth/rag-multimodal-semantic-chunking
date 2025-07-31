import os
import xlsxwriter
from loguru import logger
from azure.ai.documentintelligence.models import AnalyzeResult


class TableProcessor:
    """Handles table processing and Excel export."""

    def __init__(self, output_dir: str):
        self.output_dir = output_dir

    def export_to_excel(self, result: AnalyzeResult, file_name: str):
        """
        Export tables from analysis result to Excel file.

        Args:
            result: Document Intelligence analysis result
            file_name: Base filename for the Excel output
        """
        if not hasattr(result, "tables") or not result.tables:
            logger.warning("No tables found in the document.")
            return

        excel_output_file_name = f"{file_name}_tables.xlsx"
        excel_path = os.path.join(self.output_dir, excel_output_file_name)

        workbook = xlsxwriter.Workbook(excel_path)

        try:
            for table_idx, table in enumerate(result.tables):
                self._process_table(workbook, table, table_idx, file_name)

            logger.info(f"Excel file created: {excel_path}")

        finally:
            workbook.close()

    def _process_table(self, workbook, table, table_idx: int, file_name: str):
        """Process a single table and add it to the workbook."""
        worksheet = workbook.add_worksheet(name=f"{file_name}_{table_idx + 1}")

        logger.info(
            f"Table #{table_idx} has {table.row_count} rows and {table.column_count} columns"
        )

        for cell in table.cells:
            cell_content = self._clean_cell_content(cell.content)
            worksheet.write(cell.row_index, cell.column_index, cell_content)

    def _clean_cell_content(self, content: str) -> str:
        """Clean cell content by removing unwanted characters."""
        content = str(content).replace(":unselected:", "")
        content = content.replace(":selected:", "")
        return content.strip()
