'''
import random
Citrom = 10
liszt = []
o = 0

for i in range(5):
    r = (random.randint(1,10))
    o = o + r
    liszt.append(r)


print(liszt)
print(o)
'''
'''
import random
Citrom = 10
liszt = []
o = 0

for i in range(5):
    r = (random.randint(1,10))
    
    if r%2 == 0:
        o = o + r
        liszt.append(r)


print(liszt)
print(o)
'''
liszt = []
o = 0
b = 1
a =int(input("Adj meg egy számot -5 és 5 között"))
while -5 < a < 5:
    a =int(input("Adj meg egy számot -5 és 5 között"))
    o = o + a
    liszt.append(a)
print(liszt)
print(o)
