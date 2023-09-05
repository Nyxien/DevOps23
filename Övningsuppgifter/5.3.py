#Grafik för user interface
ui_width = 30
print(ui_width * '*')
print('MATHLETE'.center(ui_width))
print(ui_width * '-')

#lista över alla nummer som matas in

numList = []


#en oändlig while loop som pågår tills användaren bryter
while True:
    try:
        tal = input(": ") #inmatning från användaren

        if tal.lower() == "exit":  # Om användaren matar in ordet exit så ska programmet avslutas
            print(f"Kardinalitet: {len(numList)}")
            print(f"Summa: {sum(numList)}")
            if len(numList) > 0:
                print(f"Medelvärde: {sum(numList) / len(numList)}")
            else:
                print("Medelvärde: N/A")
            break  # exit the loop when "exit" is entered

        numList.append(float(tal)) #talen som användaren matat in läggs till i listan "numList"

    except ValueError: # kollar efter fel typ av inmatning
        print("Error, invalid input")
    except KeyboardInterrupt:
        print("Exiting the program.")
        break