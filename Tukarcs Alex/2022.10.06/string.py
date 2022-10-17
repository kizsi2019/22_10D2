sztring = 'Ismered ezt a számot?'

print(sztring[0])
print(sztring[-1])

print(sztring[2:11])
print(sztring[:9])
print(sztring[7:])

print(len(sztring))

for betu in sztring:
    if betu == 'e' or betu == 'E':
        szamlalo += 1
print(f'A sztringben {szamlalo} db e/E betű van.')

if 'e' in sztring:
    print('Van benne e betű.')
else:
    print('Nincs benne e betű.')