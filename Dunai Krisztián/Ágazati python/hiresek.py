class HiresNok:
    def __init__(self, név, foglalkozás):
        self.név = név
        self.foglalkozás = foglalkozás

hires1_nev = input("Add meg egy híres nő nevét! ")
hires1_foglalkozas = input("Add meg a foglalkozását! ")
hires1_nemzetiseg = input("Add meg a nemzetiségét (a/n)! ")

hires2_nev = input("Add meg egy híres nő nevét! ")
hires2_foglalkozas = input("Add meg a foglalkozását! ")
hires2_nemzetiseg = input("Add meg a nemzetiségét (a/n)! ")

hires3_nev = input("Add meg egy híres nő nevét! ")
hires3_foglalkozas = input("Add meg a foglalkozását! ")
hires3_nemzetiseg = input("Add meg a nemzetiségét (a/n)! ")

hires1 = HiresNok(hires1_nev, hires1_foglalkozas, hires1_nemzetiseg)
hires2 = HiresNok(hires2_nev, hires2_foglalkozas, hires2_nemzetiseg)
hires3 = HiresNok(hires3_nev, hires3_foglalkozas, hires3_nemzetiseg)

print(hires1.nemzetiseg_elotag() + " " + hires1.nev + " egy híres " + hires1.foglalkozas)
print(hires2.nemzetiseg_elotag() + " " + hires2.nev + " egy híres " + hires2.foglalkozas)
print(hires3.nemzetiseg_elotag() + " " + hires3.nev + " egy híres " + hires3.foglalkozas)
