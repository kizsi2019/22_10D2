szam = int(input("Adj meg egy számot!"))

elif szam % 3 ==0 and szam % 4 == 0:
    print("Hárommal és néggyel is osztható")
elif szam % 3 !=0 and szam % 4 != 0:
    print("Sem hárommal, sem néggyel nem osztható")
if szam % 3 ==0:
    print("Csak hárommal osztható")
elif szam % 4 == 0:
    print("Csak néggyel osztható")
