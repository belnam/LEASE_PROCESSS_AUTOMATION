import pandas as pd
import os
import shutil
import datetime
import getpass
from datetime import timedelta

username = getpass.getuser()
# Get the current week number
of_day = datetime.datetime.now() + timedelta(days=-1)
current_week = int(str(of_day.isocalendar()[1]))

inputdir = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\Process_Report\\WEEK_{current_week}\\to_amazon_template\\"

outputdir = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\Process_Report\\Final_Weekly_Report\\"

# Read the start date and end date from a text document
date_file_path = "date_info.txt"  # Path to the text document containing dates
with open(date_file_path, "r") as file:
    dates = file.readlines()

# Extract start date and end date
start_date = datetime.datetime.strptime(dates[0].strip(), "%Y-%m-%d").date()
end_date = datetime.datetime.strptime(dates[1].strip(), "%Y-%m-%d").date()

# Copy files from inputdir to outputdir within the date range
file_list = os.listdir(inputdir)
for file_name in file_list:
    file_path = os.path.join(inputdir, file_name)
    modified_date = datetime.date.fromtimestamp(os.path.getmtime(file_path))
    if start_date <= modified_date <= end_date:
        destination_path = os.path.join(outputdir, file_name)
        shutil.copy(file_path, destination_path)

print("Files copied successfully!")
