def square(a):
    print(f'a négyzet függvényen belül: {a}')
    return a ** 2


def kob(a):
    print(f'a köb négyzeten belül: {a}')
    return a ** 2


a = 0
print(f'A függvényen kívül: {a}')
print(square(2))
print(kob(3))
