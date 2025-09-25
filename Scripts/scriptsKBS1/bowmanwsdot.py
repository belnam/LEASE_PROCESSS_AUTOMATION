# ''''
# WSDOT OCR BOT
# '''
# from pathlib import Path
# import re
# import pandas as pd
# import pdfplumber
# import getpass
# import os

# #creating a dictionary to append data extracted from the pdf
# def bowmanwsdotprocess(pageText):
#     output_list = []
#     df = pd.DataFrame()
#     # print(pageText)
#     rowDict = {
#         'TOLL AGENCY':"WSDOT",
#         'LP':None,
#         'LP STATE':None,
#         'TRXN.DATE & TIME':None,
#         'EXIT LANE/LOCATION':None,
#         'ACCOUNT#':None,
#         'REFERENCE # OR INVOICE #':None,
#         'VIOLATION#':None,
#         'AMOUNT DUE':None,
#         'DUE DATE':None,
#         'PIN NO #':None,
#         'INVOICE#':None,
#     }

#     invoicenumber = re.findall(r'InvoiceNumber\W+(\w+)|Invoice\W+Number\W+(\w+)',pageText)
  

#     for invoice in invoicenumber:
#         inv = ''.join(invoice)
#         rowDict["INVOICE#"] = inv.replace("S1","SI")
#         output_list.append(rowDict)
#         dff = pd.DataFrame(output_list)
#         output_list = []
#         df = pd.concat([df, dff])
#         df.drop_duplicates(inplace = True)
   
        
#     output_list.append(rowDict)
#     dff = pd.DataFrame(output_list)
#     output_list = []
#     df = pd.concat([df, dff])
#     df.drop_duplicates(inplace = True)
#     return df
                            
                
                
# #         print("writing out"+fname)
# #         df.to_excel(str(output_path+fname).replace(".pdf","")+".xlsx", index=False)
# # bowmanwsdotprocess()