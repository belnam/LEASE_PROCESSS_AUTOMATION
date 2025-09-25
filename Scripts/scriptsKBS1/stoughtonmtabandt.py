import os
from pprint import pprint
from tkinter import Y
import pandas as pd
import re
import os
import pdfplumber
import datetime
import getpass
def stoughtonmtabridgesandtunnelsprocess(pageText):
    output_list = []
    df = pd.DataFrame()
    rowDict = {"TOLL AGENCY":"MTAB&T","LP":"","LP STATE":"","TRXN DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT":"", "REFERENCE # ":"","VIOLATION":"","AMOUNT DUE":"","DUE DATE":"","PIN NO #":"","INVOICE #":"","CODE 1#":"","CODE 2#":"","BILL NO#":""}
   
    transactions = re.findall(r'(T\d+\W+\w+).*([A-Z]{1}\D{1})\W+(\d+)\s+(.*)\s+(\d+\/\d+.*[:]\d+).*[$|S](\w+\W+\w+)|(T\d+\W+\w+).*([A-Z]{1}\D{1})(\d+)\s+(.*)\s+(\d+\/\d+.*[:]\d+).*[$|S](\w+\W+\w+)', pageText)
    due_date = re.findall(r'Dueby(\w+\/\w+\/\d{4})|Dueby\W+(\w+\/\w+\/\d{4})|Due\W+by(\w+\/\w+\/\d{4})|Due\W+by\W+(\w+\/\w+\/\d{4})', pageText)

    for d_d in due_date:
        dd = list(filter(None,d_d))
        date = dd[0]
        rowDict['DUE DATE'] = date.upper()
    for trans in transactions:
        transact = list(filter(None,trans))
        rowDict["VIOLATION"] = transact[0]
        rowDict["LP STATE"] = transact[1]
        rowDict["LP"] = transact[2]
        rowDict["EXIT LANE/LOCATION"] = transact[3]
        rowDict["TRXN DATE & TIME"] = transact[4]
        rowDict["AMOUNT DUE"] = transact[5]
        rowDict["PIN NO #"] = ""
    
    
    
        output_list.append(rowDict)
        dff = pd.DataFrame(output_list)
        output_list = []
        df = pd.concat([df, dff])
        df.drop_duplicates(inplace = True)
    return df
                                
                            
#         print("writing out"+i)
#         df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)

# stoughtonmtabridgesandtunnelsprocess()