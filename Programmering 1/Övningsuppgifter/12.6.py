import os
import json

# Läs in listan från notes.json
'''
notes = {
    "Important": "Lite test och annat",
    "Notes from lecture": "Testar..."
}
'''
with open('notes.json', 'a+') as f:
    try:
        notes = json.loads(f.read())
    except:
        notes = {}

while True:

    # Rensa terminalfönstret
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # Skapa UI (user interface)
    print(".: ALWAYSNOTE :.")
    print("-- GOLD EDITION --")
    print("******************")

    # Visa listan
    for key in notes:
        print("-", key)

    print('------------------')
    print('view | view note')
    print('add | add note')
    print('rm | remove note')
    print('exit | exit program')

    option = input('Menu > ')

    # Implementera view
    if(option) == 'view':
        title = input('title > ')
        try:
            print(notes[title])
        except KeyError as e:
            print("Unkown note:", e)


    # Implementera add
    elif option == 'add':
        title = input('title > ')
        desc = input('desc > ')
        notes[title] = desc
        print('------------------')
        print('INFO: Note added')

    # Implementera remove
    elif option == 'rm':
        title = input('title > ')
        del notes[title]
        print('Note deleted ...')
        #try:
            #notes

    # Implementera exit
    elif option == 'exit':
        print('Saving to notes.json ...')

        # Implementera icke-flyktigt minne
        with open('notes.json', 'w') as myFile:
            myFile.write(json.dumps(notes))

        print('Programmet stängdes!')
        break

    # Implementera felhantering
    else:
        print('Error: Unkown command ...')


    print('------------------')
    input('Press Enter to continue...')




