import os
from pprint import pprint
from tkinter import Y
import pandas as pd
import re
import os
import pdfplumber
import datetime
import getpass
def bowmandrpaprocess(pageText):
                output_list = []
                df = pd.DataFrame()
                rowDict = {"TOLL AGENCY":"DELAWARE RIVER PORT AUTHORITY","LP":"","LP STATE":"","TRXN DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT":"", "REFERENCE # ":"","VIOLATION":"","AMOUNT DUE":"","DUE DATE":"","PIN NO #":"","INVOICE #":"","CODE 1#":"","CODE 2#":"","BILL NO#":""}

                # invoicenumber = re.findall(r'InvoiceNumber\W+(\w+)|Invoice\W+Number\W+(\w+)',pageText)
                transaction = re.findall(r'(T\w+\d+\W+\w+)\W+(\w+)\W+(\w+)\W+(\w.*)\s+(\d+\W+\d+\W+\d+.*[:]\d+).*[$|S](\d+\W+\d+)\W+(\d+\W+\d+)',pageText)
                datedue = re.findall(r'Paymentdueby\W+(\w+\W+\w+\W+\w+)|Payment\W+due\W+by\W+(\w+\W+\w+\W+\w+)',pageText)
                # drpa = re.findall(r'DELAWARE\W+\w+\n+P\w+\W+\w+TY|Delaware River Port Authority',pageText)
               
                # for invoice in invoicenumber:
                #     inv = ''.join(invoice)
                #     rowDict["INVOICE #"] = inv
                #     output_list.append(rowDict)
                #     dff = pd.DataFrame(output_list)
                #     output_list = []
                #     df = pd.concat([df, dff])
                #     df.drop_duplicates(inplace = True)
                    
                for date in datedue:
                    duedate = ''.join(date)
                    rowDict["DUE DATE"] = duedate
               
                for trans in transaction:
                    transact = trans
                    violation = transact[0]
                    lpstate = transact[1]
                    lp = transact[2]
                    location = transact[3]
                    datetime =transact[4]
                    try:
                        f_num = transact[5].replace(",","").replace("00","").replace("S","")
                        first_num = float(f_num)
                        s_num = transact[6].replace(",","").replace("00","").replace("S","")
                        second_num = float(s_num)
                        amount = float(first_num + second_num)
                        rowDict['AMOUNT DUE'] = amount 
                    except:
                        pass
                    # print(second_num)
                    rowDict['VIOLATION'] = violation
                    rowDict['LP STATE'] = lpstate
                    rowDict['LP'] = lp
                    rowDict['EXIT LANE/LOCATION'] = location
                    rowDict['TRXN DATE & TIME'] = datetime
                    # rowDict['AMOUNT DUE'] = amount 
                    rowDict["PIN NO #"] = ""  
                 
                    output_list.append(rowDict)
                    dff = pd.DataFrame(output_list)
                    output_list = []
                    df = pd.concat([df, dff])
                    df.drop_duplicates(inplace = True)
                return df
                
# print("writing out"+i)
# df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)
    
    
# bowmannjtaprocess()