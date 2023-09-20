teams = {
    'Brazil': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals for': 0,
        'goals against': 0
    },
    'Serbia': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals for': 0,
        'goals against': 0
    },
    'Switzerland': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals for': 0,
        'goals against': 0
    },
    'Costa Rica': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals for': 0,
        'goals against': 0
    }
}

def add_game(home_team, home_score, away_team, away_score):
    if home_score > away_score:
        teams[home_team]['wins'] += 1
        teams[away_team]['losses'] += 1
    elif home_score < away_score:
        teams[home_team]['losses'] += 1
        teams[away_team]['wins'] += 1
    else:
        teams[home_team]['draws'] += 1
        teams[away_team]['draws'] += 1

    teams[home_team]['goals for'] += home_score
    teams[home_team]['goals against'] += away_score
    teams[away_team]['goals for'] += away_score
    teams[away_team]['goals against'] += home_score