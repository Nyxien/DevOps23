#Lista för tomma nummer

nummer = []

#Läs in talserie från användaren

while True:
    try:
        tal = float(input("Ange ett tal (negativ tal för att avsluta)"))

        #avsluta lopen om negativt tal matas in

        if tal < 0:
            break


        nummer.append(tal)
    except ValueError:
        print("Ogiltligt tal försök igen.")

#
        
