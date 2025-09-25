# import os
# from pprint import pprint
# from tkinter import Y
# import pandas as pd
# import re
# import os
# import pdfplumber
# import datetime
# import getpass

# rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
# username = getpass.getuser()
# workingDir = f"Downloaded_Scans\\"
# outputDir = f"SRTS_OUTPUT\\"

# # workingDir = f"{os.getcwd()}\\raw_files\\"
# # outputDir = f"{os.getcwd()}\\output_files\\"
# for i in os.listdir(workingDir):
#   # if "MILESTONE" in i:
#     df = pd.DataFrame()
#     with pdfplumber.open(workingDir+i) as pdf:
#         output_list = []
#         lpa = ""
#         lpa2 = ""
#       # for j, text in enumerate(pdf.pages):
#         for page in pdf.pages:
#             pageText = page.extract_text()
#             # print(pageText)
#             # transactiona = re.findall(r'(\w+.*)[ ](\d+\D+\d+)\n+(\w+.*)[|](\d{2}\W+\w+\W+\w+\W+)(\w+\W+\w+\W+\w+)\W+(\w{2})\W+(\w+)|(\w+.*)[|](\w+.*)[|](\d{2}\W+\w+\W+\w+\W+\w+\W+\w+\W+\w+)[|](\w{2})\W+(\w+)\W+(\w+\W+\w+)|(\w+.*)[|](\d{2}\W+\w+\W+\w+\W+\w+\W+\w+\W+\w+)[|](\w{2})\W+(\w+)|(\w+.*[ ]\w+)\n+(\w+.*)[|](\d{2}\W+\w+\W+\w+\W+\w+\W+\w+\W+\w+)[|](\w{2})\W+(\w+)',pageText)
#             transactiona2 = re.findall(r'(\w+.*)([|])(\w+.*)([|])(\d{2}\W+\w+\W+\w+\W+\w+\W+\w+\W+\w+)([|])(\w{2})(\W+)(\w+)\W+(\w+\W+\w+)|\w+\W+(\S+)\W+SV.*\n+(.*)\W+\d+\D+\d+\n+Toll\W+(\d+\W+\d+)\W+(.*)[|](\S+\W+\S+)|Toll\W+(\d+\W+\d+)\W+(.*)[|](\S+\W+\S+)|Toll.*\n+(\w+.*[ ]\w+)\n+Toll\W+(\d+\W+\d+)\W+(.*)[|](\w+.*)|Trailer.*\n+(\D+\w+.*[ ])(\d+\.\d{2})\n+(Toll)\W+(\d+\W+\d+)\W+(.*)[|](\S+\W+\S+)|(\w+.*)[ ](\d+\D+\d+)\n+(\w+.*)[|](\d{2}\W+\w+\W+\w+\W+)(\w+\W+\w+\W+\w+)\W+(\w{2})\W+(\w+)|(\w+.*)([|])(\d{2}\W+\w+\W+\w+)(\W+\w+\W+\w+\W+\w+)([|])(\w{2})(\W+)(\w+)|(\w+.*[ ]\w+)\n+(\w+.*)([|])(\d{2}\W+\w+\W+\w+\W+)(\w+\W+\w+\W+\w+)([|])(\w{2})(\W+)(\w+)|(\w+)\W+(\S+)\W+(SV.*)\n+(\w+.*)[ ](\d+\W+\d+)\n+(V\w+)\W+\w+\W+(\w+)\n+(\w+)\W+\w+\W+(\w+)\n+(\w+)\W+\w+\W+(\S+)|(\w+)\W+(\w+)\W+SV.*\n+(\w.*)[ ](\w+\W+\w+)\n+(\w+)\W+(\w+)\W+(\w+)\n+(\w+\W+)\w+\W+(\w+)\n+(\w+)\W+(\w+)\W+(\w+\W+\w+\W+\w+)',pageText)
#             duedate = re.findall(r'D\w+\W+Da\w+\W+(\S+)',pageText)
#             invoice = re.findall(r'In\w+\W+N\w+\W+(\w+)',pageText)
          
#             for due in duedate:
#               rowDict["DUE DATE"] = due 
#             for inv in invoice:
#               rowDict["INVOICE#"] = inv

#             for tran_sacta2 in transactiona2:
#               transacta2 = list(filter(None,tran_sacta2))
#               # print(type(transacta2))
            
#               if len(transacta2) == 7:
#                 agencya = transacta2[0].upper()
#                 amounta = transacta2[1]
#                 locationa = transacta2[2]
#                 datetime = transacta2[3]+''+transacta2[4]
#                 timedate =''.join(datetime)
#                 statea = transacta2[5]
#                 lpa = transacta2[6]
#                 rowDict["AMOUNT DUE"] = amounta
#                 rowDict["EXIT LANE/LOCATION"] = locationa
#                 rowDict["TRXN.DATE & TIME"] = timedate.replace("-","/")
#                 rowDict["LP STATE"] = statea
#                 rowDict["TOLL AGENCY"] = agencya
#                 if lpa:
#                   rowDict["LP"] = lpa
#                 else:
#                   rowDict["LP"] = lpa
#                 rowDict["VIOLATION#"] = ""
#                 rowDict["REFERENCE # OR INVOICE #"] = ""
#                 output_list.append(rowDict)
#                 dff = pd.DataFrame(output_list)
#                 output_list = []
#                 df = pd.concat([df, dff])
#                 df = df.drop_duplicates()
#                 df['TRXN.DATE & TIME']= pd.to_datetime(df['TRXN.DATE & TIME'].str.replace('\s(\d)$', ' 0\\1'),errors='coerce')
#                 df['TRXN.DATE & TIME'] = df['TRXN.DATE & TIME'].dt.strftime('%m/%d/%y %H:%M:%S')
#                 # df = df[:-1]
              
#               if len(transacta2) == 9:
#                 agencya = transacta2[0].upper()
#                 locationa = transacta2[1]
#                 datetime = transacta2[3]+''+transacta2[4]
#                 statea = transacta2[6]
#                 lpa = transacta2[8]
#                 rowDict["EXIT LANE/LOCATION"] = locationa
#                 rowDict["TRXN.DATE & TIME"] = datetime.replace("-","/")
#                 if lpa:
#                   rowDict["LP"] = lpa
#                 else:
#                   rowDict["LP"] = lpa
#                 rowDict["LP STATE"] = statea
#                 rowDict["TOLL AGENCY"] = agencya
#                 rowDict["VIOLATION#"] = ""
#                 rowDict["REFERENCE # OR INVOICE #"] = ""
#                 output_list.append(rowDict)
#                 dff = pd.DataFrame(output_list)
#                 output_list = []
#                 df = pd.concat([df, dff])
#                 df = df.drop_duplicates()
#                 df['TRXN.DATE & TIME']= pd.to_datetime(df['TRXN.DATE & TIME'].str.replace('\s(\d)$', ' 0\\1'),errors='coerce')
#                 df['TRXN.DATE & TIME'] = df['TRXN.DATE & TIME'].dt.strftime('%m/%d/%y %H:%M:%S')
              
#               if len(transacta2) == 8:
#                 locationa = transacta2[0]
#                 datetime = transacta2[2]+''+transacta2[3]
#                 statea = transacta2[5]
#                 lpa = transacta2[7]
#                 rowDict["EXIT LANE/LOCATION"] = locationa
#                 rowDict["TRXN.DATE & TIME"] = datetime
#                 if lpa:
#                   rowDict["LP"] = lpa
#                 else:
#                   rowDict["LP"] = lpa
#                 rowDict["LP STATE"] = statea
#                 rowDict["VIOLATION#"] = ""
#                 rowDict["REFERENCE # OR INVOICE #"] = ""
#                 output_list.append(rowDict)
#                 dff = pd.DataFrame(output_list)
#                 output_list = []
#                 df = pd.concat([df, dff])
#                 df = df.drop_duplicates(subset='TRXN.DATE & TIME', keep="first")
#                 df['TRXN.DATE & TIME']= pd.to_datetime(df['TRXN.DATE & TIME'].str.replace('\s(\d)$', ' 0\\1'),errors='coerce')
#                 df['TRXN.DATE & TIME'] = df['TRXN.DATE & TIME'].dt.strftime('%m/%d/%y %H:%M:%S')
                
              
#               if len(transacta2) == 11:
#                 agencya = transacta2[3].upper()
#                 amounta = transacta2[4]
#                 violation = transacta2[6]
#                 datetime = transacta2[10]
#                 lpa = transacta2[8]
#                 rowDict["AMOUNT DUE"] = amounta
#                 rowDict["VIOLATION#"] = violation
#                 rowDict["TRXN.DATE & TIME"] = datetime.replace("-","/")
#                 if lpa:
#                   rowDict["LP"] = lpa
#                 else:
#                   rowDict["LP"] = lpa
#                 rowDict["LP STATE"] = ""
#                 rowDict["TOLL AGENCY"] = agencya
#                 rowDict["EXIT LANE/LOCATION"] = ""
#                 rowDict["REFERENCE # OR INVOICE #"] = ""
#                 output_list.append(rowDict)
#                 dff = pd.DataFrame(output_list)
#                 output_list = []
#                 df = pd.concat([df, dff])
#                 df = df.drop_duplicates(subset='TRXN.DATE & TIME', keep="first")
#                 df['TRXN.DATE & TIME']= pd.to_datetime(df['TRXN.DATE & TIME'].str.replace('\s(\d)$', ' 0\\1'),errors='coerce')
#                 df['TRXN.DATE & TIME'] = df['TRXN.DATE & TIME'].dt.strftime('%m/%d/%y %H:%M:%S')
                
#               if len(transacta2) == 5:
#                 lpa2 = transacta2[0]
#                 amta2 = transacta2[2]
#                 locationa2 = transacta2[3]
#                 datetimea2 = transacta2[4].replace("-","/").replace(" 0"," ")
#                 timedate2 =''.join(datetimea2)
#                 agencya2 = transacta2[1].upper()
#                 rowDict["AMOUNT DUE"] = amta2
#                 rowDict["EXIT LANE/LOCATION"] = locationa2
#                 rowDict["TRXN.DATE & TIME"] = timedate2
#                 if lpa2:
#                   rowDict["LP"] = lpa2
#                 else:
#                   rowDict["LP"] = lpa2
#                 rowDict["TOLL AGENCY"] = agencya2
#                 rowDict["VIOLATION#"] = ""
#                 rowDict["REFERENCE # OR INVOICE #"] = ""
#                 rowDict["LP STATE"] = ""
#                 output_list.append(rowDict)
#                 dff = pd.DataFrame(output_list)
#                 output_list = []
#                 df = pd.concat([df, dff])
#                 df = df.drop_duplicates(subset='TRXN.DATE & TIME', keep="first")
#                 df['TRXN.DATE & TIME']= pd.to_datetime(df['TRXN.DATE & TIME'].str.replace('\s(\d)$', ' 0\\1'),errors='coerce')
#                 df['TRXN.DATE & TIME'] = df['TRXN.DATE & TIME'].dt.strftime('%m/%d/%y %H:%M:%S')

#               elif len(transacta2) == 4:
#                 amta2 = transacta2[1]
#                 locationa2 = transacta2[2]
#                 datetimea2 = transacta2[3].replace("-","/")
#                 agencya2 = transacta2[0]
#                 rowDict["AMOUNT DUE"] = amta2
#                 rowDict["EXIT LANE/LOCATION"] = locationa2
#                 rowDict["TRXN.DATE & TIME"] = datetimea2
#                 rowDict["TOLL AGENCY"] = agencya2.upper()
#                 rowDict["VIOLATION#"] = ""
#                 rowDict["REFERENCE # OR INVOICE #"] = ""
#                 if lpa2:
#                   rowDict["LP"] = lpa2
#                 else:
#                   rowDict["LP"] = lpa2
#                 rowDict["LP STATE"] = ""
#                 output_list.append(rowDict)
#                 dff = pd.DataFrame(output_list)
#                 output_list = []
#                 df = pd.concat([df, dff])
#                 df = df.drop_duplicates(subset='TRXN.DATE & TIME', keep="first")
#                 df['TRXN.DATE & TIME']= pd.to_datetime(df['TRXN.DATE & TIME'].str.replace('\s(\d)$', ' 0\\1'),errors='coerce')
#                 df['TRXN.DATE & TIME'] = df['TRXN.DATE & TIME'].dt.strftime('%m/%d/%y %H:%M:%S')
              
#               if len(transacta2) == 3:
#                 amta2 = transacta2[0]
#                 locationa2 = transacta2[1]
#                 datetimea2 = transacta2[2].replace("-","/").replace("Toll:","")
#                 timedate2 =''.join(datetimea2)
#                 rowDict["AMOUNT DUE"] = amta2
#                 rowDict["EXIT LANE/LOCATION"] = locationa2
#                 rowDict["TRXN.DATE & TIME"] = timedate2
#                 rowDict["VIOLATION#"] = ""
#                 rowDict["REFERENCE # OR INVOICE #"] = ""
#                 if lpa2:
#                   rowDict["LP"] = lpa2
#                 else:
#                   rowDict["LP"] = lpa2
#                 rowDict["LP STATE"] = ""
#                 output_list.append(rowDict)
#                 dff = pd.DataFrame(output_list)
#                 output_list = []
#                 df = pd.concat([df, dff])
#                 df = df.drop_duplicates(subset='TRXN.DATE & TIME', keep="first")
#                 df['TRXN.DATE & TIME']= pd.to_datetime(df['TRXN.DATE & TIME'].str.replace('\s(\d)$', ' 0\\1'),errors='coerce')
#                 df['TRXN.DATE & TIME'] = df['TRXN.DATE & TIME'].dt.strftime('%m/%d/%y %H:%M:%S')
                
#               elif len(transacta2) == 12:
#                 reference = transacta2[6]
#                 lpa2 = transacta2[8]
#                 agencya2 = transacta2[2].upper()
#                 amta2 = transacta2[3]
#                 datetimea2 = transacta2[11]
#                 rowDict["AMOUNT DUE"] = amta2
#                 rowDict["EXIT LANE/LOCATION"] = ""
#                 rowDict["TRXN.DATE & TIME"] = datetimea2
#                 rowDict["TOLL AGENCY"] = agencya2
#                 if reference:
#                   rowDict["REFERENCE # OR INVOICE #"] = reference
#                 else:
#                   rowDict["REFERENCE # OR INVOICE #"] = ""
#                 rowDict["VIOLATION#"] = ""
#                 if lpa2:
#                   rowDict["LP"] = lpa2
#                 else:
#                   rowDict["LP"] = lpa2
#                 rowDict["LP STATE"] = ""
#                 output_list.append(rowDict)
#                 dff = pd.DataFrame(output_list)
#                 output_list = []
#                 df = pd.concat([df, dff])
#                 df = df.drop_duplicates(subset='TRXN.DATE & TIME', keep="first")
#                 df['TRXN.DATE & TIME']= pd.to_datetime(df['TRXN.DATE & TIME'].str.replace('\s(\d)$', ' 0\\1'),errors='coerce')
#                 df['TRXN.DATE & TIME'] = df['TRXN.DATE & TIME'].dt.strftime('%m/%d/%y %H:%M:%S')
                
                
#               if len(transacta2) == 6:
#                 agencya2 = transacta2[0].upper()
#                 amta2 = transacta2[3]
#                 locationa2 = transacta2[4]
#                 datetimea2 = transacta2[5].replace("-","/")
#                 rowDict["AMOUNT DUE"] = amta2
#                 rowDict["EXIT LANE/LOCATION"] = locationa2
#                 rowDict["TRXN.DATE & TIME"] = datetimea2
#                 rowDict["TOLL AGENCY"] = agencya2
#                 rowDict["VIOLATION#"] = ""
#                 rowDict["REFERENCE # OR INVOICE #"] = ""
#                 if lpa2:
#                   rowDict["LP"] = lpa2
#                 else:
#                   rowDict["LP"] = lpa2
#                 rowDict["LP STATE"] = ""
#                 output_list.append(rowDict)
#                 dff = pd.DataFrame(output_list)
#                 output_list = []
#                 df = pd.concat([df, dff])
#                 df = df.drop_duplicates(subset='TRXN.DATE & TIME', keep="first")
#                 df['TRXN.DATE & TIME']= pd.to_datetime(df['TRXN.DATE & TIME'].str.replace('\s(\d)$', ' 0\\1'),errors='coerce')
#                 df['TRXN.DATE & TIME'] = df['TRXN.DATE & TIME'].dt.strftime('%m/%d/%y %H:%M:%S')
            
              
#               for line in pageText.split("\n"):
#                 trans =  re.findall(r'\w+\W+(\S+)\W+SV.*',line)
#                 translist =  list(filter(None,trans))
#                 listtrans = ''.join(translist)
#                 rowDict["LP"] = listtrans
#                 output_list.append(rowDict)
#                 dff = pd.DataFrame(output_list)
#                 output_list = []
#                 df = pd.concat([df, dff])
                
#                 df['TRXN.DATE & TIME']= pd.to_datetime(df['TRXN.DATE & TIME'].str.replace('\s(\d)$', ' 0\\1'),errors='coerce')
#                 df['TRXN.DATE & TIME'] = df['TRXN.DATE & TIME'].dt.strftime('%m/%d/%y %H:%M:%S')
#                 df = df.drop_duplicates(subset='TRXN.DATE & TIME', keep="first")
#                 break
     
#     print("writing out"+i)
#     df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx",index=False)
#   # else:
#   #   pass          