import math

gombsugi = int(input("giv gömb sugár"))

gombterfogi = (4*gombsugi*gombsugi*gombsugi*math.pi)
gombterfogi = round(gombterfogi, 2)
gombfelszin = 4*gombsugi*gombsugi*math.pi
gombfelszin = round(gombfelszin, 2)

with open('sex/gömbi.txt', 'a', encoding='utf-8') as avefile:
    print('a térfogat:',gombterfogi, end='\n', file=avefile)
    print('a felszín:',gombfelszin, end='\n', file=avefile)

avefile.close()