from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import getpass
username = getpass.getuser()

# Initialize GoogleAuth and authenticate
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # This will open a web browser to authenticate

# Create a GoogleDrive instance
drive = GoogleDrive(gauth)

# ID of the destination folder in Google Drive
folder_id = "15WvTR76LPMnVxUtDb32M71Mp2I-tVpbr"
# folder_id = "1fRiKCv-GrmP0bg8wctpPS6lmOJHflRTM"

local_directory = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\Downloaded_Scans\\"

# List all PDF files in the local directory
pdf_files = [f for f in os.listdir(local_directory) if f.endswith('.pdf')]

# Upload each PDF file to the specified folder
for pdf_file in pdf_files:
    file_metadata = {
        'name': pdf_file, 
        'parents': [{'id': folder_id}]
    }
    file_path = os.path.join(local_directory, pdf_file)
    file_drive = drive.CreateFile(file_metadata)
    file_drive.SetContentFile(file_path)
    file_drive.Upload()

print("PDF files uploaded successfully.")
