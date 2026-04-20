#Bridge between who wants to get data and one who owns the data is API (Application Programming Interface)

import requests

url = "https://pokeapi.co/api/v2/pokemon/"

response = requests.get(url).json()

print(response)

