import random


# Klass för att representera ett kort, denna skapar jag för att lättare programmera och identifiera kortet, för att definera korten med en rank och sätt att presentera objektet via sträng.
class Card:
    def __init__(self, rank): #Här används __init__ metoden för att definera objektet och dess attribut(self och rank)
        self.rank = rank

    def __str__(self): #Här används __str__ metoden för att definera objektet då den anropas av senare i koden. Då ska den returnera med en sträng som beskriver objektet.
        return self.rank


# Klass för att representera en kortlek
class Deck:
    # Detta är konstruktorsmetoden för klassen "deck" och används för att initialisera objektets egenskaper då en klassen anropas.
    def __init__(self):
        # Lista över alla kortrangerna i en kortlek.
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = ranks * 4 # Här skapar vi en kortlek genom multiplicera "ranks" listan ovanfär fyra gånger
        random.shuffle(self.cards) # Här används random.shuffle funktionen för att blanda kortleken

    def deal(self):
        return self.cards.pop()


# Klass för att representera spelaren
class Player:
    def __init__(self, name):
        self.name = name
        # Här skapas en tom lista med instansvariabeln "hand" eftersom vi är inuti en klass. Denna används för att hålla reda på de kort som användaren tilldelas.
        self.hand = []

    # Funktion för att lägga till kort i spelarens hand ovanför.
    def add_card(self, card):
        self.hand.append(card)

    # Här defineras en funktion som ska räkna ut summan av korten i spelarens hand genom att räkna korten.
    def hand_value(self):
        value = 0
        # Här tilldelas variabeln "value" värdet 0 då spelarens hand börjar tom.
        # Denna variabel kommer att användas för att hålla reda på summan i handen.

        num_aces = 0
        # Här tilldelas variabeln "num_aces" värdet 0.
        # Denna variabel är till för att hålla reda på antalet Ess(Aces) då de hanteras på ett särskilt sätt.

        # Här skapas en for loop för att räkna värdet av "suits" i handen
        for card in self.hand:
            if card in ['J', 'Q', 'K']:
                value += 10
            elif card in ['A']:
                num_aces += 1
            else:
                value += int(card) # Här läggs övriga kort till som inte är "suits" som användaren har dragit

        # Funktion för att hantera essen
        for i in range(num_aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1

        return value





#TODO implementera felhantering
#TODO implementera enkel interface och meny
#TODO kanske implementera en betting pot och en "plånbok" i json fil som sparas

