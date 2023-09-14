#Uppgift nummer 6

def är_jämntal(num):
    try:
        num = int(num)
        if num % 2 == 0:
            return True
        else:
            return False
    except ValueError:
        print("Felaktig inmatning")

input_value = input("Ange ett heltal: ")
result = är_jämntal(input_value)
print(f"{input_value} är {result}")
