
import random

class Card:
    def __init__(self, rank):
        self.rank = rank

    def __str__(self):
        return self.rank

class Deck:
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
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def hand_value(self):
        value = 0
        num_aces = 0

        for card in self.hand:
            if card.rank in ['J', 'Q', 'K']:
                value += 10
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

            print("******************")
            print(".: BLACKJACK :.")
            print("-- PLUS EDITION --")
            print("------------------")
            while True:
                self.player.hand = []
                self.dealer.hand = []

                # Deal 1 card to the player and the dealer
                self.deck.deal(self.player)
                self.deck.deal(self.dealer)

                # Show the player's hand and only one card from the dealer's hand
                print(f"Spelarens hand: {self.player.hand[0]}")
                print(f"Dealerns hand: {self.dealer.hand[0]}")

                # Implement the rest of the game logic here, including player's moves, dealer's moves, and result analysis.
                player_input = input("Hit or stand? H/S: ").lower()
                if player_input == 'h' or 'hit':
                    self.deck.deal(self.player)

                    print(f"Spelarens hand: {', '.join(str(card) for card in self.player.hand)}")
                    print(f"Dealerns hand: {self.dealer.hand[0]}")

                break

if __name__ == "__main__":
    game = MainFunction()