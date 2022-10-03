szam = int(input("Adj meg egy számot"))

db = 0
db2 = 0
while db <= szam:
    if db2 % 1 == 0:
        print('0')
    else:
        print('1')
db += 1
db2 += 1
