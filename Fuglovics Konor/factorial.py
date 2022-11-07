factor = 1
number = int(input("What number's factorial should I calculate? 3"))

for i in range(number):
    factor = factor * (i+1)
print(factor)