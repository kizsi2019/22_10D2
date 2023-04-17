name = input("Vizsgázó neve: ")
score = int(input("Vizsgázó pontszáma: "))

if score >= 48:
    print(name + " Átment a vizshán!")
else:
    print(name + " Megbukott a vizsgán.")
