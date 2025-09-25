import gql
from gql.transport.aiohttp import AIOHTTPTransport
import urllib3
import os
import logging
from pathlib import Path


service_url = "https://violations.innovativetollsolution.com/api"

def get_token():
    transport = AIOHTTPTransport(url=service_url)
    client = gql.Client(transport=transport, fetch_schema_from_transport=True)
    
    query = gql.gql('''
    mutation LoginEmployee($username: String!, $password: String!) {
        loginEmployee(username: $username, password: $password) {
            authData {
                token
            }
        }
    }
    ''')
    
    variables = {
        "username": "brian@innovativetoll.com",
        "password": "brianogwel"
    }

    result = client.execute(query, variable_values=variables)
    token = result['loginEmployee']['authData']['token']
    return token

def upload_files(file_params, folder_name, token):
    url = "https://violations.innovativetollsolution.com/upload/sftp"
    http = urllib3.PoolManager()

    final_status = ""
    for file_param in file_params:
        try:
            file_path = file_param

            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                    file_name = os.path.basename(file_path)

                    fields = [('localFilePath', (file_name, file_data, 'application/vnd.ms-excel'))]
                    fields.append(('folder_name', folder_name))

                    response = http.request(method='PUT', url=url, fields=fields, headers={'Authorization': token})

                    if response.status == 200:
                        r = file_name, "Uploaded Successfully to", folder_name, "Drop Box Folder"
                        success = " ".join(str(x) for x in r)
                        final_status = success
                        logging.info(final_status)
                        # print(final_status)
                    else:
                        s = "Error While Uploading", file_name
                        error = " ".join(str(x) for x in s)
                        final_status = error

                logging.info(final_status)

                print(final_status)
        except Exception as e:
            logging.error(f"Error: {str(e)}")

def run_scans():
    token = get_token()
    source_folder = f"AMAZON"
    file_params = [str(file) for file in Path(source_folder).glob('*')]
    upload_files(file_params, folder_name=source_folder, token=token)

run_scans()
