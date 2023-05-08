small = 17
adult = 59
age = int(input("Életkor: "))

if 0 < age <= small:
    print("Kiskorú!")
elif small < age <= adult:
    print("Felnőtt!")
elif age > adult:
    print("Időskorú!")
