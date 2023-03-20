egy = int(input("adj meg egy szamot"))
ketto = int(input("adj meg egy masik szamot"))
if egy == ketto:
    print("egyel")
else:
    if egy > ketto:
        print("egy a nagyobb")
    else:
        print("a nagyobb",ketto)
