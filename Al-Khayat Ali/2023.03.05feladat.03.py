lista = []
hossz = input("add meg az oldal hosszat! ")
while hossz != '0':
    negyzet = Negyzet(int(hossz))
    lista.append(negyzet)
    hossz = input("add meg az oldal hosszat!")

for negyzet in lista:
    print(f"A(z) {negyzet.oldalhossz} oldalhosszusagu negyzet")
    f"{negyzet.kerulet()}, terulete: {negyzet.terulet()}")