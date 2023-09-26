import random
import os

class Card:
    # Klass för att representera ett kort
    def __init__(self, rank):
        self.rank = rank

    def __str__(self):
        return self.rank

class Deck:
    # Klass för att representera en kortlek
    def __init__(self):
        self.generate_deck()

    def generate_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank) for rank in ranks * 4]
        random.shuffle(self.cards)

    def deal(self, player):
        if self.cards:
            dealt_card = self.cards.pop()
            player.add_card(dealt_card)

class Player:
    # Klass för att representera spelaren
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def hand_value(self):
        value = 0
        num_aces = 0

        for card in self.hand:
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

        for i in range(num_aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1

        return value

class MainFunction:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")
        self.play_game()

    def play_game(self):
        while True:
            print("******************")
            print(".: BLACKJACK :.")
            print("-- PLUS EDITION --")
            print("------------------")

            self.player.hand = []
            self.dealer.hand = []

            self.deck.deal(self.player)
            self.deck.deal(self.dealer)

            while True:
                print("Player's hand:", ', '.join(str(card) for card in self.player.hand))
                print("Dealer's hand:", self.dealer.hand[0], ", [?]")
                print("------------------")
                print("Player's total hand value:", self.player.hand_value())
                print("------------------")

                player_input = input("Hit or stand? H/S: ").lower()
                try:
                    if player_input == "h":
                        self.deck.deal(self.player)
                    elif player_input == "s":
                        while self.dealer.hand_value() < 17:
                            self.deck.deal(self.dealer)

                        print("Dealer's hand:", ', '.join(str(card) for card in self.dealer.hand))

                        player_score = self.player.hand_value()
                        dealer_score = self.dealer.hand_value()
                        print("------------------")
                        print("Game over!")
                        print(f"Player's hand value: {player_score}")
                        print(f"Dealer's hand value: {dealer_score}")
                        print("------------------")

                        if player_score == dealer_score:
                            print("Dealer wins!")
                        elif player_score == 21:
                            print("Player wins! Blackjack!")
                        elif player_score > 21:
                            print("Player busts. Dealer wins!")
                        elif dealer_score > 21:
                            print("Dealer busts. Player wins!")
                        elif player_score > dealer_score:
                            print("Player wins!")
                        elif dealer_score > player_score:
                            print("Dealer wins!")

                        # Här kontrolleras om användaren vill spela igen
                        play_again = input("Do you want to play again? (Press Enter to play again or type 'quit' to exit): ").strip().lower()

                        if play_again != 'quit':
                            # Om användaren vill spela igen, rensa skärmen och börja om spelet
                            os.system('cls' if os.name == 'nt' else 'clear')
                            self.deck.generate_deck()
                            break  # Gå tillbaka till början av spelet
                        else:
                            print("Exiting...")
                            return  # Avsluta spelet om användaren väljer att sluta

                    else:
                        print("Invalid input. Press any key to continue...")
                        continue

                except KeyboardInterrupt:
                    print("Exiting...")
                    return  # Avsluta spelet om användaren avbryter

if __name__ == "__main__":
    game = MainFunction()
