import os
import ocrmypdf

SCANS_FOLDER = r"C:\Users\Peace.Muthusi\Documents\Projects\RENTALS-PROCESS-AUTOMATION\Downloaded_Scans"
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

os.environ["PATH"] += os.pathsep + os.path.dirname(TESSERACT_PATH)

def ocr_all_pdfs():
    try:
        print("Starting OCR processing...")

        if not os.path.exists(SCANS_FOLDER):
            raise FileNotFoundError(f"Scans folder not found: {SCANS_FOLDER}")

        for filename in os.listdir(SCANS_FOLDER):
            if not filename.lower().endswith('.pdf'):
                continue

            input_pdf = os.path.join(SCANS_FOLDER, filename)
            temp_output = os.path.join(SCANS_FOLDER, f"temp_{filename}")

            try:
                print(f"Processing: {filename}")
                ocrmypdf.ocr(
                    input_pdf,
                    temp_output,
                    language="eng",
                    deskew=True,
                    rotate_pages=True,
                    optimize=0,                       
                    # skip_text=True,
                    force_ocr=False,
                    output_type="pdfa",
                    pdf_renderer="hocr",             
                    image_dpi=400,                  
                    oversample=600,                  
                    jpeg_quality=95,                 
                    pdfa_image_compression="lossless",  
                    keep_temporary_files=False,
                    jbig2_lossy=False,
                    color_conversion_strategy='LeaveColorUnchanged',
                )

                os.remove(input_pdf)
                os.rename(temp_output, input_pdf)
                print(f"Successfully converted: {filename}")

            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
                if os.path.exists(temp_output):
                    os.remove(temp_output)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
print("\nConversion complete! Check the scans folder for updated files.")

ocr_all_pdfs()
    