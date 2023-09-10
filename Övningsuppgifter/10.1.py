#Funktion för innehållet av skylten

def läs_skylt():
    try:
        with open("sign.txt", "r") as fil:
            innehåll = fil.read()
            return innehåll

    except:
        return "Ingen skyltmeddelande hittades"

#funktion för att ändra skyltens meddelande

def ändra_skylt():
        nytt_meddelande = input("Skriv in det nya meddelande")
        with open ("sign.txt", "w") as fil:
                fil.write(nytt_meddelande)
        print("Skyltmeddelandet har ändrats.")

#huvudfunktion:
while True:
        aktuellt_meddelande = läs_skylt()
        print(f"Aktuellt skyltmeddelande: {aktuellt_meddelande}")
        val = input("Välj ett alternativ (Ä = Ändra, E = Exit: ").upper()

        if val == 'Ä':
                ändra_skylt()
        elif val == 'E':
                break
        else:
                print("Ogiltligt val. Försök igen")

