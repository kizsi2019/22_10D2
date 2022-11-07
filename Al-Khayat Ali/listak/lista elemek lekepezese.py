eredeti = [11, 19, 7, -3]

eredmeny = [x * 2 for x in eredeti]

eredmeny_szurve = [x * 2 for x in eredeti if x > 0]

print(eredeti)
print(eredmeny)
print(eredmeny_szurve)

szamok = [5, 8, 3, 11, 12]
paros_szamok = [x for x in szamok if x % 2 == 0]

print(szamok)
print(paros_szamok)