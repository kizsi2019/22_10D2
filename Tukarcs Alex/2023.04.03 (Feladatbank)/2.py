def legnagyobb_szam(lista):
    max_szam = lista[0]
    for szam in lista:
        if szam > max_szam:
            max_szam = szam
    return max_szam

szamok = input("Adj meg egy számlistát vesszővel elválasztva: ")
lista = [int(szam) for szam in szamok.split(",")]

print("A legnagyobb szám a listában: ", legnagyobb_szam(lista))
