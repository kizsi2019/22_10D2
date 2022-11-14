import random
ABC = ('A', 'B', 'C')
a3 = (1, 2, 3)
r1 = random.randint(0, 2)
r2 = random.randint(0, 2)
sor = ABC[r1]
oszlop = a3[r2]
print(sor, oszlop)
T = False
while T == False:
   s = input("Agy sort")
   o = int(input("Agy egy oszlopot"))
   if s == sor and o == oszlop:
       T = True
if T:
    print("ügyes")
