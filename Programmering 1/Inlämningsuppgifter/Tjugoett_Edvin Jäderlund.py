import random
import os

def clear_console(): # funktion för att rensa konsolen, denna funktion används för att rensa konsolen mellan varje spelomgång.
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Card: # Klass för att representera ett kort, denna skapar jag för att lättare programmera och identifiera kortet, för att definera korten med en rank och sätt att presentera objektet via sträng.
    def __init__(self, rank): #Här används __init__ metoden för att definera objektet och dess attribut(self och rank)
        self.rank = rank

    def __str__(self): #Här används __str__ metoden för att definera objektet. Denna del av koden används för att presentera alla klädda kort såsom A, J, Q, K.
        return self.rank

class Deck: # Klass för att representera en kortlek
    def __init__(self): # Detta är konstruktorsmetoden för klassen "deck" och används för att initialisera objektets egenskaper då en klassen anropas.
        self.generate_deck() # Här anropas funktionen "generate_deck" som skapar en kortlek

    def generate_deck(self): # Här anges alla olika kortranger i kortleken. Anledningen till att jag inte gör en separat lista för de klädda korten är för att jag sedan konverterar kortet till int och jag tycker det blir lättare att ha allt i en lista istället för flera olika att hålla reda på.
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank) for rank in ranks * 4] # Här skapas en lista med alla kort i en kortlek
        random.shuffle(self.cards) # Här används random.shuffle funktionen för att blanda kortleken

    def deal(self, player): # Funktion för att dela ut kort till spelaren
        if self.cards: # Här används if satsen för att kolla om det finns kort kvar i kortleken
            dealt_card = self.cards.pop() # Här används pop funktionen för att ta bort det översta kortet i kortleken
            player.add_card(dealt_card) # Här används funktionen add_card för att lägga till kortet i spelarens hand

class Player: # Klass för att representera spelaren.
    def __init__(self, name):
        self.name = name
        self.hand = [] # Här skapas en tom lista med instansvariabeln "hand" eftersom vi är inuti en klass. Denna används för att hålla reda på de kort som användaren tilldelas.

    def add_card(self, card): # Funktion för att lägga till kort i spelarens hand ovanför.
        self.hand.append(card)

    def hand_value(self): # Här defineras en funktion som ska räkna ut summan av korten i spelarens hand genom att räkna korten.
        value = 0
        num_aces = 0

        for card in self.hand: # Här skapas en for loop för att iterrera handen och plocka ut alla "klädda" kort och tilldelar dem ett värde.
            if card.rank in 'J':
                value += 11
            elif card.rank in 'Q':
                value += 12
            elif card.rank in 'K':
                value += 13
            elif card.rank == 'A':
                num_aces += 1
            else:
                value += int(card.rank)

        for i in range(num_aces): # Här skapas en for loop för att iterrera handen och plocka ut alla ess och tilldelar dem ett värde.
            if value + 14 <= 21:
                value += 14
            else:
                value += 1

        return value

class MainFunction: # Här skapas en klass för huvudfunktionen som ska köra spelet.
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")
        self.play_game() # Här anropas funktionen "play_game" som är huvudfunktionen för spelet.

    def play_game(self):
        '''Den här funktionen är huvudfunktionen för spelet och här anropas de andra funktioner för att få spelet att fungera.
        Denna metod initierar spelet, delar ut kort till både spelare och dator och sedan kör spelet tills en vinnare har utsetts.
        Huvudfunktionen tar hand om spelarens input och om spelaren väljer hit så anropas funktionen deal som delar ut ett kort till spelaren.
        Om spelaren väljer stand så är det dealerns tur att dra kort och sedan jämförs spelarens och dealerns hand för att se vem som vinner.
        Den tillåter också spelaren att köra spelet igen om spelaren vill det eller avsluta.'''
        print("******************")
        print(".: BLACKJACK :.")
        print("-- PLUS EDITION --")
        print("------------------")

        self.player.hand = [] # Här tilldelas spelarens hand värdet 0 då spelet börjar
        self.dealer.hand = [] # Här tilldelas dealerns hand värdet 0 då spelet börjar

        # Dela ut ett kort till spelaren och dealern
        self.deck.deal(self.player)
        self.deck.deal(self.dealer)

        while True:

            # Visa spelarens hand och dealerns första kort
            print("Player's hand:", ', '.join(str(card) for card in self.player.hand))
            print("Dealer's hand:", self.dealer.hand[0], ", [?]")
            print("------------------")
            print("Player's total hand value:", self.player.hand_value())
            print("------------------")

            player_input = input("Hit or stand? h/s: ").lower() # Här anges variabeln "player_input" som används för att bestämma användarens val
            try:
                if player_input == "h":
                    # Om spelaren väljer att "hit" så får den ett till kort
                    self.deck.deal(self.player)
                elif player_input == "s":
                    # Om spelaren väljer att "stand" så är det dealerns tur att dra kort
                    while self.dealer.hand_value() < 17:
                        # För att implementera dealerns drag så används en while loop som körs så länge dealerns hand är mindre än 17, detta valde jag då grundprincipen för dealern är ofta att dra tills man får 17 eller över.
                        self.deck.deal(self.dealer)

                    # Här visas dealerns hand efter den är nöjd med sitt drag
                    print("Dealer's hand:", ', '.join(str(card) for card in self.dealer.hand))

                    # Här definieras variablerna för spelarens och dealerns handvärde
                    player_score = self.player.hand_value()
                    dealer_score = self.dealer.hand_value()
                    print("------------------")
                    print("Game over!")
                    print(f"Player's hand value: {player_score}")
                    print(f"Dealer's hand value: {dealer_score}")
                    print("------------------")

                    # Här defineras reglerna för spelet och vem som vinner
                    if player_score == dealer_score:
                        print("Dealer wins!")
                    elif player_score == 21:
                        print("Player wins! Blackjack!")
                    elif player_score > 21:
                        print("Player bust. Dealer wins!")
                    elif dealer_score > 21:
                        print("Dealer bust. Player wins!")
                    elif player_score > dealer_score:
                        print("Player wins!")
                    elif dealer_score > player_score:
                        print("Dealer wins!")
                    else:
                        print("Dealer wins!")

                    # Här kontrolleras om användaren vill spela igen
                    play_again = input("Do you want to play again? (Press Enter to play again or type 'quit' to exit): ").strip().lower()

                    if play_again != 'quit':
                        # Om användaren vill spela igen, rensa skärmen och börja om spelet
                        clear_console()
                        self.deck = Deck()
                        self.player = Player("Player")
                        self.dealer = Player("Dealer")
                        self.play_game()
                    else:
                        # Om användaren inte vill spela igen, avsluta spelet
                        clear_console()
                        print("Exiting...")
                    break
                else:
                    print(input("Invalid input. Press any key to continue..."))
                    continue

            except KeyboardInterrupt:
                print("Exiting...")
                break

if __name__ == "__main__":
    game = MainFunction()