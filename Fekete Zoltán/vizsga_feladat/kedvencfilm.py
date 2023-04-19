def oraperc(percek):
    ora = percek // 60
    perc = percek - ora * 60
    return str(ora) , ' óra' , str(perc) , ' perc'

for i in range(3):
    film = input("Add meg a film címét!")
    hossz = int(input("Hány perces a film?"))
    print("A(z)", film, "című film", oraperc(hossz), "hosszú.")