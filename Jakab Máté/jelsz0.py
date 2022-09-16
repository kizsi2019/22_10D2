valasz = input("Add meg a jelszót!")
jelszo = "fred durst"
folytatja = True
while folytatja:
    if not valasz == jelszo:
        valasz = int(input("Add meg a jelszót!"))
    else:
        folytatja = False
print("Eltaláltad a jelszót!")