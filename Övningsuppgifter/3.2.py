def calculate_sleep_recommendation(age):
    if age == 1:
        return 14
    elif age == 2:
        return 13
    elif age == 3:
        return 12
    elif age == 4:
        return 11.5
    elif age <= 6:
        return 11
    elif age == 7:
        return 10.5
    elif age <= 10:
        return 10
    elif age == 11:
        return 9.5
    elif age <= 15:
        return 9
    elif age == 16:
        return 8.5
    else:
        return 8

def main():
    name = input("Ange ditt namn: ")
    age = int(input("Ange din ålder: "))
    
    recommended_sleep = calculate_sleep_recommendation(age)
    
    print("-----")
    print(f"Hallå {name}! Enligt Vårdguidens rekommendationer behöver individer i din ålder ({age} år) sova minst {recommended_sleep} timmar per natt.")

if __name__ == "__main__":
    main()