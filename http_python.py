import requests

r = requests.get("https://pokeapi.co/api/v2/")
print(r.status_code)
print(r.text)
