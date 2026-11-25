from pathlib import Path
import os

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

WD = Path("api")
os.chdir(WD)
print(os.getcwd())

docs = WD / "sample-data"
 
pipeline_options = PdfPipelineOptions(
    do_ocr=True,                  # OCR scanned regions
    do_table_structure=True,      # Detect table structure
    generate_page_images=False,   # Keep page raster images
)
 
converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
    }
)
   
if __name__ == '__main__':
    source = docs / "02_structure_fr.pdf"
    result = converter.convert(source)
    
    print(result)