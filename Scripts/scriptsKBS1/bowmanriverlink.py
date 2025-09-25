import os
from pprint import pprint
from tkinter import Y
import pandas as pd
import re
import os
import pdfplumber
import datetime

def bowmanriverlinkprocess(pageText):
    output_list = []
    df = pd.DataFrame()
    rowDict = rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT":"", "REFERENCE # ":"","VIOLATION":"","AMOUNT DUE":"","DUE DATE":"","PIN NO #":"","INVOICE #":"","CODE 1#":"","CODE 2#":"","BILL NO#":"" }

    # print(pageText)
    invoicenumber = re.findall(r'InvoiceNumber(.*)|Invoice\W+Number(.*)',pageText)
    transaction = re.findall(r'\d{9}\W+(\w+).*([A-Z]{1}\w+)\W+(\w+\W+\w+.*[:]\w+)\W+(\w+)\W+(\w+\W+\w+)',pageText)
    duedate = re.findall(r'I\w+D\w+D\w+\W+(\d+\W+\d+\W+\d+)|I\w+\W+D\w+D\w+\W+(\d+\W+\d+\W+\d+)|I\w+D\w+\W+D\w+\W+(\d+\W+\d+\W+\d+)|I\w+\W+D\w+\W+D\w+\W+(\d+\W+\d+\W+\d+)',pageText)
    reference = re.findall(r'RE\w+NU\w+\W+(\w+)|RE\w+\W+NU\w+\W+(\w+)',pageText)
    
    
    for invoice in invoicenumber:
        inv = ''.join(invoice)
        rowDict["INVOICE #"] = inv
        output_list.append(rowDict)
        dff = pd.DataFrame(output_list)
        output_list = []
        df = pd.concat([df, dff])
        df = df.dropna(subset=['TOLL AGENCY'])
        df.drop_duplicates(inplace = True)
    for ref in reference:
        referen = ''.join(ref)
        rowDict["REFERENCE # "] = referen
    if duedate:
        for due in duedate:
            date = ''.join(due)
            rowDict["DUE DATE"] = date
    else:
        pass
    if transaction:
        for transact in transaction:
            license = transact[0]
            lpstate = transact[1]
            datetime = transact[2]
            location = transact[3]
            amount = transact[4]
            rowDict["LP"] = license
            rowDict["LP STATE"] = lpstate
            rowDict["TRXN DATE & TIME"] = datetime
            rowDict["EXIT LANE/LOCATION"] = location
            rowDict["AMOUNT DUE"] = amount
            rowDict["TOLL AGENCY"] = "RIVERLINK"
            rowDict["PIN NO #"] = ""
    else:
        pass
        
        output_list.append(rowDict)
        dff = pd.DataFrame(output_list)
        output_list = []
        df = pd.concat([df, dff])
        df.drop_duplicates(inplace = True)
        df = df.dropna(subset=['TOLL AGENCY'])
    
    return df
                
    # print("writing out testing")

                    
# bowmanriverlinkprocess()
