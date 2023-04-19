# hiresek.py
from hiresek_alap import HíresNő

hires_nok = []

for i in range(3):
    nev = input("Add meg egy híres nő nevét! ")
    foglalkozas = input("Add meg a foglalkozását! ")
    nemzetiseg = input("Add meg a nemzetiségét (a/n)! ")
    
    if nemzetiseg == "a":
        nemzetiseg = "angol"
    elif nemzetiseg == "n":
        nemzetiseg = "német"
    else:
        print("Hibás nemzetiség! Adjon meg 'a' vagy 'n' betűt.")
        continue
    
    hires_nok.append(HíresNő(nev, foglalkozas, nemzetiseg))

for hiresember in hires_nok:
    print("{} {} egy híres {} {}.".format(hiresember.elotag(), hiresember.név, hiresember.nemzetiseg, hiresember.foglalkozás))
