list = []
min = list[0]
max = list[0]
szam = int(input("adj meg egy számot'"))
while szam !="":
    list.append(szam)
for elem in list:
    if szam < min:
        min = elem
    if szam > max:
        max = elem
print(list)
print("a legnagyobb szám: ", max)
print("a legkisebb szám: ", min)
