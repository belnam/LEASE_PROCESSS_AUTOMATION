# import pandas as pd
# from pathlib import Path
# # import pathlib2 as pathlib
# import os
# import pdfplumber
# import re as reg_ex
# import glob
# import re
# import getpass
# import shutil


# def bowmanfbctraprocess():
#     rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
#     # final_df = pd.DataFrame()
#     username = getpass.getuser()
#     workingDir = f"C:\\Users\\{username}\\Documents\\Rentals_Process_Automation\\attachments_output\\"
#     outputDir = f"C:\\Users\\{username}\\Documents\\Rentals_Process_Automation\\SRTS_OUTPUT\\"
   
#     for i in os.listdir(workingDir):
#           output_list = []
#           df = pd.DataFrame()
#           with pdfplumber.open(workingDir+i) as pdf:
#               currentPage = ""
#               licensepl=""
#               for page in pdf.pages:
#                 pageText = page.extract_text()
#                 transactions = re.findall(r'(\w+\W+\d{5})\W+(\w{2})\W+(\w{7})\W+(\S+\D+\d+)\W+(\S+\W+\d+\W+\d+\W+\d+)\W+(\d+\W+\d+)', pageText)
#                 due_date = re.findall(r'Date\WDue\W\W(\d*\W\d*\W\d*)', pageText)
#                 total_due = re.findall(r'SEE.*\n\w+\W+\w+\W+(\w+\W+\w+)', pageText)
#                 violation = re.findall(r'Notice Number\W+(\w{13})', pageText)
#                 l_plate = re.findall(r'License Plate\W+(\w{7})', pageText)
#                 lp_state = re.findall(r'License Plate State\W+(\w{2})', pageText)
#                 for t_r in transactions:
#                     tr = list(filter(None, t_r))
#                     trans = ''.join(tr)
#                     violation = tr[0]
#                     state = tr[1]
#                     lp = tr[2]
#                     exit_lane = tr[3]
#                     trxn_date = tr[4]
#                     amount = tr[5]
#                     rowDict['VIOLATION#'] = violation
#                     rowDict['LP STATE'] = state
#                     rowDict['LP'] = lp
#                     rowDict['EXIT LANE/LOCATION'] = exit_lane
#                     rowDict['TRXN.DATE & TIME'] = trxn_date
#                     rowDict['AMOUNT DUE'] = amount
#                     rowDict['PIN NO#'] = ""
#                     rowDict['TOLL AGENCY'] = "FORT BEND COUNTY TOLL ROAD AUTHORITY"
#                     output_list.append(rowDict)
#                     dff = pd.DataFrame(output_list)
#                     output_list = []
#                     df = pd.concat([df, dff])
#                     df.drop_duplicates(inplace = True)
#                 for v in violation:
#                     rowDict['VIOLATION#'] = v
#                 for l_p in l_plate:
#                     rowDict['LP'] = l_p
#                 for l_s in lp_state:    
#                     rowDict['LP STATE'] = l_s 
#                 for dd in due_date:
#                     rowDict['DUE DATE'] = dd
#                 for t_d in total_due:
#                     rowDict['AMOUNT DUE'] = t_d
#                     rowDict['EXIT LANE/LOCATION'] = ""
#                     rowDict['TRXN.DATE & TIME'] = ""
#                     rowDict['PIN NO#'] = ""
#                     rowDict['TOLL AGENCY'] = "FORT BEND COUNTY TOLL ROAD AUTHORITY"
#                     output_list.append(rowDict)
#                     dff = pd.DataFrame(output_list)
#                     output_list = []
#                     df = pd.concat([df, dff])
#                     df.drop_duplicates(inplace = True)
        
#           print("writing out"+i)
#           df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)

                  
# bowmanfbctraprocess()                
    
              
              

          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
                 