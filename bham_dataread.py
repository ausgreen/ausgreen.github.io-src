import requests
url = 'https://data.birminghamal.gov/api/3/action/datastore_search?resource_id=9d55626a-afb2-4473-a084-cb70e721af23&limit=5'
r = requests.get(url)
data = r.json()
results = data['result']
print(results['records'])