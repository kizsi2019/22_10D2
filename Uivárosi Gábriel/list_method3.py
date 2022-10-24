import random
A = 1
B = []
for i in range(10):
    B.append(random.randint(1, 3))
print(B)
C = int(input('Adj meg egy számot'))
for sz in B:
 if sz == C:
     B.remove(C)
print(B)