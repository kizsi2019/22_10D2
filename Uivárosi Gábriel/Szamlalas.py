'''
Lisztt = []
b = 0
import random
a = 0
for i in range(5):
    a =random.randint(1,10)
    Lisztt.append(a)
for szam in Lisztt:
    if szam % 2 == 0:
        b = b + 1
print(Lisztt, "Páros számok:",b)




Darab = 0
szav = ("bb")
szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
for szo in szavak:

    if szo[0] == "a" or szo[0] == "A":
        Darab = Darab + 1
print(Darab)
'''
szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']
Darab = 0

EE = []
for szo in szavak:

    if szo[0] == "e" or szo[0] == "E":
        Darab = Darab + 1
        EE.append(szo)
print(Darab, EE)




