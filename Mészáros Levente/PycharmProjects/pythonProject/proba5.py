szam = int(input("Kérem, adjon meg egy négyjegyű számot: "))

ezer = szam // 1000
szaz = (szam // 100) % 10
tizes = (szam // 10) % 10
egyes = szam % 10

print("Ez a szám a következő számjegyekből áll: ")
print(ezer, szaz, tizes, egyes)
