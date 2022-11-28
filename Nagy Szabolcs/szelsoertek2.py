szamok = []
szam = None
while szam != "":
    szam = input("Számot ide")
    if szam != "":
        szamok.append(szam)

print(szamok)
min = szamok[0]
max = szamok[0]
for szam in szamok:
    if szam < min:
        min = szam
    if szam > max:
        max = szam
print("A legkissebb szám:", min)
print("A legnagyobb szám:", max)