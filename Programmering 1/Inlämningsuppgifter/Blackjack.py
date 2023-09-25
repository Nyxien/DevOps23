import random

# Klass för att representera ett kort, denna skapar jag för att lättare programmera och identifiera kortet, för att definera korten med en rank och sätt att presentera objektet via sträng.
class Card:
    def __init__(self, rank): #Här används __init__ metoden för att definera objektet och dess attribut(self och rank)
        self.rank = rank

    def __str__(self): #Här används __str__ metoden för att definera objektet. Denna del av koden används för att presentera alla klädda kort såsom A, J, Q, K.
        return self.rank




# Klass för att representera en kortlek
class Deck:
    # Detta är konstruktorsmetoden för klassen "deck" och används för att initialisera objektets egenskaper då en klassen anropas.
    def __init__(self):
        self.generate_deck() # Här anropas funktionen "generate_deck" som skapar en kortlek

    def generate_deck(self):
        # Här anges alla olika kortranger i kortleken. Anledningen till att jag inte gör en separat lista för de klädda korten är för att jag sedan konverterar kortet till int och jag tycker det blir lättare att ha allt i en lista istället för flera olika att hålla reda på.
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank) for rank in ranks * 4] # Här skapas en lista med alla kort i en kortlek
        random.shuffle(self.cards)  # Här används random.shuffle funktionen för att blanda kortleken


    def deal(self, player):
        if self.cards: # Här används if satsen för att kolla om det finns kort kvar i kortleken
            dealt_card = self.cards.pop() #
            player.add_card(dealt_card) # Här används funktionen add_card för att lägga till kortet i spelarens hand. Denna bit av kod används till funktionen I klassen "Player" för att lägga till kort i spelarens hand.




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
            if card in ['J']:
                value += 11
            elif card in ['Q']:
                value += 12
            elif card in ['K']:
                value += 13
            elif card in ['A']:
                num_aces += 1
            else:
                value += int(card.rank)# Här läggs övriga kort till som inte är "suits" som användaren har dragit

        # Funktion för att hantera essen
        for i in range(num_aces):
            if value + 14 <= 21:
                value += 14
            else:
                value += 1

        return value




class MainFunction: # Class som hanterar spelets huvudfunktioner
    def __init__(self):
        self.deck = Deck() # Här initialiseras objektet för klassen "Deck"
        self.player = Player("Player") # Här initialiseras objektet för klassen "Player"
        self.dealer = Player("Dealer") # Här initialiseras objektet för klassen "Dealer"
        self.play_game() # Här anropas funktionen "play_game" som hanterar spelets huvudfunktioner
        # Här initialiseras objekten för klasserna "Deck", "Player" och dealer som bygger upp grunderna i spelet.

    def play_game(self): # Funktion som hanterar spelets huvudfunktioner
        while True:
            print("******************")
            print(".: BLACKJACK :.")
            print("-- PLUS EDITION --")
            print("------------------")

            # Här återställs spelarens och dealerns hand för att kunna spela igen
            self.player.hand = []
            self.dealer.hand = []

            # Dela ut de två första korten till spelaren och dealern
            for i in range(2):
                self.deck.deal(self.player)
                self.deck.deal(self.dealer)

            # Visa spelarens hand och enbart ett av dealerns kort
            print(f"{self.player.name}'s Hand: {', '.join(str(card) for card in self.player.hand)}")
            print(f"{self.dealer.name}'s Hand: {self.dealer.hand[0]}")
            print("------------------")
            player_input = input("Hit or stand? H/S: ").lower()

            if player_input == 'h' or 'hit':
                self.deck.deal(self.player)
                if self.player.hand_value() > 21:
                    print(f"{self.player.name} busts! {self.dealer.name} wins!")
                    break
                elif self.player.hand_value() == 21:
                    print(f"{self.player.name} has 21! {self.dealer.name} loses!")
                    break



            # Implementera resten av spelets logik, inklusive spelarens drag, dealerens drag och resultatanalys.
            break

if __name__ == "__main__":
    game = MainFunction() # Här skapas objektet "game" för klassen "MainFunction"


#TODO implementera felhantering
#TODO implementera enkel interface och meny
#TODO kanske implementera en betting pot och en "plånbok" i json fil som sparas

