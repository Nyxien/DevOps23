import requests

url = 'https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=100'
r = requests.get(url)

input("Ange ett heltal")