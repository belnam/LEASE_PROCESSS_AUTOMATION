import pandas as pd

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from middleware import api_url,login, api_authorization
from multiprocessing.pool import ThreadPool
import numpy as np
import time


output_folder = 'res/'
input_folder = 'res/'


file_name = 'RenameAmazon 06-09-2025.xlsx'

df = pd.read_excel(input_folder + file_name, dtype=str)


token = login('peace@innovativetoll.com', 'Mwikali1234')

api_headers = api_authorization(token)


# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url=api_url(), headers=api_headers)

# Create a GraphQL client using the defined transport
# client = Client(transport=transport, fetch_schema_from_transport=True)
def create_client():
    # Create a new GraphQL client instance for each thread
    transport = AIOHTTPTransport(url=api_url(), headers=api_headers)
    return Client(transport=transport, fetch_schema_from_transport=True)



updateSrtMutation = gql(
    """
    mutation UpdateScanDocName($originalScanDocFile: String!, $scanDocName: String!, $scanDocFile: String!, $scanType: String) {
        updateScanDocName(original_scan_doc_file: $originalScanDocFile, scan_doc_name: $scanDocName, scan_doc_file: $scanDocFile, scan_type: $scanType) {
            scan_id
        }
    }
    """
)


client = create_client()


def updateScanDoc (main_df, client) :

    for i_i, i_r in main_df.iterrows():
        try:
            input = {
                "originalScanDocFile": str(i_r['original']),
                "scanDocName": str(i_r['scan doc name']),
                "scanDocFile": str(i_r['renamed as']),
                "scanType": str(i_r['scan type']),
            }
            result = client.execute(updateSrtMutation, variable_values=input)
            main_df.loc[i_i, 'results'] = result['updateScanDocName']['scan_id']
        except Exception as e:
            main_df.loc[i_i, 'results'] = str(e)
            continue

    
    # return main_df
    main_df.to_excel(output_folder + file_name, index=False)




updateScanDoc(df, client)
