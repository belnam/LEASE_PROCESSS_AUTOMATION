# ''''
# Premier OCR bot
# '''
# from pathlib import Path
# import re
# import pandas as pd
# import pdfplumber

# #creating a dictionary to append data extracted from the pdf
# stored_data = {
#     'TOLL AGENCY':None,
#     'LP':None,
#     'LP STATE':None,
#     'TRXN DATE & TIME':None,
#     'EXIT LANE/LOCATION':None,
#     'ACCOUNT#':None,
#     'REFERENCE # OR INVOICE #':None,
#     'VIOLATION':None,
#     'AMOUNT DUE':None,
#     'DUE DATE':None,
#     'INVOICE NO':None,
#     'PAGE NO #':None
# }

# input_path = Path('./Downloaded_Scans/')
# # input_path = Path('./converted_pdfs/')
# pdf_files = input_path.glob('*.pdf')
# output_path = './SRTS_OUTPUT/'

# agency = ''
# plate = ''
# state = ''
# date = ''
# exit_lane = ''
# trxn_date = ''
# amount = 0
# inv_no = ''
# due_date = ''
# # information = ""

# for file in pdf_files:
#     if "PREMIER" in file.name:
#         df = pd.DataFrame()
#         with pdfplumber.open(file) as pdf:
#             for x, text in enumerate(pdf.pages):
#                 # print(f"Page {x}")
#                 page = pdf.pages[x]
#                 page_data = page.extract_text()
#                 # print(page_data)
#                 # information += page_data
#                 invoice_no = re.findall(r'Invoice Number\W+(\w+)', page_data)
#                 d_date = re.findall(r'Invoice Due Date\W+(\w+\W+\w+\W+\w+)', page_data)
#                 # transaction_a = re.findall(r'Toll ID\W+(\d+).*[$](\d+\W+\d+)\n+Plate\W+(\w{2})\W+(\w+)\W+Toll Authority\W+(.*)Entry\W+(.*\n+.*)(\d{2}\W+\d+\W+\d+\W+\d+\:\d+[:]\d+)',page_data)
#                 transaction_a = re.findall(r'Toll ID\W+(\d+).*[$](\d+\W+\d+)\n+\wlate\W+(\w{2})\W+(\w+)\W+Toll Authority\W+(.*)Entry\W+(.*\n+.*)(\d{2}\W+\d+\W+\d+\W+\d+\:\d+[:]\d+)|Toll ID\W+(\w+).*[$](\d+\W+\d+)\W+(\w{2})\W+(\w+)\W+Toll Authority\W+(.*)Transponder\W+.*Entry\W+(.*\W+.*)Date Stamp\W+(\d+\W+\d+\W+\d+\W+\d+\W+\d+\W+\d+)|Toll ID\W+(\d+).*[$](\d+\W+\d+)\W+(\w{2})\W+(\w+)\W+Toll Authority\W+(.*)Entry\W+(.*\W+.*)Date Stamp\W+(\d+\W+\d+\W+\d+\W+\d+\W+\d+\W+\d+)|Toll ID\W+(\d+).*[$](\d+\W+\d+)\W+\wlate\W+(\w{2})\W+(\w+)\W+Toll Authority\W+(.*\W+.*)Entry\W+(.*)Toll\D+(\d+\W+\d+\W+\d+\W+\d+\W+\d+\W+\d+)|Toll ID\W+(\d+).*[$](\d+\W+\d+)\W+\wlate\W+(\w{2})\W+(\w+)\W+Toll Authority\W+(.*)Transponder\W+.*Entry\W+(.*\W+.*)Toll Date Stamp\W+(\d+\W+\d+\W+\d+\W+\d+\W+\d+\W+\d+)', page_data)
#                 transaction_b = re.findall(r'(CON\w+.*)\W+TOLL.*In\w+\W+(\d+).*[$|S](\d+\W+\d+)\W+.*Plate\W+(\w+)\W+.*Date\W+(\d+\/\d+\/\d+.*[:]\d+).*Location\W+(.*)',page_data)
                
#                 if invoice_no:
#                     inv_no = invoice_no[0]
#                     stored_data['INVOICE NO'] = inv_no
#                 if d_date:
#                     due_date = d_date[0]
#                     stored_data['DUE DATE'] = due_date
                    
#                 for transact in transaction_b:
#                     agency2 = transact[0].upper()
#                     reference2 = transact[1]
#                     amount2 = transact[2]
#                     lp2 = transact[3]
#                     trxn_date_time2 = transact[4]
#                     location2 = transact[5]
#                     stored_data['REFERENCE # OR INVOICE #'] = reference2
#                     stored_data['AMOUNT DUE'] = amount2
#                     stored_data['LP'] = lp2
#                     stored_data['LP STATE'] = ""
#                     stored_data['TOLL AGENCY'] = agency2
#                     stored_data['EXIT LANE/LOCATION'] = location2.replace("\n","").replace("Toll Date Stamp:","")
#                     stored_data['TRXN DATE & TIME'] = trxn_date_time2
#                     stored_data['PAGE NO #'] = page
#                     df = df._append(stored_data, ignore_index = True)
                
#                 for tran in transaction_a:
#                     trans = list(filter(None, tran))
#                     print(trans)
#                     reference = trans[0]
#                     amount = trans[1]
#                     lp = trans[2]
#                     lp_state = trans[3]
#                     agency = trans[4].upper()
#                     location = trans[5]
#                     trxn_date_time = trans[6]
#                     stored_data['REFERENCE # OR INVOICE #'] = reference
#                     stored_data['AMOUNT DUE'] = amount
#                     stored_data['LP'] = lp
#                     stored_data['LP STATE'] = lp_state
#                     stored_data['TOLL AGENCY'] = agency
#                     stored_data['EXIT LANE/LOCATION'] = location.replace("\n","").replace("Toll Date Stamp:","")
#                     stored_data['TRXN DATE & TIME'] = trxn_date_time
#                     stored_data['PAGE NO #'] = page
#                     df = df._append(stored_data, ignore_index = True)
#                 print(df.to_string())
            
#         print(f'Processing file {file.name}')
#         df.to_excel(str(output_path + file.name).replace('.pdf', '') + '.xlsx', index=False)
#     else:
#         pass        