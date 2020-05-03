import json
import matplotlib.pyplot as plt
import os

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from dotenv import load_dotenv
load_dotenv()

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
    query Me { 
      viewer {
        contributionsCollection(from: "2019-12-31T11:00:00.000Z") {
          commitContributionsByRepository(maxRepositories: 100) {
            repository {
              name
              primaryLanguage {
                name
              }
              languages(first: 100) {
                nodes {
                  name
                }
                totalCount
                pageInfo {
                  hasNextPage
                  startCursor
                }
              }
            }
          }
        }
      }
    }
''')

result = client.execute(query)
print('Analyzing data...')
repoList = result['viewer']['contributionsCollection']['commitContributionsByRepository']
totalRepo = len(repoList)
topLanguage = dict()

for repo in repoList: 
  repoInfo = repo['repository']
  repoName = repoInfo['name']
  if repoInfo['primaryLanguage'] is not None:
    repoTopLanguage = repoInfo['primaryLanguage']['name']
    if repoTopLanguage not in topLanguage:
      topLanguage[repoTopLanguage] = 1
    else:
      topLanguage[repoTopLanguage] = topLanguage[repoTopLanguage] + 1

for language in topLanguage:
  topLanguage[language] = round(topLanguage[language] / totalRepo * 100, 2)

labels = topLanguage.keys()
values = topLanguage.values()

explode = [0] * len(labels)
fig1, ax1 = plt.subplots()
ax1.pie(values, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
print('Done')
plt.show()
