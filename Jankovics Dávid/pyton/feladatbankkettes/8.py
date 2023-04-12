def atlag_es_indexek(szamok):
    szamok_atlaga = sum(szamok) / len(szamok)
    nagyobbak_indexei = [i for i in range(len(szamok)) if szamok[i] > szamok_atlaga]
    return szamok_atlaga, nagyobbak_indexei

szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
atlag, nagyobbak_indexei = atlag_es_indexek(szamok)
print("Az átlag:", atlag)
print("Azoknak az elemeknek az indexei, amelyek nagyobbak, mint az átlag:", nagyobbak_indexei)
