# import os
# from pprint import pprint
# from tkinter import Y
# import pandas as pd
# import re
# import os
# import pdfplumber
# import datetime
# import getpass
# def bowmancitationprocess(pageText):
#     output_list = []
#     df = pd.DataFrame()
#     rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
    
#     transaction = re.findall(r'(\d+\/\d+\/\d+.*[:]\w+)\W+(.*)([A-Z]{2})(\w+).*\n*(\w+)',pageText)
#     transactionb = re.findall(r'(\w+\d+)\W+[$](\d+\W+\d+)\W+(\d{2}\W+\d+\W+\d+)',pageText)
#     tollagency = re.findall(r'N\w+-(\w.*)\n+(\w+)',pageText)
    
#     for agency in tollagency:
#         rowDict["TOLL AGENCY"] = agency[0]+''+agency[1]
#     for trans in transaction:
#         rowDict["TRXN.DATE & TIME"] = trans[0]
#         rowDict["EXIT LANE/LOCATION"] = trans[1] +''+ trans[4]
#         rowDict["LP STATE"] = trans[2]
#         rowDict["LP"] = trans[3]
#     for tranxs in transactionb:
#         rowDict["VIOLATION#"] = tranxs[0]
#         rowDict["AMOUNT DUE"] = tranxs[1]
#         rowDict["DUE DATE"] = tranxs[2]
    
#         output_list.append(rowDict)
#         dff = pd.DataFrame(output_list)
#         output_list = []
#         df = pd.concat([df, dff])
#         df.drop_duplicates(inplace = True)
#     return df
                   
                            
# #         print("writing out"+i)
# #         df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)

# # bowmancitationprocess()