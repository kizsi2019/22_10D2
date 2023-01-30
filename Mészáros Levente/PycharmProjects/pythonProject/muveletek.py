nev = input("Add meg a vezetékneved!")
nev2 = input("Add meg a keresztneved!")



with open('./baszás.txt', 'a', encoding='utf-8') as avefile:
    print('Ave', nev, nev2, file=avefile)