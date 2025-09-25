import os
import subprocess
import time
import logging

def get_input_files(input_folder):
    input_files = [file for file in os.listdir(input_folder) if file.endswith(".pdf")]
    return input_files

def convert_scanned_pdfs_to_searchable(input_folder):
    input_files = get_input_files(input_folder)

    for input_file in input_files:
        input_pdf_path = os.path.join(input_folder, input_file)
        
        try:
            # Run ocrmypdf as a subprocess to perform OCR and overwrite the original file
            subprocess.run(["ocrmypdf", input_pdf_path, input_pdf_path], check=True)
            logging.info(f"Conversion of {input_file} completed successfully!")
        except subprocess.CalledProcessError as e:
            logging.info(f"Error converting {input_file}: {e}")

# def convert_single_scanned_pdf_to_searchable(input_pdf_path):        
#     try:
#         # Run ocrmypdf as a subprocess to perform OCR and overwrite the original file
#         subprocess.run(["ocrmypdf", input_pdf_path, input_pdf_path], check=True)
#         logging.info(f"Conversion of {input_pdf_path} completed successfully!")
#     except subprocess.CalledProcessError as e:
#         logging.info(f"Error converting {input_pdf_path}: {e}")

# def get_input_folder():
    # return util.get_amazon_dir()
# input_folder = get_input_folder()
input_folder = f"Downloaded_Scans"
convert_scanned_pdfs_to_searchable(input_folder)

