förnamn = [" Maria ", " Erik ", " Karl "]
efternamn = [" Svensson ", " Karlsson ", " Andersson "]

# nästlad for loop för att ange alla möliga kombinationer mellan förnamn och efternamn
for firstname in förnamn: # for loop för förnamn
    for lastname in efternamn: # for loop fär efternamn
        print(f"{firstname}{lastname}")