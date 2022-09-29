# Szilárd 771 hete regisztrált, az kell hány éve és hónapja jelentkezett be

import math

szilardido = 771

szilardho = (szilardido % 52) // 5
szilardev = szilardido // 52


with open('sex/Szilárd.txt', 'a', encoding='utf-8') as avefile:
    print("Szilárd",szilardev,"éve és",szilardho,"és hónapja tag", file=avefile)