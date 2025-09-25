''''
Premier OCR bot
'''
from pathlib import Path
import re
import pandas as pd
import pdfplumber

#creating a dictionary to append data extracted from the pdf
stored_data = {
    'TOLL AGENCY':None,
    'LP':None,
    'LP STATE':None,
    'TRXN DATE & TIME':None,
    'EXIT LANE/LOCATION':None,
    'ACCOUNT':None,
    'REFERENCE # ':None,
    'VIOLATION':None,
    'AMOUNT DUE':None,
    'DUE DATE':None,
    'PIN NO #':None,
    'INVOICE #':None,
    'CODE 1#':None,
    'CODE 2#':None,
    'BILL NO#':None,
    'POST DATE/TIME':None,
    'UNIT #':None
}

input_path = Path('./Downloaded_Scans/')
# input_path = Path('./converted_pdfs/')
pdf_files = input_path.glob('*.pdf')
output_path = './SRTS_OUTPUT/'
agency_mapping_df = pd.read_excel("Scripts\Agency_Names.xlsx")

agency = ''
plate = ''
state = ''
date = ''
exit_lane = ''
trxn_date = ''
amount = 0
inv_no = ''
due_date = ''
# information = ""
for file in pdf_files:
        df = pd.DataFrame()
        with pdfplumber.open(file) as pdf:
            for x, text in enumerate(pdf.pages):
                # print(f"Page {x}")
                page = pdf.pages[x]
                page_data = page.extract_text()
                print(page_data)

                invoice_no = re.findall(r'Invoice Number\W+(\w+)', page_data)
                d_date = re.findall(r'Invoice Due Date\W+(\w+\W+\w+\W+\w+)', page_data)
                transaction_a = re.findall(r'Toll\W+\w+\W+(\d+).*\$(\d+\W+\d+).*\n+.*?(\w+)\s+(\w+)\s+Toll\W+\w+\W+(.*)\W+.*Entry\W+(.*\W+.*)Toll\W+\w+\W+\w+\W+(.*\W+.*:\d{2}.*:\d{2})', page_data)
                transaction_b = re.findall(r'\d+\s+(\D.*?)?Invoice\W+(\w+\d+\w+).*?Toll.*\$(\w+\W+\w+).*\W+.*Plate\W+(\w+)\W+.*Date\W+(\w+.*:\d{2}\W+\w+)\W+.*Lo\w+\W+(.*\W+)((?!.*\$).*$)', page_data, re.MULTILINE)
                transaction_c = re.findall(r'Toll\W+\w+\W+(\d+).*Plate\W+(\w{2}).*\$(\d+\W+\d+).*\n+.*?(\w+).*Toll\W+Authority\W+(.*)Entry\W+(.*\W+.*)\W+Toll\W+\w+\W+\w+\W+(.*)', page_data)

        
                if invoice_no:
                    inv_no = invoice_no[0]
                    stored_data['INVOICE #'] = inv_no
                if d_date:
                    due_date = d_date[0]
                    stored_data['DUE DATE'] = due_date
                    # df = df._append(stored_data, ignore_index = True)
                    
                for transact in transaction_b:
                    agency2 = transact[0].upper()
                    reference2 = transact[1]
                    amount2 = transact[2]
                    LP2 = transact[3]
                    trxn_date_time2 = transact[4]
                    location2 = transact[5]+" "+transact[6]
                    stored_data['REFERENCE # '] = reference2
                    stored_data['AMOUNT DUE'] = amount2
                    stored_data['LP'] = LP2
                    stored_data['LP STATE'] = ""
                    stored_data['TOLL AGENCY'] = agency2
                    stored_data['EXIT LANE/LOCATION'] = location2.replace("\n","").replace("Toll Date Stamp:","")
                    stored_data['TRXN DATE & TIME'] = trxn_date_time2
                    stored_data['PAGE NO #'] = page
                    df = df._append(stored_data, ignore_index = True)
                
                for tran in transaction_a:
                    trans = list(filter(None, tran))
                    reference = trans[0]
                    amount = trans[1]
                    LP = trans[3]
                    LP_state = trans[2]
                    agency = trans[4].upper()
                    location = trans[5]
                    trxn_date_time = trans[6]
                    stored_data['REFERENCE # '] = reference
                    stored_data['AMOUNT DUE'] = amount
                    stored_data['LP'] = LP
                    stored_data['LP STATE'] = LP_state
                    stored_data['TOLL AGENCY'] = agency
                    stored_data['EXIT LANE/LOCATION'] = location.replace("\n","").replace("Toll Date Stamp:","")
                    stored_data['TRXN DATE & TIME'] = trxn_date_time
                    stored_data['PAGE NO #'] = page
                    df = df._append(stored_data, ignore_index = True)

                for tranx in transaction_c:
                    tranxx = list(filter(None, tranx))
                    referencec = tranxx[0]
                    amountc = tranxx[2]
                    LPc = tranxx[3]
                    LP_statec = tranxx[1]
                    agencyc = tranxx[4].upper()
                    locationc = tranxx[5]
                    try:
                        trxn_date_timec = tranxx[6]
                    except: 
                        pass
                    stored_data['REFERENCE # '] = referencec
                    stored_data['AMOUNT DUE'] = amountc
                    stored_data['LP'] = LPc
                    stored_data['LP STATE'] = LP_statec
                    stored_data['TOLL AGENCY'] = agencyc
                    stored_data['EXIT LANE/LOCATION'] = locationc
                    stored_data['TRXN DATE & TIME'] = trxn_date_timec
                    stored_data['PAGE NO #'] = page
                    df = df._append(stored_data, ignore_index = True)
                # print(df.to_string())

                # Apply agency mapping
        for index, row in df.iterrows():
            toll_agency = row['TOLL AGENCY']
            mapping_row = agency_mapping_df[agency_mapping_df['AGENCY'] == toll_agency]
            if not mapping_row.empty:
                mapping_value = mapping_row.iloc[0]['MAPPING']
                df.at[index, 'TOLL AGENCY'] = mapping_value
            
        print(f'Processing file {file.name}')
        df.to_excel(str(output_path + file.name).replace('.pdf', '') + '.xlsx', index=False)
    # else:
    #     pass        