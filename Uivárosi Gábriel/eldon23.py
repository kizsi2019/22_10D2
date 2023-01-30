a =input("adj egy szót")
T = False
l = False
K = []
while l == False:
    index = 0
    b = input("agy egy betüt")
    if b == "":
        l = True
    for betu in a:
        if b == a[index]:
            T = True
        index = index + 1
    if T:
        print("van")
    else:
        print("nincs")
        K.append(b)
        print("rosz betük", K)
