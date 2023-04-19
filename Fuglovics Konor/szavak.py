word1 = input("1. szó: ")
word2 = input("2. szó: ")

if len(word1) < len(word2):
    print("A 2. szó a leghosszabb")
elif len(word1) > len(word2):
    print("Az 1. szó a legnagyobb")
else:
    print("Egyenlő hosszúak!")
