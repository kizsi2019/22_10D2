lists = ['kék', 'zöld', 'piros', 'fehér']

hit = False
index = 0
while index < len(lists) and not hit:
    if lists[index] == 'piros':
        hit = True
    index = index + 1

if hit:
    print(f"There's a color named red in the list and it's index is: {index-1}.")
else:
    print("No red color found.")