teams = {
    'Brazil': {
        'wins': 2,
        'draws': 1,
        'losses': 0,
        'goals_for': 5,
        'goals_against': 1
    },
    'Serbia': {
        'wins': 1,
        'draws': 0,
        'losses': 2,
        'goals_for': 2,
        'goals_against': 4
    }
}

#skapa en lista
lista = []

#iterera över dictionary
for country in teams:
    print(country)
    print(teams[country])
    #skapa en dictionary
    country_dict = {
        'country': country,
    }
    lista.append(country_dict)

print(lista)

