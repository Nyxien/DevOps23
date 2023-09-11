#Angivna tal

tal_1 = int(input("Ange ett tal: "))
tal_2 = int(input("Ange ännu ett tal: "))
tal_3 = int(input("Ange ett sista tal: "))

#Funktion för att identifiera största tal

if tal_1 >= tal_2 and tal_3:
    print("The largest number is", tal_1)
elif tal_2 >= tal_1 and tal_3:
    print("The largest number is", tal_2)
else:
    print(tal_3)