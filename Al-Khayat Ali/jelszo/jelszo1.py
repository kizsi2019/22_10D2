
#!/usr/bin/env python3

bejutott = False

while not bejutott:
    felhasznalonev = input('adja meg a felhasznalonevet!')
    jelszo= input('adja meg a jelszavat!')
    if felhasznalonev == 'buzi69' and jelszo == '<3':
        print('belepes engedelyezve')
        bejutott = True
    else:
        print('belepes megtagadva')