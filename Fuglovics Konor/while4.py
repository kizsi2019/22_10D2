szoveg = input ("Adj meg egy szöveget!")
rarity =int(input("Hányszor írjam ki? "))
szamlalo = 1
while szamlalo <= rarity:
    print(szoveg)
    szamlalo = szamlalo + 1
print("Ennyiszer kérted: ", rarity)