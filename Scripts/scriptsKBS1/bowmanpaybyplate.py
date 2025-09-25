# import os
# from pprint import pprint
# from tkinter import Y
# import pandas as pd
# import re
# import os
# import pdfplumber
# import datetime
# import getpass
# def bowmanpaybyplatemaprocess(pageText):
#     output_list = []
#     df = pd.DataFrame()
#     rowDict = {"TOLL AGENCY":"PAY BY PLATE MA","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
#     # print(pageText)
#     # invoicenumber = re.findall(r'InvoiceNumber\W+(S.*)|Invoice\W+Number\W+(S.*)',pageText)
#     # reference = re.findall(r'I\w+N\w+\W+(\d+)|I\w+\W+N\w+\W+(\d+)',pageText)
#     # duedate = re.findall(r'(\d+\/\d+\W+\d+)\s+[$|S]\d+\W+\d+',pageText)
#     # transaction = re.findall(r'\d+\W+\d+\W+\d+\W+Toll.*[ ]([A-Z]{2})\W+(\w+).*(\d+\d+\/\d+\/\d+.*[:]\d+)\W+(.*)\W+\w+\W+[$|S](\w+\W+\d+)',pageText)

#     # for invoice in invoicenumber:
#     #     inv = ''.join(invoice).replace("S1","SI")
#     #     rowDict["INVOICE#"] = inv
#     #     output_list.append(rowDict)
#     #     dff = pd.DataFrame(output_list)
#     #     output_list = []
#     #     df = pd.concat([df, dff])
#     #     df.drop_duplicates(inplace = True)
#     # for ref in reference:
#     #     refer = ''.join(ref)
#     #     rowDict["REFERENCE # OR INVOICE #"] = refer
#     # for due in duedate:
#     #     date = ''.join(due)
#     #     rowDict["DUE DATE"] = date
#     # for trans in transaction:
#     #     rowDict["LP STATE"] = trans[0]
#     #     rowDict["LP"] = trans[1]
#     #     rowDict["TRXN.DATE & TIME"] = trans[2]
#     #     rowDict["EXIT LANE/LOCATION"] = trans[3]
#     #     rowDict["AMOUNT DUE"] = trans[4]

    
#         output_list.append(rowDict)
#         dff = pd.DataFrame(output_list)
#         output_list = []
#         df = pd.concat([df, dff])
#         df.drop_duplicates(inplace = True)
#     return df
                
                            
# #         print("writing out"+i)
# #         df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)

# # bowmanpaybyplatemaprocess()