import os
import shutil

# Source and destination folders
source_folder = 'PickleFiles'
destination_folder = 'Previous_Timestamps'

# Check if source folder exists
if not os.path.exists(source_folder):
    print(f"Source folder '{source_folder}' does not exist.")
    exit()

# Check if destination folder exists, create it if not
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print(f"Created destination folder '{destination_folder}'.")

# List all files in the source folder
files = os.listdir(source_folder)

# Filter .pickle files
pickle_files = [f for f in files if f.endswith('.pickle')]

# Copy each .pickle file to the destination folder with a unique name
for pickle_file in pickle_files:
    source_path = os.path.join(source_folder, pickle_file)
    
    # Construct the destination path
    base_name, ext = os.path.splitext(pickle_file)
    count = 1
    while True:
        destination_file_name = f"{base_name}_{count}{ext}"
        destination_path = os.path.join(destination_folder, destination_file_name)
        
        # Check if the destination file already exists
        if not os.path.exists(destination_path):
            shutil.copy(source_path, destination_path)
            print(f"Copied '{pickle_file}' to '{destination_folder}' as '{destination_file_name}'.")
            break
        else:
            count += 1

print("Copying process complete.")
