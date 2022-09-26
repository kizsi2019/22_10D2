darab_karakter = int(input("adj meg egy számot"))
sor = 1
while sor  >= 0:
      oszlop = 1
      while oszlop <= darab_karakter:
          print('O ', end='')
          oszlop = oszlop + 1
      print('')
      darab_karakter = darab_karakter + 1
      sor = sor - 1