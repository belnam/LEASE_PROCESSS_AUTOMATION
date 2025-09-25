# import os
# from pprint import pprint
# from tkinter import Y
# import pandas as pd
# import re
# import os
# import pdfplumber
# import datetime
# import getpass
# def stoughtondullesprocess(pageText):
#     output_list = []
#     df = pd.DataFrame()
#     rowDict = {"TOLL AGENCY":"DULLES GREENWAY","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
    
#     # license_details = re.findall(r'Li.*P\w+\W+(\w{2})(\w+)|Li.*P\w+\W+(\w{2})\W+(\w+)', pageText)
#     # due_date = re.findall(r'Due.*D\w+\W+(\w{2}\W+\w+\W+\w+)', pageText)
#     # transactions = re.findall(r'(\w{16})\W+(\d+\/\d+\/\d+.*M)\s+(.*)[$|S](\w+\W+\w+).*[$|S](\w+\W+\w+)', pageText)
    
#     # for dd in due_date:
#     #     date = dd
#     #     rowDict['DUE DATE'] = date
#     # for l_d in license_details:
#     #     ld = list(filter(None, l_d))
#     #     state = ld[0]
#     #     plate = ld[1]
#     #     rowDict['LP STATE'] = state
#     #     rowDict['LP'] = plate
        
#     # for t_r in transactions:
#     #     tr = list(filter(None, t_r))
#     #     invoice_no = tr[0]
#     #     trxn_date = tr[1]
#     #     exit_lane = tr[2]
#     #     toll_fee = float(tr[3].replace('O', '0'))
#     #     admin_fee = float(tr[4].replace('O', '0'))
#     #     total_amount = toll_fee + admin_fee

#     #     rowDict['EXIT LANE/LOCATION'] = exit_lane
#     #     rowDict['TRXN.DATE & TIME'] = trxn_date
#     #     rowDict['AMOUNT DUE'] = total_amount
#     #     rowDict['REFERENCE # OR INVOICE #'] = invoice_no
        
#         # output_list.append(rowDict)
#         # dff = pd.DataFrame(output_list)
#         # output_list = []
#         # df = pd.concat([df, dff])
#         # df.drop_duplicates(inplace = True)
#     return df
                                
                            
# #         print("writing out"+i)
# #         df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)

# # stoughtondullesprocess()