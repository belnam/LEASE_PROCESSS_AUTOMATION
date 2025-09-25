import os
from pprint import pprint
from tkinter import Y
import pandas as pd
import re
import os
import pdfplumber
import datetime
import getpass
def bowmandrjtbcprocess(pageText):
                output_list = []
                df = pd.DataFrame()
                rowDict = {"TOLL AGENCY":"DELAWARE RIVER JOINT TOLL BRIDGE COMMISSION","LP":"","LP STATE":"","TRXN DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT":"", "REFERENCE # ":"","VIOLATION":"","AMOUNT DUE":"","DUE DATE":"","PIN NO #":"","INVOICE #":"","CODE 1#":"","CODE 2#":"","BILL NO#":"","POST DATE/TIME":""  }

                # transaction = re.findall(r'(T\w+\d+\W+\w+)\W+(\w+)\W+(\w+)\W+(\w.*)\s+(\d+\W+\d+\W+\d+.*[:]\d+).*[$|S](\d+\W+\d+)\s+[$|S](\w+\W+\w+)',pageText)
                transactionb = re.findall(r'\W+(\w+)\W+(\w+\d+)\W+\d+\W+\d+\W+\d+.*DRJTBC\W+(.*)\W+\d+\W+(\d+\/\d+\/\d+\W+\d+.*[:|;]\d+)\W+(\w+\W+\w+)',pageText)
                datedue = re.findall(r'\W\d+\W+.*[$|S]\d+\W+\d+\W+(\d+\W+\d+\W+\d+)|Paymentdueby\W+(\w+\W+\w+\W+\w+)|Payment\W+due\W+by\W+(\w+\W+\w+\W+\w+)',pageText)
                accountnumber = re.findall(r'Acco.*Num\w+\W+(\d+)',pageText)
                referencenumber = re.findall(r'Toll.*B.*N\w+\W+(\w+\d+)',pageText)

                for date in datedue:
                    duedate = ''.join(date)
                    rowDict["DUE DATE"] = duedate

                for acc in accountnumber:
                    account = acc
                    rowDict["ACCOUNT"] = account
                for ref in referencenumber:
                    reference = ref
                    rowDict["REFERENCE # "] = reference
                for transb in transactionb:
                    amount = transb[4]
                    lpstate = transb[0]
                    lp = transb[1]
                    location = transb[2]
                    datetime =transb[3]
                    rowDict['AMOUNT DUE'] = amount 
                    rowDict['LP STATE'] = lpstate
                    rowDict['LP'] = lp
                    rowDict['EXIT LANE/LOCATION'] = location
                    rowDict['TRXN DATE & TIME'] = datetime
                    rowDict["PIN NO #"] = ""
                    rowDict['VIOLATION'] = ""

          
                    output_list.append(rowDict)
                    dff = pd.DataFrame(output_list)
                    output_list = []
                    df = pd.concat([df, dff])
                    df.drop_duplicates(inplace = True)
                return df
                
# print("writing out"+i)
# df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)
    
    
# bowmannjtaprocess()


      # for trans in transaction:
                #     transact = trans
                #     violation = transact[0]
                #     lpstate = transact[1]
                #     lp = transact[2]
                #     location = transact[3]
                #     datetime =transact[4]
                #     try:
                #         f_num = transact[5].replace(",","").replace("00","").replace("S","")
                #         first_num = float(f_num)
                #         s_num = transact[6].replace(",","").replace("00","").replace("S","")
                #         second_num = float(s_num)
                #         amount = float(first_num + second_num)
                #         rowDict['AMOUNT DUE'] = amount 
                #     except:
                #         pass
                #     rowDict['VIOLATION'] = violation
                #     rowDict['LP STATE'] = lpstate
                #     rowDict['LP'] = lp
                #     rowDict['EXIT LANE/LOCATION'] = location
                #     rowDict['TRXN DATE & TIME'] = datetime
                #     rowDict["PIN NO #"] = ""
               