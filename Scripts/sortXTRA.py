import os
import shutil
import pdfplumber
import getpass

username = getpass.getuser()
pdf_directory = f'Downloaded_Scans\\'
xtraPremier_folder = f'Xtra_Premier_NoSRTS\\'

for filename in os.listdir(pdf_directory):
    file_path = os.path.join(pdf_directory, filename)
    if file_path.endswith('.pdf'):
        with pdfplumber.open(file_path) as pdf:
            # Check the first page's text content
            first_page_text = pdf.pages[0].extract_text()
            
            # Add conditions to check for "XTRA" or "Leasing" in the first page's text
            if "XTRA" in first_page_text or "xtra" in first_page_text or "XTRA Lease" in first_page_text :
                for i in range(4):
                    try:
                        text = pdf.pages[i].extract_text()
                    except:
                        pass
                    identifiers = [
                            "Ticket Rebill",
                            "Rebill",
                            ]
                    if any(identifier in text for identifier in identifiers):
                        pdf.close()
                        dest_file_path = os.path.join(xtraPremier_folder, filename)

                        # Check if the file already exists in the xtraPremier_folder folder
                        if os.path.exists(dest_file_path):
                            print(f"File {filename} already exists in the xtraPremier_folder folder")
                        else:
                            try:
                                shutil.move(file_path, xtraPremier_folder)
                                print(f"File {filename} moved to xtraPremier_folder folder.")

                                # Delete the file from the attachments_output folder only if it was moved
                                if os.path.exists(file_path):
                                    os.remove(file_path)
                                    print(f"File {filename} deleted from attachments_output folder.")
                            except Exception as e:
                                print(f"Error deleting file {filename}: {e}")

                        # Exit the loop
                        break


# Print a message indicating that the PDF files have been processed
print("PDF files have been processed.")
