valasz = input("Add meg a jelszót!")
jelszo = "kutyafule"
folytatja = True
while folytatja:
    if not valasz == jelszo:
        valasz = input("Add meg a jelszót!")
    else:
        folytatja = False
print("Eltaláltad a jelszót!")




hanyszor = int(input("Hányszor írjam ki?"))
szam = 1
while szam <= hanyszor:
    print("szöveg")
    szam += 1