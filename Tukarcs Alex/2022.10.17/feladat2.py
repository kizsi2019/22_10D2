import random


rand_list=[]
n=10
for i in range(n):
    rand_list.append(random.randint(1,3))
print(rand_list)

user = int(input("Adj meg egy számot 1 és 3 között"))
rand_list.remove(user)

print(rand_list)