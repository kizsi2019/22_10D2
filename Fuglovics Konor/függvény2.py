def counter(a, b, c=100):
    return (a+b)*c

print(counter(1, 7))
print(counter(1, 7, 10000))
print(counter(c=10000, a=1, b=7))