#1
'''
def tetszoleges_szoveg():
    print("anyád bíborosra paskolt, kék-zöld-lilára baszott,gecivel teletöltött, kurva picsájából hullana rád egy mázsa szar")
tetszoleges_szoveg()
'''
#2
'''
def megallapito_gyasz():
    szam = int(input('Adjon meg egy gyászos számot'))
    if szam > 0:
        print("POZITÍV BAZDMEG!!")
    elif szam == 0:
        print("NULLA BAZDMEG!!")
    else:
        print("NEGATÍV BAZDMEG!!")
megallapito_gyasz()
'''
#3
'''
def szam_hasonlitas():
    szam1 = int(input('Adj meg egy szamot'))
    szam2 = int(input('Adj meg egy szamot'))
    if szam1 > szam2:
        print(szam1, "nagyobb")
    elif szam1 < szam2:
        print(szam2, "nagyobb")
    elif szam1 == szam2:
        print(szam1, "és", szam2, "egyenlő")
szam_hasonlitas()
'''
#4



#5.2
'''
def mezot_rajzol(x,y):
    szam1 = int(input("melyik sorban legyen x"))
    szam2 = int(input("melyik oszlopban legyen x"))
    for sor in range(x):
        for oszlop in range(y):
            if sor == szam1 - 1 and oszlop == szam2 - 1:
                print('x ', end='')
            else:
                print('0 ', end='')
        print()
mezot_rajzol(3,6)
'''