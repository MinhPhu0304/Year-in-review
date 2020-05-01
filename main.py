from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from dotenv import load_dotenv
load_dotenv()

import os
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

requestTransport=RequestsHTTPTransport(
    url='https://api.github.com/graphql',
    use_json=True,
    headers={
        "Content-type": "application/json",
        "Authorization": 'Bearer ' + GITHUB_TOKEN
    },
    verify=True
)

client = Client(
    retries=1,
    transport=requestTransport,
    fetch_schema_from_transport=True,
)

query = gql('''
    query { 
      viewer { 
        login
        companyHTML
        bioHTML
        bio
        avatarUrl
        anyPinnableItems
      }
    }
''')

result = client.execute(query)

