# import os
# from pprint import pprint
# from tkinter import Y
# import pandas as pd
# import re
# import os
# import pdfplumber
# import getpass

# def bowmanfdotprocess(pageText):
#     output_list = []
#     df = pd.DataFrame()
#     rowDict = {"TOLL AGENCY":"FDOT","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":""}
#     # print(pageText)
#     invoicenumber = re.findall(r'InvoiceNumber\W+(\w+)|In\w+\W+N\w+\W+(\w+)',pageText)
#     invlpstate = re.findall(r'\w+\#\D+(\d+)\D+(\d+)\s+\w+\s+\w+\W+(\S+)\W+\w+\W+(\w{2})',pageText) 
#     invlpstateB = re.findall(r'In\w+\D+(\S+)\W+A\w+\D+(\d{9})\W+\w+\W+(\S+)\W+\w+\W+(\S+)|In\w+\D+(\S+)\W+A\w+\D+(\d{9})\W+\w+\W+\w+\W+(\S+)\W+\w+\W+(\w+)',pageText) 
#     duedate = re.findall(r'\$(\d+\W+\d+)\W+\d+\W+\d+\W+\d+\W+\d+\W+(\S+)\W+(\S+)\W+(\d+\W+\d+\W+\d+)',pageText)
#     transaction = re.findall(r'\d+\/\d+\/\d+\W+\w+\W(.*)\s+\d+\s+(\d{2}\S+.*)[$|S](\w+\W+\w+)',pageText)
#     addfee = re.findall(r'\$\d+\W+\d+\W+\d+\W+\d+\W+\d+\W+\d+\W+(\S+)\W+\S+\W+\d+\W+\d+\W+\d+',pageText)

#     trxn_index = len(transaction) -1
#     last_index = 0

#     for invoice in invoicenumber:
#         invcnmb = list(invoice)
#         inv_nmbr = ''.join(invcnmb)
#         rowDict['INVOICE#'] = inv_nmbr
#         output_list.append(rowDict)
#         dff = pd.DataFrame(output_list)
#         output_list = []
#         df = pd.concat([df, dff])
#         df.drop_duplicates(inplace = True)
#     for add in addfee:
#         c = list(add)
#         d = ''.join(c)
#     if invlpstate:
#         for lp in invlpstate:
#             license = lp[2]
#             invoice =lp[0]
#             account = lp[1]
#             state = lp[3].replace("Da","").replace("i","I")
#             rowDict['LP'] = license
#             rowDict['REFERENCE # OR INVOICE #'] = invoice
#             rowDict['ACCOUNT#'] = account
#     #         rowDict['LP STATE'] = state 
#     # else:
#     #         rowDict['LP'] = ""
#     #         rowDict['REFERENCE # OR INVOICE #'] = ""
#     #         rowDict['ACCOUNT#'] = ""
#     #         rowDict['LP STATE'] = "" 
#     if invlpstateB:
#         for lp in invlpstateB:
#             license = lp[2]
#             invoice =lp[0]
#             account = lp[1]
#             state = lp[3].replace("Da","").replace("i","I").replace("te","")
#             rowDict['LP'] = license
#             rowDict['REFERENCE # OR INVOICE #'] = invoice
#             rowDict['ACCOUNT#'] = account
#             rowDict['LP STATE'] = state
  
#     for prev in duedate:
#         prevA = prev[0]
#         prevB = prev[1]
#         prevC = prev[2]

#         amntdue = prevA
#         dueamnt  = list(amntdue)
#         amntamntdue = ''.join(dueamnt).replace(",",".")
#         due_amount = float(amntamntdue)

#         e = prevB
#         f  = list(e)
#         g = ''.join(f).replace(",",".")
#         try:
#             h = float(g)
#         except:
#             pass
    

#         k = prevC
#         l  = list(k)
#         m = ''.join(l).replace(",",".")
#         try:
#             n = float(m)
#         except:
#             pass


#         if  due_amount + h  == n:
#             rowDict['AMOUNT DUE'] = n

#         elif due_amount + h != n:
#             rowDict['AMOUNT DUE'] = due_amount

#         rowDict['EXIT LANE/LOCATION'] = ""
#         rowDict['TRXN.DATE & TIME'] = ""
#         rowDict['PIN NO#'] = ""
        
#         output_list.append(rowDict)
#         dff = pd.DataFrame(output_list)
#         output_list = []
#         df = pd.concat([df, dff])
#         df.drop_duplicates(inplace = True)
#         df = df[df['AMOUNT DUE'] != 0]
            
            
#     for trans in transaction:
#         location = trans[0]
#         datetime = trans[1]
#         amount = trans[2]
        
#         locate = location
#         a = list(locate)
#         b = ''.join(a) 
        
#         rowDict['EXIT LANE/LOCATION'] = b.replace("SOS","50S").replace("508","50S").replace("503","50S").replace("CHA","").replace("COLLECTIONS","")
#         rowDict['TRXN.DATE & TIME'] = datetime.replace(";",":")
#         rowDict['PIN NO#'] = ""
        
        
#         amountdue = amount
#         amtdue  = list(amountdue)
#         dueamt = ''.join(amtdue).replace(",",".").replace("I","1").replace(" ","")
#         try:
#             dueamount = float(dueamt)
#         except:
#             pass
#         if last_index != trxn_index:  
#             rowDict['AMOUNT DUE'] = dueamount
#         else:
#             try:
#                 rowDict['AMOUNT DUE'] = dueamount + float(d)
#             except:
#                 pass
#         last_index += 1
        
#         output_list.append(rowDict)
#         dff = pd.DataFrame(output_list)
#         output_list = []
#         df = pd.concat([df, dff])
#         df.drop_duplicates(inplace = True)
#         df = df[df['AMOUNT DUE'] != 0]
#         df = df[df['LP'] != ""]
#     return df
    
                                
# #         print("writing out"+fname)
# #         df.to_excel(str(outputDir+fname).replace(".pdf","")+".xlsx", index=False)
# # bowmanfdotprocess()               