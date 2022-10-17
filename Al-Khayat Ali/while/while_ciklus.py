szam = 1
while szam <= 10:
    print(szam)
    szam = szam +1

szamlalo = 1
while szamlalo <= 5:
        print("programozni jo")
        szamlalo = szamlalo+1

folytatja = True
while folytatja:
    print("vidd ki a szemetet")
    valasz = input("mondjam meg egyszer? (i/n)")
    if valasz == "n":
        folytatja = False
print("a program vege")

szam = int(input("adj meg egy szamot 5 es 10 kozott"))

# while szam < 5 or 10 < szam:
while not 5 <= szam <= 10:
    szam = int(input("helytelen ertek! adj meg egy szamot 5 es 10 kozott"))

print("rendben!")

