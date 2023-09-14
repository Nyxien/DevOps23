import requests

try:
    integer = int(input)

    url = f"https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=100"
    response = requests.get(url)

    if response.status_code == 200:
        integerData = response.json():
        print("Gratis", integerData):
    else:
        print("Not Gratis", response.status_code)

except ValueError:
    print("Wrong input")
