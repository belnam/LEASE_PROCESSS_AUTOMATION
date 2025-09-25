# ''''
# Globalvia Pocahontas OCR BOT
# '''
# from pathlib import Path
# import re
# import pandas as pd
# import pdfplumber
# import getpass
# import os

# #creating a dictionary to append data extracted from the pdf
# def bowmanpocahontasprocess(pageText):
#                 output_list = []
#                 df = pd.DataFrame()
#                 # print(pageText)
#                 rowDict = {
#                     'TOLL AGENCY':"GLOBALVIA POCAHONTAS PARKWAY",
#                     'LP':None,
#                     'LP STATE':None,
#                     'TRXN DATE & TIME':None,
#                     'EXIT LANE/LOCATION':None,
#                     'ACCOUNT#':None,
#                     'REFERENCE # OR INVOICE #':None,
#                     'VIOLATION#':None,
#                     'AMOUNT DUE':None,
#                     'DUE DATE':None,
#                     'PIN NO #':None,
#                     'SCAN NO#':None
#                 }

#                 invoicenumber = re.findall(r'InvoiceNumber\W+(\w+)|Invoice\W+Number\W+(\w+)',pageText)
#                 transactions = re.findall(r'(\d+)\W+(.*)\s+(\d+\W+\d+\W+\d+.*[M]).*[$|S](\w+\W+\w+)', pageText)
               
#                 for invoice in invoicenumber:
#                     inv = ''.join(invoice).replace("S1","SI")
#                     rowDict["INVOICE#"] = inv
#                     output_list.append(rowDict)
#                     dff = pd.DataFrame(output_list)
#                     output_list = []
#                     df = pd.concat([df, dff])
#                     df.drop_duplicates(inplace = True)
             
#                 for trans in transactions:
#                     violation = trans[0]
#                     location = trans[1]
#                     datetime = trans[2]
#                     amount = trans[3]
               
#                     rowDict['VIOLATION#'] = violation
#                     rowDict['EXIT LANE/LOCATION'] = location
#                     rowDict['TRXN DATE & TIME'] = datetime
#                     rowDict['AMOUNT DUE'] = amount
                   
#                     output_list.append(rowDict)
#                     dff = pd.DataFrame(output_list)
#                     output_list = []
#                     df = pd.concat([df, dff])
#                     df.drop_duplicates(inplace = True)
#                 return df
                    
# #         #         # print(df)
# #         print("writing out"+fname)
# #         df.to_excel(str(outputDir+fname).replace(".pdf","")+".xlsx", index=False)
# # bowmanpocahontasprocess()