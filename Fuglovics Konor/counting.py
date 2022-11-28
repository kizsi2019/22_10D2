numbers = [12, 17, 0, 5, 20, 31, 9, 27]

piece = 0
for number in numbers:
    if number % 3 == 0:
        piece = piece + 1
print(f"The amount of numbers divisible by 3 is: {piece}")