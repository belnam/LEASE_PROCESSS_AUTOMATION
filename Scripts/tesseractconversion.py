import pytesseract
from pdf2image import convert_from_path
from pypdf import PdfWriter, PdfReader
from io import BytesIO
import os

# Configure paths
SCANS_FOLDER = r"C:\Users\Peace.Muthusi\Documents\Projects\RENTALS-PROCESS-AUTOMATION\Downloaded_Scans - tesseract"
POPPLER_PATH = r"C:\poppler\poppler-24.08.0\Library\bin"
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def ocr_pdf(input_pdf):
    try:
        print(f"Processing: {os.path.basename(input_pdf)}")
        
        # Create temporary output path
        temp_output = os.path.join(
            os.path.dirname(input_pdf),
            f"temp_{os.path.basename(input_pdf)}"
        )

        # Convert PDF to images
        images = convert_from_path(
            input_pdf, 
            dpi=300, 
            poppler_path=POPPLER_PATH
        )

        # Create searchable PDF
        pdf_writer = PdfWriter()
        for image in images:
            pdf_bytes = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
            pdf_stream = BytesIO(pdf_bytes)
            pdf_reader = PdfReader(pdf_stream)
            pdf_writer.append(pdf_reader)

        # Write to temporary file
        with open(temp_output, "wb") as f:
            pdf_writer.write(f)

        # Replace original file
        os.remove(input_pdf)
        os.rename(temp_output, input_pdf)
        print(f"Successfully converted: {os.path.basename(input_pdf)}")

    except Exception as e:
        print(f"Error processing {os.path.basename(input_pdf)}: {str(e)}")

if __name__ == "__main__":
    # Verify scans folder exists
    if not os.path.exists(SCANS_FOLDER):
        raise FileNotFoundError(f"Scans folder not found: {SCANS_FOLDER}")

    # Process all PDF files in the scans folder
    for filename in os.listdir(SCANS_FOLDER):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(SCANS_FOLDER, filename)
            ocr_pdf(pdf_path)

    print("\nConversion complete! Check the scans folder for updated files.")