from pathlib import Path
import pandas as pd

output_path = './SRTS_OUTPUT/'
agency_mapping_df = pd.read_excel("Scripts/REFINED AGENCY CHEAT SHEET.xlsx", engine='openpyxl')

output_path = Path(output_path)
files = list(output_path.glob("*.xlsx"))

for file in files:
    with pd.ExcelFile(file, engine='openpyxl') as excel_file:
        sheets = {sheet: pd.read_excel(excel_file, sheet_name=sheet) for sheet in excel_file.sheet_names}

    first_sheet = list(sheets.keys())[0]
    df = sheets[first_sheet]
    
    for index, row in df.iterrows():
        toll_agency = row['EXIT LANE/LOCATION']
        mapping_row = agency_mapping_df[agency_mapping_df['LOCATION'] == toll_agency]
        if not mapping_row.empty:
            mapping_value = mapping_row.iloc[0]['AGENCY']
            df.at[index, 'TOLL AGENCY'] = mapping_value
    
    sheets[first_sheet] = df
    
    print(f'Processing file {file.name}')
    

    with pd.ExcelWriter(file, engine='openpyxl') as writer:
        for sheet_name, sheet_df in sheets.items():
            sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)
