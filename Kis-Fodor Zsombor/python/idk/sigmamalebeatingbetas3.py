import math

gombsugi = int(input("giv gömb sugár"))

gombterfogi = round(((4*math.pow(gombsugi,3)*math.pi)/3),2)
gombfelszin = round((4*math.pow(gombsugi,2)*math.pi),2)

with open('../sex/gömbi.txt', 'a', encoding='utf-8') as avefile:
    print('a gömb sugara:',gombsugi, end='\n', file=avefile)
    print('a térfogat:',gombterfogi, end='\n', file=avefile)
    print('a felszín:',gombfelszin, end='\n', file=avefile)
    print('', end='\n', file=avefile)