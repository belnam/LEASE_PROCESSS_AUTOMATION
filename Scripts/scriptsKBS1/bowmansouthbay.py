# '''
# Southbay ocr bot
# '''
# from pathlib import Path
# import re
# import pandas as pd
# import pdfplumber
# import os
# import getpass

# #creating a dictionary to append data extracted from the pdf
# def bowmansouthbayprocess():
#     rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
#     username = getpass.getuser()
#     workingDir = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\attachments_output\\"
#     outputDir = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\SRTS_OUTPUT\\"
#     for fname in os.listdir(workingDir):
#         output_list = []
#         df = pd.DataFrame()
#         with pdfplumber.open(workingDir+fname) as pdf:
#           for page in pdf.pages:
#             pageText = page.extract_text()        
#             print(pageText)
#         #     invoicenumber = re.findall(r'InvoiceNumber\W+(\w+)|Invoice\W+Number\W+(\w+)',pageText)
#         #     reference =re.findall(r'Notif\w+Nu\w+\W+(\w+)|Notif\w+\W+Nu\w+\W+(\w+)',pageText)
#         #     lpstate = re.findall(r'Li\w+P\w+\W+(\w+)\W+\w+\W+(\w+)|Li\w+\W+P\w+\W+(\w+)\W+\w+\W+(\w+)',pageText)
#         #     transaction_vio = re.findall(r'(\d+)\W+\d+.*[:]\w+\W+.*[$|S]\d+\W+\d+\s+\W+\d+\W+\d+.*[$]\w+\W+\w+|(\d{9})\W+\d+.*[$|S]',pageText)
#         #     transaction_date = re.findall(r'\d+\W+(\d+.*[:]\w+)\W+.*[$|S]\d+\W+\d+\s+\W+\d+\W+\d+.*[$]\w+\W+\w+|\d+\W+(\d+.*[-]\d+\W+\d\S+).*[$|S]',pageText)
#         #     transaction_lane = re.findall(r'\d+\W+\d+.*[:]\w+\W+(.*)[$|S]\d+\W+\d+\s+\W+\d+\W+\d+.*[$]\w+\W+\w+|\d+\W+\d+.*[-]\d+\W+\d\S+(.*)[$|S].*[$|S].*[$|S]',pageText)
#         #     transaction_amnt = re.findall(r'\d+\W+\d+.*[:]\w+\W+.*[$|S]\d+\W+\d+\s+\W+\d+\W+\d+.*[$](\w+\W+\w+)|\d+\W+\d+.*[-]\d+\W+\d\S+.*[$|S].*[$|S].*[$|S](.*)',pageText)
#         #     duedate = re.findall(r'Am.*D.*b\w+(.*)[S|$]',pageText)
#         #     # for invoice in invoicenumber:
#         #     #     inv = ''.join(invoice).replace("S1","SI")
#         #     #     rowDict["INVOICE#"] = inv
#         #     #     output_list.append(rowDict)
#         #     #     dff = pd.DataFrame(output_list)
#         #     #     output_list = []
#         #     #     df = pd.concat([df, dff])
#         #     #     df.drop_duplicates(inplace = True)
#         #     for ref in reference:
#         #         refer = ''.join(ref)
#         #         rowDict['REFERENCE # OR INVOICE #'] = refer
#         #     for date in duedate:
#         #         rowDict['DUE DATE'] = date
#         #         # refer = ''.join(ref)
#         #     for state in lpstate:
#         #         date = ''.join(state)
#         #         rowDict['LP'] = state[0]
#         #         rowDict['LP STATE'] = state[1]
#         #     for transvio in transaction_vio:
#         #         tranvio = ''.join(transvio)
#         #         rowDict['VIOLATION#'] = tranvio
#         #     for transdate in transaction_date:
#         #         trandate = ''.join(transdate)
#         #         rowDict['TRXN.DATE & TIME'] = trandate
#         #     for translane in transaction_lane:
#         #         tranlane = ''.join(translane)
#         #         rowDict['EXIT LANE/LOCATION'] = tranlane
#         #     for transamnt in transaction_amnt:
#         #         tranamnt = ''.join(transamnt)
#         #         rowDict['AMOUNT DUE'] = tranamnt
           
#         #     # for trans in transaction:
#         #     #     rowDict['VIOLATION#'] = trans[0]
#         #     #     rowDict['TRXN DATE & TIME'] = trans[1]
#         #     #     rowDict['EXIT LANE/LOCATION'] = trans[2]
#         #     #     rowDict['AMOUNT DUE'] = trans[3]
           
                
                
#         #         output_list.append(rowDict)
#         #         dff = pd.DataFrame(output_list)
#         #         output_list = []
#         #         df = pd.concat([df, dff])
#         #         df.drop_duplicates(inplace = True)
          
       
#         # print("writing out"+fname)
#         # df.to_excel(str(outputDir+fname).replace(".pdf","")+".xlsx", index=False)
# bowmansouthbayprocess()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        