valasz = input("Add meg a jelszót")
jelszo = "herefasz"
folytatja = True
while folytatja:
    if not valasz == jelszo:
        valasz = input("Add meg a jelszót")
    else: folytatja = False
print("A jelszó helyes")
