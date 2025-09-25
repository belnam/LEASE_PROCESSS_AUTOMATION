import os
from pprint import pprint
from tkinter import Y
import pandas as pd
import re
import os
import pdfplumber
import datetime
import getpass
def bowmannjtaprocess(pageText):
                output_list = []
                df = pd.DataFrame()
                rowDict = {"TOLL AGENCY":"NEW JERSEY TURNPIKE AUTHORITY","LP":"","LP STATE":"","TRXN DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT":"", "REFERENCE # ":"","VIOLATION":"","AMOUNT DUE":"","DUE DATE":"","PIN NO #":"","INVOICE #":"","CODE 1#":"","CODE 2#":"","BILL NO#":""  }
                # print(pageText)
                invoicenumber = re.findall(r'InvoiceNumber\W+(\w+)|Invoice\W+Number\W+(\w+)',pageText)
                transaction = re.findall(r'(T\w+\d+\W+\w+)\W+(\w+)\W+(\w+)\W+(\w.*)\s+(\d+\W+\d+\W+\d+.*[:]\d+).*[$|S](\d+\W+\d+)\s+[$|S](\w+\W+\w+)|(\w+\d+\W+\w+)\W+(\w+)\W+(\w+)\W+(\w.*)\W+(\d+\/\d+\/.*[:|;]\d+)\W+.*\W+(\d+\.\d{2})',pageText)
                datedue = re.findall(r'Payment.*due.*by\W+(\w+\W+\w+\W+\w+)|Payment\W+due\W+by\W+(\w+\W+\w+\W+\w+)',pageText)
                # njta = re.findall(r'Interchange#TollPlaza|New Jersey Turnpike Authority',pageText)
               
                # for invoice in invoicenumber:
                #     inv = ''.join(invoice)
                #     rowDict["INVOICE #"] = inv
                #     output_list.append(rowDict)
                #     dff = pd.DataFrame(output_list)
                #     output_list = []
                #     df = pd.concat([df, dff])
                #     df.drop_duplicates(inplace = True)
                    
                if datedue:
                    duedate = datedue[0]
                    duedate = ''.join(duedate)
                    rowDict["DUE DATE"] = duedate

                    
                if transaction:
                    transact = transaction[0]
                    transact = list(filter(''.__ne__,transact))
                    print(transact)
                    violation = transact[0]
                    lpstate = transact[1]
                    lp = transact[2]
                    location = transact[3]
                    datetime =transact[4].replace("|","")
                    try:
                        f_num = transact[5].replace(",","").replace("00","").replace("S","")
                        first_num = float(f_num)
                        s_num = transact[6].replace(",","").replace("00","").replace("S","")
                        second_num = float(s_num)
                        amount = float(first_num + second_num)
                        rowDict['AMOUNT DUE'] = amount
                    except:
                        pass
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
                else:
                    rowDict['VIOLATION'] = ""
                    rowDict['LP STATE'] = ""
                    rowDict['LP'] = ""
                    rowDict['EXIT LANE/LOCATION'] = ""
                    rowDict['TRXN DATE & TIME'] = ""
                    rowDict['AMOUNT DUE'] = ""
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