# ange din sträng
text = input("Ange en text: ")

# ange den bokstav du vill räkna förekomster av
bokstav = input("Ange bokstav: ")

# använd .count() för att räkna förekomster
antal_förekomster = text.count(bokstav)

# skriv ut förekomster
print(f"Bokstaven '{bokstav}' förekommer {antal_förekomster} gånger i strängen.")


