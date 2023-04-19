szo = input("Adj meg egy szót!")
szo2 = input("Adj meg egy szót!")

if len(szo) > len(szo2):
    print(f'A hosszabb szó a {szo}')
elif len(szo) < len(szo2):
    print(f'A hosszabb szó a {szo2}')
else:
    print(f'A kettő szó egyenlő hosszú')