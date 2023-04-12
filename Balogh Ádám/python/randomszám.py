while True:
    import random

    szam2 = random.randint(1, 5)
    szam = int(input('Give me a number. '))

    if szam == szam2:
        print('The number is correct!')
        print('[END_OF_PROGRAM]')
        break
    elif szam < szam2:
        print('The number is smaller than my number')
        continue
    elif szam > szam2:
        print('The number is bigger than my number')
        continue