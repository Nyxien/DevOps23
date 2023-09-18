import random

numbers = []
for x in range(10):
    numbers.append(random.randint(0, 9))

def get_even(list):
    even = []
    for x in list:
        if x % 2 == 0:
            even.append(x)
    return even

even = get_even(numbers)
print('even:', even)
print('numbers:', numbers)