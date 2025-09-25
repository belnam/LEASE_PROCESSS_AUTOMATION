import gql
from gql.transport.aiohttp import AIOHTTPTransport
import pandas as pd


def getUrl():
    return "https://violations.innovativetoll.com/api"


def generateToken():
    service_url = getUrl()
    transport = AIOHTTPTransport(url=service_url)
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
        "username": "peace@innovativetoll.com",
        "password": "Mwikali1234" 
    }
    result = GQL_client.execute(body, variable_values=params)
    return result['loginEmployee']['authData']['token']


def querySrtAgencies():
    token = generateToken()
    service_url = getUrl()
    transport = AIOHTTPTransport(url=service_url, headers={"Authorization": f"Bearer {token}"}) 
    GQL_client = gql.Client(transport=transport, fetch_schema_from_transport=True)
    body = gql.gql('''
        query SrtAgencies {
            srtAgencies {
                srt_agency_id
                agency_name
                abbreviation
            }
        }
    ''')
    result = GQL_client.execute(body)
    # print(result)
    return result

def update_agency_ids(excel_path):
    df = pd.read_excel(excel_path)
    
    agency_data = querySrtAgencies()['srtAgencies']
    
    agency_map = {}
    for agency in agency_data:
        name_upper = agency['agency_name'].upper()
        agency_map[name_upper] = agency['srt_agency_id'] 
        if agency['abbreviation']:
            abbrev_upper = agency['abbreviation'].upper()
            agency_map[abbrev_upper] = agency['srt_agency_id']
    
    df['ID'] = df['AGENCY'].str.upper().map(agency_map)
    
    #  process location mappings
    token = generateToken()
    service_url = getUrl()
    transport = AIOHTTPTransport(
        url=service_url,
        headers={"Authorization": f"Bearer {token}"}
    )
    GQL_client  = gql.Client(transport=transport, fetch_schema_from_transport=True)
    
    mutation = gql.gql('''
        mutation CreateLocationMapping($input: LocationMappingInput!) {
            createLocationMapping(input: $input) {
                id
            }
        }
    ''')
    
    # Track successful updates
    success_count = 0
    failed_rows = []
    
    for index, row in df.iterrows():
        if pd.isna(row['ID']) or pd.isna(row['LOCATION']):
            failed_rows.append(index+1)
            continue
            
        variables = {
            "input": {
                "agencyId": str(row['ID']).strip(),
                "name": str(row['LOCATION']).strip()
            }
        }
        
        try:
            result = GQL_client.execute(mutation, variable_values=variables)
            success_count += 1
        except Exception as e:
            failed_rows.append(index+1)
            print(f"Row {index+1} failed: {str(e)}")
    
    # Save updated data once
    df.to_excel(excel_path, index=False)
    
    print(f"""
    Processed {len(df)} rows:
    - Successfully uploaded: {success_count}
    - Failed/incomplete rows: {len(failed_rows)}
    - Updated Excel file saved
    """)
    
    if failed_rows:
        print(f"Failed rows: {failed_rows}")

update_agency_ids('Scripts\REFINED AGENCY CHEAT SHEET.xlsx')

