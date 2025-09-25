# import os
# from pprint import pprint
# from tkinter import Y
# import pandas as pd
# import re
# import os
# import pdfplumber
# import datetime
# import getpass
# def bowmansrtaprocess(pageText):
#     output_list = []
#     df = pd.DataFrame()
#     rowDict = {"TOLL AGENCY":"STATE ROAD AND TOLLWAY AUTHORITY","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
#     # print(pageText)
#     invoicenumber = re.findall(r'InvoiceNumber\W+(\w+.*)|Invoice\W+Number\W+(\w+.*)',pageText)
#     reference =re.findall(r'No\w+\W+(\d+)',pageText)
#     # duedate =re.findall(r'Due.*[:](\d+\W+\d+\W+\d+)',pageText)
#     transaction = re.findall(r'(\d+\w+)\W+([A-Z]{2})\W+(\w+)\W+(\d+\W+\d+\W+\d+).*N\W+(.*)[$|S](\d+\W+\d+)',pageText)
    
#     for invoice in invoicenumber:
#         inv = ''.join(invoice).replace("S1","SI")
#         rowDict["INVOICE#"] = inv
#         output_list.append(rowDict)
#         dff = pd.DataFrame(output_list)
#         output_list = []
#         df = pd.concat([df, dff])
#         df.drop_duplicates(inplace = True)
#     for refer in reference:
#         ref = ''.join(refer)
#         rowDict["REFERENCE # OR INVOICE #"] = ref
#     for trans in transaction:
#         rowDict["LP"] = trans[0]
#         rowDict["LP STATE"] = trans[1]
#         rowDict["VIOLATION#"] = trans[2]
#         rowDict["TRXN.DATE & TIME"] = trans[3]
#         rowDict["EXIT LANE/LOCATION"] = trans[4]
#         rowDict["AMOUNT DUE"] = trans[5]
        
        
        
#         output_list.append(rowDict)
#         dff = pd.DataFrame(output_list)
#         output_list = []
#         df = pd.concat([df, dff])
#         df.drop_duplicates(inplace = True)
#     return df
                 
                            
# #         print("writing out"+i)
# #         df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)

# # bowmansrtaprocess()
               