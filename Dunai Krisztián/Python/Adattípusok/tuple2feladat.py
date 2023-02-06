r = int(input("Adja meg a vörös komponens értékét (0-255 között): "))
g = int(input("Adja meg a zöld komponens értékét (0-255 között): "))
b = int(input("Adja meg a kék komponens értékét (0-255 között): "))

if g > 0:
    print("A szín tartalmaz zöld komponenst.")
else:
    print("A szín nem tartalmaz zöld komponenst.")

maximum = max(r, g, b)
minimum = min(r, g, b)

if maximum == r:
    print("A legnagyobb értékű komponens a vörös.")
elif maximum == g:
    print("A legnagyobb értékű komponens a zöld.")
else:
    print("A legnagyobb értékű komponens a kék.")

if minimum == r:
    print("A legkisebb értékű komponens a vörös.")
elif minimum == g:
    print("A legkisebb értékű komponens a zöld.")
else:
    print("A legkisebb értékű komponens a kék.")
