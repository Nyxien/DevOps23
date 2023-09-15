import requests

try:
    city = input("Enter the name of the city for which you want forecasts:\n> ")

    # URL to the API
    url = f"https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/{city}"

    response = requests.get(url)
    if response.status_code == 200:
        cityData = response.json()
        print("-" * 22)
        print("FORECASTS")
        print("*" * 22)
        for forecast_entry in cityData["forecasts"]:
            date = forecast_entry['date']
            forecast = forecast_entry['forecast']
            print(f"{date}: {forecast}")
        print("-" * 22)

except:
    print("Wrong input")
