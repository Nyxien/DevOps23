#tom variabel för heltal

lista_heltal = 0

#for loop som adderar alla tal mellan 0-1000000 med vår tomma variabel
for i in range(0, 1000000):
 lista_heltal += i

print(lista_heltal)


#for loop som ger summan av alla udda tal mellan 0-500

total_sum = 0

for i in range(1, 501, 2):
 total_sum += i

 print(f"Summa av de udda heltalet är {total_sum}")
