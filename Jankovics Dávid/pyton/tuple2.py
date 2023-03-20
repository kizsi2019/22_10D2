print("Adja meg az RGB színkód három összetevőjét:")
red = int(input("Red: "))
green = int(input("Green: "))
blue = int(input("Blue: "))

if green > 0:
    print("A szín tartalmaz zöld komponenst.")
else:
    print("A szín nem tartalmaz zöld komponenst.")

most = max(red, green, blue)
least = min(red, green, blue)
if most == red:
    print("A legtöbb komponens vörösből van.")
elif most == green:
    print("A legtöbb komponens zöldből van.")
else:
    print("A legtöbb komponens kékből van.")

if least == red:
    print("A legkevesebb komponens vörösből van.")
elif least == green:
    print("A legkevesebb komponens zöldből van.")
else:
    print("A legkevesebb komponens kékből van.")
