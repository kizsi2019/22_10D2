def success (reqpoint):
    if reqpoint >= 48:
        return True
    else:
        return False

name = None

while name != "":
    name = input("Add meg a vizsgázó nevét!")
    point = int(input("Add meg a pontszámát!"))
    if success(point):
        print("Átjutott!")
    else:
        print("Nem jutott át!")


