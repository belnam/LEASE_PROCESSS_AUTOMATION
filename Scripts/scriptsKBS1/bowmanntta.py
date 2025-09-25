# import os
# from pprint import pprint
# from tkinter import Y
# import pandas as pd
# import re
# import os
# import pdfplumber
# import datetime
# import getpass
# def bowmannttaprocess():
  
#     rowDict = {"TOLL AGENCY":"NORTH TEXAS TOLLWAY AUTHORITY","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
#     username = getpass.getuser()
#     workingDir = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\attachments_output\\"
#     outputDir = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\SRTS_OUTPUT\\"

#     for i in os.listdir(workingDir):
#         output_list = []
#         df = pd.DataFrame()
#         with pdfplumber.open(workingDir+i) as pdf:
#             for page in pdf.pages:
#                 pageText = page.extract_text()
#                 invoicenumber = re.findall(r'InvoiceNumber\W+(S\w+)|Invoice\W+Number\W+(S\w+)',pageText)
#                 lpstateaccount = re.findall(r'(\w+)\W+(\w{2})\W+(\d+)\W+\d+\W+\d+\W+\d+\W+to\W+',pageText)
#                 reference = re.findall(r'InvoiceNumber\W+(\d+)|Invoice\W+Number\W+(\d+)',pageText)
#                 transaction = re.findall(r'\d+\W+\d+\W+\d{4}\W+(\d+\W+\d+\W+\d+.*[:]\d+)\W+(.*)[$|S](\w+\W+\w+)',pageText)
            

#                 for invoice in invoicenumber:
#                     inv = ''.join(invoice).replace("S1","SI")
#                     rowDict["INVOICE#"] = inv
#                     output_list.append(rowDict)
#                     dff = pd.DataFrame(output_list)
#                     output_list = []
#                     df = pd.concat([df, dff])
#                     df.drop_duplicates(inplace = True)

            
#                 for lpstacc in lpstateaccount:
#                     rowDict["LP"] = lpstacc[0]
#                     rowDict["LP STATE"] = lpstacc[1]
#                     rowDict["ACCOUNT#"] = lpstacc[2]
#                 for ref in reference:
#                     refer = ''.join(ref)
#                     rowDict["REFERENCE # OR INVOICE #"] = refer
#                 for trans in transaction:
#                     rowDict["TRXN.DATE & TIME"] = trans[0]
#                     rowDict["EXIT LANE/LOCATION"] = trans[1]
#                     rowDict["AMOUNT DUE"] = trans[2]



#                     output_list.append(rowDict)
#                     dff = pd.DataFrame(output_list)
#                     output_list = []
#                     df = pd.concat([df, dff])
#                     df.drop_duplicates(inplace = True)

                            
                                    
#         print("writing out"+i)
#         df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)

# bowmannttaprocess()