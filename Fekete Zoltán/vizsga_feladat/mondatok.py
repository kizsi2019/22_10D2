import random

def nevelo(szo):
    maganhangzok = 'aáeéiíoóöőuúüű'
    if szo[0].lower() in maganhangzok:
        return 'az'
    else:
        return 'a'

def jelszo():
    return random.choice(['piros', 'nagy', 'könnyed'])

print('Adj meg három főnevet!')
for szam in range (1,4):
    főnév = input(str(szam) + '.főnév')
    print(nevelo(főnév).capitalize(), '', jelszo(), '.', sep="")