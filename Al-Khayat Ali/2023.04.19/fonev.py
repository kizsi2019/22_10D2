import random

def névelő(szó):
    magánhangzók = 'aáeéiíoóöőuúüű'
    if suó[0].lower() in magánhangzók:
        return'az'
    else:
        return'a'

def jelző():
    return random.choice(['piros', 'nagy', 'könnyed'])

print('adj meg három főnevet!')
for szám in range(1,4):
    főnév = input(str(szám)) + '.'