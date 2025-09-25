# import os
# from pprint import pprint
# from tkinter import Y
# import pandas as pd
# import re
# import os
# import pdfplumber
# import datetime
# import getpass
# def bowmane470process(pageText):
#     output_list = []
#     df = pd.DataFrame()
#     rowDict = {"TOLL AGENCY":"E-470 PUBLIC HIGHWAY AUTHORITY","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
 
#     # invoicenumber = re.findall(r'InvoiceNumber\W+(\w+)|Invoice\W+Number\W+(\w+)',pageText)
#     # reference = re.findall(r'(\d{10})\W+\d+\W+\d+\W+\d+',pageText)
#     # duedate =re.findall(r'\d{10}\W+.*[$|S]\S+\W+(\w+\W+\d+\W+\w+)',pageText)
#     # transaction = re.findall(r'Li.*P\w+\#(.*\w+)([A-Z]\w+).*\n+T.*Tr.*\s(\d+\/\d+\/.*[:]\w+).*\d+\/\d+(.*)[$|S](\d.*)|T.*Tr.*\s(\d+\/\d+\/.*[:]\w+).*\d+\/\d+(.*)[$|S](\d.*)',pageText)
#     transactionB = re.findall(r'T.*Tr.*\s(\d+\/\d+\/.*[:]\w+).*\d+\/\d+(.*)[$|S](\d.*)',pageText)
    
#     # for invoice in invoicenumber:
#     #     inv = ''.join(invoice).replace("S1","SI")
#     #     rowDict["INVOICE#"] = inv
#     # for due in duedate:
#     #     date = ''.join(due)
#     #     rowDict["DUE DATE"] = date
#     # for ref in reference:
#     #     refer = ''.join(ref)
#     #     rowDict["REFERENCE # OR INVOICE #"] = refer
    
#     for trans in transaction:
#         tran = list(filter(None, trans))
#         if len(tran) == 5:
#             rowDict["LP"] = tran[0]
#             rowDict["LP STATE"] = tran[1]
#             rowDict["TRXN.DATE & TIME"] = tran[2]
#             rowDict["EXIT LANE/LOCATION"] = tran[3]
#             rowDict["AMOUNT DUE"] = tran[4]
#         elif len(tran) ==3:
#             rowDict["TRXN.DATE & TIME"] = tran[0]
#             rowDict["EXIT LANE/LOCATION"] = tran[1]
#             rowDict["AMOUNT DUE"] = tran[2]
    
#         output_list.append(rowDict)
#         dff = pd.DataFrame(output_list)
#         output_list = []
#         df = pd.concat([df, dff])
#         df.drop_duplicates(inplace = True)
#     return df
    
                
# #         print("writing out"+i)
# #         df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)

# # bowmane470process()