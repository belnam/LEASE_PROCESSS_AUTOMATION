import win32com.client
import os
import pickle
from datetime import datetime
import getpass
import openpyxl


username = getpass.getuser()
pickle_folder = "PickleFiles"
pdfpath = f"C:\\Users\\{username}\\Documents\\RENTALS-PROCESS-AUTOMATION\\Downloaded_Scans\\"

# Define the start and end dates for the date range
start_date = datetime(2024, 3, 19)
end_date = datetime(2024, 3, 20)  

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")

# Get the specific account
accounts = namespace.Accounts
desired_account = None
for account in accounts:
    if account.SmtpAddress.lower() == "rentaltolls@innovativetoll.com":
        desired_account = account
        break

if desired_account is not None:
    root_folder = namespace.Folders.Item(desired_account.DeliveryStore.DisplayName)

   
    # for folder_name in ["XTRA", "Inbox", "1ST ADVANTAGE", "Bowman Rentals", "KROSS TRUCKING", "Milestone", "Premier", "Stoughton Rental"]:
    for folder_name in ["Bowman Rentals"]:
        folder = None
        for f in root_folder.Folders:
            if f.Name == folder_name:
                folder = f
                break
        if folder is not None:
            # Restrict emails based on date range
            emails = folder.Items.Restrict("[ReceivedTime] >= '{}' AND [ReceivedTime] <= '{}'".format(start_date.strftime("%m/%d/%Y"), end_date.strftime("%m/%d/%Y")))
            emails.Sort("[ReceivedTime]", False)
      
            for email in emails:
                received_timestamp = email.ReceivedTime
                attachments = email.Attachments
                count = attachments.Count
                for j in range(1, count + 1):
                    attachment = attachments.Item(j)
                    file_extension = os.path.splitext(attachment.FileName)[1].lower()
                    if file_extension == ".pdf":
                        save_path = os.path.join(pdfpath, attachment.FileName)
                        attachment.SaveAsFile(save_path)
                        received_timestamp_str = received_timestamp.strftime("%Y-%m-%d %H:%M:%S")
                        log_data = [attachment.FileName, received_timestamp_str]
                        log_file_path = "Rental_ProcessedFilenames/email_logs.xlsx"
                        wb = openpyxl.load_workbook(log_file_path) if os.path.exists(log_file_path) else openpyxl.Workbook()
                        ws = wb.active
                        ws.append(log_data)
                        wb.save(log_file_path)
                        wb.close()
        else:
            print(f"The '{folder_name}' folder does not exist in the account.")
else:
    print("Desired account not found.")
