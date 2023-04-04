import random

random_szam = random.randint(1, 10)
print(random_szam)

folytatja = True
while folytatja:
    while (szam := int(input('adj meg egy számot!'))) != random_szam:
        print("nem talált")
    if szam == random_szam:
        print('eltaláltad')
        valasz = input('szeretnél játszani mégegyet=(i/n)?')
        if valasz == 'i':
            folytatja = True
        else:
            folytatja = False



print('program vége')


