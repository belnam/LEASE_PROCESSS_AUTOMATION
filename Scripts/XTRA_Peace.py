"""
A python ocr bot extracting data from XTRA agency
"""
from ast import And
from copyreg import constructor
import re
import pandas as pd
import pdfplumber
import getpass
import os
import datetime 
from datetime import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Function to reference equipment ID from API
def reference_equipmentID(equipment_id):
    url = "https://amazon.backend.innovativetoll.com/check-asset-exists"
    payload = {"equipment_id": str(equipment_id)}

    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Failed to fetch data for equipment_id {equipment_id}. Status code: {response.status_code}")

# Function to process rentals and update LP information
def map_xtra(file_path):
    rawfiles_df = pd.read_excel(file_path, dtype=str)
    
    # Get unique equipment IDs
    unique_equipment_ids = rawfiles_df['EQUIPMENT ID'].unique()
    
    # Dictionary to cache API responses to avoid redundant API calls
    api_cache = {}

    # start = time.time()

    # Function to fetch data for a single equipment ID
    def fetch_data(equipment_id):
        if equipment_id and equipment_id not in api_cache:
            try:
                api_data = reference_equipmentID(equipment_id)
                api_cache[equipment_id] = api_data
            except Exception as e:
                print(f"Error processing equipment ID {equipment_id}: {str(e)}")
                api_cache[equipment_id] = None
        return equipment_id

    # Use ThreadPoolExecutor to fetch data concurrently
    with ThreadPoolExecutor(max_workers=200) as executor:
        futures = [executor.submit(fetch_data, equipment_id) for equipment_id in unique_equipment_ids if equipment_id]
        
        for future in as_completed(futures):
            equipment_id = future.result()
            api_data = api_cache.get(equipment_id)
            
            if api_data and api_data["data"]["exists"]:
                if api_data["data"]["inCurrentAAP"] is True:
                    license_plate = api_data["data"]["data"]["license_plate"]
                    license_plate_state = api_data["data"]["data"]["license_plate_state"]
                elif api_data["data"]["inCurrentAAP"] is False:
                    license_plate = api_data["data"]["searchedAsset"]["license_plate"]
                    license_plate_state = api_data["data"]["searchedAsset"]["license_plate_state"]
                
                # Update all rows with the same equipment ID
                mask = rawfiles_df['EQUIPMENT ID'] == equipment_id
                rawfiles_df.loc[mask, 'LP'] = license_plate
                rawfiles_df.loc[mask, 'LP STATE'] = license_plate_state

    rawfiles_df.to_excel(file_path, index=False)
    # stop = time.time()
    # print(f'Done processing {file_path} in {stop - start} seconds')
def process_xtra_files():
    row_dict = {
        'TOLL AGENCY': None,
        'LP': None,
        'LP STATE': None,
        'TRXN DATE & TIME': None,
        'EXIT LANE/LOCATION': None,
        'ACCOUNT': None,
        'REFERENCE #': None,
        'VIOLATION': None,
        'AMOUNT DUE': None,
        'DUE DATE': None,
        'PIN NO #': None,
        'INVOICE #': None,
        'CODE 1#': None,
        'CODE 2#': None,
        'BILL NO#': None,
        'EQUIPMENT ID': None,
        'EQUIPMENT STATE': None,
        'AGREEMENT': None,
        'POST DATE/TIME': None,
        'UNIT #': None,
    }

    username = getpass.getuser()
    workingDir = f"Downloaded_Scans\\"
    outputDir = f"SRTS_OUTPUT\\"
    agency_mapping_df = pd.read_excel("Scripts\\Agency_Names.xlsx")

    for i in os.listdir(workingDir):
    # if "XTRA" in i or "xtra" in i:
        df = pd.DataFrame()
        row_dict["TOLL AGENCY"] = ""
        row_dict["LP"] = ""
        row_dict["LP STATE"] = ""
        row_dict["TRXN DATE & TIME"] = ""
        row_dict["EXIT LANE/LOCATION"] = ""
        row_dict["ACCOUNT"] = ""
        row_dict["REFERENCE #"] = ""
        row_dict["VIOLATION"] = ""
        row_dict["AMOUNT DUE"] = ""
        row_dict["DUE DATE"] = ""
        row_dict["PIN NO #"] = ""
        row_dict["INVOICE #"] = ""
        row_dict["CODE 1#"] = ""
        row_dict["CODE 2#"] = ""
        row_dict["BILL NO#"] = ""
        row_dict["EQUIPMENT ID"] = ""
        row_dict["EQUIPMENT STATE"] = ""
        row_dict["AGREEMENT"] = ""
        row_dict["POST DATE/TIME"] = ""
        with pdfplumber.open(workingDir + i) as pdf:
            for j, text in enumerate(pdf.pages):
                pages = pdf.pages[j]
                page_data = pages.extract_text(x_tolerance=1)
                # print(page_data)
                invoice = re.findall(r'In\w+.*N\w+\W+(\d+)', page_data)
                ticketrebill = re.findall(r'(\w{6})\s+(\d+\w+)\s+\w+\s+\w+\W+\d+\W+\w+\W+(\w+.*\w+)\W+\d+\/.*\/.*\/.*\/.*[S|$|s]\W+(\w+\W+\w+)\W+(\w+)|(\w+.*\w+)\W+\d+\/.*\/.*\/.*\/.*[S|$|s]\W+(\w+\W+\w+)\W+(\w+)', page_data)
                transaction_a = re.findall(r'(\w{6})\s+(\d+\w+)\s+.*To\w+.*\d{2}\W*\d{2}\W*\d{4}\s*\d{2}\W*\d{2}\W*\d{4}\D*(\d*\W*\d*)\W*(\w*)\n(\w*\W*\w*\W*\w*\W*\w*\W*\w*\s*\D*)\W+\w+\W+loc([\s\S]*?)\bon\b\W+(\d{4}\D*\d*\D*\d*\D*\d*\D*\d*)|(\w{6})\s+(\d+\w+)\s+.*VAN.*\nTo\w+.*\d{2}\W*\d{2}\W*\d{4}\s*\d{2}\W*\d{2}\W*\d{4}\D*(\d*\W*\d*)\W*(\w*)\n(\w*\W*\w*\W*\w*\W*\w*\W*\w*\s*\D*)\W+\w+\W+loc([\s\S]*?)\bon\b\W+(\d+\s?\d+\D+\d+\s?\d+\D+\d+\s?\d+\D+\d+\s?)|To\w+.*\d{2}\W*\d{2}\W*\d{4}\s*\d{2}\W*\d{2}\W*\d{4}\D*(\d*\W*\d*)\W*(\w*)\n(\w*\W*\w*\W*\w*\W*\w*\W*\w*\s*\D*)\W+\w+\W+loc([\s\S]*?)\bon\b\W+(\d+\s?\d+\D+\d+\s?\d+\D+\d+\s?\d+\D+\d+\s?)', page_data)

                if invoice:
                    row_dict['INVOICE #'] = invoice[0]
                if ticketrebill:
                    for rebill in ticketrebill:
                        rebill = list(filter(''.__ne__,rebill))
                        if len(rebill) == 5:
                            row_dict['LP'] = ""
                            row_dict['EQUIPMENT ID'] = rebill[0]
                            row_dict['AGREEMENT'] = rebill[1]
                            row_dict['EXIT LANE/LOCATION'] = rebill[2]
                            row_dict['AMOUNT DUE'] = rebill[3]
                            row_dict['EQUIPMENT STATE'] = rebill[4]
                            row_dict['TOLL AGENCY'] = ""
                            row_dict['TRXN DATE & TIME'] = ""
                            row_dict['ACCOUNT'] = ""
                            row_dict['REFERENCE #'] = ""    
                            row_dict['VIOLATION'] = ""
                            row_dict["LP STATE"] = ""
                            df = df._append(row_dict, ignore_index = True)
                            df = df[~df['EXIT LANE/LOCATION'].str.contains('Toll Fee', case=False, na=False)]
                        elif len(rebill) == 3:
                            row_dict['EQUIPMENT ID'] = ""
                            row_dict['AGREEMENT'] = ""
                            row_dict['EXIT LANE/LOCATION'] = rebill[0]
                            row_dict['AMOUNT DUE'] = rebill[1]
                            row_dict['EQUIPMENT STATE'] = rebill[2]
                            row_dict['TOLL AGENCY'] = ""
                            row_dict['TRXN DATE & TIME'] = ""
                            row_dict['ACCOUNT'] = ""
                            row_dict['REFERENCE #'] = ""    
                            row_dict['VIOLATION'] = ""
                            row_dict["LP"] = ""
                            row_dict["LP STATE"] = ""
                            df = df._append(row_dict, ignore_index = True)
                            df = df[~df['EXIT LANE/LOCATION'].str.contains('Toll Fee', case=False, na=False)]
                else:
                    pass
                if transaction_a:
                    for transaction in transaction_a:
                        transaction = list(filter(''.__ne__,transaction))
                        # print(len(transaction))
                        if len(transaction) == 7:
                            row_dict['EQUIPMENT ID'] = transaction[0]
                            row_dict['AGREEMENT'] = transaction[1]
                            row_dict['AMOUNT DUE'] = transaction[2].replace(',', '.')
                            row_dict['EQUIPMENT STATE'] = transaction[3]
                            row_dict['TOLL AGENCY'] = transaction[4].replace(',', '').replace('.', '').upper()  
                            row_dict['EXIT LANE/LOCATION'] = transaction[5].replace(':', '')
                            # row_dict['TRXN DATE & TIME'] = transaction[6].replace('\n', '').replace('-02', '-02 ').replace('-03', '-03 ').replace('-01', '-02 ').replace('  ', ' ')
                            row_dict['TRXN DATE & TIME'] = transaction[6].replace('\n', '')\
                                    .replace('-01', '-01 ').replace('-02', '-02 ').replace('-03', '-03 ')\
                                    .replace('-04', '-04 ').replace('-05', '-05 ').replace('-06', '-06 ')\
                                    .replace('-07', '-07 ').replace('-08', '-08 ').replace('-09', '-09 ')\
                                    .replace('-10', '-10 ').replace('-11', '-11 ').replace('-12', '-12 ')\
                                    .replace('-13', '-13 ').replace('-14', '-14 ').replace('-15', '-15 ')\
                                    .replace('-16', '-16 ').replace('-17', '-17 ').replace('-18', '-18 ')\
                                    .replace('-19', '-19 ').replace('-20', '-20 ').replace('-21', '-21 ')\
                                    .replace('-22', '-22 ').replace('-23', '-23 ').replace('-24', '-24 ')\
                                    .replace('-25', '-25 ').replace('-26', '-26 ').replace('-27', '-27 ')\
                                    .replace('-28', '-28 ').replace('-29', '-29 ').replace('-30', '-30 ')\
                                    .replace('-31', '-31 ').replace(' -', '-').replace('  ', ' ')

                            df = df._append(row_dict, ignore_index = True)
                        elif len(transaction) == 5:
                            row_dict['AMOUNT DUE'] = transaction[0].replace(',', '.')
                            row_dict['EQUIPMENT STATE'] = transaction[1]
                            row_dict['TOLL AGENCY'] = transaction[2].replace(',', '').replace('.', '').upper()  
                            row_dict['EXIT LANE/LOCATION'] = transaction[3].replace(':', '')
                            # row_dict['TRXN DATE & TIME'] = transaction[4].replace('\n', '').replace('-03', '-03 ').replace('  ', ' ')
                            row_dict['TRXN DATE & TIME'] = transaction[4].replace('\n', '')\
                                    .replace('-01', '-01 ').replace('-02', '-02 ').replace('-03', '-03 ')\
                                    .replace('-04', '-04 ').replace('-05', '-05 ').replace('-06', '-06 ')\
                                    .replace('-07', '-07 ').replace('-08', '-08 ').replace('-09', '-09 ')\
                                    .replace('-10', '-10 ').replace('-11', '-11 ').replace('-12', '-12 ')\
                                    .replace('-13', '-13 ').replace('-14', '-14 ').replace('-15', '-15 ')\
                                    .replace('-16', '-16 ').replace('-17', '-17 ').replace('-18', '-18 ')\
                                    .replace('-19', '-19 ').replace('-20', '-20 ').replace('-21', '-21 ')\
                                    .replace('-22', '-22 ').replace('-23', '-23 ').replace('-24', '-24 ')\
                                    .replace('-25', '-25 ').replace('-26', '-26 ').replace('-27', '-27 ')\
                                    .replace('-28', '-28 ').replace('-29', '-29 ').replace('-30', '-30 ')\
                                    .replace('-31', '-31 ').replace(' -', '-').replace('  ', ' ')


                            df = df._append(row_dict, ignore_index = True)
                        else:
                            pass
        df.loc[df['EXIT LANE/LOCATION'] == 'Rebill', 'EXIT LANE/LOCATION'] = 'Ticket Rebill'
        df = df[~df['EXIT LANE/LOCATION'].str.contains('Fee', case=False, na=False)]
        for index, row in df.iterrows():
            toll_agency = row['TOLL AGENCY']
            mapping_row = agency_mapping_df[agency_mapping_df['AGENCY'] == toll_agency]
            if not mapping_row.empty:
                mapping_value = mapping_row.iloc[0]['MAPPING']
                df.at[index, 'TOLL AGENCY'] = mapping_value

        df['ConvertedDate'] = pd.to_datetime(
            df['TRXN DATE & TIME'], format='%Y-%m-%d %H:%M', errors='coerce'
        )

        df['TRXN DATE & TIME'] = df.apply(
            lambda row: row['ConvertedDate'].strftime('%m/%d/%Y %H:%M:%S') if pd.notna(row['ConvertedDate']) else row['TRXN DATE & TIME'], 
            axis=1
        )

        df.drop(columns=['ConvertedDate'], inplace=True)

        output_file = str(outputDir + i).replace('.pdf', '') + '.xlsx'
        df.to_excel(output_file, index=False)

        # Process equipment IDs for this file
        if not df.empty and 'EQUIPMENT ID' in df.columns and any(df['EQUIPMENT ID'].notna()):
            print(f"Processing equipment IDs for file: {output_file}")
            map_xtra(output_file)
        else:
            print(f"No equipment IDs found in file: {output_file}")

if __name__ == '__main__':
    process_xtra_files()