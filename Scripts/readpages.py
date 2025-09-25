import os
import shutil
import pdfplumber

# Set the source and destination folder paths
src_folder = 'Downloaded_Scans'
dst_folder = 'MissingInfoScans'

# Initialize counters
num_files_moved = 0
num_files_deleted = 0

# Loop through all the files in the source folder
for filename in os.listdir(src_folder):
    # Check if the file is a PDF, and contains either "BOWMAN" or "STOUGHTON" in the file name
    if filename.endswith('.pdf') and ("BOWMAN" in filename or "STOUGHTON" in filename):
        # Open the PDF file using pdfplumber
        with pdfplumber.open(os.path.join(src_folder, filename)) as pdf:
            # Check if the PDF file has only one page
            if len(pdf.pages) == 1:
                # Close the file to release any locks
                pdf.close()
                # Move the file to the destination folder
                try:
                    shutil.move(os.path.join(src_folder, filename), os.path.join(dst_folder, filename))
                    print(f"Moved {filename} to {dst_folder}")
                    num_files_moved += 1
                    # Delete the original file
                    if os.path.exists(os.path.join(src_folder, filename)):
                        os.remove(os.path.join(src_folder, filename))
                        print(f"Deleted {filename} from {src_folder}")
                        num_files_deleted += 1
                except PermissionError as e:
                    print(f"Error moving file {filename}: {e}")
                    # Wait for 1 second before trying again
                    # time.sleep(1)

# Print out the number of files moved and deleted
print(f"Moved {num_files_moved} files to {dst_folder}")
print(f"Deleted {num_files_deleted} files from {src_folder}")
