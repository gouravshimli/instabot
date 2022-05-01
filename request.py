import requests

def googleSearch(query):
    with requests.session() as c:
        url = 'https://www.google.co.in'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        print (urllink.url)

for i in range(100):
    googleSearch('gourav shimli')
