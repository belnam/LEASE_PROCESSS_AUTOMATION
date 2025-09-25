# import os
# import pandas as pd
# import re
# import os
# import pdfplumber
# import getpass

# def paturnpikeprocess(pageText):
#         output_list = []
#         df = pd.DataFrame()
    
#         rowDict = {"TOLL AGENCY":"PA TURNPIKE","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
   
#         # print(pageText)
#         # invoicenumber = re.findall(r'InvoiceNumber\W+(S\w.*)|Invoice\W+Number\W+(S\w.*)',pageText)
#         # transaction = re.findall(r'PLATE\W+\d+\W+\d+\W+\d+.*[:]\d{2}\s+\w.*[ ](\d{2}\W+\d+\W+\d+.*[:]\w+)\W+(.*)\s+\w+\s+\W+(\w+\W+\w+)|PLATE\W+(\d+\W+\d+\W+\d+.*[:]\d+)\W+(.*)\W+\w+[ ]\W+(\w+\W+\w+)',pageText)
#         # transdatetime= re.findall(r'PLATE\W+\d+\W+\d+\W+\d+.*[:]\d{2}\s+\w.*[ ](\d{2}\W+\d+\W+\d+.*[:]\w+)\W+.*\s+\w+\s+\W+\w+\W+\w+|PLATE\W+(\d+\W+\d+\W+\d+.*[:]\d+)\W+.*\W+\w+[ ]\W+\w+\W+\w+',pageText)
#         amountdue=re.findall(r'PLATE\W+\d+\W+\d+\W+\d+.*[:]\d{2}\s+\w.*[ ]\d{2}\W+\d+\W+\d+.*[:]\w+\W+.*\s+\w+\s+\W+(\w+\W+\w+)|PLATE\W+\d+\W+\d+\W+\d+.*[:]\d+\W+.*\W+\w+[ ]\W+(\w+\W+\w+)',pageText)
#         # location = re.findall(r'PLATE\W+\d+\W+\d+\W+\d+.*[:]\d{2}\s+\w.*[ ]\d{2}\W+\d+\W+\d+.*[:]\w+\W+(.*)\s+\w+\s+\W+\w+\W+\w+|PLATE\W+\d+\W+\d+\W+\d+.*[:]\d+\W+(.*)\W+\w+[ ]\W+\w+\W+\w+',pageText)
#         # print(transdatetime)
        
#         # for invoice in invoicenumber:
#         #     inv = ''.join(invoice).replace("S1","SI")
#         #     rowDict["INVOICE#"] = inv
#         #     output_list.append(rowDict)
#         #     dff = pd.DataFrame(output_list)
#         #     output_list = []
#         #     df = pd.concat([df, dff])
#         #     df.drop_duplicates(inplace = True)
    
#         # for trans in transdatetime:
#         #     tran = list(filter(None,trans))
#         #     tranxs =''.join(tran)
#         #     rowDict["TRXN.DATE & TIME"]=tranxs 
#         # for loc in location:
#         #     locat = list(filter(None,loc))
#         #     locate =''.join(locat)
#         #     rowDict["EXIT LANE/LOCATION"]=locate.replace("ORT 2","ORT")
            
#         # for amt in amountdue:
#         #     amount =''.join(amt).replace(",",".").replace(" ","").replace("I","")
#         #     rowDict["AMOUNT DUE"]=amount
        
#             output_list.append(rowDict)
#             dff = pd.DataFrame(output_list)
#             output_list = []
#             df = pd.concat([df, dff])
#             df.drop_duplicates(inplace = True)
#         return df
                            

# # print("writing out"+fname)
# # df.to_excel(str(outputDir+fname).replace(".pdf","")+".xlsx", index=False)
# # paturnpikeprocess()