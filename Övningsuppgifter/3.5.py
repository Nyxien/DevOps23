#Defined variables

gender_man = ['man']
gender_kvinna = ['kvinna']

haircolor_brun = ['brun']
haircolor_röd = ['röd']

eyecolor_brun = ['brun']
eyecolor_blå = ['blå']

user_input = input("Ange kön: ")
user_input = input("Ange hårfärg: ")
user_input = input("Ange ögonfärg: ")

if user_input is gender_man and haircolor_brun and eyecolor_brun:
    print("Daniel Radcliffe")
elif user_input is gender_man and haircolor_röd and eyecolor_blå:
    print("Rupert Grint")
elif user_input is gender_kvinna and haircolor_brun and eyecolor_brun:
    print("Emma Watson")
elif user_input is gender_kvinna and haircolor_brun and eyecolor_brun:
    print("Selena Gomez")
else:
    print("Fel")