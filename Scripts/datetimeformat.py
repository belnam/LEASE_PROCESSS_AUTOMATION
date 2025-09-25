import pandas as pd

def is_datetime(value):
    """ Check if a value is already a datetime object. """
    return isinstance(value, pd.Timestamp)

# Load the Excel file
df = pd.read_excel(r'SRTS_OUTPUT\scan_150_amazon_xtra_rental_tolls_08-26-2024_(bot)_1724738440.xlsx')

# Specify the column with the dates and times
date_column = 'TRXN DATE & TIME'

# Convert the column to datetime format where needed
df[date_column] = pd.to_datetime(df[date_column], errors='coerce')

# Format the dates and times to 'MM/DD/YYYY HH:MM:SS AM/PM' only if they are datetime objects
df[date_column] = df[date_column].apply(
    lambda x: x.strftime('%m/%d/%Y %I:%M:%S %p') if pd.notna(x) and is_datetime(x) else x
)

# Save the changes to the same Excel file
df.to_excel(r'SRTS_OUTPUT\scan_150_amazon_xtra_rental_tolls_08-26-2024_(bot)_1724738440.xlsx', index=False)
