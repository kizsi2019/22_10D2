import random

lottery = set()
personguess = set()

print("\u001b[32mSTARTING UP...")
print("WELCOME TO LOTTO 2077!")
print("PLEASE GIVE 5 GUESSES FOR YOUR LOTTERY NUMBERS!")
print("--------")

for i in range(5):
    lottery.add(random.randint(0,10))

for i in range(5):
    personguess.add(int(input("\u001b[32mGIVE ME A NUMBER")))

print("--------")


print(lottery & personguess, "WERE THE NUMBERS YOU GOT RIGHT")
print(lottery - personguess, "WERE THE NUMBERS YOU DIDN'T GUESS CORRECTLY")

print("SHUTTING DOWN PROGRAM...")