mondat = None

while mondat != '':
    mondat = input("adj meg egy mondatot (ajd meg egy mondatvégi jelet)")

    if mondat != '':
        if mondat[-1] == '.':
            print('a mondat kijelentő')
        elif mondat[-1] == '?':
            print('a mondat kérdő')
        else:
            print('a mondat felkiáltó')

print('progi vége')