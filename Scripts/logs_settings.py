import pandas as pd
import time

emaillogs_path = "Rental_ProcessedFilenames/email_logs.xlsx"
dailyrentalfile_path = "Rental_ProcessedFilenames/Daily_RentalFileNames.xlsx"
dailyrentalfile = pd.read_excel(dailyrentalfile_path, dtype=str, sheet_name='Sheet1')
emaillogs = pd.read_excel(emaillogs_path)

start = time.time()

# Process matching rows based on 'Scan Name'
last_matching_index = {}
for i, row in emaillogs.iterrows():
    scan_name = row['Scan Name']
    last_matching_index[scan_name] = i

for scan_name, index in last_matching_index.items():
    matching_row = emaillogs.loc[index]
    matching_rows = dailyrentalfile[dailyrentalfile['SCAN_NAME'] == scan_name]
    if not matching_rows.empty:
        dailyrentalfile_index = matching_rows.index[-1]
        dailyrentalfile.at[dailyrentalfile_index, 'RECEIVED TIMESTAMP'] = matching_row['Received Timestamp']

# Process matching rows based on 'RENAMED_AS'
last_emaillog_index = {}
for i, row in dailyrentalfile.iterrows():
    renamed = row['SCAN_NAME']
    last_emaillog_index[renamed] = i

for renamed, index in last_emaillog_index.items():
    matching_row = dailyrentalfile.loc[index]
    matching_rows = emaillogs[emaillogs['Scan Name'] == renamed]
    if not matching_rows.empty:
        emaillogs_index = matching_rows.index[-1]
        emaillogs.at[emaillogs_index, 'Renamed As'] = matching_row['RENAMED_AS']

emaillogs.to_excel(emaillogs_path, index=False)
dailyrentalfile.to_excel(dailyrentalfile_path, index=False)

stop = time.time()
print(f'Done processing in {stop - start} seconds.')
