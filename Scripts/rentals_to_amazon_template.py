from multiprocessing.reduction import duplicate
import pandas as pd
import time
import os
import re
import getpass
from datetime import timedelta, datetime
from py_console import console

username = getpass.getuser()

curr_month = time.strftime("%B", time.localtime()).upper()
of_day = datetime.now() + timedelta(days=-1)
curr_week = str(of_day.isocalendar()[1])
curr_year = str(of_day.isocalendar()[0])


# rawfiles_dir = f'./WEEK_{curr_week}/output_file/'


rawfiles_dir = f'C:/Users/{username}/Documents/RENTALS-PROCESS-AUTOMATION/Process_Report/WEEK_{curr_week}/output_file/'
console.info("Raw File Directory -------->", rawfiles_dir)


output_df_template = pd.DataFrame(columns=['LICENSE PLATE', 'TRANSPONDER', 'STATE', 'EXIT DATE/TIME', 'AGENCY', 'EXIT LANE', 'CLASS', 'AMOUNT','ACCOUNT', "SCAN_NO.", "WEEK"])

# Convert RENTALS into Amazon template

def process_rentals(filename):
    src = filename.split("/")[-1].split(".")[0]
    console.info(src)
    output_list = []

    curr_df = pd.read_excel(filename)

    # filter relevant rows
    curr_df = curr_df[~curr_df['EXIT LANE'].isnull()]
    curr_df = curr_df[~curr_df['TRXN. DATE & TIME'].isnull()]

    # filter relevant columns
    curr_df = curr_df[['TOLL AGENCY', 'LP', 'LP STATE', 'TRXN. DATE & TIME', 'EXIT LANE', 'AMOUNT DUE', 'SOURCE', "SCAN_NO.", "WEEK"]]

    for i_i, i_row in curr_df.iterrows():
        row_dict = {'LICENSE PLATE': "", 'TRANSPONDER': "", 'STATE': "", 'EXIT DATE/TIME': "", 'EXIT LANE': "", 'AMOUNT': "", 'ACCOUNT': "", "SCAN_NO.": "", "WEEK": ""}

        row_dict['LICENSE PLATE'] = str(i_row['LP'])

        row_dict['STATE'] = str(i_row['LP STATE'])
        row_dict['AGENCY'] = str(i_row['TOLL AGENCY'])
        row_dict['EXIT DATE/TIME'] = i_row['TRXN. DATE & TIME']
        row_dict['EXIT LANE'] = str(i_row['EXIT LANE'])
        row_dict['AMOUNT'] = str(i_row['AMOUNT DUE'])
        row_dict['ACCOUNT'] = str(i_row['SOURCE'])

        # row_dict['VIOLATION #'] = str(i_row['VIOLATION #']).startswith('T')

        # if str(i_row['VIOLATION #']).startswith('T'):
        #     row_dict['VIOLATION #'] = str(i_row['VIOLATION #'])
        # else:
        #     row_dict['VIOLATION #'] = ''

        row_dict['SCAN_NO.'] = int(str(i_row['SCAN_NO.']))
        row_dict['WEEK'] = int(str(i_row['WEEK']))

        output_list.append(row_dict)

    df = pd.DataFrame(output_list)
    df[["TRANSPONDER", "CLASS"]] = ['-', "-"]
    try:
        df = df.astype({"AMOUNT": 'float64'})
    except:
        pass

    return df

def rentals_to_amazon(rawfiles_dir):
    start = time.time()

    final_df = output_df_template
    unprocessed = []

    for i in os.listdir(rawfiles_dir):
        if i.lower().endswith(".xlsx"):
            # if i .startswith("week_19 RENTALS_all"):
            if i .startswith("week_"):
                final_df = final_df._append(process_rentals(rawfiles_dir+i))
                print("!! processed :" + i)
            else:
                unprocessed.append(i)
        else:
            unprocessed.append(i)


    # Sort by Date
    # final_df['EXIT DATE/TIME'] = pd.to_datetime(final_df['EXIT DATE/TIME'])
    # final_df.sort_values(by='EXIT DATE/TIME', inplace=True)


    # RENTALS Transactions Dataframe to Amazon Template --- All with duplicates

    print("RENTALS Transactions Dataframe to Amazon Template---------------------------------------->")

    amazon_df = final_df

    amazon_df = amazon_df.drop(columns=["SCAN_NO.", "WEEK"])

    # datatoexcel = pd.ExcelWriter(
    #     f'./WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS.xlsx', datetime_format="mm/dd/yyyy hh:mm:ss")

    # output_file = './WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS.xlsx'
    # console.success("Output File Location -------->", output_file)
    # amazon_df.to_excel(datatoexcel, index=False)
    # datatoexcel.save()

    # amazon_df_count_row = amazon_df.shape[0]

    datatoexcel = pd.ExcelWriter(
        f'C:/Users/{username}/Documents/RENTALS-PROCESS-AUTOMATION/Process_Report/WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS.xlsx', datetime_format="mm/dd/yyyy hh:mm:ss")

    output_file = 'C:/Users/{username}/Documents/RENTALS-PROCESS-AUTOMATION/Process_Report/WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS.xlsx'
    console.success("Output File Location -------->", output_file)
    amazon_df.to_excel(datatoexcel, index=False)
    datatoexcel._save()

    amazon_df_count_row = amazon_df.shape[0]


    # RENTALS Transactions Dataframe wth Scan No & Week No Columns

    print("RENTALS Transactions Dataframe wth Scan No & Week No Columns----------------------------->")

    scanNo_weekNo_df = final_df

    # datatoexcel = pd.ExcelWriter(
    #     f'./WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS_Scan No & Week No.xlsx', datetime_format="mm/dd/yyyy hh:mm:ss")

    # output_file = './WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS_Scan No & Week No.xlsx'
    # console.success("Output File Location -------->", output_file)
    # scanNo_weekNo_df.to_excel(datatoexcel, index=False)
    # datatoexcel.save()

    # scanNo_weekNo_df_count_row = scanNo_weekNo_df.shape[0]

    datatoexcel = pd.ExcelWriter(
        f'C:/Users/{username}/Documents/RENTALS-PROCESS-AUTOMATION/Process_Report/WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS_Scan No & Week No.xlsx', datetime_format="mm/dd/yyyy hh:mm:ss")

    output_file = 'C:/Users/{username}/Documents/RENTALS-PROCESS-AUTOMATION/Process_Report/WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS_Scan No & Week No.xlsx'
    console.success("Output File Location -------->", output_file)
    scanNo_weekNo_df.to_excel(datatoexcel, index=False)
    datatoexcel._save()

    scanNo_weekNo_df_count_row = scanNo_weekNo_df.shape[0]



    # RENTALS Transactions Dataframe with no Duplicates - To be included in AWR

    print("RENTALS Transactions Dataframe with no Duplicates - To be included in AWR----------------->")

    no_dups_df = amazon_df

    # dropping duplicate values keep first
    no_dups_df.drop_duplicates(subset =['LICENSE PLATE', 'EXIT DATE/TIME', 'EXIT LANE', 'AGENCY', 'AMOUNT'], keep = "first", inplace = True)

    # datatoexcel = pd.ExcelWriter(
    #     f'./WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS_AMAZON.xlsx', datetime_format="mm/dd/yyyy hh:mm:ss")

    # output_file = './WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS_AMAZON.xlsx'
    # console.success("Output File Location -------->", output_file)
    # no_dups_df.to_excel(datatoexcel, index=False)
    # datatoexcel.save()

    # no_dups_df_count_row = no_dups_df.shape[0]

    datatoexcel = pd.ExcelWriter(
        f'C:/Users/{username}/Documents/RENTALS-PROCESS-AUTOMATION/Process_Report/WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS_AMAZON.xlsx', datetime_format="mm/dd/yyyy hh:mm:ss")

    output_file = 'C:/Users/{username}/Documents/RENTALS-PROCESS-AUTOMATION/Process_Report/WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS_AMAZON.xlsx'
    console.success("Output File Location -------->", output_file)
    no_dups_df.to_excel(datatoexcel, index=False)
    datatoexcel._save()

    no_dups_df_count_row = no_dups_df.shape[0]



    # Duplicated RENTALS Transactions Dataframe

    print("Duplicated RENTALS Transactions Dataframe------------------------------------------------->")

    dups_df = scanNo_weekNo_df[scanNo_weekNo_df.duplicated(['LICENSE PLATE', 'EXIT DATE/TIME', 'EXIT LANE', 'AGENCY', 'AMOUNT'])]

    # datatoexcel = pd.ExcelWriter(
    #     f'./WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS duplicates.xlsx', datetime_format="mm/dd/yyyy hh:mm:ss")

    # output_file = './WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS.xlsx'
    # console.success("Output File Location -------->", output_file)
    # dups_df.to_excel(datatoexcel, index=False)
    # datatoexcel.save()

    # dups_df_count_row = dups_df.shape[0]

    datatoexcel = pd.ExcelWriter(
        f'C:/Users/{username}/Documents/RENTALS-PROCESS-AUTOMATION/Process_Report/WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS duplicates.xlsx', datetime_format="mm/dd/yyyy hh:mm:ss")

    output_file = 'C:/Users/{username}/Documents/RENTALS-PROCESS-AUTOMATION/Process_Report/WEEK_{curr_week}/to_amazon_template/WEEK_{curr_week} ({curr_year}) RENTALS.xlsx'
    console.success("Output File Location -------->", output_file)
    dups_df.to_excel(datatoexcel, index=False)
    datatoexcel._save()

    dups_df_count_row = dups_df.shape[0]


    # print(unprocessed)
    console.error("Unprocessed Files -------->", unprocessed)

    console.info("All RENTALS ----------------------------->", amazon_df_count_row)
    console.info("All RENTALS with Scan No & Week No ------>", scanNo_weekNo_df_count_row)
    console.info("Cleaned RENTALS No Duplicates ----------->", no_dups_df_count_row)
    console.info("Duplicated RENTALS ---------------------->", dups_df_count_row)


    stop = time.time()

    # print(f'Done processing in {stop-start}')
    console.warn(f'Done processing in {stop-start}')

rentals_to_amazon(rawfiles_dir)

# if __name__ == '__main__':
#     main(rawfiles_dir)
