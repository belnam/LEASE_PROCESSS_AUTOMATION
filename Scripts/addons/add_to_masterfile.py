import gql
from gql.transport.aiohttp import AIOHTTPTransport
from middleware import getUrl, generateToken

def addToMasterfile(folder_name,new_filename_with_timestamp, new_filename  ):
    print("Adding to Masterfile")
# Request Client Data
    service_url = getUrl()
    token = generateToken()

    transport = AIOHTTPTransport(url=service_url, headers={ "Authorization": token})
    GQL_client = gql.Client(transport=transport, fetch_schema_from_transport=True)
    body =  gql.gql('''
        query Query {
            clients {
                organization
                id
            }
        }
    ''')


    result = GQL_client.execute(body)

    clients = result['clients']
    main_client_id = None
    for client in clients:
        if str(folder_name).upper() in client['organization']:
            main_client_id = client['id']
            # print(main_client_id)
        # print(client['organization'], client['id'])

    # Request Organization Departments
    body =  gql.gql('''
        query Query($clientId: ID!) {
            clientDepartments(clientId: $clientId) {
                id
                dept_name
            }
        }
    ''')                        
    params = {
        "clientId": main_client_id
    }
    result = GQL_client.execute(body, variable_values=params)
    departments = result['clientDepartments']
    main_department_id = None
    if new_filename_with_timestamp or new_filename:
        if 'ntta' in new_filename or "ntta" in new_filename_with_timestamp:
            for department in departments:
                if 'NTTA' in department['dept_name']:
                    main_department_id = department['id']
                    scantype = int("0")
                    break
        elif 'njta' in new_filename or "njta" in new_filename_with_timestamp:
            for department in departments:
                if 'NJTA' in department['dept_name']:
                    main_department_id = department['id']
                    scantype = int("0")
                    break
        elif 'rentals' in new_filename or "rentals" in new_filename_with_timestamp:
            for department in departments:
                if 'RENTALS' in department['dept_name']:
                    main_department_id = department['id']
                    scantype = int("0")
                    break
        elif 'citation' in new_filename or "citation" in new_filename_with_timestamp:
            for department in departments:
                if 'AMAZON' in department['dept_name']:
                    main_department_id = department['id']
                    scantype = int("1")
                    break
        else:
            for department in departments:
                if 'AMAZON' in department['dept_name']:
                    main_department_id = department['id']
                    scantype = int("0")
                    break
    # else:
    #     print("No new filename with timestamp found.")

    # Send File Response
    if main_department_id:
        body = gql.gql('''
            mutation Mutation($input: AddDailyScan!) {
                newDailyScan(input: $input) {
                    scan_id
                }
            }
        ''')
        params = {
            "input": {
                "client_id": main_client_id,
                "scan_doc_file": new_filename_with_timestamp,
                "scan_doc_name": new_filename,
                "scan_type": scantype,
                # "scan_type": int("0"),
                "dept_id": main_department_id
            }
        }
        try:
            result = GQL_client.execute(body, variable_values=params)
            print(result)
            scan_id = result['newDailyScan']['scan_id']
            return True, scan_id
        except Exception as e:
            return False, None
    
    else:
        return False, None

# addToMasterfile("Amazon","SCAN_1-ntta-AMAZON_TOLLS-2022-02-01_(BOT)_1643700000.pdf", "SCAN_1-ntta-AMAZON_TOLLS-2022-02-01_(BOT).pdf" )

    