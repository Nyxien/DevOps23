registrerade =[" Anna ", "Eva ", " Erik ", " Lars ", " Karl "]

avanmälningar =[" Anna ", " Erik ", " Karl "]

#For loop som identifierar namnen i avanmölningar och subrtraherar dem från registrerade
for names in avanmälningar:
    if names in registrerade:
        registrerade.remove(names)

        print(registrerade)
