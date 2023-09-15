
mondat = True


while mondat != '':
    mondat = input("írj be egy mondatot!")


if mondat != '':

    if mondat[-1] == '!':
        print("Ez a mondat felszólító")

    if mondat[-1] == '?':
        print("Ez a mondat kérdő")

    if mondat[-1] == '.':
        print("Ez a mondat kijelentő")

print("Program vége")










