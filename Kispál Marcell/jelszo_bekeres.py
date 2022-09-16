jelszo = input("Adj meg egy jelszót")
jelszo = "kutyafüle"
folytatja = True
while folytatja:
    if not valasz == jelszo:
        valasz = input("Adj meg a jelszót!")
    else:
        folytatja = False
print("Sikeres bejelentkezés")