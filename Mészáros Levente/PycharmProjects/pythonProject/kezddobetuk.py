betuk = []


betu = None
while betu != '':
    betu = input('Adj meg egy a-val kezdődő szót! ')
    if betu[0] == 'a' or betu[0] == 'A':
        betuk.append(betu)
    else:
        print("nem jo")
        print(betuk)

