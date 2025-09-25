# import os
# from pprint import pprint
# from tkinter import Y
# import pandas as pd
# import re
# import os
# import pdfplumber
# import datetime

# def bowmanmdtaprocess(pageText):
#                 output_list = []
#                 df = pd.DataFrame()
#                 rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
    
#                 # print(pageText)
#                 # invoicenumber = re.findall(r'InvoiceNumber\W+(\w+)|Invoice\W+Number\W+(\w+)',pageText)
#                 reference = re.findall(r'V\w+T\w+T\w+N\w+\W+(\w+\d+\W+\w+)|V\w+\W+T\w+T\w+N\w+\W+(\w+\d+\W+\w+)|V\w+T\w+\W+T\w+N\w+\W+(\w+\d+\W+\w+)|V\w+T\w+T\w+\W+N\w+\W+(\w+\d+\W+\w+)|V\w+\W+T\w+\W+T\w+N\w+\W+(\w+\d+\W+\w+)|V\w+\W+T\w+T\w+\W+N\w+\W+(\w+\d+\W+\w+)|V\w+T\w+\W+T\w+\W+N\w+\W+(\w+\d+\W+\w+)',pageText)
#                 lpstate = re.findall(r'Sta\w+\W+Lic.*[ ](\w+)\W+(\w+)',pageText)
#                 location = re.findall(r'V\w+T\w+Transaction\s+(.*)|V\w+\W+T\w+Transaction\s+(.*)|V\w+T\w+\W+Transaction\s+(.*)|V\w+\W+T\w+\W+Transaction\s+(.*)',pageText)
#                 datetime =re.findall(r'Tim\w+o\w+T\w+\W+(.*[:].*)|T\w+\W+o\w+T\w+\W+(.*[:].*)|Tim\w+\W+o\w+\W+T\w+\W+(.*[:].*)|Tim\w+o\w+\W+T\w+\W+(.*[:].*)',pageText)
#                 amountdue = re.findall(r'A\w+D\w+\W+(\w+\W+\d+)|A\w+\W+D\w+\W+(\w+\W+\d+)',pageText)
#                 duedate = re.findall(r'By\:(\w+\W+\w+\W+\w+)',pageText)
                
#                 # for invoice in invoicenumber:
#                 #     inv = ''.join(invoice).replace("S1","SI")
#                 #     rowDict["INVOICE#"] = inv
#                 #     output_list.append(rowDict)
#                 #     dff = pd.DataFrame(output_list)
#                 #     output_list = []
#                 #     df = pd.concat([df, dff])
#                 #     df.drop_duplicates(inplace = True)
#                 for amount in amountdue:
#                     amnt = ''.join(amount).replace(",","")
#                     try:
#                         amt = float(amnt)
#                         rowDict["AMOUNT DUE"] = amt
#                     except:
#                         pass
#                 for date in duedate:
#                     due = ''.join(date)
#                     rowDict["DUE DATE"] = due
#                 for refer in reference:
#                     ref = ''.join(refer)
#                     rowDict["REFERENCE # OR INVOICE #"] = ref
#                 for statelp in lpstate:
#                     licensestate = statelp[0]
#                     license = statelp[1]
#                     rowDict["LP"] = license
#                     rowDict["LP STATE"] = licensestate
#                 for locate in location:
#                     loc = ''.join(locate)
#                     rowDict["EXIT LANE/LOCATION"] = loc
#                 for timedate in datetime:
#                     date = ''.join(timedate)
#                     rowDict["TRXN.DATE & TIME"] = date  
#                     rowDict["TOLL AGENCY"] = "MARYLAND TRANSPORTATION AUTHORITY"
#                     rowDict["PIN NO#"] = ""
                    
#                 output_list.append(rowDict)
#                 dff = pd.DataFrame(output_list)
#                 output_list = []
#                 df = pd.concat([df, dff])
#                 df.drop_duplicates(inplace = True)
#                 return df
                  
                            
# #         print("writing out"+i)
# #         df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)
              
# # bowmanmdtaprocess()