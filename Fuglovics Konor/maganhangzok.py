vowel = "aeiouáéíóöőúüű"
count = 0
sentnc = input("Írj be egy szöveget/mondatot:")

for i in sentnc:
    if i in vowel:
        count = count + 1

print(f"Magánhangzók száma: {count}")
