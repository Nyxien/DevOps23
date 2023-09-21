import requests

url = 'https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=100'
integer = int(input("Ange ett heltal"))
response = requests.get(url)

