import random

coord = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
locat = random.choice(coord)
hit = True
index = 0
tip = input("Where could be the ship? (A-C, 1-3) ")
while index < len(coord) and not hit:
    if tip == locat:
        hit = True
    else:
        tip = input("Where could be the ship? (A-C, 1-3)")
    index = + 1

print(f"Correct! Amount of tries: {index}")
