import random

randomszamok = []

for i in range(5):
    i = random.randint(1,10)
    randomszamok.append(i)



osszegzes = 0
for szamok in randomszamok:
    if szamok % 2 == 0:
        osszegzes = osszegzes + szamok

print(osszegzes, 'az összeségük')
print('a lista számai', randomszamok)