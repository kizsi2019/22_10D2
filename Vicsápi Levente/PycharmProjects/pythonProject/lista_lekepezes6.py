szavak = []

nagybetus_szavak = [x for x in szavak]

x = None
while x != '':
    x = input("Adj meg egy szót")
    if x != '':
        nagybetus_szavak.append(x.upper())

print(nagybetus_szavak)