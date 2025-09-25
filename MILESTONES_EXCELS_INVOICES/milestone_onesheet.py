import pandas as pd
import os
import openpyxl
from datetime import datetime
   

inputxlsx_dir = "./input"
outputDir= "./output"
xlsx_files = [os.path.join(inputxlsx_dir, f) for f in os.listdir(inputxlsx_dir) if f.endswith('.xlsx')]
rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT":"","REFERENCE # ":"","VIOLATION":"","AMOUNT DUE":"","DUE DATE":"","PIN NO #":"","INVOICE #":"","CODE 1#":"","CODE 2#":"","BILL NO#":"","POST DATE/TIME":"","EQUIPMENT ID":"","UNIT #":""}


for file in xlsx_files:
    sheets_dict = pd.read_excel(file, sheet_name=None)
    non_empty_sheets = sum(1 for sheet_name, df in sheets_dict.items() if not df.empty)
    finaldf = pd.DataFrame()
    output_list = []
 
    df1 = pd.read_excel(file)
    # print(df1)
    for i, row in df1.iterrows():
        license_plate = row["PLATE NO. "].split("-")[1].strip()
        state = row["PLATE STATE"]
        # state = row.get("RegState") or row.get("Reg State")
        amount = row["TOTAL REBILL"]
        equipID= row["TRAILER NO. "]
        transaction = row["COMMENT_FUNCTION"]
        agency = str(transaction).split(":")[0].replace("Event ID","")
        # location =str(transaction).split("|",1)[-1].strip().split("|",2)[0].strip()
        # datetime_str = str(transaction).split("|",2)[-1].strip().split("|",3)[0].strip()
        datetime_str = row["TRANSACTION DATE "]
        invoice = row["Invoice No"]
        # print(datetime_str)
                
        rowDict["TOLL AGENCY"] = agency
        rowDict["LP"] = license_plate
        rowDict["LP STATE"] = state
        rowDict["TRXN DATE & TIME"] = datetime_str
        rowDict["EXIT LANE/LOCATION"] = ""
        rowDict["ACCOUNT"] = ""
        rowDict["REFERENCE # "] = ""
        rowDict["VIOLATION"] = ""
        rowDict["AMOUNT DUE"] = amount
        rowDict["DUE DATE"] = ""
        rowDict["EQUIPMENT ID"] = equipID
        if invoice:
            rowDict["INVOICE #"] = invoice
        else:
            rowDict["INVOICE #"] = ""
    
        output_list.append(rowDict)
        dff = pd.DataFrame(output_list)
        output_list = []
        finaldf = pd.concat([finaldf, dff],ignore_index= True)
            

                
    output_file = f"{outputDir}/{os.path.splitext(os.path.basename(file))[0]}.xlsx"
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        # finaldf['TRXN DATE & TIME'] = pd.to_datetime(finaldf['TRXN DATE & TIME']).dt.strftime("%m/%d/%Y %H:%M:%S")
       
        try:
            finaldf['TRXN DATE & TIME'] = pd.to_datetime(finaldf['TRXN DATE & TIME']).dt.strftime("%m/%d/%Y %H:%M:%S")
           
            finaldf['INFRACTION DATE'] = pd.to_datetime(finaldf['INFRACTION DATE']).dt.strftime("%m/%d/%Y %H:%M:%S")
          
        except:
            pass
        finaldf.to_excel(writer, sheet_name="Sheet1", index=False)
        

     

    # finaldf.to_excel(f"{outputDir}/{os.path.splitext(os.path.basename(file))[0]}.xlsx", sheet_name=sheet_name, index=False)





        


        