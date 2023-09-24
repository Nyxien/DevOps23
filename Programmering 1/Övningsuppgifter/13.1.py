import requests

'''
input_str = input("Please enter an integer: ")


try:

    integer = int(input_str)

    url = f"https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer={integer}"
    response = requests.get(url)

    if response.status_code == 200:
        integer_data = response.json()
        message = integer_data['message']

        if message == "even":
            is_prime = "inte ett primtal"
        elif message == "odd":
            is_prime = "ett primtal"

        factors = integer_data['factors']

        print(f"{integer} är ett {message} nummer.")
        print(f"Numrets faktorer är {', '.join(map(str, factors))}.")




    else:
        print("Not Gratis", response.status_code)

except ValueError:
    print("Error: Type a number")
'''

'''
def get_integer_from_user():
    while True:
        try:
            user_input = int(input("Ange ett positivt heltal: "))
            if user_input > 0:
                return user_input
            else:
                print("Var god ange ett positivt heltal.")
        except ValueError:
            print("Ogiltig inmatning. Var god ange ett heltal.")

def fetch_data_from_api(integer):
    url = f"https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer={integer}"
    response = requests.get(url)
    return response.json()

def display_output(data):
    print(f"{data['number']} är ett jämnt nummer.")
    print(f"Numret är {'inte ' if not data['is_prime'] else ''}ett primtal.")
    print(f"Numrets faktorer är {', '.join(map(str, data['factors']))}.")

if __name__ == "__main__":
    user_integer = get_integer_from_user()
    api_data = fetch_data_from_api(user_integer)
    display_output(api_data)
'''

import requests


def get_integer_from_user():
    while True:
        try:
            user_input = int(input("Ange ett positivt heltal: "))
            if user_input > 0:
                return user_input
            else:
                print("Var god ange ett positivt heltal.")
        except ValueError:
            print("Ogiltig inmatning. Var god ange ett heltal.")


def fetch_data_from_api(integer):
    url = f"https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer={integer}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"API Request Failed with Status Code: {response.status_code}")
        return None


def display_output(data):
    if data is not None:
        number = data.get('number', None)
        is_prime = data.get('is_prime', None)
        factors = data.get('factors', [])

        if number is not None:
            print(f"{number} är ett jämnt nummer.")

            if is_prime is not None:
                prime_status = "ett primtal." if is_prime else "inte ett primtal."
                print(f"Numret är {prime_status}")

            if factors:
                print(f"Numrets faktorer är {', '.join(map(str, factors))}.")
            else:
                print("Numret har inga faktorer.")
        else:
            print("Felaktigt svar från API.")
    else:
        print("Ingen data från API.")


if __name__ == "__main__":
    user_integer = get_integer_from_user()
    api_data = fetch_data_from_api(user_integer)
    display_output(api_data)
