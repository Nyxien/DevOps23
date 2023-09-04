#Grafik för user interface
ui_width = 30
print(ui_width * '*')
print('THE GREAT DIVIDER'.center(ui_width))
print(ui_width * '-')

#inmatning av flyttal
inmatning1 = input("Ange flyttal A: ")

#try block som testar de angivna talen
try:

    flyttal1 = float(inmatning1) #Försök att omvandla inmatningen till ett flyttal
    if flyttal1.is_integer():
        print("Felaktig flyttal, ange ett flyttal utan decimaler")
    else:
        print(f"Du angav ett flyttal: {flyttal1}")


        flyttal2 = float(input("Ange ytterligare ett flyttal B: "))
        if not isinstance(flyttal2, float):
            print("Error ange ett flyttal")
            if flyttal2.is_integer():
                print("Felaktig flyttal")

            else:
                print(flyttal1 / flyttal2)


except ValueError:
    print("Fel, ange ett giltigt flyttal")

except ZeroDivisionError:
    print("Division med 0 ej tillåtet")

