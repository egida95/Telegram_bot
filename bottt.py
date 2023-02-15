import requests
import json
from pprint import pprint 

url = "https://rickandmortyapi.com/api/character"
r = requests.get(url)

data = r.json()
data = data['results']
for i in data:
    ids = i['id']
    names = i['name']
    statuss = i['status']
    with open ('ricionary.txt', 'a')as f:
        f.write(f'id:{ids}\nNames{names}\nStatus{statuss}')
    
