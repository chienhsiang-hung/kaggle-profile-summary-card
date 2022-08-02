import requests

url = '/v1/vitals'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)