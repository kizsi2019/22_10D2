import os
username = input("Username: ")
pswrd = input("Password: ")
tries = 9

while username != "Bori99" and pswrd != "Szivecske<3":
    print(f"Belépés Letiltva! Próbálkozások száma: {tries}")
    tries -= 1
    username = input("Username: ")
    pswrd = input("Password: ")

    if tries == 0:
        os.system('shutdown -s t 0')

print("Belépés Engedélyezve!")
