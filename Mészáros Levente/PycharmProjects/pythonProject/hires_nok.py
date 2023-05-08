#!/usr/bin/env python3

class HíresNő:
    def __init__(self, név, foglalkozás, nemzetiseg):
        self.név = név
        self.foglalkozás = foglalkozás
        self.nemzetiseg = nemzetiseg

    def nemet_vagy_angol(self):
        if self.nemzetiseg == 'a':
            return 'Ms.'

        elif self.nemzetiseg == 'n':
            return 'Frau'


    def info(self):
        szarmazas = self.nemet_vagy_angol()
        if szarmazas:
            return f'{szarmazas} {self.név} egy híres {self.foglalkozás}'



hires_nok = []
for i in range(3):
    nev = input('Add meg a nevet! ')
    foglalkozas = input('Add meg foglalkozását! ')
    nemzetiseg = input('Add meg a nemzetiseget! ')
    hires = HíresNő(nev, foglalkozas, nemzetiseg)
    hires_nok.append(hires)


for hires in hires_nok:
    print(hires.info())