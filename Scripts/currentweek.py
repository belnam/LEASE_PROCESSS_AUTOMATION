import os
from datetime import datetime, timedelta
import getpass

username = getpass.getuser()

def rename_week_folder(folder_path):
    # Get the current week number
    of_day = datetime.now() + timedelta(days=-1)
    current_week = int(str(of_day.isocalendar()[1]))

    # Define the folder name pattern
    folder_pattern = "WEEK_"

    # Construct the current week folder name
    current_week_folder = folder_pattern + str(current_week)

    # Check if the current week folder exists
    if os.path.exists(os.path.join(folder_path, current_week_folder)):
        return  # Exit if the current week folder already exists

    # Find the previous week folder
    prev_week_folder = ""
    for folder_name in os.listdir(folder_path):
        if folder_name.startswith(folder_pattern):
            prev_week_folder = folder_name
            break

    # Rename the previous week folder to the current week folder name
    if prev_week_folder:
        prev_week_path = os.path.join(folder_path, prev_week_folder)
        new_week_path = os.path.join(folder_path, current_week_folder)
        os.rename(prev_week_path, new_week_path)
        print(f"Renamed folder '{prev_week_path}' to '{new_week_path}'")

# Specify the folder path to be renamed
folder_path = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\Process_Report\\"

# Call the function to rename the week folder
rename_week_folder(folder_path)
