import os
from pprint import pprint
from tkinter import Y
import pandas as pd
import re
import os
import pdfplumber
import datetime
import getpass
def stoughtonsouthernconnectorprocess(pageText):
    output_list = []
    df = pd.DataFrame()
    rowDict = {"TOLL AGENCY":"SOUTHERN CONNECTOR","LP":"","LP STATE":"","TRXN DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT":"", "REFERENCE # ":"","VIOLATION":"","AMOUNT DUE":"","DUE DATE":"","PIN NO #":"","INVOICE #":"","CODE 1#":"","CODE 2#":"","BILL NO#":"" }
    # print(pageText)
    transaction = re.findall(r'(\d+\/\d.*[:]\d+)\W+(.*)[$|S]\w+.*[$|S]\w+.*[$|S]\w+.*[$|S](\w+\W+\w+)', pageText)
    lp_state = re.findall(r'Li.*P\w+\W+(\w{2})\W+(\w+)', pageText)
    due_date = re.findall(r'Due Date\W+(\d+\W+\d+\W+\d+)', pageText)
    account_no = re.findall(r'Account Number\W+(\w+)|AccountNumber\W+(\w+)', pageText)
    invoice_no = re.findall(r'Document Number\W+(\w+)|DocumentNumber\W+(\w+)', pageText)
    

    for a_c in account_no:
        account = ''.join(a_c)
        rowDict['ACCOUNT'] = account
    for in_v in invoice_no:
        invoice = ''.join(in_v)
        rowDict['REFERENCE # '] = invoice
    for dd in due_date:
        date = dd
        rowDict['DUE DATE'] = date
    for l_s in lp_state:
        ls = list(filter(None, l_s))
        state = ls[0]
        plate = ls[1]
        rowDict['LP STATE'] = state
        rowDict['LP'] = plate
    for t_r in transaction:
        tr = list(filter(None, t_r))
        trxn_date = tr[0]
        exit_lane = tr[1]
        amt = tr[2]
        amount = float(amt)
        rowDict['TRXN DATE & TIME'] = trxn_date
        rowDict['EXIT LANE/LOCATION'] = exit_lane
        rowDict['AMOUNT DUE'] = amount
        rowDict["PIN NO #"] = ""
        

    
        output_list.append(rowDict)
        dff = pd.DataFrame(output_list)
        output_list = []
        df = pd.concat([df, dff])
        df.drop_duplicates(inplace = True)
    return df
                    
                            
#         print("writing out"+i)
#         df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)
