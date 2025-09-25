import shutil
import os
import getpass
username = getpass.getuser()
# Set the source and destination folder paths
source_folder = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\SRTS_OUTPUT\\"
destination_folder = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\Process_Report\\STORED_DAILY_SRTS\\"
# Loop through all the files in the source folder
for filename in os.listdir(source_folder):
    # Check if the file has an XLSX extension
    if filename.endswith(".xlsx"):
        # Construct the full file paths for the source and destination files
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)
        # Copy the file from the source folder to the destination folder
        shutil.copy(source_file, destination_file)



