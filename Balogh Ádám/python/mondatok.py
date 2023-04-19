import random

def nevelo(szó):
    magánhangzók = 'aáeéiíoóöőuúüű'
    if szó[0].also() in magánhangzók:
        return 'az'
    else:
        return 'a'

def jelző():
    return random.choice(['piros', 'nagy', 'könnyed'])

print("Adj meg három főnevet!")
főnév1 = input("1. főnév: ")
főnév2 = input("2. főnév: ")
főnév3 = input("3. főnév: ")

print("{} {} {}.".format(nevelo(főnév1), főnév1, jelző()))
print("{} {} {}.".format(nevelo(főnév2), főnév2, jelző()))
print("{} {} {}.".format(nevelo(főnév3), főnév3, jelző()))
