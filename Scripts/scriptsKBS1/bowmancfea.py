# import os
# from pprint import pprint
# from tkinter import Y
# import pandas as pd
# import re
# import os
# import pdfplumber
# import datetime

# def bowmancfeaprocess(pageText):
#                 output_list = []
#                 df = pd.DataFrame()
#                 rowDict = {"TOLL AGENCY":"CENTRAL FLORIDA EXPRESSWAY AUTHORITY","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
#                 # print(pageText)
#                 invoicenumber = re.findall(r'InvoiceNumber\W+(\w+)|Invoice\W+Number\W+(\w+)',pageText)
#                 # transaction = re.findall(r'(\w.*\s+\d+)\s+(\d+\d+\W+\d+\W+\d+.*[:]\w.*)[$|S](\w+\W+\w+)',pageText)
                
#                 for invoice in invoicenumber:
#                     inv = ''.join(invoice).replace("S1","SI")
#                     rowDict["INVOICE#"] = inv
#                     output_list.append(rowDict)
#                     dff = pd.DataFrame(output_list)
#                     output_list = []
#                     df = pd.concat([df, dff])
#                     df.drop_duplicates(inplace = True)
                
#                 # for trans in transaction:
#                 #     rowDict["EXIT LANE/LOCATION"] = trans[0]
#                 #     rowDict["TRXN.DATE & TIME"] = trans[1]
#                 #     rowDict["AMOUNT DUE"] = trans[2]
#                 #     rowDict["TOLL AGENCY"] = "CENTRA FLORIDA EXPRESSWAY AUTHORITY"
                    
#                     output_list.append(rowDict)
#                     dff = pd.DataFrame(output_list)
#                     output_list = []
#                     df = pd.concat([df, dff])
#                     df.drop_duplicates(inplace = True)
#                 return df
                 
                            
# #         print("writing out"+i)
# #         df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)

                    
# # bowmancfeaprocess()