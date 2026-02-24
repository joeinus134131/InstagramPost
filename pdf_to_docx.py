import argparse
import sys
from pypdf import PdfReader
from docx import Document

def pdf_to_docx(pdf_path, docx_path):
    """
    Converts a PDF file to a DOCX file.
    """
    try:
        reader = PdfReader(pdf_path)
        doc = Document()

        num_pages = len(reader.pages)
        print(f"Processing {num_pages} pages from {pdf_path}...")

        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                doc.add_paragraph(text)

            # Add page break unless it's the last page
            if i < num_pages - 1:
                doc.add_page_break()

        doc.save(docx_path)
        print(f"Successfully converted to {docx_path}")
        return True

    except Exception as e:
        print(f"Error converting PDF: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Convert PDF to DOCX")
    parser.add_argument("-i", "--input", required=True, help="Input PDF file path")
    parser.add_argument("-o", "--output", required=True, help="Output DOCX file path")

    args = parser.parse_args()

    success = pdf_to_docx(args.input, args.output)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
