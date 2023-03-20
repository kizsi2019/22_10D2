piros = int(input("Add meg a piros komponenst! (0-255-ig terjedő értékkel.):"))
zöld = int(input("Add meg a zöld komponenst! (0-255-ig terjedő értékkel.):"))
kék = int(input("Add meg a kék komponenst! (0-255-ig terjedő értékkel.):"))

komponensek = piros, zöld, kék
if zöld > 0:
    print("Van benne zöld komponens.")
else:
    print("Nincs benne zöld komponens.")

min = komponensek[0]
max = komponensek[0]

for komponens in komponensek:
    if komponens < min:
        min = komponens
    if komponens > max:
        max = komponens
if piros == max:
    print("Ebből a komponensből van a legtöbb: piros")
if piros == min:
    print("Ebből a komponensből van a legkevesebb: piros")

if zöld == max:
    print("Ebből a komponensből van a legtöbb: zöld")
if zöld == min:
    print("Ebből a komponensből van a legkevesebb: zöld")

if kék == max:
    print("Ebből a komponensből van a legtöbb: kék")
if kék == min:
    print("Ebből a komponensből van a legkevesebb: kék")

