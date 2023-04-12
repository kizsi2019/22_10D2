list = []
min = list[0]
max = list[0]
szam = int(input("adj meg egy számot!"))
while szam !="":
    list.append(szam)
for elem in list:
    if elem < min:
        min = elem
    if elem > max:
        max = elem

print(list)
print("A legkisebb: ", min)
print("A legnagyobb: ", min)
