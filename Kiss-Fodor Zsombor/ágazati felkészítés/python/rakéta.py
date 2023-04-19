visszaszamlalo = int(input("Hány órás visszaszámláláast tervetünk?"))
kerdes = "n"
while visszaszamlalo > 0 and kerdes != "i":
    kerdes = input("Felfüggesztjük?")
    if kerdes == "i":
        print("kilövés megszakítva")
    else:
        visszaszamlalo -= 1
        print("visszaszámolás", visszaszamlalo)