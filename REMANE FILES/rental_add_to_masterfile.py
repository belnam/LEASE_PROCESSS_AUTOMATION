import gql
from gql.transport.aiohttp import AIOHTTPTransport
from rental_middleware import getUrl, generateToken

def addToMasterfile(folder_name,new_filename_with_timestamp, new_filename,original_name):
# def addToMasterfile(folder_name,new_filename_with_timestamp, new_filename):
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
    # print(clients)

    main_client_id = None
    
    for client in clients:

        if str(folder_name).upper() == "RENTALS" and client['organization'] == 'AMAZON':
            main_client_id = client['id']
            print(main_client_id)

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
    # print(departments)
    for department in departments:
        if department['dept_name'] == 'RENTALS':
            main_department_id = department['id']
            # print(main_department_id)   
            break
   
    body = gql.gql(''' 
            query SubDepartment($filter: subDepartmentFilter) {
            subDepartments(filter: $filter) {
                id
                name
            }
        }
    ''')

    params = {
        "subDepartmentFilter": main_department_id
    }
    result = GQL_client.execute(body, variable_values=params)
    subdepartments = result['subDepartments']
    # print(subdepartments)

    main_subdepartment_id = None
    if new_filename_with_timestamp or new_filename:
        # if 'stoughton' in new_filename or "STOUGHTON" in new_filename_with_timestamp:
        if ('stoughton' in new_filename or 'STOUGHTON' in new_filename) and ("tolls" in new_filename_with_timestamp or "TOLLS" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'STOUGHTON' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("0")
                    break
        elif ('xtra' in new_filename or 'XTRA' in new_filename) and ("tolls" in new_filename_with_timestamp or "TOLLS" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'XTRA' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("0")
                    break
        elif ('transport' in new_filename or 'TRANSPORT' in new_filename) and ("tolls" in new_filename_with_timestamp or "TOLLS" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'XL TRANSPORT LLC' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("0")
                    break
        elif ('ride' in new_filename or 'RIDE' in new_filename) and ("tolls" in new_filename_with_timestamp or "TOLLS" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'JOY RIDE' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("0")
                    break
        elif ('canadian' in new_filename or 'CANADIAN' in new_filename) and ("tolls" in new_filename_with_timestamp or "TOLLS" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'CANADIAN' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("0")
                    break
        elif ('bowman' in new_filename or 'BOWMAN' in new_filename) and ("tolls" in new_filename_with_timestamp or "TOLLS" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'BOWMAN' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("0")
                    break
        elif ('premier' in new_filename or 'PREMIER' in new_filename) and ("tolls" in new_filename_with_timestamp or "TOLLS" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'PREMIER' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("0")
                    break
        elif ('milestone' in new_filename or 'MILESTONE' in new_filename) and ("tolls" in new_filename_with_timestamp or "TOLLS" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'MILESTONE' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("0")
                    break
                
        # elif 'citation' in new_filename or "CITATION" in new_filename_with_timestamp:
        #     for subdepartment in subdepartments:
        #         if 'OTHERS' in subdepartment['name']:
        #             main_subdepartment_id = subdepartment['id']
        #             scantype = int("1")
        #             break
        elif ('citation' in new_filename and 'milestone' in new_filename) or ("CITATION" in new_filename_with_timestamp and "MILESTONE" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'MILESTONE' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("1")
                    break
        elif ('citation' in new_filename and 'stoughton' in new_filename) or ("CITATION" in new_filename_with_timestamp and "STOUGHTON" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'STOUGHTON' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("1")
                    break
        elif ('citation' in new_filename and 'xtra' in new_filename) or ("CITATION" in new_filename_with_timestamp and "XTRA" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'XTRA' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("1")
                    break
        elif ('citation' in new_filename and 'transport' in new_filename) or ("CITATION" in new_filename_with_timestamp and "TRANSPORT" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'TRANSPORT' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("1")
                    break
        elif ('citation' in new_filename and 'ride' in new_filename) or ("CITATION" in new_filename_with_timestamp and "RIDE" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'RIDE' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("1")
                    break
        elif ('citation' in new_filename and 'canadian' in new_filename) or ("CITATION" in new_filename_with_timestamp and "CANADIAN" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'CANADIAN' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("1")
                    break
        elif ('citation' in new_filename and 'bowman' in new_filename) or ("CITATION" in new_filename_with_timestamp and "BOWMAN" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'BOWMAN' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("1")
                    break
        elif ('citation' in new_filename and 'premier' in new_filename) or ("CITATION" in new_filename_with_timestamp and "PREMIER" in new_filename_with_timestamp):
            for subdepartment in subdepartments:
                if 'PREMIER' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    scantype = int("1")
                    break
        
        else:
            for subdepartment in subdepartments:
                if 'OTHERS' in subdepartment['name']:
                    main_subdepartment_id = subdepartment['id']
                    if "citation" in new_filename.lower():
                        scantype = int("1")
                    else:
                        scantype = int("0")
                    break
    # else:
    #     print("No new filename with timestamp found.")

    # Send File Response
    if main_subdepartment_id:
        body = gql.gql('''
            mutation NewDailyScan($input: AddDailyScan!) {
                newDailyScan(input: $input) {
                    scan_id
                }
            }
        ''')
        input = {
            "client_id": main_client_id,
            "scan_doc_file": new_filename_with_timestamp,
            "scan_doc_name": new_filename,
            "scan_type": scantype,
            "original_name": original_name,
            "dept_id": main_department_id,
        }
        if main_subdepartment_id and str(main_subdepartment_id).strip() != "" and str(main_subdepartment_id).strip() != "None":
            input["sub_dept_id"] = main_subdepartment_id

        params = {
            "input":input
        }
        # print(params)
        try:
            result = GQL_client.execute(body, variable_values=params)
            # print(result)
            scan_id = result['newDailyScan']['scan_id']
            return True, scan_id, scantype
        except Exception as e:
            # print(e)
            return False, None, None

    else:
        return False, None, None

addToMasterfile("rentals","scan_711_amazon_milestone_rental_tolls_05-19-2025_(bot)_1747714331.pdf", "scan_12_amazon_rental_milestone_citation_05-19-2025_(bot).pdf","M00447190A J1-16333752_05192025.pdf")

