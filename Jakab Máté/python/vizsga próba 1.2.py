import random
def paros_szamok(szamok):
    szam = input('Adja meg az első számot')
    while szam != "":
        szamok.append(szam)
        szam = input("Adja meg a következő számot (Enterrel kilép):")

parosak = paros_szamok()
print(parosak)