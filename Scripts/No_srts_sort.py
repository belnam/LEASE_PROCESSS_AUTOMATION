
import shutil
import os
import getpass

source_folder_1 = "XTRA_NOSRTS"
source_folder_2 = "Premier_NOSRTS"
destination_folder = "PRE_XTRA_STORE"
def move_files(source_folder, destination_folder):
    for filename in os.listdir(source_folder):
        if filename.endswith(".pdf"):
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, filename)
            shutil.move(source_file, destination_file)

move_files(source_folder_1, destination_folder)

move_files(source_folder_2, destination_folder)
