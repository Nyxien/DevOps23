# Define conversion functions outside the loop
def km_to_miles(dist):
    return dist / 1.609

def miles_to_km(dist):
    return dist * 1.609

while True:
    try:
        user_input = input("Enter a distance (e.g. 100km or 100miles) or 'exit' to quit: ")

        if user_input.lower() == 'exit':
            break

        # Split the input into a number and a unit
        dist, unit = int(user_input[:-2]), user_input[-2:]

        if user_input[-2:] == 'km':
            print(f"{dist}km is {km_to_miles(dist)} miles")
        elif user_input[-5:] == 'miles':
            print(f"{dist}miles is {miles_to_km(dist)} km")


    except ValueError:
        print("Invalid input. Please enter a valid distance (e.g., '100km' or '100miles') or 'exit' to quit.")
