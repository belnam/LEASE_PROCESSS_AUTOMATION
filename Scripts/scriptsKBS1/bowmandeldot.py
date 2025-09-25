# import os
# from tkinter import Y
# import pandas as pd
# import re
# import os
# import pdfplumber
# import datetime
# import getpass
# def bowmandeldotprocess(pageText):
#     output_list = []
#     df = pd.DataFrame()
#     rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
#     # print(pageText)
#     # invoicenumber = re.findall(r'InvoiceNumber\W+(\w+\w.*)|Invoice\W+Number\W+(\w+\w.*)',pageText)
#     violation = re.findall(r'FORVIOLATION(\w+\W+\w+)|F\w+\W+VIOLATION(\w+\W+\w+)|FO\w+\W+V\w+\W+(\w+\W+\w+)|F\w+VIO\w+\W+(\w+\W+\w+)',pageText)
#     datetime = re.findall(r'D\w+\W+(\w+\W+\w+\W+\w+)\W+T\w+\W+(\w+\W+\w+\W+\d+)',pageText)
#     location = re.findall(r'P\w+\W+(\w+)\W+L\w+\W+(\w+)',pageText)
#     # lpstate = re.findall(r'Li\w+\:(\w{2})\W+(\w+)|Li\w+\W+\w+\:(\w{2})\W+(\w+)',pageText)
#     # duedate = re.findall(r'PA\w+\W+(\d+\W+\d+\W+\d+)|P\w+\W+D\w+\W+B\w+\W+(\d+\W+\d+\W+\d+)|P\w+\W+D\w+\w+\W+(\d+\W+\d+\W+\d+)|P\w+\w+\W+B\w+\W+(\d+\W+\d+\W+\d+)|Re\w+D\w+D\w+\W+(\w+\W+\w+\W+\w+)|Re\w+\W+D\w+\W+D\w+\W+(\w+\W+\w+\W+\w+)',pageText)
#     amountdue = re.findall(r'BA\w+D\w+\W+(\d+\W+\w+)|BA\w+\W+DU\w+\W+(\d+\W+\w+)',pageText)
#     # transactiondeldotb = re.findall(r'In\w+N\w+\W+(\w+\W+\w+)\W+L\w+P\w+\W+S\w+\W+(\w+)\W+(\w+)\W+A\w+N\w+\W+(\w+)|In\w+\W+N\w+\W+(\w+\W+\w+)\W+L\w+P\w+\W+S\w+\W+(\w+)\W+(\w+)\W+A\w+N\w+\W+(\w+)|In\w+\W+N\w+\W+(\w+\W+\w+)\W+L\w+\W+P\w+\W+S\w+\W+(\w+)\W+(\w+)\W+A\w+N\w+\W+(\w+)|In\w+\W+N\w+\W+(\w+\W+\w+)\W+L\w+\W+P\w+\W+S\w+\W+(\w+)\W+(\w+)\W+A\w+\W+N\w+\W+(\w+)',pageText)
#     transactiondelb = re.findall(r'\d+\W+\d+\W+\d+\W+(\d+.*[:]\w+).*Toll\W+(\w+)\W+[$](\w+\W+\w+)',pageText)
#     # duedateb = re.findall(r'Re\w+D\w+D\w+\W+(\w+\W+\w+\W+\w+)|Re\w+\W+D\w+\W+D\w+\W+(\w+\W+\w+\W+\w+)',pageText)
#     # for invoice in invoicenumber:
#     #     inv = ''.join(invoice)
#     #     rowDict["INVOICE#"] = inv
#     #     output_list.append(rowDict)
#     #     dff = pd.DataFrame(output_list)
#     #     output_list = []
#     #     df = pd.concat([df, dff])
#     for timedate in datetime:
#         date_time = timedate[0] +' ' +timedate[1]
#         rowDict["TRXN.DATE & TIME"] = date_time
#     for locate in location:
#         rowDict["EXIT LANE/LOCATION"] = locate[0] +' ' +locate[1]
#     # for lstate in lpstate:
#     #     license = lstate[0]
#     #     state = lstate[1]
#     #     rowDict["LP"] = license
#     #     rowDict["LP STATE"] = state
#     # for datedue in duedate:
#     #     date = ''.join(datedue)
#     #     rowDict["DUE DATE"] = date
#     if violation:
#         for vio in violation:
#             violate = ''.join(vio)
#             rowDict["VIOLATION#"] = violate
#     else:
#         rowDict["VIOLATION#"] = ""
#     for amount in amountdue:
#         amt = ''.join(amount).replace(",",".")
#         amnt = float(amt)
#         rowDict["AMOUNT DUE"] = amnt
#         rowDict["TOLL AGENCY"] = "DELAWARE DEPARTMENT OF TRANSPORTATION"
      
        
#     # if transactiondeldotb:
#     #     for transaction in transactiondeldotb:
#     #         rowDict["REFERENCE # OR INVOICE #"] = transaction[0]
#     #         rowDict["LP"] = transaction[1]
#     #         rowDict["LP STATE"] = transaction[2]
#     #         rowDict["ACCOUNT#"] = transaction[3]
#     # else:y
#     #     rowDict["REFERENCE # OR INVOICE #"] = ""
#     #     rowDict["ACCOUNT#"] = ""
        
#     for trans in transactiondelb:
#         rowDict["TRXN.DATE & TIME"] = trans[0]
#         rowDict["EXIT LANE/LOCATION"] = trans[1]
#         rowDict["AMOUNT DUE"] = trans[2]
#         rowDict["TOLL AGENCY"] = "DELAWARE DEPARTMENT OF TRANSPORTATION"
        
#         output_list.append(rowDict)
#         dff = pd.DataFrame(output_list)
#         output_list = []
#         df = pd.concat([df, dff])
#         df.drop_duplicates(inplace = True)
#     return df
    
    
# #             print("writing out"+i)
# #             df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)


# # bowmandeldotprocess()