def óraperc(hossz):
    óra = hossz // 60
    perc = hossz - óra * 60
    return str(óra)+ " óra " + str(perc) + " perc."

for i in range(3):
    filmnev = input("Add meg egy film címét!")
    hossz = int(input("Hány perces a film?"))
    print("A(z)",filmnev,"című film",óraperc(hossz),"hosszú.")