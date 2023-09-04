try:
    flyttal1 = float(input("Ange ett flyttal A: "))
    flyttal2 = float(input("Ange ytterligare ett flyttal B: "))

    if flyttal2 == 0:
        print("Fel, kan inte dividera med 0")

    else:
        print(flyttal1 / flyttal2)

except ValueError:
    print("Fel, ange ett giltigt flyttal")

except ZeroDivisionError:
    print("Division med 0 ej tillåtet")
