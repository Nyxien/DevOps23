import math
#2.1
"""""

citat =" datatyper har inbyggda metoder "
print ( "--------------" )

"""""
#2.2

"""""

flyttal = float (input("Skriv in ett flyttal: "))
print(round(flyttal))

"""""

#2.3

"""""
print("Datorn: Hallå!")
print("Datorn: Vad är ditt förnamn?")
förnamn = input("Du:")
print("Datorn: Vad är ditt efternamn?")
efternamn = input("Du:")
print("Trevligt att träffas", förnamn, efternamn)
"""""

#2.4

"""""
age = int(input("Hur gammal är du?:"))

if age >= 18:
    print("Grattis, du är myndig!")
else:
   print("Du är myndig inom", 18-age, "år")

"""""

#2.5

"""""

a = int(input("Mata in heltal #1:"))
b = int(input("Mata in heltal #2:"))
c = int(input("Mata in heltal #3:"))
d = int(input("Mata in heltal #4:"))

print("Det största heltalet är", max(a, b, c ,d))

"""""

#2.6
print("Korvkontrollen v1.4.7")

korv_2 = int(input("Hur många elever som vill ha 2 vanliga korvar:"))
korv_3 = int(input("Hur många elever som vill ha 3 vanliga korvar:"))
vegKorv_2 = int(input("Hur många elever som vill ha 2 veg korvar:"))
vegKorv_3 = int(input("Hur många elever som vill ha 3 veg korvar:"))

totkorv = (korv_2*2 + korv_3*3)
totvegkorv = (vegKorv_2*2 + vegKorv_3*3)
totelev = korv_2 + korv_3 + vegKorv_2 + vegKorv_3

print("Totala antalet vanlig korv korv_som behövs är:", totkorv)
print("Totala antalet veg korv korv som behövs är:", totvegkorv)

print("---------------")
print("--Inköpslista--")
print("---------------")

prisVanligKorv = math.ceil(totkorv / 8)*20.95
prisVegKorv = math.ceil(totvegkorv/ 4)*34.95
prisDricka = math.ceil(totelev)*13.95

print(math.ceil(totkorv / 8), "Vanliga korvpacket")
print(math.ceil(totvegkorv / 4), "veg korvpacket")
print(totelev, "Drickor")

print("---------------")

print("totala pris", prisVanligKorv+prisVegKorv+prisDricka)
