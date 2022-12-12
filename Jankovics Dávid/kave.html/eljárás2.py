def szamos_szar():
    szam = int(input("adj meg egy számot"))
    if szam == 0:
        print('nulla a kurva anyád')
    if szam < 0:
        print('negativ a kurva anyád')
    else:
        print('pozitiv a kurva anyád')

szamos_szar()