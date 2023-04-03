with open('forrifálj.txt', 'r', encoding='utf-8') as forrasfajl, \
        open('newfálj.txt', 'a', encoding='utf-8') as celfajl:
    for sor in forrasfajl:
        for sor in forrasfajl:
            line = sor.strip().split(';')
            print(line[0], line[1], file=celfajl)