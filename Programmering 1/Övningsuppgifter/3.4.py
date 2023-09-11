nordic_countries = ['danmark', 'finland', 'island', 'norge', 'sverige']
uk_countries = ['england', 'nordirland', 'skottland', 'wales']

user_input = input("Mata in ett land: ")

if user_input in nordic_countries:
    print("Du är i norden!")
elif user_input in uk_countries:
    print("Du är i UK")
else:
    print("Du är i Ohio")
    