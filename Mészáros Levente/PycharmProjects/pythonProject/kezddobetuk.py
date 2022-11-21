betuk = []


betu = None
while betu != '':
    betu = input('Adj meg egy a-val kezdődő szót! ')
    if betu[0] == 'a' or betu[0] == 'A':
        betuk.append(betu)

    elif betu[0] == '':
        print("nem jo")

