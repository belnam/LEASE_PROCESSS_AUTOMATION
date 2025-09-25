# import os
# from pprint import pprint
# from tkinter import Y
# import pandas as pd
# import re
# import os
# import pdfplumber
# import datetime
# import getpass
# def bowmanhctraprocess(pageText):
#     output_list = []
#     df = pd.DataFrame()
#     rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
#     # print(pageText)
#     for line in pageText.split("\n"): 
   
#         # invoicenumber = re.findall(r'InvoiceNumber\W+(\w{8}$)|In\w+\W+N\w+\W+(\w{8}$)',line)
#         transaction = re.findall(r'(^\d+\D+\d{2}\D+\d{4}\D+\d{2}\D+\d+\w+)\W+(.*)[$|S](\w+\W+\w+)',line)

#         # for invoicen in invoicenumber:
#         #     invcnmb = list(invoicen)
#         #     inv_nmbr = ''.join(invcnmb)
#         #     rowDict['INVOICE#'] = inv_nmbr
#         #     output_list.append(rowDict)
#         #     dff = pd.DataFrame(output_list)
#         #     output_list = []
#         #     df = pd.concat([df, dff])
#         #     df.drop_duplicates(inplace = True)
            
#         # for trans in transaction:
#         #     transact = list(filter(None,trans))
#         #     datetime = transact[0]
#         #     location = transact[1]
#         #     amount = transact[2]
#         #     rowDict["TRXN.DATE & TIME"] = datetime
#         #     rowDict["EXIT LANE/LOCATION"] = location
#         #     rowDict["AMOUNT DUE"] = amount
#         #     rowDict["TOLL AGENCY"] = "HARRIS COUNTY TOLL ROAD AUTHORITY"
    
#             output_list.append(rowDict)
#             dff = pd.DataFrame(output_list)
#             output_list = []
#             df = pd.concat([df, dff])
#             df.drop_duplicates(inplace = True)
#     return df
            
# #         print("writing out"+i)
# #         df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)

# # bowmanhctraprocess()