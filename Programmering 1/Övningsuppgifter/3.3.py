import random

def calculate_dice_throw(dice):
    if dice == 1:
        return (
        "-----\n"
        "|   |\n"
        "| x |\n"
        "|   |\n"
        "-----"
        )
    elif dice == 2:
        return (
        "-----\n"
        "|x  |\n"
        "|   |\n"
        "|  x|\n"
        "-----"
        )
    elif dice == 3:
        return (
        "-----\n"
        "|x  |\n"
        "| x |\n"
        "|  x|\n"
        "-----"
        )
    elif dice == 4:
        return (
        "-----\n"
        "|x x|\n"
        "|   |\n"
        "|x x|\n"
        "-----"
        )
    elif dice == 5:
        return (
        "-----\n"
        "|x x|\n"
        "| x |\n"
        "|x x|\n"
        "-----"
        )
    else:
        return (
        "-----\n"
        "|x x|\n"
        "|x x|\n"
        "|x x|\n"
        "-----"
        )


def main():

    dice = random.randint (1, 6)
    dice_throw = calculate_dice_throw(dice)

    print(dice_throw)

if __name__ == "__main__":
    main()

