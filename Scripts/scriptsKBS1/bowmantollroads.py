# import pandas as pd
# import pdfplumber
# import re as reg_ex
# import os
# import getpass
# import re

# def bowmantollroadsprocess(pageText):
#     output_list = []
#     df = pd.DataFrame()
#     rowDict = {"TOLL AGENCY":"THE TOLL ROADS","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
#     # print(pageText)
#     invoicenumber = re.findall(r'InvoiceNumber\W+(\w+)|Invoice\W+Number\W+(\w+)',pageText)
#     # transaction = re.findall(r'(\d{2}\D+\d{2}\D+\d+\:\d.*[M])\s+(\w+)\s+(.*)[$|S]\w+\W+\w+\W+\w+\W+\w+\W+(\S+).*[\/]\w+\W+(\S+)',pageText)
#     # reference = reg_ex.findall(r'Reference#\D+(\S+)|R\w+#(\w+)',pageText)
#     # duedate = reg_ex.findall(r'Amount Due Before\D+(\S+\d+)|A\w+D\w+Before(\S+)|A\w+\W+D\w+\W+Before\W+(\S+)',pageText)
    
#     for invoice in invoicenumber:
#         inv = ''.join(invoice).replace("S1","SI")
#         rowDict["INVOICE#"] = inv
#         # output_list.append(rowDict)
#         # dff = pd.DataFrame(output_list)
#         # output_list = []
#         # df = pd.concat([df, dff])
        
#     # for ref in reference:
#     #     refer = ''.join(ref)
#     #     rowDict['REFERENCE # OR INVOICE #'] = refer.replace(",","").replace(".","")
#     # for date in duedate:
#     #     rowDict['DUE DATE'] = date 
#     # for trans in transaction:
#     #     rowDict['TRXN.DATE & TIME'] = trans[0]
#     #     rowDict['LP'] = trans[1]
#     #     rowDict['EXIT LANE/LOCATION'] = trans[2]
#     #     rowDict['AMOUNT DUE'] = trans[3].replace(",",".")
#     #     rowDict['VIOLATION#'] = trans[4]
       
#     output_list.append(rowDict)
#     dff = pd.DataFrame(output_list)
#     output_list = []
#     df = pd.concat([df, dff])
#     return df

                        
# #             print("writing out"+fname)
# #             df.to_excel(str(outputDir+fname).replace(".pdf","")+".xlsx", index=False)
# # tollroadsprocess()