import random

def névelő(szo):
    maganhangzok = 'aáéeiíoóöőuúüű'
    if szo[0].lower() in maganhangzok:
        return 'az '
    else:
        return 'a '

def jelzo():
    return random.choice([" piros"," nagy"," könnyed"])

print("Adj meg három főnevet")
for szam in range(1,4):
    fonev= input(str(szam) + '. főnév')
    print(névelő(fonev).capitalize(),'',fonev,jelzo(),'.',sep="")