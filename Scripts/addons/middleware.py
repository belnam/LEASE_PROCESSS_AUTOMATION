import gql
from gql.transport.aiohttp import AIOHTTPTransport
# from renamescans_incrementdaily import*


def getUrl():
    return "https://violations.innovativetollsolution.com/api"



def generateToken():
    # transport = AIOHTTPTransport(url=service_url, headers={ "apikey": "2TTJsQm9QalH7miqRGDm9sMB9CwumyNAaaiskdkqa9320samd"})
    service_url = getUrl()
    transport = AIOHTTPTransport(url=service_url)

    # Request Authentication Token
    GQL_client = gql.Client(transport=transport, fetch_schema_from_transport=True)
    body =  gql.gql('''
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
        "password": "Mwikali1996"
    }
    result = GQL_client.execute(body, variable_values=params )

    token = result['loginEmployee']['authData']['token']
    print(token)
    
    return token
# generateToken()