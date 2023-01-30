import random
ABC = ('A', 'B', 'C')
a3 = (1, 2, 3)
r1 = random.randint(0, 2)
r2 = random.randint(0, 2)
sor = ABC[r1]
oszlop = a3[r2]
P = 0
T = False

while T == False and P < 5:
   s = input("Agy sort")
   o = int(input("Agy egy oszlopot"))
   P = P + 1

   if s == sor and o == oszlop:
       T = True
if T:
    print("ügyes Próbálkozások száma:", P)
else:
    print("Nem vagy ügyes")
