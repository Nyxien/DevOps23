import json

width = 30

numbers = []
counter = 0
summa = 0

# funktion för UI interaction
while True:
    with open("heltal.json", "r") as fil:
        numbers = fil.read()
    numbers = json.loads(numbers)
    while True:
        print(".: intMEMORIZER :.")
        print("*" * width, "\n")
        summa = 0
        for i in numbers:
            print("*", i)
            summa += 1
        print("------------------")
        print("SUMMA: ", summa)
        print("------------------")
        print("Ange ett heltal:")
        print("0 stänger programmet")
        print("------------------")

        try:
            heltal = int(input("Ange ett heltal: "))
            if heltal == 0:
                break
            else:
                for i in numbers:
                    if i == heltal:
                        counter += 1
                if counter == 0:
                    numbers.append(heltal)
                else:
                    counter = 0
        except:
            print("FEL: Ogiltligt heltal")
            exvar = input("Tryck enter för att fortsätta")
        print("Heltalet har sparats i filen 'heltal.json'.")
        exvar = input("Tryck på 0 för att avsluta programmet eller enter för att fortsätta. > ")
        if exvar == "o":
            break
        else:
            continue
