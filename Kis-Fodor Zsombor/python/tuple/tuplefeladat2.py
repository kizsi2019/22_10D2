r = int(input("R"))
g = int(input("G"))
b = int(input("B"))

ergibittiq = (r, g, b)

if ergibittiq[1] == 0:
    print("a színben nincs zöld")
else:
    print("a számban van zöld")

if r > g and r > b:
    print("R")
elif g > r and g > b:
    print("G")
elif b > r and b > g:
    print("B")
else:
    print("kettő vagy mind a három ugyanannyi")

if r < g and r < b:
    print("legkisebb R")
elif g < r and g < b:
    print("legkisebb G")
elif b < r and b < g:
    print("legkisebb B")
else:
    print("kettő vagy mind a három ugyanannyi")