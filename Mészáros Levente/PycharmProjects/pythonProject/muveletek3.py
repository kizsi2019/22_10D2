import math

r = int(input("Add meg a sugarat!"))

gömb_térfogat = round((4*r*r*r*math.pi/3),2)
gömb_felszín = round((4*r*r*math.pi),2)

print(gömb_térfogat)
print(gömb_felszín)

with open('./gömb.txt', 'a',  encoding='utf-8') as yeah:
    print('Ez a gömb térfogata', gömb_térfogat, file=yeah)
    print('Ez a gömb felszíne', gömb_felszín, file=yeah)