import random
sex = []

for i in range(5):
    penis = []
    for j in range(3):
        egyfos = random.randint(-5,5)
        penis.append(egyfos)
    sex.append(penis)

print("Véletlen számok:", sex)

sexjó = []
for sexytime in sex:
    rósz = 0
    for sexelek in sexytime:
        if sexelek < 0:
            rósz += 1
    if rósz == 0:
        sexjó.append(sexytime)


print("Nemnegatív véletlen számok:", sexjó)