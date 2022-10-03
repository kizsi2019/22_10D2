scanner = ['▮▯▯▯▯▯▯▯','▯▮▯▯▯▯▯▯','▯▯▮▯▯▯▯▯','▯▯▯▮▯▯▯▯','▯▯▯▯▮▯▯▯','▯▯▯▯▯▮▯▯','▯▯▯▯▯▯▮▯','▯▯▯▯▯▯▯▮','▯▯▯▯▯▯▮▯','▯▯▯▯▯▮▯▯','▯▯▯▯▮▯▯▯','▯▯▯▮▯▯▯▯','▯▯▮▯▯▯▯▯','▯▮▯▯▯▯▯▯']
infinte = True

bulb = 0

while infinte == True:
    for i in range(14):
        print(scanner[bulb])
        bulb += 1
        if bulb == 14:
            bulb = 0
