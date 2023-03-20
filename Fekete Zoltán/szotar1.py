dog = {}

Név = input("Mi a kutya neve? ")
Életkor = input("Mekkora az életkora? ")
Fajta = input("Mi a fajtája? ")
Oltási_Állapot = input("Rendelkezik-e érvényes oltással veszettség ellen? (igen/nem) ")

dog["name"] = Név
dog["age"] = Életkor
dog["breed"] = Fajta
dog["vaccinated"] = Oltási_Állapot

print("A kutya adatai:")
print(dog)
