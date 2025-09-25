import pandas as pd
import os
import openpyxl
from datetime import datetime
   

inputxlsx_dir = "./input"
outputDir= "./output"
xlsx_files = [os.path.join(inputxlsx_dir, f) for f in os.listdir(inputxlsx_dir) if f.endswith('.xlsx')]
rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT":"","REFERENCE # ":"","VIOLATION":"","AMOUNT DUE":"","DUE DATE":"","PIN NO #":"","INVOICE #":"","CODE 1#":"","CODE 2#":"","BILL NO#":"","POST DATE/TIME":"","EQUIPMENT ID":"", "UNIT #":""}
vioDict = {"PAYABLE TO":"","STATE":"","VIOLATION":"","INFRACTION DATE":"","NOTICE #":"","CITATION/CASE #":"","CLIENT":"AMAZON LOGISTIC","LICENSE PLATE":"","LP STATE":"","AMOUNT DUE":"","DUE DATE":""}

for file in xlsx_files:
    sheets_dict = pd.read_excel(file, sheet_name=None)
    non_empty_sheets = sum(1 for sheet_name, df in sheets_dict.items() if not df.empty)
    finaldf = pd.DataFrame()
    finaldf_vio = pd.DataFrame()
    output_list = []
    try:
        if non_empty_sheets >= 2:
                df2 = pd.read_excel(file,sheet_name= "Toll Guard")
                df3 = pd.read_excel(file,sheet_name= "Violations")

                # print(df2)
                # print(df3)
                for i_i, i_row in df2.iterrows():
                    # print(df2)
                    license_plate = i_row["Plate"]
                    state = i_row["Reg State"]
                    
                    try:
                        amount = i_row["Amount"]
                    except:
                        amount = i_row.iloc[7]
                    equipID= i_row["EquipId"]
                    transaction = i_row["Comments"]
                    
                    agency = str(transaction).split(":",1)[-1].strip().split("|",1)[0].strip()
                    location =str(transaction).split("|",1)[-1].strip().split("|",2)[0].strip()
                    datetime_str = str(transaction).split("|",2)[-1].strip().split("|",3)[0].strip()
                    # print(location)
                    rowDict["TOLL AGENCY"] = agency.upper()
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
                    amount = j_row.get("REBILL TOTAL") or j_row.get("TOTAL REBILL")
                    # agency = j_row.get("AUTHORITY") or j_row.get("AUTHORITY ID. ")
                    # datetime_str = j_row["TRANSACTION DATE "]
                    # citationcase = j_row.get("EVENT ID.") or j_row.get("TRANSACTION ID. ")
                    # violation = j_row.get("UNIT NO. ") or j_row.get("PO", "")
                    transaction = j_row["COMMENT_FUNCTION"]
                    # print(transaction)
                    # agency = transaction.split('\n')[0].strip()
                    # location = str(transaction).split("Event ID:", 1)[-1].strip().split("|")[1].strip()
                    # datetime_str = str(transaction).split("Event ID:", 1)[-1].strip().split("|")[2].strip()

                    # print(datetime_str)

                    vioDict["PAYABLE TO"] = transaction
                    vioDict["STATE"] = ""
                    # vioDict["VIOLATION"] = violation
                    vioDict["VIOLATION"] = ""
                    vioDict["INFRACTION DATE"] = datetime_str
                    vioDict["NOTICE #"] = ""
                    # vioDict["CITATION/CASE #"] = citationcase
                    vioDict["CITATION/CASE #"] = ""
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





        


        