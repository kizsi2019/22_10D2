accessed = False
while not accessed:
    name1 = input("név: ")
    pswrd = input("jelszó: ")

    if name1 == "bori99" and pswrd == "Szivecske<3":
        print("Bejelentkezve!")
        accessed = True
    else:
        print("Hibás név vagy jelszó!")