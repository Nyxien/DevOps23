import random

#TODO Fixa till kommentarerna
#TODO Möjligtsvis utöka klassen
#TODO Städa upp koden

class Dice:
    def __init__(self): # Här är en konstruktor som när den anropas initierar klassen Dice med en lista som innehåller tärningssidor.
        self.sides = [ # Här är listan av tärningssidor som representeras av strängar.
            # Tärningsnummer 1
            [' ------- ',
             '|       |',
             '|   ●   |',
             '|       |',
             ' ------- '],

            # Tärningsnummer 2
            [' ------- ',
             '| ●     |',
             '|       |',
             '|     ● |',
             ' ------- '],

            # Tärningsnummer 3
            [' ------- ',
             '| ●     |',
             '|   ●   |',
             '|     ● |',
             ' ------- '],

            # Tärningsnummer 4
            [' ------- ',
             '| ●   ● |',
             '|       |',
             '| ●   ● |',
             ' ------- '],

            # Tärningsnummer 5
            [' ------- ',
             '| ●   ● |',
             '|   ●   |',
             '| ●   ● |',
             ' ------- '],

            # Tärningsnummer 6
            [' ------- ',
             '| ●   ● |',
             '| ●   ● |',
             '| ●   ● |',
             ' ------- ']
        ]

    def throw_dice(self): # Funktion för att kasta tärningen. Ett tal mellan 1-6 slumpas fram.
        dice1_value = random.randint(1, 6)
        dice2_value = random.randint(1, 6)
        return dice1_value, dice2_value


    def show_dice(self, dice_values): # Funktion för att visa tärningen samt visa vilket nummer som tärningen visar.
        dice1_value, dice2_value = dice_values

        # Visar tärning 1
        print("Die 1:")
        dice1 = self.sides[dice1_value - 1]
        for dice_side in dice1:
            print(dice_side)

        # Visar tärning 2
        print("Die 2:")
        dice2 = self.sides[dice2_value - 1]
        for dice_side in dice2:
            print(dice_side)

        print(f"Thrown value: {dice1_value + dice2_value}")


#testar koden
dice = Dice()
result = dice.throw_dice()
dice.show_dice(result)