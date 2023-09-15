with open('oop_negyzet.py', 'r', encoding='utf-8') as celfajl:
    fajl = celfajl.read()
    print(fajl)

with open('fajl3.txt', 'w', encoding='utf-8') as forrasfajl:
    forrasfajl.write(fajl)