with open('rilke.txt', 'r') as f:
    text = f.read()

# Betűk száma
num_chars = len(text)

# Magánhangzók száma
vowels = 'aeiouáéíóöőúüű'
num_vowels = sum([1 for char in text if char.lower() in vowels])

# Szavak száma
num_words = len(text.split())

print(f"A vers {num_chars} betűt, {num_vowels} magánhangzót és {num_words} szót tartalmaz.")