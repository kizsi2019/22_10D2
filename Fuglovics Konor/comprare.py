numbers = [0, 2, 5, 9, 14, 20, 39, 70, 100]

minimum = numbers[0]
maximum = numbers[0]
for number in numbers:
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number
print(f"The highest number is: {maximum}")
print(f"The lowest number is: {minimum}")
