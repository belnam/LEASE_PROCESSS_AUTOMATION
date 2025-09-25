import os
from pprint import pprint
from tkinter import Y
import pandas as pd
import re
import os
import pdfplumber
import datetime
import getpass
def bowmanctrmaprocess(pageText):
    output_list = []
    df = pd.DataFrame()
    curr_invoice =""
    currentPaged= ""
    rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT":"", "REFERENCE # ":"","VIOLATION":"","AMOUNT DUE":"","DUE DATE":"","PIN NO #":"","INVOICE #":"","CODE 1#":"","CODE 2#":"","BILL NO#":""  }
    # print(pageText)
    ctrma = re.findall(r'\w+-(CTRMA)|TRIP',pageText)
    invoice = re.findall(r'Invoice\D+(\d{12})|INVOICE\W+(\S+)',pageText)
    invoicenumber = re.findall(r'InvoiceNumber\W+(.*)|Invoice\W+Number\W+(.*)',pageText)
    licenseplate = re.findall(r'Vehicle\W+L\w+\W+\w+\W+(\S+)|V\w+L\w+P\w+\W+(\S+)|V\w+\W+L\w+P\w+\W+(\S+)|V\w+L\w+\W+P\w+\W+(\S+)',pageText)
    duedate= re.findall(r'Payment\W+\Due\W+\D+\W+(\w+\W+\d+\W+\d{4})|P\w+D\w+D\w+\W+(\w.*)|P\w+\W+D\w+D\w+\W+(\w.*)|P\w+D\w+\W+D\w+\W+(\w.*)|Payment\W+D\w+\W+D\w+\W+(\w.*)',pageText)
    account = re.findall(r'Account\W+\w+\W+(\S+)',pageText)
    transaction = re.findall(r'(\d{2}\D+\d{2}\D+\d{4}\W+\d{2}\D+\d{2}\D+\d+\D+)\d+\W+(\w.*)[$|S](\w+\W+\w+)',pageText)
    # print(invoice)

    for invoice in invoicenumber:
        inv = ''.join(invoice)
        rowDict["INVOICE #"] = inv.replace("S1","SI")
        output_list.append(rowDict)
        dff = pd.DataFrame(output_list)
        output_list = []
        df = pd.concat([df, dff])
        df.drop_duplicates(inplace = True)
        
    if invoice:
        for inv in invoice:
            invo = list(filter(None,inv))
            invoic =''.join(invo)
            curr_invoice = invoic
            rowDict["REFERENCE # "]=curr_invoice
    else: 
            rowDict["REFERENCE # "]=curr_invoice
            
            
    for lp in  licenseplate:
        license = list(filter(None,lp))
        lplate =''.join(license)
        rowDict["LP"]=lplate

    for due in duedate:
        date = list(filter(None,due))
        datedue =(''.join(date) .replace("January", "1/")
            .replace("February", "2")
            .replace("March", "3")
            .replace("April", "4")
            .replace("May", "5")
            .replace("June", "6")
            .replace("July", "7")
            .replace("August", "8")
            .replace("October", "10")
            .replace("September", "9")
            .replace("November", "11")
            .replace("December", "12")
            .replace( ",","/")
            .replace( " ","")
        )
        rowDict["DUE DATE"]=datedue
    if account:    
        for acc in account:
            accou = list(filter(None,acc))
            accoun =''.join(accou)
            rowDict["ACCOUNT"]=accoun
    else:
            rowDict["ACCOUNT"]=""
        
    for trans in transaction:
        datetime = trans[0]
        location = trans[1]
        amount = trans[2]
        rowDict["TRXN DATE & TIME"]= datetime
        rowDict["EXIT LANE/LOCATION"]=location
        rowDict["AMOUNT DUE"]=amount.replace(",",".")
        rowDict['TOLL AGENCY'] = "CENTRAL TEXAS REGIONAL MOBILITY AUTHORITY"
        rowDict["PIN NO #"] = ""

        
        output_list.append(rowDict)
        dff = pd.DataFrame(output_list)
        output_list = []
        df = pd.concat([df, dff])
        df.drop_duplicates(inplace = True)
        df["REFERENCE # "] = df[df.index.isin(df.reset_index().groupby("LP")["index"].first().to_list())]["REFERENCE # "]  #compare two cells if equl the invoice of first cell to be duplicated in the other cells
        df["REFERENCE # "].fillna(method='ffill', inplace=True)
    return df
                                    
#         print("writing out"+ fname)
#         df.to_excel(str(outputDir+fname).replace(".pdf","")+".xlsx", index=False)
# bowmanctrmaprocess()