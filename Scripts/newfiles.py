import os
import re
import shutil

source_folder = "Downloaded_Scans"
destination_folder = "New_scans"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

files = os.listdir(source_folder)


for file in files:
    if "NEW SCAN" in file:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)
        print(f"Moved {file} to {destination_folder}")
