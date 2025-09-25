import pandas as pd
import os
import openpyxl
from datetime import datetime
   

inputxlsx_dir = "./input"
outputDir= "./output"
xlsx_files = [os.path.join(inputxlsx_dir, f) for f in os.listdir(inputxlsx_dir) if f.endswith('.xlsx')]
rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT":"","REFERENCE # ":"","VIOLATION":"","AMOUNT DUE":"","DUE DATE":"","PIN NO #":"","INVOICE #":"","CODE 1#":"","CODE 2#":"","BILL NO#":"","POST DATE/TIME":"","EQUIPMENT ID":"","UNIT #":""}
vioDict = {"PAYABLE TO":"","STATE":"","VIOLATION":"","INFRACTION DATE":"","NOTICE #":"","CITATION/CASE #":"","CLIENT":"AMAZON LOGISTIC","LICENSE PLATE":"","LP STATE":"","AMOUNT DUE":"","DUE DATE":""}

for file in xlsx_files:
    sheets_dict = pd.read_excel(file, sheet_name=None)
    non_empty_sheets = sum(1 for sheet_name, df in sheets_dict.items() if not df.empty)
    finaldf = pd.DataFrame()
    finaldf_vio = pd.DataFrame()
    output_list = []
    try:
        if non_empty_sheets == 1:
            df1 = pd.read_excel(file)
            # print(df1)
            if "TOTAL REBILL" in df1.columns:
                for i, row in df1.iterrows():
                    license_plate = row["PLATE NO. "]
                    state = row["PLATE STATE"]
                    amount = row["TOTAL REBILL"]
                    equipID= row["TRAILER NO. "]
                    agency = row["AUTHORITY"]
                    datetime_str = row["TRANSACTION DATE "]
                    citationcase = row["EVENT ID."]
                    violation = row["PO"]

                    vioDict["PAYABLE TO"] = agency
                    vioDict["STATE"] = ""
                    vioDict["VIOLATION"] = violation
                    vioDict["INFRACTION DATE"] = datetime_str
                    vioDict["NOTICE #"] = ""
                    vioDict["CITATION/CASE #"] = citationcase
                    vioDict["CLIENT"] = ""
                    vioDict["LICENSE PLATE"] = license_plate
                    vioDict["LP STATE"] = state
                    vioDict["AMOUNT DUE"] = amount
                    vioDict["DUE DATE"] = ""
                
                    output_list.append(vioDict)
                    dff = pd.DataFrame(output_list)
                    output_list = []
                    finaldf = pd.concat([finaldf, dff],ignore_index= True)
            else:
                df1.columns = df1.iloc[0]   # Set the first row as column names
                df1 = df1[1:] # Drop the first row to avoid repetition
                print(df1)
                for i, row in df1.iterrows():
                    license_plate = row["Plate"]
                    state = row.get("RegState") or row.get("Reg State")
                    amount = row["Amount"]
                    equipID= row["EquipId"]
                    transaction = row["Comments"]
                    agency = str(transaction).split(":",1)[-1].strip().split("|",1)[0].strip()
                    location =str(transaction).split("|",1)[-1].strip().split("|",2)[0].strip()
                    datetime_str = str(transaction).split("|",2)[-1].strip().split("|",3)[0].strip()
                    invoice = row.get("Invoice No") or row.get("Inv #")
                    # print(datetime_str)
                            
                    rowDict["TOLL AGENCY"] = agency
                    rowDict["LP"] = license_plate
                    rowDict["LP STATE"] = state
                    rowDict["TRXN DATE & TIME"] = datetime_str
                    rowDict["EXIT LANE/LOCATION"] = location
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
                

        if non_empty_sheets >= 2:
            try:
                # df2 = pd.read_excel(file,sheet_name= "Tollguard")
                df2 = pd.read_excel(file,sheet_name= "TollGuard")
            except:
                df2 = pd.read_excel(file,sheet_name= "Toll Guard")
            try:
                # df3 = pd.read_excel(file,sheet_name= "Violations")
                df3 = pd.read_excel(file,sheet_name= "PaperViolation")
            except:
                df3 = pd.read_excel(file,sheet_name= "Paper Toll & Violation")
            
            df2.columns = df2.iloc[0]   
            df2 = df2[1:]
            df3.columns = df3.iloc[0]   
            df3 = df3[1:]
            print(df2)
            # if "Plate" in df2.columns or "Invoice No" in df2.columns:
            if "Invoice" in df2.columns or "Invoice No" in df2.columns:
                for i_i, i_row in df2.iterrows():
                    license_plate = i_row["Plate"]
                    # print(license_plate)
                    state = i_row.get("RegState") or i_row.get("Reg State")
                    try:
                        amount = i_row["Amount"]
                    except:
                        amount = i_row.iloc[7]
                    equipID= i_row["EquipId"]
                    transaction = i_row["Comments"]
                    agency = str(transaction).split(":",1)[-1].strip().split("|",1)[0].strip()
                    location =str(transaction).split("|",1)[-1].strip().split("|",2)[0].strip()
                    datetime_str = str(transaction).split("|",2)[-1].strip().split("|",3)[0].strip()
                    invoice = i_row.get("Invoice") or i_row.get("Invoice No")
                    
                    rowDict["TOLL AGENCY"] = agency
                    rowDict["LP"] = license_plate
                    rowDict["LP STATE"] = state
                    rowDict["TRXN DATE & TIME"] = datetime_str
                    rowDict["EXIT LANE/LOCATION"] = location
                    rowDict["ACCOUNT"] = ""
                    rowDict["REFERENCE # "] = ""
                    rowDict["VIOLATION"] = ""
                    rowDict["AMOUNT DUE"] = amount
                    rowDict["DUE DATE"] = ""
                    rowDict["INVOICE #"] = invoice
                    rowDict["EQUIPMENT ID"] = equipID
                    output_list.append(rowDict)
                    dff = pd.DataFrame(output_list)
                    output_list = []
                    finaldf = pd.concat([finaldf, dff],ignore_index= True)

                for i_j, j_row in df3.iterrows():
                    if "AUTHORITY" in df3:
                        license_plate = j_row.get("PLATE NO. ")  
                        state = j_row["PLATE STATE"]
                        amount = j_row["TOTAL REBILL"]
                        equipID= j_row["TRAILER NO. "]
                        agency = j_row["AUTHORITY"]
                        datetime_str = j_row["TRANSACTION DATE "]
                        citationcase = j_row["EVENT ID."]
                        violation = j_row["PO"]
                        vioDict["PAYABLE TO"] = agency
                        vioDict["STATE"] = ""
                        vioDict["VIOLATION"] = violation
                        vioDict["INFRACTION DATE"] = datetime_str
                        vioDict["NOTICE #"] = ""
                        vioDict["CITATION/CASE #"] = citationcase
                        vioDict["CLIENT"] = ""
                        vioDict["LICENSE PLATE"] = license_plate
                        vioDict["LP STATE"] = state
                        vioDict["AMOUNT DUE"] = amount
                        vioDict["DUE DATE"] = ""
                        output_list.append(vioDict)
                        dff = pd.DataFrame(output_list)
                        output_list = []
                        finaldf_vio = pd.concat([finaldf_vio, dff],ignore_index= True)

                    else:
                        license_plate = j_row.get("PLATE NO. ")  
                        state = j_row["PLATE STATE"]
                        amount = j_row["TOTAL REBILL"]
                        equipID= j_row["TRAILER NO. "]
                        datetime_str = j_row["TRANSACTION DATE "]
                        commentfunction = j_row["COMMENT_FUNCTION"]
                        agency = str(commentfunction).split("|",1)[-1].strip().split("|",1)[0].strip()
                        citationcase = str(commentfunction).split(":")[-1].split("|")[0].strip()
                        # violation = j_row["PO"]
                        # print(citationcase)

                        vioDict["PAYABLE TO"] = agency
                        vioDict["STATE"] = ""
                        vioDict["VIOLATION"] = ""
                        vioDict["INFRACTION DATE"] = datetime_str
                        vioDict["NOTICE #"] = ""
                        vioDict["CITATION/CASE #"] = citationcase
                        vioDict["CLIENT"] = ""
                        vioDict["LICENSE PLATE"] = license_plate
                        vioDict["LP STATE"] = state
                        vioDict["AMOUNT DUE"] = amount
                        vioDict["DUE DATE"] = ""

                        output_list.append(vioDict)
                        dff = pd.DataFrame(output_list)
                        output_list = []
                        finaldf_vio = pd.concat([finaldf_vio, dff],ignore_index= True)

            else:
                for i_i, i_row in df2.iterrows():
                    license_plate = i_row["Plate"]
                    print(license_plate)
                    state = i_row["RegState"]
                    try:
                        amount = i_row["Amount"]
                    except:
                        amount = i_row.iloc[7]
                    equipID= i_row["EquipId"]
                    transaction = i_row["Comments"]
                    agency = str(transaction).split(":",1)[-1].strip().split("|",1)[0].strip()
                    location =str(transaction).split("|",1)[-1].strip().split("|",2)[0].strip()
                    datetime_str = str(transaction).split("|",2)[-1].strip().split("|",3)[0].strip()
                    # print(datetime_str)
                    rowDict["TOLL AGENCY"] = agency
                    rowDict["LP"] = license_plate
                    rowDict["LP STATE"] = state
                    rowDict["TRXN DATE & TIME"] = datetime_str
                    rowDict["EXIT LANE/LOCATION"] = location
                    rowDict["ACCOUNT"] = ""
                    rowDict["REFERENCE # "] = ""
                    rowDict["VIOLATION"] = ""
                    rowDict["AMOUNT DUE"] = amount
                    rowDict["DUE DATE"] = ""
                    rowDict["INVOICE #"] = ""
                    rowDict["EQUIPMENT ID"] = equipID
                
                    output_list.append(rowDict)
                    dff = pd.DataFrame(output_list)
                    output_list = []
                    finaldf = pd.concat([finaldf, dff],ignore_index= True)

                for i_j, j_row in df3.iterrows():
                    license_plate = j_row["PLATE NO. "]
                    state = j_row["PLATE STATE"]
                    amount = j_row["TOTAL REBILL"]
                    agency = j_row.get("AUTHORITY") or j_row.get("AUTHORITY ID. ")
                    datetime_str = j_row["TRANSACTION DATE "]
                    citationcase = j_row.get("EVENT ID.") or j_row.get("TRANSACTION ID. ")
                    # violation = j_row["PO"]
                    violation = j_row.get("PO") or j_row.get("PO", "")

                    vioDict["PAYABLE TO"] = agency
                    vioDict["STATE"] = ""
                    vioDict["VIOLATION"] = violation
                    vioDict["INFRACTION DATE"] = datetime_str
                    vioDict["NOTICE #"] = ""
                    vioDict["CITATION/CASE #"] = citationcase
                    vioDict["CLIENT"] = ""
                    vioDict["LICENSE PLATE"] = license_plate
                    vioDict["LP STATE"] = state
                    vioDict["AMOUNT DUE"] = amount
                    vioDict["DUE DATE"] = ""

                    output_list.append(vioDict)
                    dff = pd.DataFrame(output_list)
                    output_list = []
                    finaldf_vio = pd.concat([finaldf_vio, dff],ignore_index= True)
    except:
        pass
    output_file = f"{outputDir}/{os.path.splitext(os.path.basename(file))[0]}.xlsx"
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        # finaldf['TRXN DATE & TIME'] = pd.to_datetime(finaldf['TRXN DATE & TIME']).dt.strftime("%m/%d/%Y %H:%M:%S")
       
        try:
            finaldf['TRXN DATE & TIME'] = pd.to_datetime(finaldf['TRXN DATE & TIME']).dt.strftime("%m/%d/%Y %H:%M:%S")
            finaldf_vio['INFRACTION DATE'] = pd.to_datetime(finaldf_vio['INFRACTION DATE']).dt.strftime("%m/%d/%Y %H:%M:%S")
            finaldf['INFRACTION DATE'] = pd.to_datetime(finaldf['INFRACTION DATE']).dt.strftime("%m/%d/%Y %H:%M:%S")
            finaldf_vio['TRXN DATE & TIME'] = pd.to_datetime(finaldf_vio['TRXN DATE & TIME']).dt.strftime("%m/%d/%Y %H:%M:%S")
        except:
            pass
        finaldf.to_excel(writer, sheet_name="Sheet1", index=False)
        finaldf_vio.to_excel(writer, sheet_name="Sheet2", index=False)

     

    # finaldf.to_excel(f"{outputDir}/{os.path.splitext(os.path.basename(file))[0]}.xlsx", sheet_name=sheet_name, index=False)





        


        