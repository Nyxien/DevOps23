import random


class Dice:
    def __init__(self):
        self.sides = [
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

    def throw_dice(self):
        return random.randint(1, 6)

    def show_dice(self, dice_number):
        dice_value = self.sides[dice_number - 1]
        for line in dice_value:
            print(line)
        print(f"Thrown value: {result}")


# Create an instance of the Dice class
dice = Dice()

# Simulate throwing the dice
result = dice.throw_dice()

# Display the result
dice.show_dice(result)