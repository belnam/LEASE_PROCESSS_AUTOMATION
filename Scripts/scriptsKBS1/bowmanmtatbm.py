# '''
# python ocr bot extracting data from mta bridges
# and tunnels agency
# '''
# import os
# import re
# import pandas as pd
# import pdfplumber
# import getpass
# import os

# def bowmanmtatollsbymailprocess():
#     rowDict = {
#         'TOLL AGENCY':'MTA BRIGES AND TUNNELS(TOLLS BY MAIL)',
#         'LP':None,
#         'LP STATE':None,
#         'TRXN DATE & TIME':None,
#         'EXIT LANE/LOCATION':None,
#         'ACCOUNT#':None,
#         'REFERENCE # OR INVOICE #':None,
#         'VIOLATION#':None,
#         'AMOUNT DUE':None,
#         'DUE DATE':None,
#         'PIN #':None,
#         'INVOICE#':None,
#     }
  
#     workingDir = f"raw_files\\"
#     outputDir = f"output\\"

#     for i in os.listdir(workingDir):
#         df = pd.DataFrame()
#         with pdfplumber.open(workingDir+i) as pdf:
#             output_list = []
#             for page in pdf.pages:
#                 pageText = page.extract_text()
#                 # print(pageText)
#                 invoicenumber = re.findall(r'InvoiceNumber\W+(\w+)|Invoice\W+Number\W+(\w+)',pageText)
#                 reference = re.findall(r'TO\w+B\w+N\w+\W+(\d+)|T\w+\W+B\w+\W+N\w+\W+(\d+)',pageText)
#                 duedate = re.findall(r'M\w+B\w+R\w+b\w+\W+(\w+\W+\w+\W+\w+)|M\w+\W+B\w+\W+R\w+\W+b\w+\W+(\w+\W+\w+\W+\w+)',pageText)
#                 transaction = re.findall(r'([A-Z]{1}\w{1})(\d+).*\W+(\w+)\W+\w+\W+(\d+\/\d+\/\d+.*[:]\d+).*[$|S](\w+\W+\w+)',pageText)

#                 for invoice in invoicenumber:
#                     inv = ''.join(invoice).replace("S1","SI")
#                     rowDict["INVOICE#"] = inv
#                 for ref in reference:
#                     refer = ''.join(ref)
#                     rowDict["REFERENCE # OR INVOICE #"] = refer
#                 for due in duedate:
#                     date = ''.join(due)
#                     rowDict["DUE DATE"] = date
#                 for trans in transaction:
#                     rowDict["LP STATE"] = trans[0]
#                     rowDict["LP"] = trans[1]
#                     rowDict["EXIT LANE/LOCATION"] = trans[2]
#                     rowDict["TRXN DATE & TIME"] = trans[3]
#                     rowDict["AMOUNT DUE"] = trans[4]
            
#                     output_list.append(rowDict)
#                     dff = pd.DataFrame(output_list)
#                     output_list = []
#                     df = pd.concat([df, dff])
#                     df.drop_duplicates(inplace = True)

#         print('Processing file' + i)
#         df.to_excel(str(outputDir + i).replace('.pdf', '') + '.xlsx', index=False)
# bowmanmtatollsbymailprocess()