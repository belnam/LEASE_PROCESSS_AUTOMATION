import os
import shutil
import pdfplumber
import getpass

# Set the path to the directory containing the PDF files
username = getpass.getuser()
pdf_directory = f'Downloaded_Scans\\'
citations_folder = f'Citations\\'

for filename in os.listdir(pdf_directory):
    # Construct the path to the file
    file_path = os.path.join(pdf_directory, filename)
    if file_path.endswith('.pdf'):
        # Open the PDF file
        with pdfplumber.open(file_path) as pdf:
            # Check if the PDF file has at least two pages
            # if len(pdf.pages) < 2:
            # Check if the PDF file has at least 2 pages but no more than 3 pages
            # if 2 < len(pdf.pages) < 3:
            if 2 < len(pdf.pages) < 2:
                continue
            for i in range(2):
                try:
                    text = pdf.pages[i].extract_text()
                except:
                    pass
                identifiers = [
                        "citation n",
                        "N N011V1I0",
                        "NN011V1I0",
                        "citationn",
                        "Citation N",
                        "CitationN",
                        "CITATION N",
                        "CITATIONN",
                        "City of",
                        "CITY OF",
                        "JO AIIO",
                        "JOAIIO",
                        "CITYOF",
                        "city of",
                        "cityof",
                        "CitationsProcessingCenter",
                        "Citations Processing Center",
                        "Cityof",
                        "Department of Finance",
                        "Departmentof Finance",
                        "Department ofFinance",
                        "COUNTYDISTRICTCOURT",
                        "COUNTY DISTRICTCOURT",
                        "COUNTYDISTRICT COURT",
                        "COUNTY DISTRICT COURT"
                        ]
                # if any(identifier in text for identifier in identifiers):
                if any(identifier in text for identifier in identifiers) and "MILESTONE" not in text and "Premier" not in text:

                    # Construct the path to the destination file
                    pdf.close()
                    dest_file_path = os.path.join(citations_folder, filename)

                    # Check if the file already exists in the Citations folder
                    if os.path.exists(dest_file_path):
                        print(f"File {filename} already exists in the Citations folder")
                    else:
                        try:
                            shutil.move(file_path, citations_folder)
                            print(f"File {filename} moved to Citations folder.")

                            # Delete the file from the attachments_output folder only if it was moved
                            if os.path.exists(file_path):
                                os.remove(file_path)
                                print(f"File {filename} deleted from attachments_output folder.")
                        except Exception as e:
                            print(f"Error deleting file {filename}: {e}")

                    # Exit the loop
                    break
else:
    pass

# Print a message indicating that the PDF files have been processed
print("PDF files have been processed.")
