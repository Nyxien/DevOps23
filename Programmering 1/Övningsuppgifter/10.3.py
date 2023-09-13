# Funktion för lista av människor
def läs_list():
    try:
        with open(r'C:\Users\edvin\Downloads\database.csv', 'r') as file:
            innehåll = file.readlines()
            return [line.strip().split(', ') for line in innehåll]

    except FileNotFoundError:
        print("Error, fil ej hittad")

# Funktion för att söka efter människor
def sök_list():
    sökID_list = input("")


# Huvud funktion

