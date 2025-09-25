from ast import And
from copyreg import constructor
import re
import pandas as pd
import pdfplumber
import getpass
import os
import datetime 
from datetime import datetime

def extract_and_format_date_from_exit_lane(exit_lane):
    # Regex to find the date pattern
    date_pattern = r'\b([A-Za-z]{3} \d{1,2} \d{4} \d{1,2}:\d{2}(?: ?[AP]M)?)\b'
    match = re.search(date_pattern, exit_lane)
    if not match:
        return None, exit_lane
    date_str = match.group(1)
    # Remove the date from exit_lane
    new_exit_lane = re.sub(date_pattern, '', exit_lane).strip()
    # Format the date_str into MM/DD/YYYY HH:MM AM/PM
    try:
        # Try parsing with different formats
        try:
            dt = datetime.strptime(date_str, "%b %d %Y %I:%M%p")
        except ValueError:
            dt = datetime.strptime(date_str, "%b %d %Y %I:%M %p")
        formatted_date = dt.strftime("%m/%d/%Y %I:%M%p")
    except Exception as e:
        # If parsing fails, return the original date_str
        formatted_date = date_str
    return formatted_date, new_exit_lane

row_dict = {
    'TOLL AGENCY': "MCKINNEY TRAILER RENTALS",
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
    'UNIT #': None,
    'POSTED DATE': None,
    
}

username = getpass.getuser()
workingDir = f"Downloaded_Scans\\"
outputDir = f"SRTS_OUTPUT\\"
agency_mapping_df = pd.read_excel("Scripts\\Agency_Names.xlsx")

for i in os.listdir(workingDir):
        df = pd.DataFrame()

        
        with pdfplumber.open(workingDir + i) as pdf:
            for j, text in enumerate(pdf.pages):
                pages = pdf.pages[j]
                page_data = pages.extract_text()
                
                # print(page_data)
                vinreference = re.findall(r"VIN\W+(\w+)", page_data)
                transactiona= re.findall(r"Toll.*C\w+\W+\d{6}\W+(\w{2})\W+(\w+)\W+.*\W+[$]\d+\W+\d+.*[$](\d+\W+\d+)", page_data)
                transaction_full_e = re.findall(r"(VIN)\W+(\w+)\W+.*Toll.*C\w+\W+(\d{6})\W+(\w{2})\W+(\w+)\W+(.*?)\$(\d+\W+\d+)(?:.*?\n)?(.*?)(AM|PM)|(VIN)\W+(\w+)\W+.*Toll.*C\w+\W+(\d{6})\W+(\w{2})\W+(\w+)\W+(.*?)\$(\d+\W+\d+)(?:.*?\n)?(.*?)(\b[A-Za-z]{3}\W+\d{1,2}\W+\d{4} \d{1,2}:\d{2}AM|PM)|(VIN)\W+(\w+)\W+Our.*\W.*\W.*\W.*\W.*\W.*\W.*\W.*\W.*\W.*\W.*\W.*\W.*Toll.*C\w+\W+(\d{6})\W+(\w{2})\W+(\w+)\W+(.*?)\$(\d+\W+\d+)(?:.*?\n)?(.*?)(\b[A-Za-z]{3}\W+\d{1,2}\W+\d{4} \d{1,2}:\d{2}AM|PM)|(VIN)\W+(\w+)\W+.*Toll.*C\w+\W+(\d{6})\W+(\w{2})\W+(\w+)\W+(.*?)(\b[A-Za-z]{3}\W+\d{1,2}\W+\d{4} \d{1,2}:\d{2}AM|PM)\W+(\d+\W+\d+)|Toll.*C\w+\W+(\d{6})\W+(\w{2})\W+(\w+)\W+(.*?)\$(\d+\W+\d+)(?:.*?\n)?(.*?)(\b[A-Za-z]{3}\W+\d{1,2}\W+\d{4} \d{1,2}:\d{2}AM|PM)|Toll.*C\w+\W+(\d{6})\W+(\w{2})\W+(\w+)\W+(.*?)\$(\d+\W+\d+)(?:.*?\n)?(.*?)(AM|PM)|Toll.*C\w+\W+(\d{6})\W+(\w{2})\W+(\w+)\W+(.*?)(\b[A-Za-z]{3}\W+\d{1,2}\W+\d{4} \d{1,2}:\d{2}AM|PM)\W+(\d+\W+\d+)", page_data)
                # transaction_vinref = re.findall(r"VIN\W+(\w+)\W+.*Toll.*C\w+\W+(\d{6})\W+(\w{2})\W+(\w+)\W+(.*?)\$(\d+\W+\d+)(?:.*?\n)?(.*?)(\b[A-Za-z]{3}\W+\d{1,2}\W+\d{4} \d{1,2}:\d{2}AM|PM)|VIN\W+(\w+)\W+.*Toll.*C\w+\W+(\d{6})\W+(\w{2})\W+(\w+)\W+(.*?)(\b[A-Za-z]{3}\W+\d{1,2}\W+\d{4} \d{1,2}:\d{2}AM|PM)\W+(\d+\W+\d+)", page_data)
                invoice = re.findall(r"Invoice\W+(\w+\d+)", page_data)
                duedate = re.findall(r"Invoice\W+\w+\W+(\d+\W+\d+\W+\d+)", page_data)   
                timedateextension = re.findall(r"(\w+.*:\d+\w+)", page_data)

                if invoice:
                    row_dict["INVOICE #"] = invoice[0]
          
                if duedate:
                    row_dict["DUE DATE"] = duedate[0]  

                if transaction_full_e:
                    for tran_e in transaction_full_e:
                        while tran_e and tran_e[0].strip() == '':
                            tran_e = tran_e[1:]
                        while tran_e and tran_e[-1].strip() == '':
                            tran_e = tran_e[:-1]
                        # print(list(tran_e))
                        if len(tran_e) == 6:
                            row_dict['LP'] = tran_e[2]
                            row_dict["LP STATE"] = tran_e[1]
                            row_dict["UNIT #"] = tran_e[0]
                            row_dict['EXIT LANE/LOCATION'] = tran_e[3]
                            row_dict["TRXN DATE & TIME"] = (tran_e[4]
                                                                .replace("Jan", "01/")
                                                                .replace("Feb", "02/")
                                                                .replace("Mar", "03/")
                                                                .replace("Apr", "04/")
                                                                .replace("May", "05/")
                                                                .replace("Jun", "06/")
                                                                .replace("Jul", "07/")
                                                                .replace("Aug", "08/")
                                                                .replace("Sep", "09/")
                                                                .replace("Oct", "10/")
                                                                .replace("Nov", "11/")
                                                                .replace("Dec", "12/")
                                                                .replace(" ", "/")
                                                                .replace("//", "/")
                                                                .replace("AM/", "AM")
                                                                .replace("PM/", "PM")
                                                                .replace("2024/", "2024 ")
                                                                .replace("2025/", "2025 ")
                                                                )
                            formatted_date, new_exit_lane = extract_and_format_date_from_exit_lane(row_dict['EXIT LANE/LOCATION'])
                            if formatted_date:
                                row_dict['EXIT LANE/LOCATION'] = new_exit_lane
                                # Format the extracted date
                                formatted_date = (formatted_date
                                                .replace("Jan", "01/")
                                                .replace("Feb", "02/")
                                                .replace("Mar", "03/")
                                                .replace("Apr", "04/")
                                                .replace("May", "05/")
                                                .replace("Jun", "06/")
                                                .replace("Jul", "07/")
                                                .replace("Aug", "08/")
                                                .replace("Sep", "09/")
                                                .replace("Oct", "10/")
                                                .replace("Nov", "11/")
                                                .replace("Dec", "12/")
                                                .replace(" ", "/")
                                                .replace("//", "/")
                                                .replace("AM/", "AM")
                                                .replace("PM/", "PM")
                                                .replace("2024/", "2024 ")
                                                .replace("2025/", "2025 "))
                                
                                # Check if TRXN DATE & TIME already has a value and concatenate with existing data last
                                if row_dict['TRXN DATE & TIME']:
                                    row_dict['TRXN DATE & TIME'] = formatted_date + " " + row_dict['TRXN DATE & TIME']
                                else:
                                    row_dict['TRXN DATE & TIME'] = formatted_date
                            row_dict["AMOUNT DUE"] = float(tran_e[5].replace(',', '')) + 6
                            df = df._append(row_dict, ignore_index = True)
                        
                        elif len(tran_e) == 7:
                            row_dict['LP'] = tran_e[2]
                            row_dict["LP STATE"] = tran_e[1]
                            row_dict["UNIT #"] = tran_e[0]
                            row_dict['EXIT LANE/LOCATION'] = tran_e[3] + tran_e[5]
                            row_dict["TRXN DATE & TIME"] = (tran_e[6]
                                                                .replace("Jan", "01/")
                                                                .replace("Feb", "02/")
                                                                .replace("Mar", "03/")
                                                                .replace("Apr", "04/")
                                                                .replace("May", "05/")
                                                                .replace("Jun", "06/")
                                                                .replace("Jul", "07/")
                                                                .replace("Aug", "08/")
                                                                .replace("Sep", "09/")
                                                                .replace("Oct", "10/")
                                                                .replace("Nov", "11/")
                                                                .replace("Dec", "12/")
                                                                .replace(" ", "/")
                                                                .replace("//", "/")
                                                                .replace("AM/", "AM")
                                                                .replace("PM/", "PM")
                                                                .replace("2024/", "2024 ")
                                                                .replace("2025/", "2025 ")
                                                                )
                            formatted_date, new_exit_lane = extract_and_format_date_from_exit_lane(row_dict['EXIT LANE/LOCATION'])
                            if formatted_date:
                                row_dict['EXIT LANE/LOCATION'] = new_exit_lane
                                # Format the extracted date
                                formatted_date = (formatted_date
                                                .replace("Jan", "01/")
                                                .replace("Feb", "02/")
                                                .replace("Mar", "03/")
                                                .replace("Apr", "04/")
                                                .replace("May", "05/")
                                                .replace("Jun", "06/")
                                                .replace("Jul", "07/")
                                                .replace("Aug", "08/")
                                                .replace("Sep", "09/")
                                                .replace("Oct", "10/")
                                                .replace("Nov", "11/")
                                                .replace("Dec", "12/")
                                                .replace(" ", "/")
                                                .replace("//", "/")
                                                .replace("AM/", "AM")
                                                .replace("PM/", "PM")
                                                .replace("2024/", "2024 ")
                                                .replace("2025/", "2025 "))
                                
                                # Check if TRXN DATE & TIME already has a value and concatenate with existing data last
                                if row_dict['TRXN DATE & TIME']:
                                    row_dict['TRXN DATE & TIME'] = formatted_date + " " + row_dict['TRXN DATE & TIME']
                                else:
                                    row_dict['TRXN DATE & TIME'] = formatted_date
                            row_dict["AMOUNT DUE"] = float(tran_e[4].replace(',', '')) + 6
                            df = df._append(row_dict, ignore_index = True)

           
                        elif len(tran_e) == 8:
                            row_dict['LP'] = tran_e[4]
                            row_dict["LP STATE"] = tran_e[3]
                            row_dict["UNIT #"] = tran_e[2]
                            row_dict['EXIT LANE/LOCATION'] = tran_e[5]
                            row_dict["REFERENCE #"] = tran_e[1]
                            row_dict["TRXN DATE & TIME"] = (tran_e[6]
                                                                .replace("Jan", "01/")
                                                                .replace("Feb", "02/")
                                                                .replace("Mar", "03/")
                                                                .replace("Apr", "04/")
                                                                .replace("May", "05/")
                                                                .replace("Jun", "06/")
                                                                .replace("Jul", "07/")
                                                                .replace("Aug", "08/")
                                                                .replace("Sep", "09/")
                                                                .replace("Oct", "10/")
                                                                .replace("Nov", "11/")
                                                                .replace("Dec", "12/")
                                                                .replace(" ", "/")
                                                                .replace("//", "/")
                                                                .replace("AM/", "AM")
                                                                .replace("PM/", "PM")
                                                                .replace("2024/", "2024 ")
                                                                .replace("2025/", "2025 ")
                                                                )
                            formatted_date, new_exit_lane = extract_and_format_date_from_exit_lane(row_dict['EXIT LANE/LOCATION'])
                            if formatted_date:
                                row_dict['EXIT LANE/LOCATION'] = new_exit_lane
                                # Format the extracted date
                                formatted_date = (formatted_date
                                                .replace("Jan", "01/")
                                                .replace("Feb", "02/")
                                                .replace("Mar", "03/")
                                                .replace("Apr", "04/")
                                                .replace("May", "05/")
                                                .replace("Jun", "06/")
                                                .replace("Jul", "07/")
                                                .replace("Aug", "08/")
                                                .replace("Sep", "09/")
                                                .replace("Oct", "10/")
                                                .replace("Nov", "11/")
                                                .replace("Dec", "12/")
                                                .replace(" ", "/")
                                                .replace("//", "/")
                                                .replace("AM/", "AM")
                                                .replace("PM/", "PM")
                                                .replace("2024/", "2024 ")
                                                .replace("2025/", "2025 "))
                                
                                # Check if TRXN DATE & TIME already has a value and concatenate with existing data last
                                if row_dict['TRXN DATE & TIME']:
                                    row_dict['TRXN DATE & TIME'] = formatted_date + " " + row_dict['TRXN DATE & TIME']
                                else:
                                    row_dict['TRXN DATE & TIME'] = formatted_date
                            row_dict["AMOUNT DUE"] = float(tran_e[7].replace(',', '')) + 6
                            df = df._append(row_dict, ignore_index = True)
                        
                        elif len(tran_e) == 9:
                            row_dict['LP'] = tran_e[4]
                            row_dict["LP STATE"] = tran_e[3]
                            row_dict["UNIT #"] = tran_e[2]
                            row_dict["REFERENCE #"] = tran_e[1]
                            row_dict['EXIT LANE/LOCATION'] = tran_e[5] + tran_e[7]
                            row_dict["TRXN DATE & TIME"] = (tran_e[8]
                                                                .replace("Jan", "01/")
                                                                .replace("Feb", "02/")
                                                                .replace("Mar", "03/")
                                                                .replace("Apr", "04/")
                                                                .replace("May", "05/")
                                                                .replace("Jun", "06/")
                                                                .replace("Jul", "07/")
                                                                .replace("Aug", "08/")
                                                                .replace("Sep", "09/")
                                                                .replace("Oct", "10/")
                                                                .replace("Nov", "11/")
                                                                .replace("Dec", "12/")
                                                                .replace(" ", "/")
                                                                .replace("//", "/")
                                                                .replace("AM/", "AM")
                                                                .replace("PM/", "PM")
                                                                .replace("2024/", "2024 ")
                                                                .replace("2025/", "2025 ")
                                                                )
                            formatted_date, new_exit_lane = extract_and_format_date_from_exit_lane(row_dict['EXIT LANE/LOCATION'])
                            if formatted_date:
                                row_dict['EXIT LANE/LOCATION'] = new_exit_lane
                                # Format the extracted date
                                formatted_date = (formatted_date
                                                .replace("Jan", "01/")
                                                .replace("Feb", "02/")
                                                .replace("Mar", "03/")
                                                .replace("Apr", "04/")
                                                .replace("May", "05/")
                                                .replace("Jun", "06/")
                                                .replace("Jul", "07/")
                                                .replace("Aug", "08/")
                                                .replace("Sep", "09/")
                                                .replace("Oct", "10/")
                                                .replace("Nov", "11/")
                                                .replace("Dec", "12/")
                                                .replace(" ", "/")
                                                .replace("//", "/")
                                                .replace("AM/", "AM")
                                                .replace("PM/", "PM")
                                                .replace("2024/", "2024 ")
                                                .replace("2025/", "2025 "))
                                
                                # Check if TRXN DATE & TIME already has a value and concatenate with existing data last
                                if row_dict['TRXN DATE & TIME']:
                                    row_dict['TRXN DATE & TIME'] = formatted_date + " " + row_dict['TRXN DATE & TIME']
                                else:
                                    row_dict['TRXN DATE & TIME'] = formatted_date
                            row_dict["AMOUNT DUE"] = float(tran_e[6].replace(',', '')) + 6
                            df = df._append(row_dict, ignore_index = True)
                       
                else:
                    for tran in transactiona:
                        tran = list(filter(''.__ne__,tran))
                        row_dict["LP"] = tran[1]
                        row_dict["LP STATE"] = tran[0]
                        row_dict["AMOUNT DUE"] = float(tran[2].replace(',', '')) + 6
                        row_dict["EXIT LANE/LOCATION"] = ""
                        row_dict["TRXN DATE & TIME"] = ""
                        row_dict["TOLL AGENCY"] = ""
                        row_dict["ACCOUNT"] = ""
                        row_dict["VIOLATION"] = ""
                        row_dict["PIN NO #"] = ""
                        row_dict["CODE 1#"] = ""
                        row_dict["CODE 2#"] = ""
                        row_dict["BILL NO#"] = ""
                        row_dict["POSTED DATE"] = ""
                        row_dict["UNIT #"] = ""                                                        
                        df = df._append(row_dict, ignore_index = True)              
        for index, row in df.iterrows():
            toll_agency = row['TOLL AGENCY']
            mapping_row = agency_mapping_df[agency_mapping_df['AGENCY'] == toll_agency]
            if not mapping_row.empty:
                mapping_value = mapping_row.iloc[0]['MAPPING']
                df.at[index, 'TOLL AGENCY'] = mapping_value            
        df.to_excel(str(outputDir + i).replace('.pdf', '') + '.xlsx', index=False)