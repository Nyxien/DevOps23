def skriv_multiplikationstabell(tabell, start_tal, antal_tal):
    for i in range(start_tal, start_tal + antal_tal):
        resultat = tabell * i
        print(resultat)

while True:
    try:
        tabell = int(input("Ange multiplikationstabell > "))
        start_tal = 1
        antal_tal = 3

        while True:
            skriv_multiplikationstabell(tabell, start_tal, antal_tal)
            fortsatt = input("Fortsätt? (ja/nej) ")
            if fortsatt.lower() != "ja":
                break
            start_tal += antal_tal
    except ValueError:
        print("Felaktig inmatning. Ange ett heltal för multiplikationstabellen.")
