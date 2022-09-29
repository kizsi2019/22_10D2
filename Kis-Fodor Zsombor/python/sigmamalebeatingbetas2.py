sex = (18-12)*2+(10-3)*2
sex2 = 145/9
sex3 = 632%8
sex3 = 11+10025
sex4 = 7*45+10*(5+6)
sex5 = 8*3

with open('sex/operátorok.txt', 'a', encoding='utf-8') as avefile:
    print(sex, end='\n', file=avefile)
    print(sex2, end='\n', file=avefile)
    print(sex3, end='\n', file=avefile)
    print(sex4, end='\n', file=avefile)
    print(sex5, end='\n', file=avefile)

avefile.close()