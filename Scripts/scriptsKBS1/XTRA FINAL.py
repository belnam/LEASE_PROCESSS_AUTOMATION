# """
# A python ocr bot extracting data from XTRA agency
# """
# from ast import And
# from copyreg import constructor
# import re
# import pandas as pd
# import pdfplumber
# import getpass
# import os

# import pandas as pd
# # df = pd.DataFrame()

# row_dict = {
#     'TOLL AGENCY':None,
#     'LP':None,
#     'LP STATE':None,
#     'TRXN. DATE & TIME':None,
#     'EXIT LANE/LOCATION':None,
#     'ACCOUNT#':None,
#     'REFERENCE # OR INVOICE #':None,
#     'VIOLATION#':None,
#     'AMOUNT DUE':None,
#     'DUE DATE':None,
#     'PIN NO#':None
# }

# username = getpass.getuser()
# workingDir = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\Downloaded_Scans\\"
# outputDir = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\SRTS_OUTPUT\\"

# # workingDir = f"Downloaded_Scans\\"
# # outputDir = f"SRTS_OUTPUT\\"

# for i in os.listdir(workingDir):
#     if "XTRA" in i or "xtra" in i:
#         df = pd.DataFrame()
#         with pdfplumber.open(workingDir+i) as pdf:
#             for j, text in enumerate(pdf.pages):    

#                 pages = pdf.pages[j]
#                 page_data = pages.extract_text()
#                 # print(page_data)
                

#                 invoice = re.findall(r'^Invoice\s*No\W*(\d*)\nInvoice\s*\Date\s*\d{2}\W*\d{2}\W*\d{4}', page_data)
#                 license_plate = re.findall(r'(\w{6})\s+\d+\s+\w+\s+\w+\W+\d+\W+', page_data)
#                 agency_exit_time = re.findall(r'Toll\s*\w*\s*\d{2}\W*\d{2}\W*\d{4}\s*\d{2}\W*\d{2}\W*\d{4}\W*(\d*\W*\d*)\W*\w*\n(\w*\W*\w*\W*\w*\W*\w*\W*\w*\s*\D*)loc(\D*)(\d*\D*\d*\D*\d*\D*\d*\D*\d*)', page_data)
#                 amount_due = re.findall(r'Toll\s*\w*\s*\d{2}\W*\d{2}\W*\d{4}\s*\d{2}\W*\d{2}\W*\d{4}\W*(\d*\W*\d*)', page_data)
#                 trxn_date_time = re.findall(r'\wn\W*(\d{4}\W*\d{2}\W*\d{2}\W*\d{2}\W*\d{2})', page_data)
#                 grabUnitRgx = re.compile(r'^(\w{6})\s+\d+\s+\w+\s+\w+\W+\d+\W+')
#                 grabTollFee = re.compile(r'Toll Fee')
#                 grabInvoiceNbr = re.compile(r'Invoice No. \d*')
#                 locRgx = re.findall(r'loc:\W+\S+\W+\S+\D+|loc:\W+\S+\W+\D+',page_data)
#                 lpstate = re.findall(r'Toll.*F.*[$|S].*([A-Z]{2})',page_data)

#                 lpNameArry =[]
#                 lpcount  =0
#                 nameCount  = 0
#                 prevLp = ''
#                 # for state in lpstate:
#                 #     row_dict["LP STATE"] = state
#                 for line in page_data.split("\n"):

#                     lp = re.match(grabUnitRgx, line)
#                     name  =  re.findall(grabTollFee,line)
#                     invoiceNbr = re.findall(grabInvoiceNbr,line)
#                     if invoiceNbr:
                        
#                         row_dict["REFERENCE # OR INVOICE #"] = str(invoiceNbr[0]).split('.')[1]
#                         # print(str(invoiceNbr[0]).split('.')[1])
                    
#                     if lp  and nameCount>0 :
#                         lpNameArry.append([prevLp,nameCount])
#                         nameCount =0
#                         prevLp = lp.group(1)
#                     elif lp:
#                         prevLp = lp.group(1)
                
#                     if name:
#                         nameCount =  nameCount+1                    
#                 lpNameArry.append([prevLp,nameCount])
#                 prevIndex = 0
#                 for val in lpNameArry:                 
#                     for amt in range(prevIndex,prevIndex+ val[1]) :
#                         output_list = []
#                         row_dict["AMOUNT DUE"] = amount_due[amt]
#                         row_dict["LP"] = val[0]
#                         row_dict["TRXN. DATE & TIME"] = trxn_date_time[amt]
#                         row_dict["TOLL AGENCY"] = str(str(agency_exit_time[amt]).split(',')[1]).replace("'","").replace(r'\n',"").replace("Transponder Account","")
#                         row_dict["EXIT LANE/LOCATION"] = str(locRgx[amt]).replace("loc:","").replace("on:","")
#                         # row_dict["Loc"] = str(str(agency_exit_time[amt]).split(',')[3]).replace(r'\n',"")
#                         # row_dict["LP STATE"] =str( str(agency_exit_time[amt]).split(',')[2]).replace("'","").replace(r'\n',"")
#                         row_dict["LP STATE"] = lpstate[amt]

#                         row_dict["Page"] = j+1
#                         output_list.append(row_dict)
#                         dff = pd.DataFrame(output_list)
#                         df = pd.concat([df, dff])
            

#                     prevIndex = prevIndex+ val[1]
      
#         print("writing out"+i)
#         df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx",index=False)
#     else:
#         pass        
     



        