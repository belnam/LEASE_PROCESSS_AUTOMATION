import logging
import schedule
import time
import os
import shutil
from datetime import datetime
import getpass
import gql
import urllib3
from gql.transport.aiohttp import AIOHTTPTransport
import json

class QueryFilter(logging.Filter):
    def filter(self, record):
        message = record.getMessage()
        return all(exclude_str not in message for exclude_str in [
            '{"query": "query IntrospectionQuery',
            '{"data":{"__schema":{"queryType',
            '{"query": "mutation LoginEmployee',
            '{"data":{"loginEmployee":{"authData',
             '{"data":{"createDropBoxLogs"'
        ])

# Create a logger
logger = logging.getLogger('')
logger.setLevel(logging.INFO)

# Configure logging
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Function to generate log file name with current date
def get_log_file_name():
    current_date = datetime.now().strftime("%m-%d-%Y")
    return os.path.join("Logs", f"log_file_{current_date}.txt")

os.makedirs("Logs", exist_ok=True)

# File handler to write logs to a file with current date
file_handler = logging.FileHandler(get_log_file_name())
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
file_handler.addFilter(QueryFilter())  # Apply the filter to exclude specific messages
logger.addHandler(file_handler)

# Logging to console remains the same
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
console.addFilter(QueryFilter())  # Apply the filter to exclude specific messages
logger.addHandler(console)


logging.info("================= BEGIN PROCESS =================")


# service_url = "https://violations.innovativetollsolution.com/api"
service_url = "https://violations.innovativetoll.com/api"


def upload_files(file_params, folder_name):

    url = f"{service_url}/api"
    transport = AIOHTTPTransport(url=url)

    # Request Authentication Token
    GQL_client = gql.Client(transport=transport, fetch_schema_from_transport=True)
    body = gql.gql('''
        mutation LoginEmployee($username: String!, $password: String!) {
            loginEmployee(username: $username, password: $password) {
                authData {
                token
                }
            }
        }
    ''')
    params = {
        "username": "brian@innovativetoll.com",
        "password": "brianogwel"
    }
    result = GQL_client.execute(body, variable_values=params)

    token = result['loginEmployee']['authData']['token']

    # Upload Files
    http = urllib3.PoolManager()

    # url = "https://violations.innovativetollsolution.com/upload/sftp"
    url = "https://violations.innovativetoll.com/upload/sftp"


    with open("./application.json") as application_file:
        json_string = json.load(application_file)
        machine_name = json_string["machine_name"]

    final_status = ""
    for file_param in file_params:
        try:
            file_path = file_param

            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                    file_name = os.path.basename(file_path)

                    file_name_split = file_name.split(".")
                    file_name = '.'.join(file_name_split[:-1]) + "_" + machine_name + "." + file_name_split[-1]

                    fields = [('localFilePath', (file_name, file_data, 'application/vnd.ms-excel'))]
                    fields.append(('folder_name', folder_name))

                    response = http.request(method='PUT', url=url, fields=fields, headers={'Authorization': token})

                    if response.status == 200:
                        r = file_name, "Uploaded Successfully to", folder_name, "Drop Box Folder"
                        success = " ".join(str(x) for x in r)
                        final_status = success
                    else:
                        s = "Error While Uploading", file_name
                        error = " ".join(str(x) for x in s)
                        final_status = error

                    logging.info(final_status)
                    # print(response.data)

        except Exception as e:
            logging.error(f"Error: {str(e)}")

    return token  # return the token after obtaining it




def copy_new_pdf_files(source_folder, archive_folder, processed_files, folder_names, token):
    files_to_upload = {}
    current_date = datetime.now().strftime("%m-%d-%Y")
    current_month = datetime.now().strftime("%B")
    current_year = datetime.now().strftime("%Y")

    for client_folder in os.listdir(source_folder):
        if os.path.isdir(os.path.join(source_folder, client_folder)):
            files_to_upload[client_folder] = []
            for root, _, files in os.walk(os.path.join(source_folder, client_folder)):
                for file_name in files:
                    if file_name.endswith('.pdf'):
                        source_file_path = os.path.join(root, file_name)

                        if current_date in source_file_path:
                            # Check if the file has already been processed
                            if source_file_path not in processed_files:
                                files_to_upload[client_folder].append(source_file_path)

                                # Check if the file already exists in the archive folder for the same date
                                relative_path = os.path.relpath(source_file_path, source_folder)
                                archive_date_folder = os.path.join(archive_folder, client_folder, current_year, current_month, current_date)
                                archive_file_path = os.path.join(archive_date_folder, file_name)

                                if not os.path.exists(archive_file_path):
                                    # Try to upload file, but don't move if error occurs
                                    try:
                                        upload_files([source_file_path], client_folder)  # Pass token to upload_files
                                    except Exception as e:
                                        logging.error(f"Error occurred while uploading {file_name}: {str(e)}")
                                        # Remove the file from files_to_upload to prevent moving it to archive
                                        files_to_upload[client_folder].remove(source_file_path)

    # Copy uploaded files to archive folders
    files_moved_per_folder = {}
    for client_folder, files in files_to_upload.items():
        for source_file_path in files:

            relative_path = os.path.relpath(source_file_path, source_folder)
            archive_date_folder = os.path.join(archive_folder, client_folder, current_year, current_month, current_date)
            archive_file_path = os.path.join(archive_date_folder, os.path.basename(source_file_path))

            # The rest of the code remains the same
            if not os.path.exists(archive_file_path):
                os.makedirs(archive_date_folder, exist_ok=True)
                shutil.copy(source_file_path, archive_file_path)
                processed_files.append(source_file_path)  # Append to the list of processed files
                # Update files_moved_per_folder dictionary
                folder = os.path.dirname(relative_path)
                files_moved_per_folder[folder] = files_moved_per_folder.get(folder, 0) + 1

                logging.info(f"{os.path.basename(source_file_path)} Copied Successfully to {client_folder} SCANS - ARCHIVES")
            else:
                logging.info(f"{os.path.basename(source_file_path)} already exists in {client_folder}.")

    return processed_files, files_moved_per_folder


def read_processed_files():
    return []

def write_processed_files(processed_files, source_folder, files_moved_per_folder):
    processed_files_per_folder = {}
    for file_path in processed_files:
        relative_path = os.path.relpath(file_path, source_folder)
        folder = os.path.dirname(relative_path)
        processed_files_per_folder[folder] = processed_files_per_folder.get(folder, []) + [os.path.basename(file_path)]

def get_archive_folder_counts(archive_folder):
    folder_counts = {}

    for root, folders, files in os.walk(archive_folder):
        folder_name = os.path.relpath(root, archive_folder)
        file_count = len(files)
        folder_counts[folder_name] = file_count

    return folder_counts

def run_scans(token):  # Accept the token as an argument
    current_date = datetime.now().strftime("%m-%d-%Y")
    current_month = datetime.now().strftime("%B")
    current_year = datetime.now().strftime("%Y")
    username = getpass.getuser()

    # source_folder = f"C:/Users/{username}/Desktop/SCANS"
    # archive_folder = f"C:/Users/{username}/Desktop/SCANS - ARCHIVES"

    source_folder = f"C:/Users/{username}/OneDrive - Innovative Toll Solution/Desktop/SCANS"
    archive_folder = f"C:/Users/{username}/OneDrive - Innovative Toll Solution/Desktop/SCANS - ARCHIVES"

    folder_counts = get_archive_folder_counts(archive_folder)

    files_count_folder = f"C:/Users/{username}/Desktop/Files Count"
    files_count_folder = "./Files Count"
    per_upload_count_path = f"{files_count_folder}/per_upload_count.txt"

    os.makedirs(archive_folder, exist_ok=True)
    os.makedirs(files_count_folder, exist_ok=True)

    folder_names = [folder_name for folder_name in os.listdir(source_folder) 
                    if os.path.isdir(os.path.join(source_folder, folder_name))]

    for folder_name in folder_names:
        folder_path = os.path.join(source_folder, folder_name, current_year, current_month, current_date)
        archive_folder_path = os.path.join(archive_folder, folder_name, current_year, current_month, current_date)
        os.makedirs(folder_path, exist_ok=True)
        os.makedirs(archive_folder_path, exist_ok=True)

    processed_files = read_processed_files()
    processed_files, files_moved_per_folder = copy_new_pdf_files(source_folder, archive_folder, processed_files, folder_names, token)  # Pass token to copy_new_pdf_files

    # archive_counts = get_archive_folder_counts(archive_folder_path)

    # for folder, count in archive_counts.items():
    #     files_in_archives_count = (count)
    #     files_in_archives = f"Files in {folder_name} SCANS - ARCHIVES Folder ----> " + str(count)
    #     logging.info(files_in_archives)

    files_in_archives_count = 0
    
    # Check if archive_folder_path is defined
    if 'archive_folder_path' in locals():
        archive_counts = get_archive_folder_counts(archive_folder_path)

        for folder, count in archive_counts.items():
            files_in_archives_count = count
            files_in_archives = f"Files in {folder_name} SCANS - ARCHIVES Folder ----> " + str(count)
            logging.info(files_in_archives)

    write_processed_files(processed_files, source_folder, files_moved_per_folder)

    existing_counts = {}
    daily_count_folder = os.path.join(files_count_folder, current_year, current_month)
    file_path = os.path.join(daily_count_folder, f"{current_date}.txt")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(": ")
                if len(parts) == 2:
                    folder, count = parts
                    existing_counts[folder] = int(count)

    cumulative_count = 0
    for folder, count in files_moved_per_folder.items():
        existing_counts[folder] = existing_counts.get(folder, 0) + count
        with open(per_upload_count_path, 'w') as f:
            scans_uploaded = f"Scans Uploaded in {folder_name} Folder ----> " + str(count)
            logging.info(scans_uploaded)
            f.write(f"{folder}: {count}")

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        for folder, count in existing_counts.items():
            f.write(f"{folder}: {count}\n")
            # cumulative_count = (count)
            cumulative_count += count
            cumulative_files_count = f"Total Scans Uploaded in {folder_name} Folder ----> " + str(count)
            logging.info(cumulative_files_count)

        
    with open("./application.json") as application_file:
        json_string = json.load(application_file)
        machine_name = json_string["machine_name"]

    # Send File Counts
    url = f"{service_url}/api"
    transport = AIOHTTPTransport(url=url, headers={"Authorization": f"Bearer {token}"})

    GQL_client = gql.Client(transport=transport, fetch_schema_from_transport=True)

    body = gql.gql('''
        mutation Mutation($countOfScans: Int!, $countOfScansArchived: Int!, $currentDate: String!, $username: String!) {
            createDropBoxLogs(countOfScans: $countOfScans, countOfScansArchived: $countOfScansArchived, currentDate: $currentDate, username: $username) {
                id
            }
        }
    ''')

    params = {
        "countOfScans": int(cumulative_count),
        "countOfScansArchived": int(files_in_archives_count),
        "currentDate": str(current_date).strip(),
        "username": str(machine_name)
    }

    result = GQL_client.execute(body, variable_values=params)
            

    logging.info("=============== PROCESS COMPLETED ===============")

if __name__ == "__main__":
    token = upload_files([], "")
    while True:
        run_scans(token)
        time.sleep(3600)
