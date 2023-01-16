randomszamok = []
adottszam = 0

while adottszam >= -5 and adottszam <= 5:
    adottszam = int(input("adj meg egy számot"))
    if adottszam >= -5 and adottszam <= 5:
        randomszamok.append(adottszam)

oszegzes = 0
for szamok in randomszamok:
    oszegzes = oszegzes + szamok

print(oszegzes, 'az összeségük')
print('a lista számai', randomszamok)