
def harommal_oszthato(*args):
    oszthato = 0
    for szam in args:
        if szam % 3 == 0:
            oszthato = oszthato + 1
            print(oszthato)
harommal_oszthato(6,3,6,9,12)

