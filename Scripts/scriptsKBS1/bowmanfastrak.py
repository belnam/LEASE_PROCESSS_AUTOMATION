import pandas as pd
from pathlib import Path
# import pathlib2 as pathlib
import os
import pdfplumber
import re as reg_ex
import glob
import re
import getpass
import shutil


def bowmanfastrakprocess():
    rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT":"", "REFERENCE # ":"","VIOLATION":"","AMOUNT DUE":"","DUE DATE":"","PIN NO #":"","INVOICE #":"","CODE 1#":"","CODE 2#":"","BILL NO#":"" }
    # final_df = pd.DataFrame()
    username = getpass.getuser()
    # workingDir = f"C:\\Users\\{username}\\Documents\\Rentals_Process_Automation\\attachments_output\\"
    # outputDir = f"C:\\Users\\{username}\\Documents\\Rentals_Process_Automation\\SRTS_OUTPUT\\"

    # workingDir = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\\converted_pdfs\\"
    # outputDir = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\SRTS_OUTPUT\\"
    workingDir = "./attachments_output/"
    outputDir = "./SRTS_OUTPUT/"
    for i in os.listdir(workingDir):
          output_list = []
          df = pd.DataFrame()
          with pdfplumber.open(workingDir+i) as pdf:
              currentPage = ""
              licensepl=""
              for page in pdf.pages:
                pageText = page.extract_text()
                print(pageText)
                reference = re.findall(r"In\w+N\w+\W+(\d+)|in\w+N\w+\W+(\d+)",pageText)
                licplactestate = re.findall(r'Li.*Pl\w+\W+(\w{2})\W+(\w+\d+)|Li\w+\W+P\w+\W+(\w+)\W+(\w+\d+)|Li\w+P\w+\W+(\w+)\W+(\w+\d+)',pageText)
                transaction = re.findall(r'(\d{2}\D\d+\D\d+\s+\d+\W+\d+\W+\d+)\s+(\w+\s+\d+)\s+\D+(\d+\W+\d+)',pageText)
                transaction_delinquent = re.findall(r'(T\d+)\W+(\w{2})\W+(\w+).*[$|S]\w+\W+\w+\W+(\w+\/\w+\W+\w+)\W+(\d+\W+\d+)|(T\d+)\W+(\w{2})(\w+\d+).*[$|S]\w+\W+\w+\W+(\w+\/\w+\W+\w+)\W+(\d+\W+\d+)',pageText)
                transaction_tollevasion = re.findall(r'(T\d+)\W+(\w{2})\W+(\w+).*[$|S]\w+\W+\w+\W+(\w+\/\w+\W+\w+)\W+(\d+\W+\d+)|(T\d+)\W+(\w{2})(\w+\d+).*[$|S]\w+\W+\w+\W+(\w+\/\w+\W+\w+)\W+(\d+\W+\d+)',pageText)
                duedate = re.findall(r'D.*Da\w+\W+(\d+\/\d+\W+\d{2})',pageText)
                amountdue_delinquent = re.findall(r'Am.*D.*On.*O.*Be\w+.*[$|S](\d+\W+\d+)',pageText)
                for inv in reference:
                  invce =''.join(inv) 
                  curr_invoice = invce               
                  rowDict["REFERENCE # "] = curr_invoice  
                for trans in transaction:
                  Trxndatetime = trans[0]
                  location = trans[1]
                  amount = trans[2]
                  rowDict["TRXN DATE & TIME"] = Trxndatetime
                  rowDict["EXIT LANE/LOCATION"] = location
                  rowDict["AMOUNT DUE"] = amount
                for lic in licplactestate:
                  lpstate =lic[0]
                  license = lic[1]
                  rowDict["LP"] = license
                  rowDict["LP STATE"] = lpstate
                for date in duedate:
                  rowDict["DUE DATE"] = date
                  rowDict["TOLL AGENCY"] = "FASTRAK"
                  rowDict["PIN NO #"] = ""
                  rowDict["VIOLATION"] = ""
                  rowDict["ACCOUNT"] = ""
                  output_list.append(rowDict)
                  dff = pd.DataFrame(output_list)
                  output_list = []
                  df = pd.concat([df, dff])
                  df.drop_duplicates(inplace = True)   
                for trans_delinquent in transaction_delinquent:
                  tr = list(filter(None, trans_delinquent))
                  violation = tr[0]
                  licensestate = tr[1]
                  licenseplate = tr[2]
                  datedue = tr[3]
                for amnt in amountdue_delinquent:
                  rowDict["TRXN DATE & TIME"] = ""
                  rowDict["EXIT LANE/LOCATION"] = ""
                  rowDict["AMOUNT DUE"] = amnt
                  rowDict["LP"] = licenseplate
                  rowDict["LP STATE"] = licensestate
                  rowDict["VIOLATION"] = violation
                  rowDict["DUE DATE"] = datedue
                  rowDict["PIN NO #"] = ""
                  rowDict["TOLL AGENCY"] = "FASTRAK"
                  rowDict["REFERENCE # "] = "" 
                  rowDict["ACCOUNT"] = ""
                  output_list.append(rowDict)
                  dff = pd.DataFrame(output_list)
                  output_list = []
                  df = pd.concat([df, dff])
                  df.drop_duplicates(inplace = True)     
                for trans_tollevasion in transaction_tollevasion:
                  tr_b = list(filter(None, trans_tollevasion))
                  violationb = tr_b[0]
                  licensestateb = tr_b[1]
                  licenseplateb = tr_b[2]
                  datedueb = tr_b[3]
                for amntb in amountdue_delinquent:
                  rowDict["TRXN DATE & TIME"] = ""
                  rowDict["EXIT LANE/LOCATION"] = ""
                  rowDict["AMOUNT DUE"] = amntb
                  rowDict["LP"] = licenseplateb
                  rowDict["LP STATE"] = licensestateb
                  rowDict["VIOLATION"] = violationb
                  rowDict["DUE DATE"] = datedueb
                  rowDict["PIN NO #"] = ""
                  rowDict["TOLL AGENCY"] = "FASTRAK"
                  rowDict["REFERENCE # "] = ""
                  rowDict["ACCOUNT"] = "" 
                  output_list.append(rowDict)
                  dff = pd.DataFrame(output_list)
                  output_list = []
                  df = pd.concat([df, dff])
                  df.drop_duplicates(inplace = True)
                      
          print("writing out"+i)
          df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)

                  
bowmanfastrakprocess()                
    
              
              

          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
                 