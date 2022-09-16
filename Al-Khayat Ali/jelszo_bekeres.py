valasz = input("add meg a jelszot!")
jelszo = "kutyafule"
folytatja = True
while folytatja:
    if not valasz == jelszo:
        valasz = input("add meg a jelszot!")
    else: folytatja = False
print("eltalaltad a jelszot!")