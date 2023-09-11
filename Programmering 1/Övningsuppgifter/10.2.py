#Funktion för att läsa filen

with open(r'C:\Users\edvin\Python files\numbers.csv', 'r') as fil:
    #En dictionary
    frequency = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    #Läs varje rad i filen
    for line in fil:
        #Går igenom alla varje tecken i filen
        for char in line:
            if char.isdigit():
                digit = int(char)
                frequency[digit] += 1

#Presentera resultatet till användaren
for digit, count in frequency.items():
    print(f'Heltal {digit}: {count} förekomster')
