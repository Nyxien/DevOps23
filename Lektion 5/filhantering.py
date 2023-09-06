attendants = ['Lisa', 'Kalle', 'Olivia', 'Johan']

with open('textfil.txt', 'w') as f:
    for attendants in attendants:
        f.write('Hello' + attendants + '!\n')