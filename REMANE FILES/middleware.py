from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport




# def api_url():
#     urlPrefix = "http://localhost:4000/api"
#     return urlPrefix
def api_url():
    urlPrefix = "https://violations.innovativetoll.com/api"
    return urlPrefix
# def api_url():
#     urlPrefix = "https://violations.innovativetollsolution.com/api"
#     return urlPrefix

def api_headers():
    headerPrefix =  {'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjQsImVtcGxveWVlSWQiOjQsImVtYWlsIjoibmFvbWlAaW5ub3ZhdGl2ZXRvbGwuY29tIiwidXNlcm5hbWUiOiJuYW9taSIsInJvbGUiOls4XSwicHJvZmlsZWltYWdlIjpudWxsLCJ2ZXJpZmllZEVtYWlsIjpmYWxzZSwidmVyaWZpZWRQaG9uZSI6ZmFsc2UsInN0YXR1cyI6IjAiLCJ0b2tlbkV4cGlyYXRpb24iOiIyMDI0LTA4LTAyVDA5OjA0OjUzLjk1NFoiLCJpYXQiOjE3MjI1MDMwOTMsImV4cCI6MTcyMjU4OTQ5M30.iDrbUzT1Eg_6Pf-GpFiO6TzitELEZDHulVl29sELmEc'}
    # headerPrefix =  {'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjQsImVtcGxveWVlSWQiOjQsImVtYWlsIjoibmFvbWlAaW5ub3ZhdGl2ZXRvbGwuY29tIiwidXNlcm5hbWUiOiJuYW9taSIsInJvbGUiOls4XSwicHJvZmlsZWltYWdlIjpudWxsLCJ2ZXJpZmllZEVtYWlsIjpmYWxzZSwidmVyaWZpZWRQaG9uZSI6ZmFsc2UsInN0YXR1cyI6IjAiLCJpYXQiOjE3MTAxNTQxNjUsImV4cCI6MTcxNTMzODE2NX0.xOQfJldlUSzwGA__vHfTb_PaWDbGpjTuUw_UImmI6qw'}
    
    return headerPrefix


def create_client():
    # Create a new GraphQL client instance for each thread
    transport = AIOHTTPTransport(url=api_url(), headers=api_headers())
    return Client(transport=transport, fetch_schema_from_transport=True)


loginMutation = gql(   
    """
  mutation Mutation($username: String!, $password: String!) {
  loginEmployee(username: $username, password: $password) {
    authData {
      token
    }
  }
}
    """
)


def login (username, password) :
    client = create_client()
    input = {
        "username": username,
        "password": password
    }
    result = client.execute(loginMutation, variable_values=input)
    return result['loginEmployee']['authData']['token']



def api_authorization(token):
    headerPrefix =  {'Authorization': token}
    # headerPrefix =  {'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjQsImVtcGxveWVlSWQiOjQsImVtYWlsIjoibmFvbWlAaW5ub3ZhdGl2ZXRvbGwuY29tIiwidXNlcm5hbWUiOiJuYW9taSIsInJvbGUiOls4XSwicHJvZmlsZWltYWdlIjpudWxsLCJ2ZXJpZmllZEVtYWlsIjpmYWxzZSwidmVyaWZpZWRQaG9uZSI6ZmFsc2UsInN0YXR1cyI6IjAiLCJpYXQiOjE3MTAxNTQxNjUsImV4cCI6MTcxNTMzODE2NX0.xOQfJldlUSzwGA__vHfTb_PaWDbGpjTuUw_UImmI6qw'}
    
    return headerPrefix