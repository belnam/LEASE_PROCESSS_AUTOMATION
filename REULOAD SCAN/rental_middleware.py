from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport



def getUrl():
    return "https://violations.innovativetoll.com/api"



def generateToken():
    # transport = AIOHTTPTransport(url=service_url, headers={ "apikey": "2TTJsQm9QalH7miqRGDm9sMB9CwumyNAaaiskdkqa9320samd"})
    service_url = getUrl()
    transport = AIOHTTPTransport(url=service_url)

    # Request Authentication Token
    GQL_client = Client(transport=transport, fetch_schema_from_transport=True)
    body =  gql('''
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
    result = GQL_client.execute(body, variable_values=params )

    token = result['loginEmployee']['authData']['token']
    
    return token
   