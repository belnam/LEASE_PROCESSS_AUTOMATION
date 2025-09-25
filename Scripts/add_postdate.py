import pandas as pd
import os
import time

srts_directory = "SRTS_OUTPUT"

for file in os.listdir(srts_directory):
    if file.endswith(".xlsx"):
        file_path = os.path.join(srts_directory, file)
        
        # Read the Excel file and load all sheets
        with pd.ExcelFile(file_path, engine='openpyxl') as excel_file:
            sheets = {sheet: pd.read_excel(excel_file, sheet_name=sheet) for sheet in excel_file.sheet_names}

        # Process each sheet
        for sheet_name, df in sheets.items():
            # Update the 'POST DATE/TIME' column to the specific date (12/12/2024) and format it as MM/DD/YYYY
            formatted_date = pd.to_datetime('04/25/2025').strftime('%m/%d/%Y')
            df['POST DATE/TIME'] = formatted_date

            # Update the sheet in the dictionary
            sheets[sheet_name] = df

        # Write back all updated sheets to the file
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            for sheet_name, sheet_df in sheets.items():
                sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)

        print(f"{file} has been updated")
        time.sleep(1)

print("All files have been updated.")
