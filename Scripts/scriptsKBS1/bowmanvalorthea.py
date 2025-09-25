import pandas as pd
import re
import os
import os
import pdfplumber
import getpass

def bowmanvalortheaprocess(pageText):
    output_list = []
    df = pd.DataFrame()
    rowDict = {"TOLL AGENCY":"TAMPA HILLSBOROUGH EXPRESSWAY AUTHORITY","LP":"","LP STATE":"","TRXN DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT":"", "REFERENCE # ":"","VIOLATION ":"","AMOUNT DUE":"","DUE DATE":"","PIN NO #":"","INVOICE #":"","CODE 1#":"","CODE 2#":"","BILL NO#":"" }
    workingDir = f"raw_files\\"
    # print(pageText)
   

    invoicenumber = re.findall(r'InvoiceNumber\W+(\w+)|Invoice\W+Number\W+(\w+)',pageText)
    # lpstate = re.findall(r'Li\w+\W+P\w+\W+(\w+)\W+(\w+)\W+|Li\w+P\w+\W+(\w+)\W+(\w{2})\W+',pageText)
    lpstate = re.findall(r'Li\w+P\w+\W+(\w+\d+\w+)|Li\w+\W+P\w+\W+(\w+\d+\w+)',pageText)
    statelp = re.findall(r'Li\w+P\w+\W+\w+\d+\w+\W+(\w+)\W+|Li\w+\W+P\w+\W+\w+\d+\w+\W+(\w+)\W+',pageText)
    account = re.findall(r'A\w+\W+N\w+\W+(\w+\d+)|Acc\w+N\w+\W+(\d+)',pageText)
    notice = re.findall(r'N\w+\W+N\w+\W+(\w+\d+)|No\w+N\w+\W+(\w+)',pageText)
    duedate = re.findall(r'P\w+\W+r\w+\W+\w+\W+\w+\W+\w+\W+(\d+\D+\d+\D+\d+)',pageText)
    previousamount = re.findall('T\w+A\w+D\w+\W+(\w+\W+\w+)',pageText)
    transaction = re.findall(r'\d+\D+\d+\D+\d+\W+(\S+\W+\d+\S+.*[00])\W+(\w+.*)[$|S](\w+\W+\w+)|\d+\D+\d+\D+\d{4}\W+(\d{2}\D+\d{2}\D+\d{4}\W+\w+\W+\w+\W+\S+)\W+(\w+.*)[$|S](\w+\W+\w+)',pageText)
    
    
    for invoice in invoicenumber:
        inv = ''.join(invoice).replace("S1","SI")
        rowDict["INVOICE #"] = inv
        output_list.append(rowDict)
        dff = pd.DataFrame(output_list)
        output_list = []
        df = pd.concat([df, dff])
        df.drop_duplicates(inplace = True)
    
    
    for lp in lpstate:
        license =''.join(lp)
        rowDict["LP"] = license
        
    for state in statelp:
        stat =''.join(state)
        rowDict["LP STATE"] = stat
        
    for acc in account:
        acc_nt = ''.join(acc)
        rowDict["ACCOUNT"] = acc_nt
        
    for notic in notice:
        not_ice = ''.join(notic)
        rowDict["REFERENCE # "] = not_ice
    if duedate:    
        for due in duedate:
            rowDict["DUE DATE"] = due
    else:
        rowDict["DUE DATE"] = "IMMEDIATELY"
        
        
    for previous in previousamount:
        rowDict["AMOUNT DUE"] = previous
        rowDict["TRXN DATE & TIME"] = ""
        rowDict["EXIT LANE/LOCATION"] = ""
        rowDict["PIN NO #"] = ""
        
        output_list.append(rowDict)
        dff = pd.DataFrame(output_list)
        output_list = []
        df = pd.concat([df, dff])
        df.drop_duplicates(inplace = True)
    # return df
    if transaction:
        for trans in transaction:
            rowDict["TRXN DATE & TIME"] = trans[0]
            rowDict["EXIT LANE/LOCATION"] = trans[1]
            rowDict["AMOUNT DUE"] = trans[2]
            rowDict["PIN NO #"] = ""
    else:
            rowDict["TRXN DATE & TIME"] = ""
            rowDict["EXIT LANE/LOCATION"] = ""
            rowDict["AMOUNT DUE"] = ""
            rowDict["PIN NO #"] = ""
                
            output_list.append(rowDict)
            dff = pd.DataFrame(output_list)
            output_list = []
            df = pd.concat([df, dff])
            df.drop_duplicates(inplace = True)
    return df
         
            
            
            
            
