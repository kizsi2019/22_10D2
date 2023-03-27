lista = []
hossz = input("add meg az oldal hosszát!")
while hossz != '0':
    negyzet = negyzet(int(hossz))
    lista.append(negyzet)
    hossz = input('add meg az oldal hosszát')

    for negyzet in lista:
        print(f"A(z) {negyzet.oldalhossz} oldalhosszúságú")