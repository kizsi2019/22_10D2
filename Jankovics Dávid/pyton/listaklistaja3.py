import random

def main():
    matrix = [[random.randint(-5, 5) for j in range(3)] for i in range(5)]
    print("Matrix before filtering:")
    for row in matrix:
        print(row)
    matrix = [row for row in matrix if all(x >= 0 for x in row)]
    print("Matrix after filtering:")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()
'''A fenti kód egy Python program, amely egy 5 sorból és 3 oszlopból álló kétdimenziós listát (matrix) generál, amelyek elemei véletlen számok az [-5, 5] intervallumból. Az első print segítségével kiírjuk a lista tartalmát, amely a generálás előtt volt.

A következő lépés a negatív számok törlése a listából. Ehhez átitéljük a matrix listát azzal a feltétellel, hogy minden sor elemeinek mindegyike nagyobb vagy egyenlő 0-val. Az átírt lista tartalma az eredeti lista sorai, amelyek minden eleme pozitív.

Az utolsó lépés, a tisztított lista tartalmának újbóli kiírása.

A if __name__ == "__main__": szakasz biztosítja, hogy a main függvény csak akkor fut le, ha a fájl futtatása során futtatjuk (nem, ha egy másik fájlból hívjuk meg).'''