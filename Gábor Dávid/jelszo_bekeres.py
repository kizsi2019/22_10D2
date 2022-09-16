valasz = input("Add meg a jelszót! ")
jelszo = "alma"
folytatja = True
while folytatja:
    if not valasz == jelszo:
        valasz = input("Add meg a jelszót! ")
    else:
        folytatja = False
print("Eltaláltad a jelszót!")