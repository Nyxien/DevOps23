notes = {
'Meddelande från skolan': 'Friluftsdag på tisdag',
'Kom ihåg!': 'Ta bilen till verkstad',
'Inför tentamen': 'Gör alla instuderingsuppgifter',
}


print(".: ANTECKNINGAR :.")
print("******************")
for titel in notes:
    print("-", titel)
print("------------------")

while True:
    user_input = input("Anteckning > ")
    print("-----")
    if user_input in notes:
        print(f"{user_input} > {notes[user_input]}")
    else:
        print("FEL: Anteckning finns inte")
    print("-----")

    exvar = input("Tryck på 0 för att avsluta programmet eller enter för att fortsätta. > ")
    if exvar == "o":
        break
    else:
        continue

