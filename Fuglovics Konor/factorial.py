factor = 1
number = int(input("What number's factorial should I calculate? "))

for i in range(number):
    factor = factor * (i+1)
print(factor)