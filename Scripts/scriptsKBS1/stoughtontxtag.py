# import os
# from pprint import pprint
# from tkinter import Y
# import pandas as pd
# import re
# import os
# import pdfplumber
# import datetime
# import getpass
# def stoughtontxtagprocess(pageText):
#     output_list = []
#     df = pd.DataFrame()
#     rowDict = {"TOLL AGENCY":"TXTAG","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
    
#     # invoicenumber = re.findall(r'InvoiceNumber\W+(\w+)|Invoice\W+Number\W+(\w+)',pageText)
#     transactions = re.findall(r'(\d{2}\/\d+\W+\d+.*[M])\W+\w+\W+(\w{7}|\w{8})\W+\S+\W+(.*)[-][$](\d+\W+\d+|\S+)|(\d+\/\d+\/\d+\W+\d+\W+\d+\W+\w+)\W+\w+\W+(\S+)\W+\S+\W+(.*)[-][$](\d+\W+\d+)|(\d{2}\/\d+\W+\d+)\W+\S+\W+(\w{7})\W+\S+\W+(.*)[-][$](\d+\W+\d+)|(\d{2}\/\d+\W+\d+.*[M])\W+\S+\W+(\S+)\W+(.*)[-]\W+(\w+\W+\w+)|(\d{2}\/\d+\W+\d+.*[M])\W+\w+\W+(\w{7}|\w{8})\W+\S+\W+(.*)[-][$|S](\d+\W+\d+)', pageText)
#     account = re.findall(r'^Account\W+(\w{10})', pageText)
#     due_date = re.findall(r'Pay\w+D\w+D\w+\W+(\w+\W+\w+\W+\w+)', pageText)
#     reference = re.findall(r'Statement\W+(\d{12})',pageText)
    
#     # for invoice in invoicenumber:
#     #     inv = ''.join(invoice).replace("S1","SI")
#     #     rowDict["INVOICE#"] = inv
#     #     output_list.append(rowDict)
#     #     dff = pd.DataFrame(output_list)
#     #     output_list = []
#     #     df = pd.concat([df, dff])
#     #     df.drop_duplicates(inplace = True)
#     #     df['INVOICE#'] = df.pop('INVOICE#')

#     for d_date in due_date:
#         date = d_date
#         rowDict['DUE DATE'] = date
#     if account:
#         for a_c in account:
#             ac = a_c
#             rowDict['ACCOUNT#'] = ac
#     else:
#         rowDict['ACCOUNT#'] = ""
#     for ref in reference:
#         rf = ref
#         rowDict['REFERENCE # OR INVOICE #'] = rf
#     for t_r in transactions:
#         tr = list(filter(None, t_r))
#         trxn_date = tr[0]
#         lp = tr[1]
#         exit_lane = tr[2]
#         amt = tr[3].replace(',','.').replace(';','.').replace(':','.').replace('Q','0')
#         amount = float(amt)

#         rowDict['LP'] = lp
#         rowDict['TRXN.DATE & TIME'] = trxn_date
#         rowDict['EXIT LANE/LOCATION'] = exit_lane
#         rowDict['AMOUNT DUE'] = amount
        
#         output_list.append(rowDict)
#         dff = pd.DataFrame(output_list)
#         output_list = []
#         df = pd.concat([df, dff])
#         df.drop_duplicates(inplace = True)
       
#     return df
                    
                            
# #         print("writing out"+i)
# #         df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)

# # stoughtontxtagprocess()