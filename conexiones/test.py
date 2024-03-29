import requests

x = requests.get("")
print(f'estatus code: {x.status_code}')
print(x.text)
