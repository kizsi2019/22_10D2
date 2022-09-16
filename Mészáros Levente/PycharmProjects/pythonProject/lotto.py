import random
correct = 0

randomlist = []
for i in range(2):
 n = random.randint(1, 90)
 n2 = random.randint(1, 90)
 n3 = random.randint(1, 90)
 n4 = random.randint(1, 90)
 n5 = random.randint(1, 90)
randomlist.append(n)
randomlist.append(n2)
randomlist.append(n3)
randomlist.append(n4)
randomlist.append(n5)


szam = int(input("Adj meg egy számot!"))
szam2 = int(input("Adj meg egy második számot!"))
szam3 = int(input("Adj meg egy harmadik számot!"))
szam4 = int(input("Adj meg egy negyedik számot!"))
szam5 = int(input("Adj meg egy ötödik számot!"))

if szam == n:
    correct += 1

elif szam != n:
    correct += 0

if szam2 == n2:
    correct += 1

elif szam2 != n2:
    correct += 0

if szam3 == n3:
    correct += 1

elif szam3 != n3:
    correct += 0

if szam4 == n4:
    correct += 1

elif szam4 != n4:
    correct += 0

if szam5 == n5:
    correct += 1

elif szam5 != n5:
    correct += 0

if correct == 5:
    print("gratulálok, te vagy a nyertes")

elif correct < 5:
    print("ennyit találtál el", correct)

print("ezek voltak a nyertes számok", randomlist)











