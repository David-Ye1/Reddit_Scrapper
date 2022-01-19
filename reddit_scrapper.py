import requests, json

headers = {"X-API-KEY": "INSERT_KEY_HERE"}
user = input('Search: ')
url = f'https://api.pushshift.io/reddit/search/submission/?q={user}&subreddit=UMD'
results = requests.get(url, headers=headers).json()

for output in results['data']:
    print(output)

f = open('results.json', 'w')
json.dump(results, f, indent = 2)
