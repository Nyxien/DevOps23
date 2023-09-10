nummer = []


while True:
    try:
        tal = float(input("Ange ett tal: "))

        if tal < 0:
            break

        nummer.append(tal)
    except ValueError:
        print("Ogiltligt försök")


minstaNummer = min(nummer) 
maxNummer = max(nummer)
summa = sum(nummer)
medelVärde = summa / tal

print("Minsta tal:", minstaNummer)
print("Största nummer:", maxNummer)
print("Summa:", summa)
print("Medelvärd:", medelVärde)
