import random

szam2 = int(input('agy mo meg 1 számooot'))

szamlist = []

for i in range(10):
    szam = random.randint(1,3)
    szamlist.append(szam)
print(szamlist)
szam2 = int(input("agy mo meg 1 szamot 1,3 köz ött"))

for i in szam:
    if szamlist[i] == szam2:
        print anyád



