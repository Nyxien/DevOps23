import random


# Klass för att representera ett kort
class Card:
    def __init__(self, rank):
        self.rank = rank

    def __str__(self):
        return self.rank


# Klass för att representera en kortlek
class Deck:
    # Detta är konstruktorsmetoden för klassen "deck" och används för att initialisera objektets egenskaper.
    def __init__(self):
        # Lista över alla kortrangerna i en kortlek.
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        # Skapar en attributvariabel som kommer innehålla korten i kortleken.
        # Denna typ av lista är en komprehensionslista

        self.cards = [Card(rank) for rank in ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


# Klass för att representera spelaren
class Player:
    def __init__(self, name):
        self.name = name
        # Här skapas en tom lista med instansvariabeln "hand" eftersom vi är inuti en klass.
        # Denna används för att hålla reda på de kort som användaren tilldelas.
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    # Här defineras en funktion som ska räkna ut summan av korten i spelarens hand genom att räkna korten.
    def get_hand_value(self):
        value = 0
        # Här tilldelas variabeln "value" värdet 0 då spelarens hand börjar tom.
        # Denna variabel kommer att användas för att hålla reda på summan i handen.

        num_aces = 0
        # Här tilldelas variabeln "num_aces" värdet 0.
        # Denna variabel är till för att hålla reda på antalet Ess(Aces) då de hanteras på ett särskilt sätt.

        for card in self.hand:
            if card in ['K', 'Q', 'J']:
                value += 10



