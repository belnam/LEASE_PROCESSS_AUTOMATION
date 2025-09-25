
from bowmanfdot import*
from bowmanriverlink import*
from bowmannjta import*
from bowmandeldot import*
from bowmanctrma import*
from bowmanvalorthea import*
from bowmanhctra import*
from bowmancfea import*
from bowmane470 import*
from bowmanmtatbm import*
from bowmanntta import*
from bowmanpaturnpike import*
from bowmanpaybyplate import*
from bowmanpocahontas import*
from bowmansouthbay import*
from bowmansrta import*
from bowmanwsdot import*
from bowmandrjtbc import*
from bowmandrpa import*
from bowmandrba import*
from stoughtontxtag import*
from stoughtonmtabandt import*
from stoughtonsouthern import*
from stoughtondulles import*
from bowmancitation import*
from bowmanbcbc import*
import getpass
import re as reg_ex


rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT":"", "REFERENCE # ":"","VIOLATION":"","AMOUNT DUE":"","DUE DATE":"","PIN NO #":"","INVOICE #":"","CODE 1#":"","CODE 2#":"","BILL NO#":"","UNIT #":"","POST DATE/TIME":"" }

username = getpass.getuser()
print(username)
workingDir = f"C:\\Users\\{username}\\Documents\\Projects\\RENTALS-PROCESS-AUTOMATION\\Downloaded_Scans\\"
outputDir = f"C:\\Users\\{username}\\Documents\\Projects\\RENTALS-PROCESS-AUTOMATION\\SRTS_OUTPUT\\"
# final_df = pd.DataFrame()
# output_list = []
text = ""
for i in os.listdir(workingDir):
      output_list = []
      final_df = pd.DataFrame(columns=rowDict)
      rowDict["INVOICE #"] = ""
      rowDict["TOLL AGENCY"] = ""
      rowDict["LP"] = ""
      rowDict["LP STATE"] = ""
      rowDict["TRXN DATE & TIME"] = ""
      rowDict["EXIT LANE/LOCATION"] = ""
      rowDict["ACCOUNT"] = ""
      rowDict["REFERENCE # "] = ""
      rowDict["VIOLATION"] = ""
      rowDict["AMOUNT DUE"] = ""
      rowDict["DUE DATE"] = ""
      rowDict["PIN NO #"] = ""
      rowDict["INVOICE #"] = ""
      rowDict["POST DATE/TIME"] = ""
 
      with pdfplumber.open(workingDir+i) as pdf:
          currentPage = ""
          licensepl=""
          for page in pdf.pages:
            pageText = page.extract_text(x_tolerance=1)
            # pageText = page.extract_text()
            text += pageText
            # print(pageText)
            with open("text.txt", "w", encoding="utf-8") as file:
              file.write(text)
            
            page1 = re.findall(r'(Page:1)|(Page: 1)|(Page:)|(Page!)',pageText)
            fdot = re.findall(r'TOLL\W+(ENFORCEMENT)',pageText)
            riverlink = re.findall(r'(RIV)-LINK|RIVERLINK',pageText)
            deldot = re.findall(r'D\w+(Department)|D\w+\W+(Department)',pageText)
            fastrak = re.findall(r'(BRIDGE)|(DELINQUENT).*T.*E.*V|fastrak|(Keeps).*Y.*Mo',pageText)
            tollroads = re.findall(r'(NOTICE)O\w+|(NOTICE)\W+O\w+',pageText)
            ctrma = re.findall(r'L.*P.*T.*(BILL)|(RMA).*T.*P\w+',pageText)
            valorthea =re.findall(r'(TAMPA)',pageText)
            hctra = re.findall(r'\W+(ZERO).*F\w+.*P.*DA',pageText)
            cfea = re.findall(r'PAY.*(PLATE).*IN\w+|Why.*P.*(Double)',pageText)
            mdta = re.findall(r'(NOTD)\W+A\w+|(NOTD)+A\w+',pageText)
            e470 = re.findall(r'E.*47.*PU.*H.*A\w+|E-470 PUBLIC HIGHWAY AUTHORITY|LIC.*PLA.*TOL.*(STATEMENT)|(License).*P\w+\#.*\w+[A-Z]\w+.*\n+T.*Tr.*\s\d+\/\d+\/.*[:]\w+.*\d+\/\d+.*[$|S]\w.*|(Statement)ID\W+State|(License).*P\w+\#.*\w+[A-Z]\w+.*\n+T.*Tr.*\s\d+\/\d+\/.*[:]\w+.*\d+\/\d+.*[$|S]s\d.*',pageText)
            mtatbym = re.findall(r'(TOLLS.*MAIL) |(ATTENTION)\:|(ATTENTION)\:.*E|Already.*NY.*customer.*.*(tollsbymailny).*com',pageText)
            ntta = re.findall(r'(NORTH)TEXAS|(NORTH)\W+TEXAS|(Electronic)',pageText)
            paturnpike = re.findall(r'Pen\w+\W+(Turnpike)|Pen\w+(Turnpike)',pageText)
            paybyplatema = re.findall(r'(EZDriveMA)\W+|(Massachusetts).*D\w.*T\w+',pageText)
            pocahontas = re.findall(r'(Pocahontas).*P\w+|(Pocahontas)P\w+',pageText)
            southbay = re.findall(r'(South)B|(South)\W+B',pageText)
            srta = re.findall(r'The.*(SRTA)',pageText)
            wsdot = re.findall(r'T\w+\W+(STATEMENT)',pageText)
            drjtbc = re.findall(r'Joint.*To.*Bridge|DRJTBC|(Delaware).*\n+J.*\n+C.*|Delaware River Joint Toll Bridge Commission',pageText)
            drpa = re.findall(r'DELAWARE\W+\w+\n+P\w+\W+\w+TY|Delaware River (Port) Authority',pageText)
            drba = re.findall(r'and.*(bay).*Authority|(DELAWARE)\W+\w.*\n+&\w+TY|Delaware River and Bay Authority|(DELAWARE)\W+R\w+|(DELAWARE)R\w+',pageText)
            njta = re.findall(r'(interchange).*\W+.*To\w+.*P\w+|(Interchange).*\W+.*To\w+.*P\w+|(Interchange).*\W+.*Toll.*Pl\w+|(Interchange)#TollPlaza|New Jersey Turnpike Authority',pageText)
            txtag = re.findall(r'C\w.*(Account)\#\W+\d+|TxTag.org',pageText)
            mtabridgesandtunnels = re.findall(r'(VIOLATION).*TR\w+.*F\w+.*C\w+',pageText)
            southern = re.findall(r'(Southern)',pageText)
            dulles = re.findall(r'dullesgreenway|Notice.*(Unpaid).*Toll',pageText)
            citation = re.findall(r'(CITATION)',pageText)
            fbctra = re.findall(r'(Fort).*B.*Co.*',pageText)
            milestone = re.findall(r'MILESTONE|(Trailer).*Do\w+\W+',pageText)
            xtra = re.findall(r'XTRA|\w{4}\W+(Agreement)',pageText)
            premier = re.findall(r'PREMIER|\w{4}\W+(Description)',pageText)
            bcbc = re.findall(r'(Burlington).*C.*B\w+.*C\w+',pageText)
            ohturnpike = re.findall(r'(Ohio).*T\w+',pageText)
            kansas = re.findall(r'(KANSAS).*TU\w+.*AUTHORITY',pageText)


            if page1 :
              invoicenumber = re.findall(r'In.*Num\w+\W+(\$\w+)|InvoiceNumber\W+(\w+.*)|Invoice\W+Number\W+(\W\w+.*)|invoiceNumber\W+(\w+.*)|invoice\W+Number\W+(\w+.*)',pageText)
              for invoice in invoicenumber:
                inv = ''.join(invoice).replace("S1","SI").replace("51","SI").replace("$","")
                if inv.startswith("1"):
                  inv = "SI" + inv[1:]
                #   inv = "SI" + inv
                # if not inv.startswith("SI"):
                  # inv = "SI" + inv
                rowDict["INVOICE #"] = inv
                output_list.append(rowDict) 
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
                
            if drjtbc or currentPage  == "Delaware" :
              currentPage = "Delaware" 
              op_drjtbc = bowmandrjtbcprocess(pageText)
              op_drjtbc["INVOICE #"] = rowDict["INVOICE #"]
              final_df = pd.concat([final_df,op_drjtbc],ignore_index=True)

            if bcbc or currentPage  == "Burlington" :
              currentPage = "Burlington" 
              op_bcbc = bowmanbcbcprocess(pageText)
              op_bcbc["INVOICE #"] = rowDict["INVOICE #"]
              final_df = pd.concat([final_df,op_bcbc],ignore_index=True)     
            
            if drpa or currentPage  == "Port":
              currentPage = "Port" 
              op_drpa = bowmandrpaprocess(pageText)
              op_drpa["INVOICE #"] = rowDict["INVOICE #"]
              final_df = pd.concat([final_df,op_drpa],ignore_index=True)
                          
            if drba or currentPage  == "DELAWARE":
              currentPage = "DELAWARE" 
              op_drba = bowmandrbaprocess(pageText)
              op_drba["INVOICE #"] = rowDict["INVOICE #"]
              final_df = pd.concat([final_df,op_drba],ignore_index=True)
             
            if njta or currentPage  == "Interchange":
              currentPage = "Interchange" 
              op_njta = bowmannjtaprocess(pageText)
              op_njta["INVOICE #"] = rowDict["INVOICE #"]
              final_df = pd.concat([final_df,op_njta],ignore_index=True)
     
            # if citation or currentPage  == "CITATION":
            #   currentPage = "CITATION"
            #   state = re.findall(r'N\w+-(\w.*)\n+(\w+)',pageText)
            #   for agency in tollagency:
            #     rowDict["TOLL AGENCY"] = agency[0]+''+agency[1]
            #   transaction = re.findall(r'(\d+\/\d+\/\d+.*[:]\w+)\W+(.*)([A-Z]{2})(\w+).*\n*(\w+)',pageText) 
            #   for trans in transaction:
            #     rowDict["TRXN DATE & TIME"] = trans[0]
            #     rowDict["EXIT LANE/LOCATION"] = trans[1] +''+ trans[4]
            #     rowDict["LP STATE"] = trans[2]
            #     rowDict["LP"] = trans[3]
            #   transactionb = re.findall(r'(\w+\d+)\W+[$](\d+\W+\d+)\W+(\d{2}\W+\d+\W+\d+)',pageText)
            #   for tranxs in transactionb:
            #     rowDict["VIOLATION"] = tranxs[0]
            #     rowDict["AMOUNT DUE"] = tranxs[1]
            #     rowDict["DUE DATE"] = tranxs[2]
            #     output_list.append(rowDict)
            #     dff = pd.DataFrame(output_list)
            #     output_list = []
            #     final_df = pd.concat([final_df, dff])
            #     final_df.drop_duplicates(inplace = True)

            if kansas or currentPage  == "KANSAS":
              currentPage = "KANSAS"
              tollagency = re.findall(r'N\w+-(\w.*)\n+(\w+)',pageText)
              for agency in tollagency:
                rowDict["TOLL AGENCY"] = agency[0]+''+agency[1]
              transaction = re.findall(r'(\d+\/\d+\/\d+.*[:]\w+)\W+(.*)([A-Z]{2})(\w+).*\n*(\w+)',pageText) 
              for trans in transaction:
                rowDict["TRXN DATE & TIME"] = trans[0]
                rowDict["EXIT LANE/LOCATION"] = trans[1] +''+ trans[4]
                rowDict["LP STATE"] = trans[2]
                rowDict["LP"] = trans[3]
              transactionb = re.findall(r'(\w+\d+)\W+[$](\d+\W+\d+)\W+(\d{2}\W+\d+\W+\d+)',pageText)
              for tranxs in transactionb:
                rowDict["VIOLATION"] = tranxs[0]
                rowDict["AMOUNT DUE"] = tranxs[1]
                rowDict["DUE DATE"] = tranxs[2]
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)

            if ohturnpike or currentPage  == "Ohio":
              currentPage = "Ohio"
              invoicenumber = re.findall(r'IN\w+.*NU\w+\W+(\w+\d+\w+)',pageText)
              if invoicenumber:
                inv = invoicenumber[0]
                rowDict["REFERENCE # "] = inv
                rowDict['TOLL AGENCY'] = "OHIO TURNPIKE"
              accountnumber = re.findall(r'AC\w+.*N\w+\W+(\w+\d+\w+)',pageText)
              if accountnumber:
                acc = accountnumber[0]
                rowDict["ACCOUNT"] = acc
              licenseplate_state = re.findall(r'LI\w+.*PL\w+\W+(\w+)\W+(\w+\d+\w+)',pageText)
              if licenseplate_state:
                lp = licenseplate_state[0]
                rowDict["LP STATE"] = lp[0]
                rowDict["LP"] = lp[1]
              duedate = re.findall(r'PA\w+.*D.*D\w+\W+(\d+\W+\d+\W+\d+)',pageText)
              if duedate:
                dd = duedate[0]
                rowDict["DUE DATE"] = dd
              transactions = re.findall(r'(.*)\W+(\d+\/\d+\/\d+.*[:]\d+).*[$|S](\d+\W+\d+)',pageText)
              if transactions:
                trans = transactions[0]
                rowDict["EXIT LANE/LOCATION"] = trans[0]
                rowDict["TRXN DATE & TIME"]= trans[1]
                rowDict["AMOUNT DUE"] = trans[2]
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
              
            if fbctra or currentPage  == "Fort":
              currentPage = "Fort"
              transactions = re.findall(r'(\w+\W+\d{5})\W+(\w{2})\W+(\w{7})\W+(\S+\D+\d+)\W+(\S+\W+\d+\W+\d+\W+\d+)\W+(\d+\W+\d+)', pageText)
              due_date = re.findall(r'Date\WDue\W\W(\d*\W\d*\W\d*)', pageText)
              total_due = re.findall(r'SEE.*\n\w+\W+\w+\W+(\w+\W+\w+)', pageText)
              violation = re.findall(r'Notice Number\W+(\w{13})', pageText)
              l_plate = re.findall(r'License Plate\W+(\w{7})', pageText)
              lp_state = re.findall(r'License Plate State\W+(\w{2})', pageText)
              for t_r in transactions:
                  tr = list(filter(None, t_r))
                  trans = ''.join(tr)
                  violation = tr[0]
                  state = tr[1]
                  lp = tr[2]
                  exit_lane = tr[3]
                  trxn_date = tr[4]
                  amount = tr[5]
                  rowDict['VIOLATION'] = violation
                  rowDict['LP STATE'] = state
                  rowDict['LP'] = lp
                  rowDict['EXIT LANE/LOCATION'] = exit_lane
                  rowDict['TRXN DATE & TIME'] = trxn_date
                  rowDict['AMOUNT DUE'] = amount
                  rowDict['PIN NO #'] = ""
                  rowDict['TOLL AGENCY'] = "FORT BEND COUNTY TOLL ROAD AUTHORITY"
                  output_list.append(rowDict)
                  dff = pd.DataFrame(output_list)
                  output_list = []
                  final_df = pd.concat([final_df, dff])
                  final_df.drop_duplicates(inplace = True)
              for v in violation:
                  rowDict['VIOLATION'] = v
              for l_p in l_plate:
                  rowDict['LP'] = l_p
              for l_s in lp_state:    
                  rowDict['LP STATE'] = l_s 
              for dd in due_date:
                  rowDict['DUE DATE'] = dd
              for t_d in total_due:
                  rowDict['AMOUNT DUE'] = t_d
                  rowDict['EXIT LANE/LOCATION'] = ""
                  rowDict['TRXN DATE & TIME'] = ""
                  rowDict['PIN NO #'] = ""
                  rowDict['TOLL AGENCY'] = "FORT BEND COUNTY TOLL ROAD AUTHORITY"
                  output_list.append(rowDict)
                  dff = pd.DataFrame(output_list)
                  output_list = []
                  final_df = pd.concat([final_df, dff])
                  final_df.drop_duplicates(inplace = True)
              
            if dulles or currentPage  == "Unpaid":
              currentPage = "Unpaid" 
              due_date = re.findall(r'Due.*D\w+\W+(\w{2}\W+\w+\W+\w+)', pageText)
              if due_date:
                date = due_date[0]
                rowDict['DUE DATE'] = date
              license_details = re.findall(r'Li.*P\w+\W+(\w{2})(\w+)|Li.*P\w+\W+(\w{2})\W+(\w+)', pageText)  
              if license_details:
                l_d = license_details[0]
                ld = list(filter(None, l_d))
                state = ld[0]
                plate = ld[1]
                rowDict['LP STATE'] = state
                rowDict['LP'] = plate
              transactions = re.findall(r'(\w{16})\W+(\d+\/\d+\/\d+.*M)\s+(.*)[$|S](\w+\W+\w+).*[$|S](\w+\W+\w+)', pageText)  
              if transactions:
                tr = transactions[0]
                tr = list(filter(None, t_r))
                invoice_no = tr[0]
                trxn_date = tr[1]
                exit_lane = tr[2]
                try:
                  toll_fee = float(tr[3].replace('O', '0'))
                  admin_fee = float(tr[4].replace('O', '0'))
                  total_amount = toll_fee + admin_fee
                  rowDict['AMOUNT DUE'] = total_amount
                except:
                  pass
                rowDict['EXIT LANE/LOCATION'] = exit_lane
                rowDict['TRXN DATE & TIME'] = trxn_date
                # rowDict['AMOUNT DUE'] = total_amount
                rowDict['REFERENCE # '] = invoice_no
                rowDict['TOLL AGENCY'] = "DULLES GREENWAY"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
              else:
                amountdue = re.findall(r'Am\w+.*D\w+\W+(\d+\W+\d+)', pageText)
                if amountdue:
                  amount = amountdue[0]
                  rowDict['AMOUNT DUE'] = amount
                location = re.findall(r'To\w+.*(Pl\w+\W+\w.*)(L\w+\W+\w+)', pageText)
                if location:
                  loc = location[0]
                  plaza = loc[0]
                  lane = loc[1]
                  locate = plaza +''+ lane
                  rowDict['EXIT LANE/LOCATION'] = locate
                transaction_date = re.findall(r'Da\w+.*u.*to\w+\W+(\w+)', pageText)
                transaction_time = re.findall(r'Ti\w+.*u.*to\w+\W+(\w+\W+\w+\W+\w+\W+\w+)', pageText)
                if transaction_date and transaction_time:
                  date = transaction_date[0]
                  time = transaction_time[0]
                  rowDict['TRXN DATE & TIME'] = date +''+ time
                reference = re.findall(r'Se\w+\W+N\w+\W+(\w+\d+)', pageText)
                if reference:
                  ref = reference[0]
                  rowDict['REFERENCE # '] = ref
                  rowDict['TOLL AGENCY'] = "DULLES GREENWAY"
                  output_list.append(rowDict)
                  dff = pd.DataFrame(output_list)
                  output_list = []
                  final_df = pd.concat([final_df, dff])
                  final_df.drop_duplicates(inplace = True)
             
            if southern or currentPage  == "Southern":
              currentPage = "Southern" 
              op_southern = stoughtonsouthernconnectorprocess(pageText)
              op_southern["INVOICE #"] = rowDict["INVOICE #"]
              final_df = pd.concat([final_df,op_southern],ignore_index=True)
              
            if mtabridgesandtunnels or currentPage  == "VIOLATION":
              currentPage = "VIOLATION" 
              op_mtabnt = stoughtonmtabridgesandtunnelsprocess(pageText)
              op_mtabnt["INVOICE #"] = rowDict["INVOICE #"]
              final_df = pd.concat([final_df,op_mtabnt],ignore_index=True)
              
            if txtag or currentPage  == "Account":
              currentPage = "Account"
              due_date = re.findall(r'Pay\w+D\w+D\w+\W+(\w+\W+\w+\W+\w+)', pageText)
              for d_date in due_date:
                date = d_date
                rowDict['DUE DATE'] = date
              account = re.findall(r'^Account\W+(\w{10})', pageText)
              if account:
                for a_c in account:
                    ac = a_c
                    rowDict['ACCOUNT'] = ac
              else:
                rowDict['ACCOUNT'] = ""
              reference = re.findall(r'Statement\W+(\d{12})',pageText)
              for ref in reference:     
                rf = ref
                rowDict['REFERENCE # '] = rf
              transactions = re.findall(r'(\d{2}\/\d+\W+\d+.*[M])\W+\w+\W+(\w{7}|\w{8})\W+\S+\W+(.*)[-][$](\d+\W+\d+|\S+)|(\d+\/\d+\/\d+\W+\d+\W+\d+\W+\w+)\W+\w+\W+(\S+)\W+\S+\W+(.*)[-][$](\d+\W+\d+)|(\d{2}\/\d+\W+\d+)\W+\S+\W+(\w{7})\W+\S+\W+(.*)[-][$](\d+\W+\d+)|(\d{2}\/\d+\W+\d+.*[M])\W+\S+\W+(\S+)\W+(.*)[-]\W+(\w+\W+\w+)|(\d{2}\/\d+\W+\d+.*[M])\W+\w+\W+(\w{7}|\w{8})\W+\S+\W+(.*)[-][$|S](\d+\W+\d+)', pageText)
              for t_r in transactions:
                tr = list(filter(None, t_r))
                trxn_date = tr[0]
                lp = tr[1]
                exit_lane = tr[2]
                try:
                  amt = tr[3].replace(',','.').replace(';','.').replace(':','.').replace('Q','0')
                  amount = float(amt)
                  rowDict['AMOUNT DUE'] = amount
                except:
                  pass
                rowDict['LP'] = lp
                rowDict['TRXN DATE & TIME'] = trxn_date
                rowDict['EXIT LANE/LOCATION'] = exit_lane
                # rowDict['AMOUNT DUE'] = amount
                rowDict['TOLL AGENCY'] = "TXTAG"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
            
            if riverlink or currentPage  == "RIV" or currentPage  == "RIVERLINK" :
              currentPage = "RIV" or "RIVERLINK"
              op_riverlink = bowmanriverlinkprocess(pageText)
              op_riverlink["INVOICE #"] = rowDict["INVOICE #"]
              final_df = pd.concat([final_df,op_riverlink],ignore_index=True)
              final_df.drop_duplicates(inplace = True)
              
            if fdot or currentPage  == "ENFORCEMENT" :
              currentPage = "ENFORCEMENT"
              transaction = re.findall(r'\d+\/\d+\/\d+\W+\w+\W(.*)\s+\d+\s+(\d{2}\S+.*)[$|S](\w+\W+\w+)',pageText)
              trxn_index = len(transaction) -1
              last_index = 0
              addfee = re.findall(r'\$\d+\W+\d+\W+\d+\W+\d+\W+\d+\W+\d+\W+(\S+)\W+\S+\W+\d+\W+\d+\W+\d+',pageText)
              for add in addfee:
                c = list(add)
                d = ''.join(c)
              for line in pageText.split("\n"):
                duedate = re.findall(r'\$(\d+\W+\d+)\W+\d+\W+\d+\W+\d+\W+\d+\W+(\S+)\W+(\S+)\W+(\d+\W+\d+\W+\d+)',line)
                for d_d in duedate:
                  dd = d_d[3] 
                  rowDict["DUE DATE"] = dd
              invlpstate = re.findall(r'IN\w+\W+(\d+).*A\w+\W+(\d+).*LI.*PL\w+\W+(\w+).*S\w+\W+(\w+)|I\w+\#\D+(\d+)\D+(\d+).*Li.*Pl\w+\W+(\w+).*S\w+\W+(\w+)|\w+\#\D+(\d+)\D+(\d+)\s+\w+\s+\w+\W+(\S+)\W+\w+\W+(\w{2})',pageText) 
              if invlpstate:
                lp = invlpstate[0]
                license = lp[2]
                invoice =lp[0]
                account = lp[1]
                state = lp[3].replace("Da","").replace("i","I").replace("WL","WI")
                rowDict['LP'] = license
                rowDict['REFERENCE # '] = invoice
                rowDict['ACCOUNT'] = account
                rowDict['LP STATE'] = state 
              invlpstateB = re.findall(r'In\w+\D+(\S+)\W+A\w+\D+(\d{9})\W+\w+\W+(\S+)\W+\w+\W+(\S+)|In\w+\D+(\S+)\W+A\w+\D+(\d{9})\W+\w+\W+\w+\W+(\S+)\W+\w+\W+(\w+)',pageText) 
              if invlpstateB:
                lp = invlpstate[0]
                license = lp[2]
                invoice =lp[0]
                account = lp[1]
                state = lp[3].replace("Da","").replace("i","I").replace("te","").replace("WL","WI")
                rowDict['LP'] = license
                rowDict['REFERENCE # '] = invoice
                rowDict['ACCOUNT'] = account
                rowDict['LP STATE'] = state
              amnt_duee = re.findall(r'\$\d+\W+\d+\W+\d+\W+\d+\W+\d+\W+\d+\W+\S+\W+(\S+)\W+\d+\W+\d+\W+\d{2}',pageText)
              for dueamnt in amnt_duee:
                  rowDict['AMOUNT DUE'] = dueamnt
                  rowDict['EXIT LANE/LOCATION'] = ""
                  rowDict['TRXN DATE & TIME'] = ""
                  rowDict['TOLL AGENCY'] = "FDOT"
                  rowDict["PIN NO #"] = ""
                  rowDict["VIOLATION"] = ""
                  output_list.append(rowDict)
                  dff = pd.DataFrame(output_list)
                  output_list = []
                  final_df = pd.concat([final_df, dff])
                  final_df.drop_duplicates(inplace = True)
                  final_df = final_df[final_df['TRXN DATE & TIME'] != ""]    
              # duedate = re.findall(r'\$(\d+\W+\d+)\W+\d+\W+\d+\W+\d+\W+\d+\W+(\S+)\W+(\S+)\W+(\d+\W+\d+\W+\d+)',pageText)
              # for prev in duedate:
              #   prevA = prev[0]
              #   prevB = prev[1]
              #   prevC = prev[2]
              #   amntdue = prevA
              #   dueamnt  = list(amntdue)
              #   amntamntdue = ''.join(dueamnt).replace(",",".")
              #   try:
              #     due_amount = float(amntamntdue)
              #     e = prevB
              #     f  = list(e)
              #     g = ''.join(f).replace(",",".")
              #     try:
              #         h = float(g)
              #     except:
              #         pass             
              #     k = prevC
              #     l  = list(k)
              #     m = ''.join(l).replace(",",".")
              #     try:
              #         n = float(m)
              #     except:
              #         pass
              #     if  due_amount + h  == n:
              #       rowDict['AMOUNT DUE'] = n
              #     elif due_amount + h != n:
              #       rowDict['AMOUNT DUE'] = due_amount
              #   except:
              #     pass
              #   rowDict['EXIT LANE/LOCATION'] = ""
              #   rowDict['TRXN DATE & TIME'] = ""
              #   rowDict['TOLL AGENCY'] = "FDOT"
              #   output_list.append(rowDict)
              #   dff = pd.DataFrame(output_list)
              #   output_list = []
              #   final_df = pd.concat([final_df, dff])
              #   final_df.drop_duplicates(inplace = True)
              #   final_df = final_df[final_df['AMOUNT DUE'] != 0]
              transaction = re.findall(r'\d+\/\d+\/\d+\W+\w+\W(.*)\s+\d+\s+(\d{2}\S+.*)[$|S](\w+\W+\w+)',pageText)
              for trans in transaction:
                location = trans[0]
                datetime = trans[1]
                amount = trans[2]
                
                locate = location
                a = list(locate)
                b = ''.join(a) 
                
                rowDict['EXIT LANE/LOCATION'] = b.replace("SOS","50S").replace("508","50S").replace("503","50S").replace("CHA","").replace("COLLECTIONS","")
                rowDict['TRXN DATE & TIME'] = datetime.replace(";",":")
                
                amountdue = amount
                # amtdue  = list(amountdue)
                # dueamt = ''.join(amtdue).replace(",",".").replace("I","1").replace(" ","")
                try:
                    amtdue  = list(amountdue)
                    dueamt = ''.join(amtdue).replace(",",".").replace("I","1").replace(" ","")
                    dueamount = float(dueamt)
                    if last_index != trxn_index:  
                     rowDict['AMOUNT DUE'] = dueamount
                    else:
            
                     rowDict['AMOUNT DUE'] = dueamount + float(d)
                    
                    last_index += 1
                except:
                    pass
                # if last_index != trxn_index:  
                #     rowDict['AMOUNT DUE'] = dueamount
                # else:
                #     try:
                #      rowDict['AMOUNT DUE'] = dueamount + float(d)
                #     except:
                #         pass
                # last_index += 1
                rowDict['TOLL AGENCY'] = "FDOT"
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
                final_df = final_df[final_df['AMOUNT DUE'] != 0]
              
            if fastrak or currentPage  == "BRIDGE" or currentPage == "fastrak": 
                currentPage = "BRIDGE" or "fastrak"         
                reference = re.findall(r"In\w+.*N\w+\W+(\d+)|in\w+.*N\w+\W+(\d+)|In\w+N\w+\W+(\d+)|in\w+N\w+\W+(\d+)",pageText)
                licplactestate = re.findall(r'Li.*Pl\w+\W+(\w{2})\W+(\w+\d+)|Li\w+\W+P\w+\W+(\w+)\W+(\w+\d+)|Li\w+P\w+\W+(\w+)\W+(\w+\d+)',pageText)
                transaction = re.findall(r'(\d{2}\D\d+\D\d+\s+\d+\W+\d+\W+\d+)\s+(\w+\s+\d+)\s+\D+(\d+\W+\d+)',pageText)
                transaction_withLocation = re.findall(r'(T\d+\W+\d+)\W+(\w{2})(\w+).*(\W+\w+\W+\w+)\W+(\d+\/\d+\/\d{2}.*[:|;]\d+).*[$\S]\W+(\d+\W+\d+)',pageText)
                
                transaction_delinquent = re.findall(r'(T\d+)\W+(\w{2})\W+(\w+).*[$|S]\w+\W+\w+\W+(\w+\/\w+\W+\w+)\W+(\d+\W+\d+)|(T\d+)\W+(\w{2})(\w+\d+).*[$|S]\w+\W+\w+\W+(\w+\/\w+\W+\w+)\W+(\d+\W+\d+)',pageText)
                transaction_tollevasion = re.findall(r'(T\d+)\W+(\w{2})\W+(\w+).*[$|S]\w+\W+\w+\W+(\w+\/\w+\W+\w+)\W+(\d+\W+\d+)|(T\d+)\W+(\w{2})(\w+\d+).*[$|S]\w+\W+\w+\W+(\w+\/\w+\W+\w+)\W+(\d+\W+\d+)',pageText)
                duedate = re.findall(r'D.*Da\w+\W+(\d+\/\d+\W+\d+)',pageText)
                datedue = re.findall(r'\$\d+\W+\d+\W+(\d+\/\d+\/\d{2})',pageText)
                amountdue_delinquent = re.findall(r'Am.*D.*On.*O.*Be\w+.*[$|S](\d+\W+\d+)',pageText)
                for inv in reference:
                  invce =''.join(inv) 
                  curr_invoice = invce               
                  rowDict["REFERENCE # "] = curr_invoice
                  rowDict["TOLL AGENCY"] = "FASTRAK" 
                 
                for trans in transaction:
                  Trxndatetime = trans[0]
                  location = trans[1]
                  amount = trans[2]
                  rowDict["TRXN DATE & TIME"] = Trxndatetime
                  rowDict["EXIT LANE/LOCATION"] = location
                  rowDict["AMOUNT DUE"] = amount
                  rowDict["TOLL AGENCY"] = "FASTRAK"
                for due in datedue:
                  rowDict["DUE DATE"] = due
                 
                for lic in licplactestate:
                  lpstate =lic[0]
                  license = lic[1]
                  rowDict["LP"] = license
                  rowDict["LP STATE"] = lpstate
                  rowDict["TOLL AGENCY"] = "FASTRAK"
                  output_list.append(rowDict)
                  dff = pd.DataFrame(output_list)
                  output_list = []
                  final_df = pd.concat([final_df, dff])
                  final_df.drop_duplicates(inplace = True) 
                for transacte in transaction_withLocation:
                  tre = list(filter(None, transacte))
                  violatione = tre[0]
                  licensestatee = tre[1]
                  licenseplatee = tre[2]
                  locatione = tre[3]
                  datetimee =tre[4]
                  amounte = tre[5]
                  rowDict["TRXN DATE & TIME"] = datetimee
                  rowDict["EXIT LANE/LOCATION"] = locatione
                  rowDict["AMOUNT DUE"] = amounte
                  rowDict["LP"] = licenseplatee
                  rowDict["LP STATE"] = licensestatee
                  rowDict["VIOLATION"] = violatione
                  # rowDict["DUE DATE"] = datedue
                  rowDict["PIN NO #"] = ""
                  rowDict["TOLL AGENCY"] = "FASTRAK"
                  rowDict["REFERENCE # "] = "" 
                  rowDict["ACCOUNT"] = ""
                  output_list.append(rowDict)
                  dff = pd.DataFrame(output_list)
                  output_list = []
                  final_df = pd.concat([final_df, dff])
                  final_df.drop_duplicates(inplace = True)


                for date in duedate:
                  rowDict["DUE DATE"] = date
                  rowDict["TOLL AGENCY"] = "FASTRAK"
                  rowDict["PIN NO #"] = ""
                  rowDict["VIOLATION"] = ""
                  rowDict["ACCOUNT"] = ""
                  output_list.append(rowDict)
                  dff = pd.DataFrame(output_list)
                  output_list = []
                  final_df = pd.concat([final_df, dff])
                  final_df.drop_duplicates(inplace = True)
               
                for trans_delinquent in transaction_delinquent:
                  tr = list(filter(None, trans_delinquent))
                  violation = tr[0]
                  licensestate = tr[1]
                  licenseplate = tr[2]
                  datedue = tr[3]
                for amnt in amountdue_delinquent:
                  rowDict["TRXN DATE & TIME"] = ""
                  rowDict["EXIT LANE/LOCATION"] = ""
                  rowDict["AMOUNT DUE"] = amnt
                  rowDict["LP"] = licenseplate
                  rowDict["LP STATE"] = licensestate
                  rowDict["VIOLATION"] = violation
                  rowDict["DUE DATE"] = datedue
                  rowDict["PIN NO #"] = ""
                  rowDict["TOLL AGENCY"] = "FASTRAK"
                  rowDict["REFERENCE # "] = "" 
                  rowDict["ACCOUNT"] = ""
                  output_list.append(rowDict)
                  dff = pd.DataFrame(output_list)
                  output_list = []
                  final_df = pd.concat([final_df, dff])
                  final_df.drop_duplicates(inplace = True)     
                for trans_tollevasion in transaction_tollevasion:
                  tr_b = list(filter(None, trans_tollevasion))
                  violationb = tr_b[0]
                  licensestateb = tr_b[1]
                  licenseplateb = tr_b[2]
                  datedueb = tr_b[3]
                for amntb in amountdue_delinquent:
                  rowDict["TRXN DATE & TIME"] = ""
                  rowDict["EXIT LANE/LOCATION"] = ""
                  rowDict["AMOUNT DUE"] = amntb
                  rowDict["LP"] = licenseplateb
                  rowDict["LP STATE"] = licensestateb
                  rowDict["VIOLATION"] = violationb
                  rowDict["DUE DATE"] = datedueb
                  rowDict["PIN NO #"] = ""
                  rowDict["TOLL AGENCY"] = "FASTRAK"
                  rowDict["REFERENCE # "] = ""
                  rowDict["ACCOUNT"] = "" 
                  output_list.append(rowDict)
                  dff = pd.DataFrame(output_list)
                  output_list = []
                  final_df = pd.concat([final_df, dff])
                  final_df.drop_duplicates(inplace = True)
              
              
            if deldot or currentPage  == "Department" :
              currentPage = "Department"
              duedate = re.findall(r'P.*D.*B\w+\W+(\d+\W+\d+\W+\d+)|PA\w+\W+(\d+\W+\d+\W+\d+)|P\w+\W+DU\w+\W+BY\w+\W+(\d+\W+\d+\W+\d+)|P\w+\W+D\w+\w+\W+(\d+\/\d+\W+\d+)|P\w+\w+\W+BY\w+\W+(\d+\W+\d+\W+\d+)|Re\w+D\w+D\w+\W+(\w+\W+\w+\W+\w+)|Re\w+\W+D\w+\W+D\w+\W+(\w+\W+\w+\W+\w+)',pageText)
              if duedate:
                date = duedate[0] 
                date = list(filter(''.__ne__,date))
                datedue =  date[0]
                rowDict["DUE DATE"] = datedue
              lpstate = re.findall(r'Li.*P\w+\W+(\w+\d+\w+)\W+(\w+)|Li.*Pl\w+.*N.*S\w+\W+(\w+\d+)\W+(\w+)',pageText)
              if lpstate:
                lstate = lpstate[0]
                lp = lstate[0]
                state = lstate[1]
                rowDict["LP"] = lp
                rowDict["LP STATE"] = state
                rowDict["TOLL AGENCY"] = "DELAWARE DEPARTMENT OF TRANSPORTATION"
              datetime = re.findall(r'Da\w+\W+(\w+\W+\w+\W+\w+)\W+T\w+\W+(\w+\W+\w+\W+\d+)|DA\w+\W+(\w+\W+\w+\W+\w+)\W+T\w+\W+(\w+\W+\w+\W+\d+)',pageText)    
              for timedate in datetime:
                date_time = timedate[0] +' ' +timedate[1]
                rowDict["TRXN DATE & TIME"] = date_time
              location = re.findall(r'P\w+\W+(\w+)\W+L\w+\W+(\w+)',pageText)  
              for locate in location:
                rowDict["EXIT LANE/LOCATION"] = locate[0] +' ' +locate[1]
                # output_list.append(rowDict)
                # dff = pd.DataFrame(output_list)
                # output_list = []
                # final_df = pd.concat([final_df, dff])
                # final_df.drop_duplicates(inplace = True)
                # final_df = final_df[final_df['TRXN DATE & TIME'] != ""]
  
              transactiondeldotb = re.findall(r'In.*Nu\w+\W+(\w+\W+\d+).*St\w+\W+(\w+)\W+(\w+).*N\w+\W+(\w+)',pageText)
              if transactiondeldotb:
                  for transaction in transactiondeldotb:
                    rowDict["REFERENCE # "] = transaction[0]
                    rowDict["LP"] = transaction[1]
                    rowDict["LP STATE"] = transaction[2]
                    rowDict["ACCOUNT"] = transaction[3]
              else:
                  rowDict["REFERENCE # "] = ""
                  rowDict["ACCOUNT"] = ""
              violation = re.findall(r'FORVIOLATION(\w+\W+\w+)|F\w+\W+VIOLATION(\w+\W+\w+)|FO\w+\W+V\w+\W+(\w+\W+\w+)|F\w+VIO\w+\W+(\w+\W+\w+)',pageText)    
              if violation:
                  for vio in violation:
                      violate = ''.join(vio)
                      rowDict["VIOLATION"] = violate
              else:
                    rowDict["VIOLATION"] = ""
                    output_list.append(rowDict)
                    dff = pd.DataFrame(output_list)
                    output_list = []
                    final_df = pd.concat([final_df, dff])
                    final_df.drop_duplicates(inplace = True)
                
              amountdue = re.findall(r'BA\w+.*D\w+\W+(\d+.*)|BA\w+D\w+\W+(\d+\W+\w+)|BA\w+\W+DU\w+\W+(\d+\W+\w+)',pageText)
              for amount in amountdue:
                try:
                  amt = ''.join(amount).replace(",",".")
                  amnt = float(amt)
                  rowDict["AMOUNT DUE"] = amnt
                  output_list.append(rowDict)
                  dff = pd.DataFrame(output_list)
                  output_list = []
                  final_df = pd.concat([final_df, dff])
                  final_df.drop_duplicates(inplace = True)
                except:
                  pass
              transactiondelb = re.findall(r'\d+\W+\d+\W+\d+\W+(\d+.*[:]\w+).*Toll\W+(\w+)\W+[$](\w+\W+\w+)',pageText)
              for trans in transactiondelb:
                rowDict["TRXN DATE & TIME"] = trans[0]
                rowDict["EXIT LANE/LOCATION"] = trans[1]
                rowDict["AMOUNT DUE"] = trans[2]
                rowDict["TOLL AGENCY"] = "DELAWARE DEPARTMENT OF TRANSPORTATION"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
                final_df = final_df[final_df['TRXN DATE & TIME'] != ""]
            
              
            if ctrma or currentPage  ==  "BILL" or currentPage  ==  "RMA":
              currentPage = "BILL" or "RMA"
              op2_ctrma = bowmanctrmaprocess(pageText)
              op2_ctrma["INVOICE #"] = rowDict["INVOICE #"]
              final_df = pd.concat([final_df,op2_ctrma],ignore_index=True)
              
            if tollroads or currentPage  == "NOTICE":
              currentPage = "NOTICE" 
              duedate = reg_ex.findall(r'Amount Due Before\D+(\S+\d+)|A\w+D\w+Before(\S+)|A\w+\W+D\w+\W+Before\W+(\S+)',pageText)
              for date in duedate:
                due =''.join(date).replace("-", "")
                rowDict['DUE DATE'] = due
              reference = reg_ex.findall(r'Reference#\D+(\S+)|R\w+#(\w+)',pageText)
              for ref in reference:
                refer = ''.join(ref).replace(",","").replace(".","")
                rowDict['REFERENCE # '] = refer
              transaction = re.findall(r'(\d{2}\D+\d{2}\D+\d+\:\d.*[M])\s+(\w+)\s+(.*)[$|S]\w+\W+\w+\W+\w+\W+\w+\W+(\S+).*[\/]\w+\W+(\S+)',pageText)
              for trans in transaction:
                rowDict['TRXN DATE & TIME'] = trans[0]
                rowDict['LP'] = trans[1]
                rowDict['EXIT LANE/LOCATION'] = trans[2]
                rowDict['AMOUNT DUE'] = trans[3].replace(",",".")
                rowDict['VIOLATION'] = trans[4]
                rowDict['TOLL AGENCY'] = "THE TOLL ROADS"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
              
            if valorthea or currentPage  == "TAMPA":
              currentPage = "TAMPA" 
              op2_valorthea = bowmanvalortheaprocess(pageText)
              op2_valorthea["INVOICE #"] = rowDict["INVOICE #"]
              final_df = pd.concat([final_df,op2_valorthea],ignore_index=True)
              
            if hctra or currentPage  == "ZERO":
              currentPage = "ZERO" 
              licenseplate = re.findall(r'L\w+\W+Pl\w+\W+(\S+)\W+\w+\W+$|L\w+\W+P\w+\W+N\w+\W+\w+\W+(\S+)|LicensePlate\W+(\w+)',pageText)
              for license in licenseplate:
                lp = list(filter(None,license))
                lplate =''.join(lp).replace("(","")
                rowDict["LP"] = lplate
              licensestate = re.findall(r'L\w+\W+Pl\w+\W+\S+\W+(\w+)\W+$|L\w+\W+P\w+\W+N\w+\W+(\w+)\W+\S+|LicensePlate\W+\w+\W+(\w+)',pageText)
              for state in licensestate:
                st = list(filter(None,state))
                lstate =''.join(st)
                rowDict["LP STATE"] = lstate
              invoice = re.findall(r'In\w+N\w+:(\d+).*[$|S]|InvoiceNumber\W+(\d{12})',pageText)
              for inv in invoice:
                invo = list(filter(None,inv))
                invoic =''.join(invo)
                rowDict["REFERENCE # "] = invoic
              duedate = re.findall(r'P\w+\W+\w+\W+D\w+\W+(\d{2}\D+\w+\D+\w+)|PaymentDueDate\W+(\S+)',pageText)
              for due in duedate:
                date = list(filter(None,due))
                datedue =''.join(date)
                rowDict["DUE DATE"] = datedue
              amnt_due = re.findall(r'To.*Am.*Du.*[$|S](.*)',pageText)
              for dueamnt in amnt_due:
                rowDict["AMOUNT DUE"] = dueamnt
                rowDict["TRXN DATE & TIME"] = ""
                rowDict["EXIT LANE/LOCATION"] = ""
                rowDict["TOLL AGENCY"] = "HARRIS COUNTY TOLL ROAD AUTHORITY"
                rowDict["PIN NO #"] = ""
                rowDict['ACCOUNT'] = ""
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
              for line in pageText.split("\n"):
                transaction = re.findall(r'(^\d+\D+\d{2}\D+\d{4}\D+\d{2}\D+\d+\w+)\W+(.*)[$|S](\w+\W+\w+)',line) 
                for trans in transaction:
                  transact = list(filter(None,trans))
                  datetime = transact[0]
                  location = transact[1]
                  amount = transact[2]
                  rowDict["TRXN DATE & TIME"] = datetime
                  rowDict["EXIT LANE/LOCATION"] = location
                  rowDict["AMOUNT DUE"] = amount
                  rowDict["TOLL AGENCY"] = "HARRIS COUNTY TOLL ROAD AUTHORITY"
                  rowDict["PIN NO #"] = ""
                  rowDict['ACCOUNT'] = ""
                  output_list.append(rowDict)
                  dff = pd.DataFrame(output_list)
                  output_list = []
                  final_df = pd.concat([final_df, dff])
          
            if cfea or currentPage  == "PLATE" or currentPage  == "PLATE":
              currentPage = "PLATE"   
              reflpstate = re.findall(r'(\w+\d+)\W+(\w+\d+)\W+(\w+)\W+.*\W+(\d+\W+\d+\W+\d+)\W+[$|S]\d+|(S\w+\d+)\W+(\w+).*([A-Z]{1}\w+)\W+\d+\W+\d+\W+\d+\W+(\d+\W+\d+\W+\d+)',pageText)
              for ref in reflpstate:
                rowDict["REFERENCE # "] = ref[0]
                rowDict["LP"] = ref[1]
                rowDict["LP STATE"] = ref[2]
                rowDict["DUE DATE"] = ref[3]
              transactionC = re.findall(r'(\d+.*)\s+\w+\/\w+\/.*[:]\w+\s+.*\s+\d+\.\d+\s\d+\S+',pageText)
              if transactionC:
                for transac in transactionC:
                  rowDict["VIOLATION"] = transac
              else:
                rowDict["VIOLATION"] = ""  
              transaction = re.findall(r'(\w.*\s+\d+)\s+(\d+\/\d+\/.*[:].*M).*[$|S](\d+\W+\d+)|(\w.*\s+\d+)\s+(\d+\d+\W+\d+\W+\d+.*[:]\w.*)[$|S](\w+\W+\w+)',pageText)
              for trans in transaction:
                rowDict["EXIT LANE/LOCATION"] = trans[0]
                rowDict["TRXN DATE & TIME"] = trans[1]
                rowDict["AMOUNT DUE"] = trans[2]
                rowDict["TOLL AGENCY"] = "CENTRAL FLORIDA EXPRESSWAY AUTHORITY"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
              transactionB = re.findall(r'(\d+.*)\s+(\w+\/\w+\/.*[:]\w+)\s+(.*)\s+\d+\.\d+\s(\d+\S+)',pageText)
              for transact in transactionB:
                rowDict["EXIT LANE/LOCATION"] = transact[2]
                rowDict["TRXN DATE & TIME"] = transact[1]
                rowDict["AMOUNT DUE"] = transact[3]
                rowDict["TOLL AGENCY"] = "CENTRAL FLORIDA EXPRESSWAY AUTHORITY"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
        
            if mdta or currentPage  == "NOTD":
              currentPage = "NOTD"
              amountdue = re.findall(r'A\w+D\w+\W+(\w+\W+\d+)|A\w+\W+D\w+\W+(\w+\W+\d+)',pageText)
              for amount in amountdue:
                # amnt = ''.join(amount).replace(",","")
                try:
                  amnt = ''.join(amount).replace(",","")
                  amt = float(amnt)
                  rowDict["AMOUNT DUE"] = amt
                except:
                    pass
              duedate = re.findall(r'By\:(\w+\W+\w+\W+\w+)',pageText)
              for date in duedate:
                due = ''.join(date)
                rowDict["DUE DATE"] = due
              reference = re.findall(r'V\w+T\w+T\w+N\w+\W+(\w+\d+\W+\w+)|V\w+\W+T\w+T\w+N\w+\W+(\w+\d+\W+\w+)|V\w+T\w+\W+T\w+N\w+\W+(\w+\d+\W+\w+)|V\w+T\w+T\w+\W+N\w+\W+(\w+\d+\W+\w+)|V\w+\W+T\w+\W+T\w+N\w+\W+(\w+\d+\W+\w+)|V\w+\W+T\w+T\w+\W+N\w+\W+(\w+\d+\W+\w+)|V\w+T\w+\W+T\w+\W+N\w+\W+(\w+\d+\W+\w+)',pageText)     
              for refer in reference:
                ref = ''.join(refer)
                rowDict["REFERENCE # "] = ref
              lpstate = re.findall(r'Sta\w+\W+Lic.*[ ](\w+)\W+(\w+)',pageText)
              for statelp in lpstate:
                licensestate = statelp[0]
                license = statelp[1]
                rowDict["LP"] = license
                rowDict["LP STATE"] = licensestate
              location = re.findall(r'V\w+T\w+Transaction\s+(.*)|V\w+\W+T\w+Transaction\s+(.*)|V\w+T\w+\W+Transaction\s+(.*)|V\w+\W+T\w+\W+Transaction\s+(.*)',pageText)
              for locate in location:
                loc = ''.join(locate)
                rowDict["EXIT LANE/LOCATION"] = loc
              datetime =re.findall(r'Tim\w+o\w+T\w+\W+(.*[:].*)|T\w+\W+o\w+T\w+\W+(.*[:].*)|Tim\w+\W+o\w+\W+T\w+\W+(.*[:].*)|Tim\w+o\w+\W+T\w+\W+(.*[:].*)',pageText)
              for timedate in datetime:
                date = ''.join(timedate)
                rowDict["TRXN DATE & TIME"] = date  
                rowDict["TOLL AGENCY"] = "MARYLAND TRANSPORTATION AUTHORITY"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff]) 
                final_df.drop_duplicates(inplace = True)
              
            if e470 or currentPage  == "Statement" or currentPage  == "License" or currentPage  == "STATEMENT":
              currentPage = "Statement" or "STATEMENT"
              reference = re.findall(r'(\d{10})\W+\d+\W+\d+\W+\d+',pageText)
              for ref in reference:
                refer = ''.join(ref)
                rowDict["REFERENCE # "] = refer
              duedate =re.findall(r'\d{10}\W+.*[$|S]\S+\W+(\w+\/\d+\W+\w+)|\d{10}.*\W+(\d+\/\d+\W+\d+)\*',pageText)
              for due in duedate:
                date = ''.join(due)
                rowDict["DUE DATE"] = date
                
              transaction = re.findall(r'Li.*Pla\w+\W+(\w+\d+).*([A-Z]{2}).*\n+T.*Tr\w+\W+(\w+.*[\/].*P\w+)\s+\w+\/\w+\/\w+(.*)[ ][$|S](.*)|Li.*Pla\w+\W+(\w+\d+).*([A-Z]{2}).*\n+T.*Tr\w+\W+(\w+.*[M])\W+\S+\W+(.*)[ ][$|S](.*)|Li.*Pla\w+\W+(\w+\d+).*(\w{2}).*\n+T.*Tr\w+\W+(\d+.*[M])\W+\S+\W+(.*)[$|S](.*)|T.*Tr\w+\W+(\d+.*[M])\W+\S+\W+(.*)[$|S](.*)|Li.*Pla\w+\W+(\w+\d+).*([A-Z]{2}).*\n+T.*Tr\w+\W+(\d+.*[M])\W+\S+\W+(.*)[ ][\$|S](.*)|T.*Tr\w+\W+(\d+.*[M])\W+\S+\W+(.*)[ ](.*)',pageText)
              for trans in transaction:
                tran = list(filter(None, trans))
                if len(tran) == 5:
                    licensepl = tran[0]
                    rowDict["LP"] = licensepl
                    rowDict["LP STATE"] = tran[1]
                    rowDict["TRXN DATE & TIME"] = tran[2]
                    rowDict["EXIT LANE/LOCATION"] = tran[3]
                    rowDict["AMOUNT DUE"] = tran[4]
                    rowDict["TOLL AGENCY"] = "E-470 PUBLIC HIGHWAY AUTHORITY"
                    rowDict["PIN NO #"] = ""
                    output_list.append(rowDict)
                    dff = pd.DataFrame(output_list)
                    output_list = []
                    final_df = pd.concat([final_df, dff])
                    final_df.drop_duplicates(inplace = True)
                    # final_df = final_df[final_df['LP'] != ""]
                elif len(tran) ==3:
                    rowDict["TRXN DATE & TIME"] = tran[0]
                    rowDict["EXIT LANE/LOCATION"] = tran[1]
                    rowDict["AMOUNT DUE"] = tran[2]
                    rowDict["TOLL AGENCY"] = "E-470 PUBLIC HIGHWAY AUTHORITY"
                    rowDict["PIN NO #"] = ""
                    rowDict["LP"] = licensepl
                    output_list.append(rowDict)
                    dff = pd.DataFrame(output_list)
                    output_list = []
                    final_df = pd.concat([final_df, dff])
                    final_df.drop_duplicates(inplace = True)
                    final_df = final_df[final_df['LP'] != ""]
          
            if mtatbym or currentPage  == "ATTENTION" or currentPage  == "tollsbymailny":
              currentPage = "ATTENTION" or "tollsbymailny"
              duedate = re.findall(r'M\w+B\w+R\w+b\w+\W+(\w+\W+\w+\W+\w+)|M\w+\W+B\w+\W+R\w+\W+b\w+\W+(\w+\W+\w+\W+\w+)',pageText)
              if duedate:
                date = duedate[0]
                date = ''.join(date)
              #   rowDict["DUE DATE"] = date
              reference = re.findall(r'TO\w+B\w+N\w+\W+(\d+)|T\w+\W+B\w+\W+N\w+\W+(\d+)',pageText)
              if reference:
                ref = reference[0]
                refer = ''.join(ref)
                rowDict["REFERENCE # "] = refer
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
              transaction = re.findall(r'(\w{2})\W+(\w+\d+)\W+\w+\W+(.*\d+)\W+(\d+\/\d+\/\d+.*[:|;]\d+)\W+[$|S](\d+\W+\d+)|([A-Z]{1}\w{1})(\d+).*\W+(\w+)\W+\w+\W+(\d+\/\d+\/\d+.*[:]\d+).*[$|S](\w+\W+\w+)',pageText)
              if transaction:
                trans = transaction[0]
                rowDict["LP STATE"] = trans[0]
                rowDict["LP"] =trans[1]
                rowDict["EXIT LANE/LOCATION"] = trans[2]
                rowDict["TRXN DATE & TIME"] = trans[3]
                rowDict["AMOUNT DUE"] = trans[4]
                rowDict["TOLL AGENCY"] = "MTA (TBM) NY"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
            
            if ntta or currentPage  == "NORTH" or currentPage == "Electronic":
              currentPage = "NORTH" or "Electronic"
              zipcashpin =re.findall(r'Z\w+C\w+P\w+\W+(\d+)|Z\w+C\w+\W+P\w+\W+(\d+)',pageText)
              for pin in zipcashpin:
                zippin = "".join(pin)
                rowDict["PIN NO #"] = zippin
              duedate = re.findall(r'P\w+\W+D\w+\W+D\w+\W+(\d+\W+\w+\/\w{4})|P\w+D\w+D\w+\W+(\d+\W+\w+\/\w{4})',pageText)
              for date in duedate:
                due = ''.join(date)
                rowDict["DUE DATE"] = due
              lpstateaccount = re.findall(r'(\w+)\W+(\w{2})\W+(\d+)\W+\d+\W+\d+\W+\d+\W+to\W+',pageText)
              for lpstacc in lpstateaccount:
                rowDict["LP"] = lpstacc[0]
                rowDict["LP STATE"] = lpstacc[1]
                rowDict["ACCOUNT"] = lpstacc[2]
              transactionb = re.findall(r'\d+\W+\d+\W+\d{4}\W+(\d+\W+\d+\W+\d+.*[:]\d+)\W+(.*)',pageText) 
              for transb in transactionb:
                rowDict["TRXN DATE & TIME"] = transb[0]
                rowDict["EXIT LANE/LOCATION"] = transb[1]
                rowDict["AMOUNT DUE"] = ""
                rowDict["TOLL AGENCY"] = "NTTA" 
                rowDict["REFERENCE # "] = ""
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
              reference = re.findall(r'InvoiceNumber\W+(\d+)|Invoice\W+Number\W+(\d+)',pageText)
              for ref in reference:
                refer = ''.join(ref)
                rowDict["REFERENCE # "] = refer
              transaction = re.findall(r'\d+\W+\d+\W+\d{4}\W+(\d+\W+\d+\W+\d+.*[:]\d+)\W+(.*)[$|S](\w+\W+\w+)',pageText) 
              for trans in transaction:
                rowDict["TRXN DATE & TIME"] = trans[0]
                rowDict["EXIT LANE/LOCATION"] = trans[1]
                rowDict["AMOUNT DUE"] = trans[2]
                rowDict["TOLL AGENCY"] = "NTTA" 
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
            
            if paturnpike or currentPage  == "Turnpike":
              currentPage = "Turnpike" 
              licenseplatestate = re.findall(r'Li\w+\W+P\w+\W+(\w+)\W+(\w+)|Li\w+P\w+\W+(\w+)\W+(\w+)',pageText)
              for lpst in licenseplatestate:
                rowDict["LP"]=lpst[1]
                rowDict["LP STATE"]=lpst[0]
              account = re.findall(r'Ac\w+\W+N\w+\D+(\d+)|Ac\w+N\w+\D+(\d+)',pageText)
              for acc in account:
                accnt =''.join(acc)
                rowDict["ACCOUNT"]=accnt
              invoice = re.findall(r'In\w+\W+N\w+\D+(\d+\D+\d+)|In\w+N\w+\W+(\w+\W+\d+)|In\w+\W+N\w+\W+(\w+\W+\d+)',pageText)
              for invo in invoice:
                inv_ce = ''.join(invo).replace("BW I","BW -").replace("BW l","BW -")
                rowDict["REFERENCE # "]=inv_ce
              duedate = re.findall(r'Pay\w+\W+D\w+\W+D\w+\D+(\d{2}\D+\d{2}\D+\d{4})|D\w+\W+D\w+\W+(\d{2}\W+\d+\W+\d+)|D\w+D\w+\W+(\d{2}\W+\d+\W+\d+)',pageText)
              for due in duedate:
                date = list(filter(None,due))
                datedue =''.join(date)
                rowDict["DUE DATE"]=datedue.replace("0DDDDDDaDD0DDDDDD152","")
                rowDict["TRXN DATE & TIME"]=""
                rowDict["EXIT LANE/LOCATION"]=""
                rowDict["AMOUNT DUE"]=""
                rowDict["TOLL AGENCY"] = "PENNSYLVANIA TURNPIKE COMMISSION"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
              transdatetime= re.findall(r'PLATE\W+(\d+\W+\d+\W+\d+.*[:]\d+)\W+.*|PL\w+\W+(\d+\W+\d+\W+\d+\d+)|PLATE\W+\d+\W+\d+\W+\d+.*[:]\d{2}\s+\w.*[ ](\d{2}\W+\d+\W+\d+.*[:]\w+)\W+.*\s+\w+\s+\W+\w+\W+\w+|PLATE\W+(\d+\W+\d+\W+\d+.*[:]\d+)\W+.*\W+\w+[ ]\W+\w+\W+\w+',pageText)
              trx_date_matched = False
              for trans in transdatetime:
                tran = list(filter(None,trans))
                tranxs =''.join(tran)
                if not rowDict["TRXN DATE & TIME"]:
                  rowDict["TRXN DATE & TIME"] = tranxs
                  trx_date_matched = True
              location = re.findall(r'PLATE\W+\d+\W+\d+\W+\d+.*[:]\d+\W+(.*)\W+\w+\W+[$|S]|PL\w+\W+\d+\W+\d+\W+\d+\d+(.*)[S|$]|PLATE\W+\d+\W+\d+\W+\d+.*[:]\d{2}\s+\w.*[ ]\d{2}\W+\d+\W+\d+.*[:]\w+\W+(.*)\s+\w+\s+\W+\w+\W+\w+|PLATE\W+\d+\W+\d+\W+\d+.*[:]\d+\W+(.*)\W+\w+[ ]\W+\w+\W+\w+',pageText)
              exit_location_matched = False
              for loc in location:
                locat = list(filter(None,loc))
                locate =''.join(locat)
                if not rowDict["EXIT LANE/LOCATION"]:
                  rowDict["EXIT LANE/LOCATION"] = locate
                  exit_location_matched = True
              amountdue=re.findall(r'PLATE\W+\d+\W+\d+\W+\d+.*[:]\d+\W+.*\W+\w+\W+[$|S](.*)|PL\w+\W+\d+\W+\d+\W+\d+\d+.*[S|$](.*)|PLATE\W+\d+\W+\d+\W+\d+.*[:]\d{2}\s+\w.*[ ]\d{2}\W+\d+\W+\d+.*[:]\w+\W+.*\s+\w+\s+\W+(\w+\W+\w+)|PLATE\W+\d+\W+\d+\W+\d+.*[:]\d+\W+.*\W+\w+[ ]\W+(\w+\W+\w+)',pageText)
              for amt in amountdue:
                amount =''.join(amt).replace(",",".").replace(" ","").replace("I","").replace("i","")
                rowDict["AMOUNT DUE"]=amount
                rowDict["TOLL AGENCY"] = "PENNSYLVANIA TURNPIKE COMMISSION"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict)
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
                final_df = final_df[final_df['AMOUNT DUE'] != ""]
                    # final_df.drop_duplicates(subset=['TRXN DATE & TIME', 'AMOUNT DUE',], keep='first', inplace=True)
                    # final_df.drop_duplicates(subset='TRXN DATE & TIME', keep='first', inplace=True)
            
            if paybyplatema or currentPage  == "EZDriveMA" or currentPage  == "Massachusetts":
              currentPage = "EZDriveMA"
              currentPage = "Massachusetts"
              reference = re.findall(r'I\w+N\w+\W+(\d{8})|I\w+\W+N\w+\W+(\d{8})',pageText)
              for ref in reference:
                refer = ''.join(ref)
                rowDict["REFERENCE # "] = refer
              duedate = re.findall(r'(\d+\/\d+\W+\d+)\s+[$|S]\d+\W+\d+',pageText)
              for due in duedate:
                date = ''.join(due)
                rowDict["DUE DATE"] = date
              license = re.findall(r'Li.*Pl\w+\W+(\w+\d+)',pageText)
              for lic in license:
                li_nse = ''.join(lic)
                rowDict["LP"] = li_nse
              licenseplate = re.findall(r'Li.*Pl.*S\w+\W+(\w+)',pageText)
              for licpl in licenseplate:
                li_nsepl = ''.join(licpl)
                rowDict["LP STATE"] = li_nsepl
              amount_due = re.findall(r'\$\d+\W+\d+\W+\d+\W+\d+\W+\d+\W+\d+\W+\S+\W+(\S+)\W+\d+\W+\d+\W+\d{4}',pageText)
              for due in amount_due:
                amnt = ''.join(due)
                rowDict["AMOUNT DUE"] = amnt 
                rowDict["TRXN DATE & TIME"] = ""
                rowDict["EXIT LANE/LOCATION"] = ""
                rowDict["TOLL AGENCY"] = "PAY BY PLATE MA"
                rowDict["PIN NO #"] = ""
                rowDict["ACCOUNT"] = ""
                rowDict["VIOLATION"] = ""
                output_list.append(rowDict) 
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
              transaction = re.findall(r'\d+.*MA\W+(\w+)\W+(\w+).*(\d+\d+\/\d+\/\d+.*[:]\d+)(.*)\W+\w+\W+[$|S](\w+\W+\d+)|\d+\W+\d+\W+\d+\W+T.*[ ]([A-Z]{1}\w+)\W+(\w+\d+).*(\d+\d+\/\d+\/\d+.*[:]\d+)(.*)\W+\w+\W+[$|S](\w+\W+\d+)|\d+\W+\d+\W+\d+\W+T.*[ ]([A-Z]{2})\W+(\w+).*(\d+\d+\/\d+\/\d+.*[:]\d+)\W+(.*)\W+\w+\W+[$|S](\w+\W+\d+)',pageText)  
              for trans in transaction:
                rowDict["LP STATE"] = trans[0]
                rowDict["LP"] = trans[1]
                rowDict["TRXN DATE & TIME"] = trans[2]
                rowDict["EXIT LANE/LOCATION"] = trans[3]
                rowDict["AMOUNT DUE"] = trans[4]
                rowDict["TOLL AGENCY"] = "PAY BY PLATE MA"
                rowDict["PIN NO #"] = ""
                rowDict["ACCOUNT"] = ""
                rowDict["VIOLATION"] = ""
                output_list.append(rowDict) 
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df = final_df[final_df['TRXN DATE & TIME'] != ""]  
                final_df.drop_duplicates(inplace = True)
            
            if pocahontas or currentPage  == "Pocahontas":
              currentPage = "Pocahontas"
              lpstate = re.findall(r'Li\w+.*P\w+\W+(\w+)\W+(\w+\d+)',pageText)
              for lp in lpstate:
                rowDict["LP"] = lp[1]
                rowDict["LP STATE"] = lp[0]
              duedate = re.findall(r'D\w+.*D\w+\W+(\d+\W+\d+\W+\d+)',pageText)
              for date in duedate:
                rowDict['DUE DATE'] = date
              transactions = re.findall(r'(\d+)\W+(.*)\s+(\d+\W+\d+\W+\d+.*[M]).*[$|S](\w+\W+\w+)', pageText)
              for trans in transactions:
                violation = trans[0]
                location = trans[1]
                datetime = trans[2]
                amount = trans[3]
                rowDict['VIOLATION'] = violation
                rowDict['EXIT LANE/LOCATION'] = location
                rowDict['TRXN DATE & TIME'] = datetime
                rowDict['AMOUNT DUE'] = amount
                rowDict["TOLL AGENCY"] = "GLOBALVIA POCAHONTAS PARKWAY"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict) 
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
            
            if southbay or currentPage  == "South":
              currentPage = "South"
              duedate = re.findall(r'Am.*D.*b\w+(.*)[S|$]|A\w+D\w+b\w{1}(\w+\W+\w+\W+\w+)|A\w+\W+D\w+b\w{1}(\w+\W+\w+\W+\w+)|A\w+D\w+\W+b\w{1}(\w+\W+\w+\W+\w+)|A\w+\W+D\w+\W+b\w{1}(\w+\W+\w+\W+\w+)',pageText)
              for due in duedate:
                date = ''.join(due)
                rowDict['DUE DATE'] = date
              reference =re.findall(r'Notif\w+Nu\w+\W+(\w+)|Notif\w+\W+Nu\w+\W+(\w+)',pageText)
              for ref in reference:
                refer = ''.join(ref)
                rowDict['REFERENCE # '] = refer
              lpstate = re.findall(r'Li\w+P\w+\W+(\w+)\W+\w+\W+(\w+)|Li\w+\W+P\w+\W+(\w+)\W+\w+\W+(\w+)',pageText)  
              for state in lpstate:
                date = ''.join(state)
                rowDict['LP'] = state[0]
                rowDict['LP STATE'] = state[1]
              transaction_vio = re.findall(r'(\d+)\W+\d+.*[:]\w+\W+.*[$|S]\d+\W+\d+\s+\W+\d+\W+\d+.*[$]\w+\W+\w+|(\d{9})\W+\d+.*[$|S]',pageText)
              for transvio in transaction_vio:
                tranvio = ''.join(transvio)
                rowDict['VIOLATION'] = tranvio
              transaction_date = re.findall(r'\d+\W+(\d+.*[:]\w+)\W+.*[$|S]\d+\W+\d+\s+\W+\d+\W+\d+.*[$]\w+\W+\w+|\d+\W+(\d+.*[-]\d+\W+\d\S+).*[$|S]',pageText)
              for transdate in transaction_date:
                trandate = ''.join(transdate)
                rowDict['TRXN DATE & TIME'] = trandate
              transaction_lane = re.findall(r'\d+\W+\d+.*[:]\w+\W+(.*)[$|S]\d+\W+\d+\s+\W+\d+\W+\d+.*[$]\w+\W+\w+|\d+\W+\d+.*[-]\d+\W+\d\S+(.*)[$|S].*[$|S].*[$|S]',pageText)
              for translane in transaction_lane:
                tranlane = ''.join(translane)
                rowDict['EXIT LANE/LOCATION'] = tranlane
              transaction_amnt = re.findall(r'\d+\W+\d+.*[:]\w+\W+.*[$|S]\d+\W+\d+\s+\W+\d+\W+\d+.*[$](\w+\W+\w+)|\d+\W+\d+.*[-]\d+\W+\d\S+.*[$|S].*[$|S].*[$|S](.*)',pageText)
              for transamnt in transaction_amnt:
                tranamnt = ''.join(transamnt)
                rowDict['AMOUNT DUE'] = tranamnt
                rowDict["TOLL AGENCY"] = "SOUTH BAY EXPRESSWAY"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict) 
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
            
            if srta or currentPage  == "SRTA":
              currentPage = "SRTA" 
              duedate =re.findall(r'Due.*[:](\d+\W+\d+\W+\d+)',pageText)
              for due in duedate:
                date = ''.join(due)
                rowDict["DUE DATE"] = date
              reference =re.findall(r'No\w+\W+(\d+)',pageText)
              for refer in reference:
                ref = ''.join(refer)
                rowDict["REFERENCE # "] = ref
              transaction = re.findall(r'(\d+\w+)\W+([A-Z]\w+)\W+(\w+)\W+(\d+\W+\d+\W+\d+).*N\W+(.*)[$|S](\d+\W+\d+)',pageText)
              for trans in transaction:
                rowDict["LP"] = trans[0]
                rowDict["LP STATE"] = trans[1]
                rowDict["VIOLATION"] = trans[2]
                rowDict["TRXN DATE & TIME"] = trans[3]
                rowDict["EXIT LANE/LOCATION"] = trans[4]
                rowDict["AMOUNT DUE"] = trans[5].replace(",",".")
                rowDict["TOLL AGENCY"] = "STATE ROAD AND TOLLWAY AUTHORITY"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict) 
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
            
            if wsdot or currentPage  == "STATEMENT":
              currentPage = "STATEMENT"
              reference = re.findall(r'S\w+Nu\w+\W+(\d+)|S\w+\W+Nu\w+\W+(\d+)', pageText)
              for ref in reference:
                refer = ''.join(ref)
                rowDict["REFERENCE # "] = refer
              due_date = re.findall(r'Amount.*\n+.*Du\w+D\w+\W+(\w+\W+\d+\W+\w+)|Amount.*\n+.*Du\w+\W+D\w+\W+(\w+\W+\d+\W+\w+)',pageText)
              for due in due_date:
                date = ''.join(due)
                rowDict["DUE DATE"] = date
              transactions = re.findall(r'\d+\/\d+\/\d+\W+(\d+)\W+\D+(\d+\/\d+\/\d+\W+.*[M])\W+(\w+)([A-Z]{2})\W+(.*)\W+[$](\w+\W+\w+)\n+(.*)', pageText)
              for trans in transactions:
                rowDict["VIOLATION"] = trans[0]
                rowDict["TRXN DATE & TIME"] = trans[1]
                rowDict["LP"] = trans[2]
                rowDict["LP STATE"] = trans[3]
                rowDict["EXIT LANE/LOCATION"] = trans[4]+' '+trans[6]
                rowDict["AMOUNT DUE"] = trans[5]
                rowDict["TOLL AGENCY"] = "WSDOT"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict) 
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)
              transactionsB = re.findall(r'(\w+)\n+(\d+\/\d+\/\d+)\W+(\d+)\W+\D+(\d+\/\d+\/\d+\W+.*[M])\W+(\w+)([A-Z]{1}\w+)\W+[$](\w+\W+\w+)\n+(.*)', pageText)  
              for transact in transactionsB:
                rowDict["VIOLATION"] = transact[2]
                rowDict["TRXN DATE & TIME"] = transact[3]
                rowDict["LP"] = transact[4]
                rowDict["LP STATE"] = transact[5]
                rowDict["EXIT LANE/LOCATION"] = transact[0]+' '+transact[7]
                rowDict["AMOUNT DUE"] = transact[6]  
                rowDict["TOLL AGENCY"] = "WSDOT"
                rowDict["PIN NO #"] = ""
                output_list.append(rowDict) 
                dff = pd.DataFrame(output_list)
                output_list = []
                final_df = pd.concat([final_df, dff])
                final_df.drop_duplicates(inplace = True)

                                  # if not output_list:
                                  #       final_df = pd.DataFrame(columns=rowDict) 
                                    #         if final_df.empty:
                                    # final_df = pd.DataFrame(columns=column_names)
      # final_df= final_df.drop(final_df[(final_df['TOLL AGENCY'] == 'NEW JERSEY TURNPIKE AUTHORITY') & (final_df['LP'] == '')].index)
      final_df = final_df[final_df['TOLL AGENCY'] != ""]  
      final_df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)        

             
           
              
              
             


              
              
              
              
              
              
              
      