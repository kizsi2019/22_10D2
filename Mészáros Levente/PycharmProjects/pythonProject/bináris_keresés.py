import random

szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

MIN = 1
MAX = 15



szam = int(input(f"adj meg egy számot! {MIN} és {MAX} között"))






talalat = False

while not talalat:
    if szam > MAX:
        print('a szám nagyobb mint a maximum érték')
        break
    if szam < MIN:
        print('a szám kisebb mint a minimum érték')
        break
    random_szam = random.choice(szamok)
    print(random_szam)
    if random_szam == szam:
        talalat = True





if talalat:
    print('van ilyen szám a listában')




