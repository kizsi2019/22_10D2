import random

random_szam = random.randint(1,2)
if random_szam == 1:
    penz = "fej"
else:
    penz = "írás"
szam2 =(input("Fej vagy írás? (fej/írás)"))
if szam2 == penz:
    print("Eltaláltad!")
else:
    print("Nem találtad el!")